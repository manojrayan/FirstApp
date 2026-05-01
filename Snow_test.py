import snowflake.connector

ctx = snowflake.connector.connect(
user='xxxxxx',
password='xxxxxxx',
account='VN92705.us-east-2'
)
cs = ctx.cursor()
try:
    cs.execute("SELECT current_version()")
    one = cs.fetchone()
    print(one[0])
finally:
    cs.close()
