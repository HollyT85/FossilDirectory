from django.urls import path
from rocks import views

urlpatterns = [
    path('rocks/', views.RockList.as_view()),
]