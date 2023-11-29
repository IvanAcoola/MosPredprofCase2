from django.urls import path
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserListView

urlpatterns = [
    path('', views.home_view, name="main-home"),
    path('blog/', PostListView.as_view(), name="main-blog"),
    path('post/<int:pk>', PostDetailView.as_view(), name="main-blog-detail"),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name="main-blog-update"),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name="main-blog-delete"),
    path('post/new/', PostCreateView.as_view(), name="main-blog-create"),
    path('user/<str:username>', UserListView.as_view(), name="main-user-posts"),
    path('about/', views.about, name="main-about"),
]
