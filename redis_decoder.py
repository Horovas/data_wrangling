import redis
import typing
import pyodbc
from credentials import server, database, login, password

connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
							f'SERVER={server};'
							f'DATABASE={database};'
							f'UID={login};'
							f'PWD={password}')

cursor = connection.cursor()

cursor_redis = redis.Redis(host="redis-host.myserver.com", port=6379, db=0, decode_responses=True)

trigger_id = 13827   # main variable
users = 0
all_events_set = set()
all_list = []


def clean_str(data: typing.Union[bytes, str]):
    delete_from_str = (' ', '[', ']')
    if isinstance(data, bytes):
        data = data.decode('utf-8')
    for symbol in delete_from_str:
        data = data.replace(symbol, '')
    return data


user_list = cursor_redis.keys(pattern=f"{trigger_id}_*") # >keys *15245_*   triggerId_userId

for user in user_list:
    bytes_line = cursor_redis.get(name=user)

# for bytes_line in text:
    users += 1
    int_list = []
    line = clean_str(bytes_line)
    for i in line.split(','):
        x = int(i)
        int_list.append(x)
        all_events_set.add(x)
        all_list.append(x)

print(f'Users: {users}')
print(f'All events counter: {len(all_events_set)}')
print(all_events_set)
print(f'All list: {len(all_list)}')
print('Events stats')

for unique in all_events_set:
    cursor.execute(f'''
            SELECT name 
            FROM schema1.trigger_user_event_log 
            WHERE object_id = {unique}
        ''')
    show_name = cursor.fetchone()
    print(unique, end='\t')
    print(round(all_list.count(unique) * 100 / users), '%', sep='', end='\t')
    print(all_list.count(unique), 'шт', sep=' ', end='\t')
    print(show_name[0], sep=' ')



cursor.close()
connection.close()

cursor_redis.close()

