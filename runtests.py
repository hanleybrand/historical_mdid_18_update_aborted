import sys

try:
    from django.conf import settings

    settings.configure(
        DEBUG=True,
        USE_TZ=True,
        DATABASES={
            'default': {
                'ENGINE': 'django.db.backends.mysql',
                'NAME': 'test_mdid',
                'USER': 'rooibos',
                'PASSWORD': 'rooibos',
                'HOST': '127.0.0.1',
                'PORT': '',
                'OPTIONS': {
                    # MYISAM doesn't support transactions
                    'init_command': 'SET storage_engine=INNODB',
                },
            }
        },
        ROOT_URLCONF="rooibos.urls",
        INSTALLED_APPS=[
            # "django.contrib.contenttypes",
            # "django.contrib.auth",
            # "django.contrib.sites",
            "rooibos",
        ],
        SITE_ID=1,
        NOSE_ARGS=['-s'],
    )

    from django_nose import NoseTestSuiteRunner
except ImportError:
    raise ImportError("To fix this error, run: pip install -r requirements/dev.txt")


def run_tests(*test_args):
    if not test_args:
        test_args = ['tests']

    # Run tests
    test_runner = NoseTestSuiteRunner(verbosity=1)

    failures = test_runner.run_tests(test_args)

    if failures:
        sys.exit(failures)


if __name__ == '__main__':
    run_tests(*sys.argv[1:])