# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from deploy.models import DeployLog, DeployPlan

def deploy(modeladmin, request, queryset):
    for plan in queryset:
        DeployLog.objects.create(
            plan = plan
        )

class DeployPlanAdmin(admin.ModelAdmin):
    list_display = ['name', 'code', 'auth_key', 'is_active']
    readonly_fields = ['code', 'auth_key']
    actions = [deploy, ]

class DeployLogAdmin(admin.ModelAdmin):
    list_display = ['plan', 'deploy_date']

admin.site.register(DeployPlan, DeployPlanAdmin)
admin.site.register(DeployLog, DeployLogAdmin)
