from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views import defaults as default_views


from .Users.views import UserSignupView

urlpatterns = [
    # Django Admin, use {% url 'admin:index' %}
    path("admin/", admin.site.urls),
    # User management
    path("accounts/signup/", UserSignupView.as_view(), name="account_signup"),
    path("accounts/", include("allauth.urls")),
    # App
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)