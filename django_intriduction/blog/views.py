from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from blog.models import Article

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
    article_list = Article.objects.all()
    return render(request,
                  'blog/index.html',
                  {'article_list': article_list}
                  )


# 文章详情
def detail_index_page(request, article_id):
    all_article = Article.objects.all()
    curr_article = None
    for at in all_article:
        if at.article_id == article_id:
            curr_article = at
            break

    content_list = curr_article.content.split('\n')

    return render(request,
                  'blog/detail.html',
                  {
                      'detail_article': curr_article,
                      'content_list': content_list
                  }
                  )
