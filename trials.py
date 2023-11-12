import mysql.connector as mysql
mydb = mysql.connect(host='localhost', user='root', passwd='sahal@1234', database='cnn')
mycursor = mydb.cursor()
q = "select * from flower where flower_name = 'Rose'"
mycursor.execute(q)
instructions = mycursor.fetchall()[0]
# mycursor.close()
print(type(instructions[2]))