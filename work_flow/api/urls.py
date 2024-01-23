from rest_framework.routers import DefaultRouter

from .views import RequestView, ResponseView

app_name = 'workflow'

router = DefaultRouter()
router.register('response', ResponseView, basename='response')
router.register('', RequestView, basename='request')

urlpatterns = [
]

urlpatterns += router.urls
