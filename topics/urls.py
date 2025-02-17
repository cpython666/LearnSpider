from django.urls import path
from . import views
from django.urls import path
from .views import topic_view

urlpatterns = [
    path("", views.index, name="index"),
    path("list", views.list, name="list"),
    path("tools", views.tools, name="tools"),
    path("shorthand", views.shorthand, name="shorthand"),
    path("solutions", views.solutions, name="solutions"),
    # ------------------ 试金场 -----------------
    path("sandbox/", views.sandbox, name="sandbox"),
    path("sandbox/news/", views.sandbox_news, name="sandbox_news"),
    path("sandbox/news/search/", views.sandbox_news, name="sandbox_news_search"),
    path(
        "sandbox/news/about/", views.sandbox_news_about_us, name="sandbox_news_about_us"
    ),  # 关于我们页面
    path("sandbox/news/notice/", views.sandbox_news_notice, name="sandbox_news_notice"),
    path(
        "sandbox/news/category/",
        views.sandbox_news_category,
        name="sandbox_news_category",
    ),
    path(
        "sandbox/news/category/<slug:slug>/",
        views.sandbox_news_category_detail,
        name="sandbox_news_category_detail",
    ),
    # 详情页面路由
    path(
        "sandbox/news/source/<slug:slug>/",
        views.sandbox_news_source_detail,
        name="sandbox_news_source_detail",
    ),
    # path('news/category/<slug:slug>/', views.category_detail, name='category_detail'),
    path("sandbox/news/hot/", views.sandbox_news_hot, name="sandbox_news_hot"),
    path(
        "sandbox/news/hot/<slug:slug>/",
        views.sandbox_news_hot_detail,
        name="sandbox_news_hot_detail",
    ),
    path("sandbox/news/category/technology/", views.sandbox_news, name="sandbox_news"),
    path("sandbox/news/category/web3/", views.sandbox_news, name="sandbox_news"),
    path(
        "sandbox/news/news_detail/<int:id>/",
        views.sandbox_news_detail,
        name="sandbox_news_detail",
    ),
    # ------------------------------------------
    # topic开头重定向到视图返回/html
    path("page/<str:response_path>/", topic_view, name="topic_view"),
    # 请求视图类型
    path("view/hello-spider/", views.hello_spider, name="request_twice"),
    path("view/request-twice/", views.request_twice, name="request-twice"),
    path("view/ua/", views.ua, name="ua"),
    path("view/encode/", views.encode_page, name="encode"),
    path("view/table/", views.table, name="table"),
    # 混合请求接口类型
    path("demo/", views.demo),
    path("demo1/", views.demo1),
]
