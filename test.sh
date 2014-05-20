#!/bin/sh
ROOIBOS_ADDITIONAL_SETTINGS=config.settings_test python manage.py test ${1:-rooibos.access rooibos.converters \
rooibos.data rooibos.federatedsearch  rooibos.presentation rooibos.statistics rooibos.storage \
rooibos.userprofile rooibos.util rooibos.viewers rooibos.workers}

# rooibos.federatedsearch.artstor removed because it's empty
#