from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet


router_constructor_api_v1 = (
    ('follow', FollowViewSet, 'follow'),
    ('posts', PostViewSet, 'post'),
    ('groups', GroupViewSet, 'group'),
    (r'posts/(?P<post_id>\d+)/comments', CommentViewSet, 'comment')
)
router_api_v1 = DefaultRouter()

for url_prefix, view_set, base_name in router_constructor_api_v1:
    router_api_v1.register(url_prefix, view_set, basename=base_name)

urlpatterns = [
    path('v1/', include('djoser.urls.jwt')),
    path('v1/', include(router_api_v1.urls)),
]
