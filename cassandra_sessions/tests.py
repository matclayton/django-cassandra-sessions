r"""
>>> from django.conf import settings
>>> from cassandra_sessions import SessionStore as CassandraSession

>>> cassandra_session = CassandraSession()
>>> cassandra_session.modified
False
>>> cassandra_session.get('cat')
>>> cassandra_session['cat'] = "dog"
>>> cassandra_session.modified
True
>>> cassandra_session.pop('cat')
'dog'
>>> cassandra_session.pop('some key', 'does not exist')
'does not exist'
>>> cassandra_session.save()
>>> cassandra_session.exists(cassandra_session.session_key)
True
>>> cassandra_session.delete(cassandra_session.session_key)
>>> cassandra_session.exists(cassandra_session.session_key)
False

>>> cassandra_session['foo'] = 'bar'
>>> cassandra_session.save()
>>> cassandra_session.exists(cassandra_session.session_key)
True
>>> prev_key = cassandra_session.session_key
>>> cassandra_session.flush()
>>> cassandra_session.exists(prev_key)
False
>>> cassandra_session.session_key == prev_key
False
>>> cassandra_session.modified, cassandra_session.accessed
(True, True)
>>> cassandra_session['a'], cassandra_session['b'] = 'c', 'd'
>>> cassandra_session.save()
>>> prev_key = cassandra_session.session_key
>>> prev_data = cassandra_session.items()
>>> cassandra_session.cycle_key()
>>> cassandra_session.session_key == prev_key
False
>>> cassandra_session.items() == prev_data
True
"""

if __name__ == '__main__':
    import os
    os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
    import doctest
    doctest.testmod()
