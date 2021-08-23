from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('posts/<int:pk>/', views.post_detail, name='post_detail'),
    path('<int:pk>/comment', views.comment, name='comment'),
    path('create_post/', views.create_post, name='create_post'),
    path('edit_post/<int:pk>/', views.edit_post, name='edit_post'),
    path('delete_post/<int:pk>/', views.delete_post, name='delete_post'),
    path('delete_commment/<int:pk>/', views.delete_comment, name='delete_comment'),
    
    # rest framework urls
    path('api/posts/', views.PostListView.as_view(), name='list-view'),
    path('api/posts/<int:pk>/', views.PostDetailView.as_view(), name='detail-view'),
    path('api/authors/', views.AuthorListView.as_view(), name='list-view'),
    path('api/authors/<int:pk>/', views.AuthorDetailView.as_view(), name='detail-view'),
    
    
    
]
