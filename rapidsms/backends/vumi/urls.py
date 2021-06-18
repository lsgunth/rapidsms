from django.conf.urls import include, re_path
from rapidsms.backends.vumi import views


urlpatterns = (
    re_path(r'^account/', include('rapidsms.urls.login_logout')),
    re_path(r"^backend/vumi/$",
            views.VumiBackendView.as_view(backend_name='vumi-backend'),
            name='vumi-backend'),
)
