from django.contrib import admin

# Register your models here.
# 在Admin 里面注册我们定义的模型
from .models import Article
admin.site.register(Article)