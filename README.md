#  experimental django upgrade - do not use in production


## Django 1.7 upgrade - clone to a new directory, copy the database

This snippet for settings_local can help:

```python
from django import get_version
from distutils.version import StrictVersion

DJANGO_VERSION = StrictVersion(get_version())
DJANGO_16 = StrictVersion('1.6.10')

if DJANGO_VERSION > DJANGO_16:
    DATABASE_NAME = 'rooibos17'
else:
    DATABASE_NAME = 'rooibos'

print('Django version is %s' % DJANGO_VERSION)
print('using database %s' % DATABASE_NAME)

DATABASES = {
    'default': {
        # ...
        'NAME': DATABASE_NAME,
        # ...
        },
    }
}


```

### **Status:** 

#### AttributeError at /data/record/7/arc5262/
##### 'function' object has no attribute 'compile'

Request Method:	**GET**

Request URL:	**http://127.0.0.1:8000/data/record/7/arc5262/**

Django Version:	**1.7.6**

Exception Type:	**AttributeError**

Exception Value:	

**'function' object has no attribute 'compile'**

from __rooibos/contrib/tagging/models.py in usage_for_queryset__

```where, params = queryset.query.where.as_sql(compiler.quote_name_unless_alias, compiler.connection) ```

**This branch has the potential to mess up the database of any existing installation, copy your existing db and use the copy**


### setting up

You my friend, are on your own.
