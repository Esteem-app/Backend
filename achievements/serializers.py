from rest_framework import serializers
from achievements.models import Achievement

class AchievementSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(
            default=serializers.CurrentUserDefault()
        )

    class Meta:
        model = Achievement
        fields = ('id', 'content', 'owner', 'created')
        read_only_fields = ('created',)


