from rest_framework.routers import DefaultRouter

from .views import UserView, GroupView

app_name = 'user'

router = DefaultRouter()
router.register('group', GroupView, basename='group')
router.register('', UserView, basename='user')

urlpatterns = [
]

urlpatterns += router.urls
