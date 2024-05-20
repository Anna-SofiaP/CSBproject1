from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'myapp'
urlpatterns = [
    path('', LoginView.as_view(template_name='myapp/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    #path('', views.IndexView.as_view(), name='index'),
    path('home/', views.indexView, name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    #path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/results/', views.resultsView, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('end/', views.endView, name='endpage'),
    path('timeout/', views.timeoutView, name='timeout'),
]