from django.contrib import admin

from achievements.models import Achievement

class AchievementAdmin(admin.ModelAdmin):
    pass
admin.site.register(Achievement, AchievementAdmin)
