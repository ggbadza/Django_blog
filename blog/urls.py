from django.urls import path
from . import views
urlpatterns=[
    path('modify/<int:pk>/', views.PostModify.as_view()),
    path('create_post/',views.PostCreate.as_view()),
    path('category/<str:slug>/',views.category_page),
    path('',views.PostList.as_view()),
    path('<int:pk>/',views.PostDetail.as_view()),   
]