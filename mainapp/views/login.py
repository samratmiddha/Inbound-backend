
from urllib.request import Request
from mainapp.models import User
from django.shortcuts import redirect
from rest_framework.response import Response
from django.shortcuts import render
import requests
from django.http import HttpResponse, HttpRequest, HttpResponseForbidden
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.backends import BaseBackend
from decouple import config
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from mainapp.serializers import UserInfoSerializer
CLIENT_ID = config('CLIENT_ID')
CLIENT_SECRET = config('CLIENT_SECRET')
BACKEND_HOST =config('BACKEND_HOST')
FRONTEND_HOST = config('FRONTEND_HOST')


def auth(username, name, year, email, enrolment_number):
    try:
        user = User.objects.get(username=username)
        return user

    except User.DoesNotExist:
        User.objects.create(username=username, name=name, email=email,
                            year=year, enrolment_number=enrolment_number)
        user = User.objects.get(username=username)
        if year == 3 or year == 4:
            user.FullAccessPermission = True
        return user


def get_user(username):
    try:
        return User.objects.get(username=username)
    except User.DoesNotExist:
        return None


@api_view(('GET',))
@permission_classes([])
def check_login(request):
    content = {'Logged_In': False}
    if request.user.is_authenticated:
        serializer = UserInfoSerializer(request.user)
        content = {'Logged_In': True, 'user': serializer.data}

    return Response(content)


@api_view(('GET',))
@authentication_classes([])
@permission_classes([])
def login_redirect(request):
    SITE = f'https://channeli.in/oauth/authorise/?client_id={CLIENT_ID}&redirect_uri={BACKEND_HOST}get_oauth_token/'
    return redirect(SITE)


@api_view(('GET', 'POST'))
@authentication_classes([])
@permission_classes([])
def get_token(request):
    AUTHORISATION_CODE = request.GET.get('code', '')

    post_data = {
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "grant_type": "authorization_code",
        "redirect_uri": f"{BACKEND_HOST}get_oauth_token/",
        "code": AUTHORISATION_CODE,
    }

    response = requests.post('https://channeli.in/open_auth/token/', post_data)

    ACCESS_TOKEN = response.json().get('access_token', '')
    TOKEN_TYPE = response.json().get('token_type', '')
    REFRESh_TOKEN = response.json().get('refresh_token', '')

    authorization_data = {
        "Authorization": f"{TOKEN_TYPE} {ACCESS_TOKEN}"
    }

    response = requests.get(
        'https://channeli.in/open_auth/get_user_data/', headers=authorization_data)
    print(response.json())
    is_member = False
    name = response.json()['person']['fullName']
    username = response.json()['username']
    year = response.json()['student']['currentYear']
    email = response.json()['contactInformation']['emailAddress']
    enrolment_number = response.json()['student']['enrolmentNumber']

    for role in response.json()['person']['roles']:
        if (role['role'] == "Maintainer"):
            is_member = True

    if is_member:
        try:
            user = auth(username=username, name=name, year=year,
                        email=email, enrolment_number=enrolment_number)
        except:
            return Response("unable to create user")
        try:
            login(request, user)
        except:
            return Response("unable to log in successfully")
    else:
        return Response("You are not a member of IMG")

    return redirect(f'{FRONTEND_HOST}dashboard')


@api_view(('GET',))
def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
        return Response("user logged out Successfully")
