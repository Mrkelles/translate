from rest_framework import serializers

class UserInfoSerializer(serializers.Serializer):
    info = serializers.ListField(
        child=serializers.CharField(max_length=100)
    )
