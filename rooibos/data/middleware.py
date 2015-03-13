from __future__ import absolute_import
import logging

from django.core.exceptions import MiddlewareNotUsed

from .models import get_system_field

log = logging.getLogger('rooibos')


class DataOnStart:

    def __init__(self):

        # initialize system field, so later it does not get created multiple
        # times in a race condition

        get_system_field()

        # Only need to run once
        raise MiddlewareNotUsed
