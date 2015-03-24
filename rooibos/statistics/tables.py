from __future__ import absolute_import

import django_tables2 as tables

from rooibos.userprofile.models import User

from .models import Activity


class ActivityTable(tables.Table):
    date = tables.DateColumn()
    time = tables.TimeColumn()
    user_field = tables.Column(verbose_name='username')
    event = tables.Column()
    data_field = tables.Column()

    class Meta:
        model = Activity
        fields = ("date", "time", "user_field", "event", "data_field")
        order_by = ("-date", "-time")
        attrs = {"class": "paleblue"}

    def render_username(self):
        return User.models.get(id=self.user_field).username

    # model ref
    # class Activity(models.Model):
    # content_type = models.ForeignKey(ContentType, null=True)
    # object_id = models.PositiveIntegerField(null=True, db_index=True)
    # content_object = generic.GenericForeignKey('content_type', 'object_id')
    # user_field = models.ForeignKey(User, null=True, blank=True, db_column='user_id')
    # date = models.DateField(db_index=True)
    # time = models.TimeField()
    # event = models.CharField(max_length=64, db_index=True)
    # data_field = models.TextField(blank=True, db_column='data')