from django.urls import path
from users.views import UserCreateView
from projects.views import ProjectListCreateView, ProjectDetailView
from bids.views import BidListCreateView
from messages.views import MessageListCreateView

urlpatterns = [
    path('users/register/', UserCreateView.as_view(), name='register'),
    path('projects/', ProjectListCreateView.as_view(), name='project-list-create'),
    path('projects/<int:pk>/', ProjectDetailView.as_view(), name='project-detail'),
    path('bids/', BidListCreateView.as_view(), name='bid-list-create'),
    path('messages/', MessageListCreateView.as_view(), name='message-list-create'),
]
