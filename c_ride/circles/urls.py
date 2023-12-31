"""Circles URLs."""

# Django
from django.urls import include, path

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from c_ride.circles.views import circles as circle_views
from c_ride.circles.views import memberships as membership_views

app_name = "circles"

router = DefaultRouter()
router.register(
    r"",
    circle_views.CircleViewSet,
    basename="circle",
)


urlpatterns = [
    path("", include((router.urls, app_name))),
    path(
        "<slug:slug_name>/members/",
        membership_views.MembershipViewSet.as_view(
            {"get": "list", "post": "create"}
        ),
        name="members_list",
    ),
    path(
        "<slug:slug_name>/members/<str:name>/",
        membership_views.MembershipViewSet.as_view(
            {"get": "retrieve", "delete": "destroy"}
        ),
        name="member_detail",
    ),
    path(
        "<slug:slug_name>/members/<str:name>/invitations/",
        membership_views.MembershipViewSet.as_view({"get": "invitations"}),
        name="invitations",
    ),
]
