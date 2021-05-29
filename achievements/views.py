from rest_framework import viewsets

from achievements.models import Achievement
from achievements.serializers import AchievementSerializer

class AchievementViewSet(viewsets.ModelViewSet):
    queryset = Achievement.objects.all()
    serializer_class = AchievementSerializer
