import mysql.connector


# class Connection():
def mysql_connect():
    mydb = mysql.connector.connect(
        host='localhost',
        user='root',
        password='1234!@#$',
        port='3306',
        database='project'
    )
    return mydb


def search_data(self, link):
    mydb1 = mysql_connect()
    mycursor1 = mydb1.cursor()
    # link = "www.voting-yahoo.com"
    mycursor1.execute('SELECT DISTINCT * FROM fake_urls where domain=%s', [link])
    users = mycursor1.fetchall()

    # for user in users:
    #   print(user)

    return users


def profile_data(self):
    name = self.root.get_screen('profile1').ids.name.text
    mail = self.root.get_screen('profile1').ids.mail.text
    mydb2 = mysql_connect()
    mycursor2 = mydb2.cursor()

    mycursor2.execute('SELECT DISTINCT email_id FROM profile where email_id=%s', [mail])
    users1 = mycursor2.fetchall()
    user = ['']
    for user in users1:
        pass

    if user[0] == mail:
        mycursor2.execute('UPDATE profile SET name=%s WHERE email_id=%s', [name, mail])
        mydb2.commit()
    else:
        mycursor2.execute('INSERT INTO profile(email_id,name) VALUES(%s,%s)', [mail, name])
        mydb2.commit()

# p1 = Connection()
# p1.connect()
