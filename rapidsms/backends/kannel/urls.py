from django.conf.urls import include, re_path
from rapidsms.backends.kannel import views


urlpatterns = (
    re_path(r'^account/', include('rapidsms.urls.login_logout')),
    re_path(r"^delivery-report/$",
            views.DeliveryReportView.as_view(),
            name="kannel-delivery-report"),
    re_path(r"^backend/kannel/$",
            views.KannelBackendView.as_view(backend_name='kannel-backend'),
            name='kannel-backend'),
)
