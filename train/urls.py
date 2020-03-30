from django.urls import path
from . import views

app_name = 'train'

urlpatterns = [
    #/train/
    path('', views.IndexView.as_view(),name='index'),
    #train/id
    path('<int:pk>/', views.DetailsView.as_view(), name='details'),
    #train/id/results/
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    #train/id/votes/
    path('<int:zarfiat_id>/votes/', views.votes, name = 'vote'),


]
