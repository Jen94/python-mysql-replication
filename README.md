tornado-mysql-replication
========================

```python
from tornado_mysqlreplication import BinLogStreamReader
from tornado import gen, ioloop

@gen.coroutine
def start_mysql_replication():
mysql_settings = {'host': '127.0.0.1', 'port': 3306, 'user': 'root', 'passwd': ''}
stream = BinLogStreamReader(connection_settings = mysql_settings, server_id=100)
for msg in stream:
    msg = yield msg
    print(msg)
stream.close()

def main():
    ioloop.IOLoop.current().run_sync(start_mysql_replication)
    
if __name__ == "main":
    main()
```
