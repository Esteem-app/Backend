from rest_framework import serializers
from achievements.models import Achievement

class AchievementSerializer(serializers.ModelSerializer):
    readonly_fields = ('created',)
    owner = serializers.HiddenField(
            default=serializers.CurrentUserDefault()
        )

    class Meta:
        model = Achievement
        fields = ('id', 'content', 'owner', 'created')
