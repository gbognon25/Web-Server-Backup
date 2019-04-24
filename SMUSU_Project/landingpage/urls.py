from django.urls import path,include,re_path
from . import views

app_name = "landingpage"

urlpatterns = [
    path("",views.index, name="IndexPage"),
    re_path(r"^AboutPage/$",views.AboutPageView.as_view(),name="AboutPage"),
    re_path(r"^ContributionPage/$",views.ContributionPageView.as_view(),name="ContributionPage"),
]
