
from django.urls import path
from django.conf.urls import include
from django.conf.urls import url
from rest_framework import routers
from django.views.generic.base import RedirectView

from . import views



router = routers.DefaultRouter()
router.register(r'client', views.ClientViewSet)
router.register(r'section', views.SectionViewSet)
router.register(r'question', views.QuestionViewSet)
router.register(r'surveyQuestion', views.SurveyQuestionViewSet)
router.register(r'survey', views.SurveyViewSet)
router.register(r'answer', views.AnswerViewSet)
router.register(r'answerStruct', views.AnswerStructViewSet)


app_name = 'acx'

urlpatterns = [
    # ex: /polls/
    path('', include(router.urls)),
    path('index', views.index, name='index'),
    path('portal', views.portal, name='portal'),
    path('graphAcx', views.graphAcx, name='portal'),
    path('renderAnswer', views.renderAnswer, name='finStructure')
]


