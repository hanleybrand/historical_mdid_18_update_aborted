from django.db import models
from django.conf import settings
from django.contrib.sites.models import Site

if getattr(settings, 'GOOGLE_ANALYTICS_MODEL', False):
    class Analytics(models.Model):
        site = models.ForeignKey(Site)
        analytics_code = models.CharField(blank=True, max_length=100)

        class Meta:
            db_table = 'google_analytics_analytics'

        def __unicode__(self):
            return u"%s" % (self.analytics_code)
