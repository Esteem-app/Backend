from rest_framework import routers

from achievements import views as achiev_views

router = routers.DefaultRouter()
router.register(f'achievements', achiev_views.AchievementViewSet)
