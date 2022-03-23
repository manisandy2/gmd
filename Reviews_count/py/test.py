import sqlite3

con = sqlite3.connect('test.db')

cur = con.cursor()
#
# # Create table
# cur.execute('''CREATE TABLE Google_reviews
#                (date text, name text,  rating real, review real)''')
#
# # Insert a row of data
# cur.execute("INSERT INTO Google_reviews VALUES ('2020-03-05','new_name',100,785)")
#
# # Save (commit) the changes
# con.commit()
#
# # We can also close the connection if we are done with it.
# # Just be sure any changes have been committed or they will be lost.
# con.close()

for row in cur.execute('SELECT * FROM Google_reviews '):
        print(row)
