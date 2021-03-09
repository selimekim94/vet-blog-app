from django.urls import path
from .views import BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView, CategoryListView, \
    PostByCategoryView, CategoryCreateView

urlpatterns = [
    path('', BlogListView.as_view(), name='home'),
    path('post/new/', BlogCreateView.as_view(), name='post_new'),
    path('post/<slug:slug>/', BlogDetailView.as_view(), name='post_detail'),
    path('post/<slug:slug>/edit/', BlogUpdateView.as_view(), name='post_edit'),
    path('post/<slug:slug>/delete/', BlogDeleteView.as_view(), name='post_delete'),
    path('category/new/', CategoryCreateView.as_view(), name='category_new'),
    # path('categories/', CategoryListView.as_view(), name='categories'),
    path('category/<int:id>/<slug:slug>/', PostByCategoryView.as_view(), name='post_by_category'),
]
