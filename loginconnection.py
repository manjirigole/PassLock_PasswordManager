import pymysql
def dbconn(firstname,mkey):
    db = pymysql.connect(host='localhost', user='root', password='Shsss@234', database='reg_form')
    cur = db.cursor()
    query = 'use reg_form'
    cur.execute(query)
    print("database connected")
    try:
        query = 'create table pass(id int not null auto_increment, firstname varchar(40),' \
                'mkey int, primary key(id))'
        cur.execute(query)
    except:
        cur.execute('use reg_form')
        query2 = 'insert into pass(firstname, mkey) values(%s,%s)'
        #print("Inserting user----name--", username, " --lastname--", password, "--mkey--",mkey)
        cur.execute(query2, (firstname,mkey))
        db.commit()
        db.close()