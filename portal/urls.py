from django.conf import settings
from django.urls import path, re_path, include, reverse_lazy
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic.base import RedirectView
from rest_framework.routers import DefaultRouter
from users.views import UserViewSet, UserLogIn, UserRegister
from groups.views import GroupViewSet, GroupPostViewSet, GroupPostReactionViewSet
from forms.views import LeaveFormViewSet, InventoryFormViewSet, FineSheetFormViewSet, VerifyFormsRequest



router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'group-posts', GroupPostViewSet)
router.register(r'group-post-reactions', GroupPostReactionViewSet)
router.register(r'leave-forms', LeaveFormViewSet)
router.register(r'inventory-forms', InventoryFormViewSet)
router.register(r'fine-sheet-forms', FineSheetFormViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('api-user-login/', UserLogIn.as_view()),
    path('api-user-register/', UserRegister.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api-verify-forms/', VerifyFormsRequest.as_view({'get': 'list', 'post': 'update'})),
    re_path(r'^$', RedirectView.as_view(url=reverse_lazy('api-root'), permanent=False)),
]