from django.urls import path,include,re_path
from . import views

app_name = "landingpage"

urlpatterns = {
    path("",views.index, name="IndexPage"),
    path("AboutPage/",views.AboutPageView.as_view(),name="AboutPage"),
    # path("AboutPage/",views.AboutPage,name="AboutPage"),
}
