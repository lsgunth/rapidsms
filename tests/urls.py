from django.urls import include, re_path
from django.contrib import admin

from rapidsms import views as rapidsms_views

admin.autodiscover()

urlpatterns = (
    re_path(r'^admin/', admin.site.urls),

    # RapidSMS core URLs
    re_path(r'^account/', include('rapidsms.urls.login_logout')),
    re_path(r'^$', rapidsms_views.dashboard, name='rapidsms-dashboard'),

    # RapidSMS contrib app URLs
    re_path(r'^httptester/', include('rapidsms.contrib.httptester.urls')),
    re_path(r'^messagelog/', include('rapidsms.contrib.messagelog.urls')),
    re_path(r'^messaging/', include('rapidsms.contrib.messaging.urls')),
    re_path(r'^registration/', include('rapidsms.contrib.registration.urls')),

    # Third party URLs
    re_path(r'^selectable/', include('selectable.urls')),
)
