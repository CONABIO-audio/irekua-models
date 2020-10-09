from django.conf.urls import url, include
from django.contrib import admin


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(
        r'^models/',
        include(('irekua_models.urls', 'irekua_models'))
    ),
]
