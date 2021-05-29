from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from achievements.models import Achievement
from achievements.permissions import IsOwner
from achievements.serializers import AchievementSerializer

class AchievementViewSet(viewsets.ModelViewSet):
    queryset = Achievement.objects.all()
    serializer_class = AchievementSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def get_queryset(self):
        """
        This view should return a list of all the purchases
        for the currently authenticated user.
        """
        user = self.request.user
        return Achievement.objects.filter(owner=user)
