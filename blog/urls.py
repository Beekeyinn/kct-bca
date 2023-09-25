"""
URL configuration for blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from home.views import home, about, contact
from post.views import PostListView, IndexView
from django.conf.urls.static import static
from django.conf import settings
from accounts.views import LoginView, SignUpView, Logout
from home.views import handle_404, handle_unauthorized

urlpatterns = [
    path("admin/", admin.site.urls),
    path("404_error/", handle_404),
    path("unauthorized/", handle_unauthorized),
    path("", IndexView.as_view(), name="index"),
    path("post/list/", PostListView.as_view(), name="post-list"),
    path("contact/", contact, name="contact"),
    path("about", about, name="about"),
    path("login", LoginView.as_view(), name="login"),
    path("logout", Logout.as_view(), name="logout"),
    path("register", SignUpView.as_view(), name="register"),
    path("post/", include("post.urls")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
