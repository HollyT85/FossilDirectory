from django.urls import path
from comments import views

urlpatterns = [
    path('comments/', views.RockCommentList.as_view()),
    path('comments/<int:pk>/', views.RockCommentDetail.as_view())

]