from rest_framework import serializers
from achievements.models import Achievement

class AchievementSerializer(serializers.ModelSerializer):
    readonly_fields = ('created',)
    class Meta:
        model = Achievement
        fields = ('id', 'content', 'owner', 'created')
