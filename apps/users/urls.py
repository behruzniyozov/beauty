from django.urls import path
from apps.users.views import *


app_name = "users"


urlpatterns = [
    path('interest/', InterestListView.as_view(), name='interest-list'),
    path('interest/<int:pk>/', InterestDetailView.as_view(), name='interest-detail'),
    path('interest/create/', InterestCreateView.as_view(), name='interest-create'),
    path('interest/<int:pk>/update/', InterestUpdateView.as_view(), name='interest-update'),
    path('interest/<int:pk>/delete/', InterestDeleteView.as_view(), name='interest-delete'),

    path('users/', UserListView.as_view(), name='user-list'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('users/create/', UserCreateView.as_view(), name='user-create'),
    path('users/<int:pk>/update/', UserUpdateView.as_view(), name='user-update'),
    path('users/<int:pk>/delete/', UserDeleteView.as_view(), name='user-delete'),

    path('user-courses/', UserCourseListView.as_view(), name='user-course-list'),
    path('user-courses/<int:pk>/', UserCourseDetailView.as_view(), name='user-course-detail'),
    path('user-courses/create/', UserCourseCreateView.as_view(), name='user-course-create'),
    path('user-courses/<int:pk>/update/', UserCourseUpdateView.as_view(), name='user-course-update'),
    path('user-courses/<int:pk>/delete/', UserCourseDeleteView.as_view(), name='user-course-delete'),

    path('user-webinars/', UserWebinarListView.as_view(), name='user-webinar-list'),
    path('user-webinars/<int:pk>/', UserWebinarDetailView.as_view(), name='user-webinar-detail'),
    path('user-webinars/create/', UserWebinarCreateView.as_view(), name='user-webinar-create'),
    path('user-webinars/<int:pk>/update/', UserWebinarUpdateView.as_view(), name='user-webinar-update'),
    path('user-webinars/<int:pk>/delete/', UserWebinarDeleteView.as_view(), name='user-webinar-delete'),
]