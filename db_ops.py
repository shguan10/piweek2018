import psycopg2
import datetime


def update_django(item_name, is_insert, user_id):
  conn = psycopg2.connect("dbname=snowflake user=snowflake password=snowflake")
  cursor = conn.cursor()

  is_fail = False
  try:
    if is_insert:
      cursor.execute("INSERT INTO \"snowflake_item\" VALUES (default, %s, %s, (select id from \"snowflake_fridge\" where \"user_id\"=%s))", (item_name, datetime.datetime.now(), user_id));
    else:
      cursor.execute("DELETE FROM \"snowflake_item\" WHERE id=(select id from \"snowflake_item\" where name=%s and fridge_id=(select id from \"snowflake_fridge\" where \"user_id\"=%s) limit 1)", (item_name, user_id));
    conn.commit()
  except psycopg2.Error as e:
    is_fail = True
    print(e.pgcode + " " + e.pgerror)

  cursor.close()
  conn.close()
  return not is_fail;
