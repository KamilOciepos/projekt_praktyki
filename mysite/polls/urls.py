from django.urls import path
from django.http import HttpResponse

from .models import Question
from . import views

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index.html'),
    # ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail.html'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results.html'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote.html'),
]


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)