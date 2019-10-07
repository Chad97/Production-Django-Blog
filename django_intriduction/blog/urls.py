#  配置应用层的路由
from django.urls import path, include
#  引入定义的视图文件
import blog.views

urlpatterns = [
    path('hello_wold', blog.views.hello_wold),
    path('test', blog.views.test),
    path('content', blog.views.article_content),
    path('index', blog.views.get_index_page),
    # path('detail', blog.views.detail_index_page),
    path('detail/<int:article_id>', blog.views.detail_index_page),
]
