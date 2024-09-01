from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class UserInfoSerializer(serializers.ModelSerializer):
    groups = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name'
    )
    permissions = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = [
            'id', 'first_name', 'last_name', 'email', 'username',
            'groups', 'is_superuser', 'is_staff', 'is_active',
            'date_joined', 'last_login', 'permissions'
        ]

    def get_permissions(self, obj):
        return obj.get_all_permissions()
