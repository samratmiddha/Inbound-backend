
from django.urls import path, include
from mainapp.views.round_info import RoundInfoViewSet
from rest_framework import routers

from mainapp.views import *

router = routers.SimpleRouter()
router.register(r'users', UserViewSet)
router.register(r'candidates', CandidiateViewSet)
router.register(r'info', InfoToConveyViewSet)
router.register(r'panels', InterviewPanelViewSet)
router.register(r'marks', QuestionStatusViewSet)
router.register(r'questions', QuestionViewSet)
router.register(r'rounds', RoundViewSet)
router.register(r'seasons', SeasonViewSet)
router.register(r'sections', SectionViewSet)
router.register(r'sectional_marks', SectionalMarksViewSet)
router.register(r'round_candidates', RoundInfoViewSet)
router.register(r'chats',ChatViewSet)
router.register(r'waitlist',WaitlistViewSet)
urlpatterns = [
    path('', include(router.urls)),
    path('get_oauth_token/', get_token),
    path('send_token_request/', login_redirect),
    path('logout/', logout_user),
    path('check_login/', check_login)
]
