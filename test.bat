@setlocal
@set ROOIBOS_ADDITIONAL_SETTINGS=config.settings_test
@set apps=%*
@if "%apps%" == "" set apps=rooibos.access rooibos.converters rooibos.data rooibos.federatedsearch rooibos.presentation rooibos.statistics rooibos.storage rooibos.userprofile rooibos.util rooibos.viewers rooibos.workers
manage.py test %apps%
@endlocal
