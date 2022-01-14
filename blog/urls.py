from django.urls import path
from .views import BlogListView, BlogDetailView, BlogStoreView, BlogUpdateView, BlogDeleteView

app_name = 'blog'

urlpatterns = [
    path('', BlogListView.as_view(), name='index'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name='show'),
    path('post/<int:pk>/edit', BlogUpdateView.as_view(), name='update'),
    path('post/<int:pk>/delete', BlogDeleteView.as_view(), name='delete'),
    path('post/new', BlogStoreView.as_view(), name='store')
]
