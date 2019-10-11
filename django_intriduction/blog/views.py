from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from blog.models import Article
# 引入分页组件
from django.core.paginator import Paginator

import json

def hello_wold(resquest):
    return HttpResponse('你好啊 python ! ')


def test(resquest):
    return HttpResponse('<h1>测试 带标签带文件～</h1>')


def article_content(resquest):
    article = Article.objects.all()[0]
    title = article.title
    brief_content = article.brief_content
    content = article.content
    article_id = article.article_id
    publish_date = article.publish_date

    res_srt = '%s, %s, %s, %s, %s' % (title, brief_content, content, article_id, publish_date)

    return HttpResponse(res_srt)


#  文章首页
def get_index_page(request):
    page = request.GET.get('page')
    next_page = None
    if page:
        page = int(page)
    else:
        page = 1

    article_list = Article.objects.all()
    # 参数2 为每页的数量
    p = Paginator(article_list, 3)
    #  总页数
    print(p.num_pages)

    # 防止超出报错
    if page >= p.num_pages:
        page = p.num_pages
    elif page <= 1:
        page = 1

    # 获取第几页list
    page_list = p.page(page)
    # 最近5篇文章 倒序排序
    top5_list = Article.objects.order_by('-publish_date')[:5]
    return render(request,
                  'blog/index.html',
                  {
                      'article_list': page_list,
                      'page_num': range(1, p.num_pages + 1),
                      'previous_page': page - 1,
                      'next_page': page + 1,
                      'top5_list': top5_list,
                      # 传递数据给JavaScript 的 测试
                      'testjson' : json.dumps({'aa':1, 'bb':2})
                  })


# 文章详情
def detail_index_page(request, article_id):
    all_article = Article.objects.all()
    curr_article = None
    previous_article = None
    next_article = None
    # previous_index = 0
    # next_index = 0

    for index, at in enumerate(all_article):
        # if index == 0:
        #     previous_index = 0
        #     next_index = index + 1
        # elif index == len(all_article) -1:
        #     previous_index = index - 1
        #     next_index = index
        # else:
        #     previous_index = index - 1
        #     next_index = index + 1

        if at.article_id == article_id:
            curr_article = at
            previous_article = all_article[0 if index == 0 else index - 1]
            next_article = all_article[index if index == len(all_article) - 1 else index + 1 ]
            break

    content_list = curr_article.content.split('\n')

    return render(request,
                  'blog/detail.html',
                  {
                      'detail_article': curr_article,
                      'content_list': content_list,
                      'previous_article': previous_article,
                      'next_article': next_article
                  })


# 模板和组件测试页面
def muban_page(request):
    pass

    return render(request,
                  'blog/muban_test.html',
                  {
                    'var_muban ': '后端 data'
                  })