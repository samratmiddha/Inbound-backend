
from mainapp.models import User
from django.shortcuts import redirect
from rest_framework.response import Response
from django.shortcuts import render
import requests
from django.http import HttpResponse,HttpRequest
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import login,authenticate
from django.contrib.auth.backends import BaseBackend

CLIENT_ID='RdXQYzPYBpaZcAhp5GMrPCRMudSDd0QlBM502ooq'
CLIENT_SECRET='tBKSwiH2DS1XYF7CpjZF2idcsAxdI7rchflEjHBNGduL0zth5RTOK3HGdXlbTDPywqBkNA1zcKi4Ds40cGGp6VrWfjyRSMZC5BUWbrvhsYUjydHClvoraFavYcf1EBBh'

class PasswordlessAuthBackend(BaseBackend):
    def authenticate(self,username,name,year,email,enrolment_number):
        print("hi4")
        try:
            print("hi2")
            user=User.objects.get(username=username)
            print(user)
            return user
        except User.DoesNotExist:
            User.objects.create(username=username,name=name,email=email,year=year,enrolment_number=enrolment_number)
            user=User.objects.get(username=username)
            print("hi3")
            print(user)
            if year==3 or year==4:
                user.is_staff=True
            return user
            

    def get_user(self, username):
        try:
            return User.objects.get(username=username)
        except User.DoesNotExist:
            return None


def login_redirect(request):
    SITE=f'https://channeli.in/oauth/authorise/?client_id={CLIENT_ID}&redirect_uri=http://localhost:8000/get_oauth_token/'
    return redirect(SITE)

def get_token(request):
    AUTHORISATION_CODE=request.GET.get('code','')

    post_data={
  "client_id": CLIENT_ID,
  "client_secret": CLIENT_SECRET,
  "grant_type": "authorization_code",
  "redirect_uri": "http://localhost:8000/get_oauth_token/",
  "code": AUTHORISATION_CODE,
}

    response=requests.post('https://channeli.in/open_auth/token/',post_data)

    ACCESS_TOKEN=response.json().get('access_token','')
    TOKEN_TYPE=response.json().get('token_type','')
    REFRESh_TOKEN=response.json().get('refresh_token','')

    authorization_data={
        "Authorization":f"{TOKEN_TYPE} {ACCESS_TOKEN}"
    }

    response=requests.get('https://channeli.in/open_auth/get_user_data/',headers=authorization_data)

    is_member=False
    name=response.json()['person']['fullName']
    username=response.json()['username']
    year=response.json()['student']['currentYear']
    email=response.json()['contactInformation']['emailAddress']
    enrolment_number=response.json()['student']['enrolmentNumber']
    
    for role in response.json()['person']['roles']:
        if(role['role']=="Maintainer"):
            is_member=True

    if is_member:
        user=authenticate(username=username,name=name,year=year,email=email,enrolment_number=enrolment_number)
        print(user)
        if user is not None:
            login(request,user)
            print("logged in")


    return HttpResponse(response.content)





