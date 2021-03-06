from django.db import models
from django.contrib.auth.models import User


class Preference(models.Model):
    setting = models.CharField(max_length=128)
    value = models.TextField()

    class Meta:
        db_table = 'userprofile_preference'

    def __unicode__(self):
        return "%s=%s" % (self.setting, self.value)


class UserProfile(models.Model):
    # TODO: should this get changed?
    # user = OneToOneField(User, related_name="profile")
    user = models.ForeignKey(User, unique=True)
    preferences = models.ManyToManyField(Preference,
                                         blank=True,
                                         db_table='userprofile_userprofile_preferences')

    class Meta:
        db_table = 'userprofile_userprofile'

    def __unicode__(self):
        return "%s" % self.user
