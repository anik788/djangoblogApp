from django.urls import path
# from blog.views import home, post_list, post_detail, post_create, post_update, post_delete,
from blog.views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

app_name = 'blog'

urlpatterns = [
    path('post-list/', PostListView.as_view(), name='post_list'),
    path('post-detail/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post-create/', PostCreateView.as_view(), name='post_create'),
    path('post-update/<int:pk>/', PostUpdateView.as_view(), name='post_update'),
    path('post-delete/<int:pk>/', PostDeleteView.as_view(), name='post_delete'),
]

# path('', home),
#     path('post-create/', post_create, name='post_create'),
#     path('post-update/<int:post_id>/', post_update, name='post_update'),
#     path('post-delete/<int:post_id>/', post_delete, name='post_delete'),
