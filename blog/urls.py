from django.urls import path
from . import views
from . views import all_posts

urlpatterns = [
    # 게시물 생성을 위한 URL 패턴
    path('blog/create/', views.create, name='create'),
    # 게시물 상세 페이지를 위한 URL 패턴
    path('blog/<int:blog_id>/', views.detail, name='detail'),
    # 내가 작성한 게시물 목록을 위한 URL 패턴
    path('all_posts/', all_posts, name='all_posts'),
]
