from django.contrib import admin
from django.urls import path, include

from .schema import swagger_urlpatterns


from django.http import HttpResponse
def home(request):
    return HttpResponse("Welcome to BeautyMaker API")

urlpatterns = [
    path("", home, name="home"),
    path("admin/", admin.site.urls),
    path("api/v1/common/", include("apps.common.urls", namespace="common")),
    path("api/v1/users/", include("apps.users.urls", namespace="users")),
    path("api/v1/courses/", include("apps.courses.urls", namespace="courses")),
    path("api/v1/news/", include("apps.news.urls", namespace="news")),
]

# add swagger + redoc here
urlpatterns += swagger_urlpatterns

