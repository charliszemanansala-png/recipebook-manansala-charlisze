from django.urls import path, include

app_name = "useraccounts"

urlpatterns = [path("accounts/", include("django.contrib.auth.urls"))]
