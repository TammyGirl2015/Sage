from . import views
from django.urls import path
from .views import AddCategoryView, AddReviewView

urlpatterns = [
    path("", views.PostList.as_view(), name="home"),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('category/add/', AddCategoryView.as_view(), name='add_category'),
    path('review/add/', AddReviewView.as_view(), name='add_review'),
]