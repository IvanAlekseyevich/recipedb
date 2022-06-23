import psycopg2

conn = psycopg2.connect("host=db dbname=postgres user=postgres password=postgres")
cur = conn.cursor()
with open('recipes_ingredient.txt', 'r', encoding="utf-8") as f:
    next(f)
    cur.copy_from(f, 'recipes_ingredient', sep='|')
conn.commit()

with open('users_user.txt', 'r', encoding="utf-8") as f:
    next(f)
    cur.copy_from(f, 'users_user', sep='|')
conn.commit()

with open('recipes_tag.txt', 'r', encoding="utf-8") as f:
    next(f)
    cur.copy_from(f, 'recipes_tag', sep='|')
conn.commit()
