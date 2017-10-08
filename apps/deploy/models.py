# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import uuid
from django.db import models
from django.db.models.signals import post_save

class DeployPlan(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField(null=True, blank=True)
    code = models.CharField(max_length=255, default = uuid.uuid4)
    auth_key = models.CharField(max_length=255, default = uuid.uuid4)
    is_active = models.BooleanField(default=False)
    
    def __unicode__(self):
        return self.name
    
class DeployLog(models.Model):
    plan = models.ForeignKey('deploy.DeployPlan')
    deploy_date = models.DateTimeField(auto_now_add=True)
    
    def __unicode__(self):
        return self.plan.code

def send_deploy_plan(sender, **kwargs):
    from channels import Group
    log = kwargs["instance"]
    Group(log.plan.code).send({"text": 'deploy'})
    
post_save.connect(send_deploy_plan, sender=DeployLog)