from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/5/
    # name вызывеется тегом {% url %} шаблона html
    # можно заменить в шаблоне переопределив path с именем details
    # path('/cpecifics/<int:question_id>', views.detail, name='detail'),
    path('<int:question_id>/', views.detail, name='detail'),

    # ex: /polls/5/result/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
