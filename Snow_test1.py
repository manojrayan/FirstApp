#!/usr/bin/env pyth
import snowflake.connector

# Gets the version
ctx = snowflake.connector.connect(
    user='manojrayan',
    password='Jmr123#open',
    account='SQBCIFA-DE78525'
    )
cs = ctx.cursor()
try:
    cs.execute("SELECT current_version()")
    one_row = cs.fetchone()
    print(one_row[0])
finally:
    cs.close()
ctx.close()