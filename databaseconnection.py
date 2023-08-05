import pymysql
def dbconn(name,last_name,password,confirm):

    db = pymysql.connect(host='localhost', user='root', password='Shsss@234', database='reg_form')
    cur = db.cursor()
    try:
        query = 'create database reg_form'
        cur.execute(query)
        query = 'use reg_form'
        cur.execute(query)
        query = 'create table users(id int not null auto_increment, firstname varchar(40),' \
                'lastname varchar(40), password varchar(60), cpass varchar(60),primary key(id))'
        cur.execute(query)
    except:
        cur.execute('use reg_form')
        query = 'insert into users(firstname, lastname, password, cpass) values(%s,%s,%s,%s)'
        print("Inserting user----name--", name, " --lastname--", last_name, "--password--", password, "--confirm--", confirm)
        cur.execute(query, (name, last_name, password, confirm))
        db.commit()
        db.close()
        #messagebox.showinfo('success', 'successful connection')
