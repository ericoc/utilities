from rest_framework.serializers import ModelSerializer


class APIUtilitySerializer(ModelSerializer):
    """Base Django-Rest-Framework (DRF) utility usage API model serializer."""
    class Meta:
        fields = "__all__"
