"""Circle serializers."""

from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from c_ride.circles.models import Circle


class CircleSerializer(serializers.Serializer):
    """Circle serializer."""

    name = serializers.CharField()
    slug_name = serializers.SlugField()
    rides_offered = serializers.IntegerField()
    rides_taken = serializers.IntegerField()
    members_limit = serializers.IntegerField()


class CreateCircleSerializer(serializers.Serializer):
    """Create circle serializer."""

    name = serializers.CharField(max_length=140)
    slug_name = serializers.SlugField(
        max_length=40,
        validators=[UniqueValidator(queryset=Circle.objects.all())],
    )
    about = serializers.CharField(max_length=255, required=False)

    def create(self, validated_data):
        """Create circle."""
        return Circle.objects.create(**validated_data)