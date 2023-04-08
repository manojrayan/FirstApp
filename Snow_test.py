import snowflake.connector

ctx = snowflake.connector.connect(
user='manojrayan',
password='Jmr123#open',
account='VN92705.us-east-2'
)
cs = ctx.cursor()
try:
    cs.execute("SELECT current_version()")
    one = cs.fetchone()
    print(one[0])
finally:
    cs.close()