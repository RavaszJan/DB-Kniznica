import psycopg2
conn=psycopg2.connect(
    dbname="bmuomgsubfezvhmd6yds",
    user="ujmxnu7y1aakiwkktf6x",
    password="a1eJVsU85ceBGqpoTrqo6mPVgYX9K1",
    host="bmuomgsubfezvhmd6yds-postgresql.services.clever-cloud.com",
    port="50013"
)
print(conn)
cursor=conn.cursor()
print(cursor)

# cursor.execute("SELECT*FROM authors")
# autori=cursor.fetchall()
#
# print(autori)

cursor.execute("SELECT*FROM authors ORDER BY author_id DESC")
prvy_autor=cursor.fetchone()
print(prvy_autor)



class Author:

    def __init__(self,ID,name,text):
        self.ID=ID
        self.name=name
        self.text=text

    def __str__(self):
        return f'---AUTHOR--- \nID Author:{self.ID}\nMeno:{self.name} \nBio:{self.text}'



author=Author(prvy_autor[0],prvy_autor[1],prvy_autor[2])
print(author)

# print(str(author))



cursor.close()
conn.close()

