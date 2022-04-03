from django.urls import path, include

from django.contrib import admin

admin.autodiscover()

import main.views

urlpatterns = [
    path("", main.views.index, name="index"),
#    path("db/", hello.views.db, name="db"),
	path("login/", main.views.login, name="login"),
	path("register/", main.views.register, name="register"),
    path("admin/", admin.site.urls),
]
