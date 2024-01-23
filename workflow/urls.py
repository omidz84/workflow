from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/workflow/', include('work_flow.api.urls', namespace='workflow'), name='workflow'),
    path('api/user/', include('user.api.urls', namespace='user'), name='user'),

    path('api-auth/', include('rest_framework.urls')),
]
