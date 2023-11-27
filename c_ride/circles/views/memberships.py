"""Circle membership views."""

# Django REST Framework
from rest_framework import mixins, viewsets
from rest_framework.generics import get_object_or_404

# Permissions
from rest_framework.permissions import IsAuthenticated

# Models
from c_ride.circles.models import Circle, Membership
from c_ride.circles.permissions import IsActiveCircleMember

# Serializers
from c_ride.circles.serializers import MembershipModelSerializer


class MembershipViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    """Circle membership view set."""

    serializer_class = MembershipModelSerializer

    def dispatch(self, request, *args, **kwargs):
        """Verify that the circle exists."""
        slug_name = kwargs["slug_name"]
        self.circle = get_object_or_404(Circle, slug_name=slug_name)
        return super().dispatch(request, *args, **kwargs)

    def get_permissions(self):
        """Assign permissions based on action."""
        permissions = [IsAuthenticated, IsActiveCircleMember]
        return [p() for p in permissions]

    def get_queryset(self):
        """Return circle members."""
        return Membership.objects.filter(circle=self.circle, is_active=True)

    def get_object(self):
        """Return the circle member by using the user's name."""
        return get_object_or_404(
            Membership,
            user__name=self.kwargs["name"],
            circle=self.circle,
            is_active=True,
        )

    def perform_destroy(self, instance):
        """Disable membership."""
        instance.is_active = False
        instance.save()