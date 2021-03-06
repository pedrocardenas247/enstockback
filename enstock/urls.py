from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views
from rest_framework_simplejwt.views import TokenVerifyView
from django.conf.urls.static import static
from core.views import MyObtainTokenPairView
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', MyObtainTokenPairView.as_view(), name ='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name ='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('', include('core.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# urlpatterns += [re_path(r'^.*', TemplateView.as_view(template_name='index.html'))]