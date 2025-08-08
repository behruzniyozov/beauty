from django.urls import path
from apps.news.views import *


app_name = "news"

urlpatterns = [
    path('events/', EventListView.as_view(), name='event-list'),
    path('events/<int:pk>/', EventDetailView.as_view(), name='event-detail'),
    path('events/create/', EventCreateView.as_view(), name='event-create'),
    path('events/<int:pk>/update/', EventUpdateView.as_view(), name='event-update'),
    path('events/<int:pk>/delete/', EventDeleteView.as_view(), name='event-delete'),

    path('posts/', PostListView.as_view(), name='post-list'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('posts/create/', PostCreateView.as_view(), name='post-create'),
    path('posts/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('posts/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
   
    path('questions/', QuestionListView.as_view(), name='question-list'),
    path('questions/<int:pk>/', QuestionDetailView.as_view(), name='question-detail'),
    path('questions/create/', QuestionCreateView.as_view(), name='question-create'),
    path('questions/<int:pk>/update/', QuestionUpdateView.as_view(), name='question-update'),
    path('questions/<int:pk>/delete/', QuestionDeleteView.as_view(), name='question-delete'),

    path('question-options/', QuestionOptionListView.as_view(), name='question-option-list'),
    path('question-options/<int:pk>/', QuestionOptionDetailView.as_view(), name='question-option-detail'),
    path('question-options/create/', QuestionOptionCreateView.as_view(), name='question-option-create'),
    path('question-options/<int:pk>/update/', QuestionOptionUpdateView.as_view(), name='question-option-update'),
    path('question-options/<int:pk>/delete/', QuestionOptionDeleteView.as_view(), name='question-option-delete'),

    path('submissions/', SubmissionListView.as_view(), name='submission-list'),
    path('submissions/<int:pk>/', SubmissionDetailView.as_view(), name='submission-detail'),
    path('submissions/create/', SubmissionCreateView.as_view(), name='submission-create'),
    path('submissions/<int:pk>/update/', SubmissionUpdateView.as_view(), name='submission-update'),
    path('submissions/<int:pk>/delete/', SubmissionDeleteView.as_view(), name='submission-delete'),

    path('surveys/', SurveyListView.as_view(), name='survey-list'),
    path('surveys/<int:pk>/', SurveyDetailView.as_view(), name='survey-detail'),
    path('surveys/create/', SurveyCreateView.as_view(), name='survey-create'),
    path('surveys/<int:pk>/update/', SurveyUpdateView.as_view(), name='survey-update'),
    path('surveys/<int:pk>/delete/', SurveyDeleteView.as_view(), name='survey-delete'),
]