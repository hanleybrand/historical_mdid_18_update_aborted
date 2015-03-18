from django.db import models
from django.contrib.auth.models import User, Group


class Impersonation(models.Model):
    group = models.ForeignKey(Group, related_name='impersonating_set')
    users = models.ManyToManyField(User,
                                   verbose_name='Allowed users',
                                   related_name='impersonated_set',
                                   blank=True,
                                   db_table='impersonate_impersonation_users')
    groups = models.ManyToManyField(Group,
                                    verbose_name='Allowed groups',
                                    related_name='impersonated_set',
                                    blank=True,
                                    db_table='impersonate_impersonation_groups')
    class Meta:
        db_table = 'impersonate_impersonation'

    def __unicode__(self):
        return self.group.name
