from mainapp.models import User
from django.shortcuts import redirect
from rest_framework.response import Response
from django.shortcuts import render
import requests
from django.http import HttpResponse,HttpRequest
CLIENT_ID='RdXQYzPYBpaZcAhp5GMrPCRMudSDd0QlBM502ooq'
CLIENT_SECRET='tBKSwiH2DS1XYF7CpjZF2idcsAxdI7rchflEjHBNGduL0zth5RTOK3HGdXlbTDPywqBkNA1zcKi4Ds40cGGp6VrWfjyRSMZC5BUWbrvhsYUjydHClvoraFavYcf1EBBh'

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
    return HttpResponse(response.content)

def get_access_token(request):
    return HttpResponse(request)



