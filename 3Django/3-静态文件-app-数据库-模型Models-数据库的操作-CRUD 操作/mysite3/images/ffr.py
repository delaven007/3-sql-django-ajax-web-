import pymysql

db = pymysql.connect(user='root',
                     passwd='123456',
                     database='dict',
                     charsrt='utf8')
cur = db.cursor()
sql ="insert into words (word,name) values (%s,%s)"

for line in f:
    tup =re.findall(r'(\s+)\s+(.*)',line)[0]
    try:
    cur.execute(sql)
    db.commit()
    except:
    db.rollback()
