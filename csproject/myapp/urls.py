from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

app_name = 'myapp'
urlpatterns = [
    #path('', views.IndexView.as_view(), name='index'),
    path('', views.indexView, name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    #path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/results/', views.resultsView, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]