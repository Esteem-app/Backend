from django.contrib import admin

from achievements.models import Achievement

class AchievementAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)


admin.site.register(Achievement, AchievementAdmin)

