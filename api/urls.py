from django.urls import include
from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views
from .views import TopicsViewSet
from .views import check_answer

router = DefaultRouter()
router.register(r"api/topics", TopicsViewSet)

urlpatterns = [
    # 关于题目模型的的api接口
    path("", include(router.urls)),

    # ---------------页面所需的数据接口-----------

    path("api/ajax/", views.ajax, name="ajax"),
    path("api/pagination1/<int:pageNo>/", views.pagination1, name="pagination1"),

    # ---------------页面所需的数据接口----------------

    # ------------------工具接口--------------------
    path("api/delay/<int:delay_time>/", views.delay, name="delay"),

    # 延迟多少秒返回结果
    path("api/delay/<int:delay_time>/", views.delay, name="delay"),
    # 返回请求客户端的IP
    path("api/ip/", views.get_client_ip, name="get_client_ip"),
    # 检查答案是否正确
    path("api/check-answer/", check_answer, name="check_answer"),

    path('api/server_time/', views.get_server_time, name='get_server_time'),
    path('api/ua/', views.get_user_agent, name='get_user_agent'),
    path('api/health/', views.health_check, name='health_check'),
    path('api/headers/', views.get_request_headers, name='get_request_headers'),
    path('api/reverse_string/', views.reverse_string, name='reverse_string'),
    path('api/base64_encode/', views.base64_encode, name='base64_encode'),
    path('api/base64_decode/', views.base64_decode, name='base64_decode'),

    # 返回服务器的时间戳，加密格式
    path(
        "api/server-timestamp/", views.get_server_timestamp, name="get_server_timestamp"
    ),
    # ------------------工具接口--------------------

]
