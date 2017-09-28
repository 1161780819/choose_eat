#coding=utf-8
file = open("sql.txt",'r')
files = open("res.txt",'w')
list = []
str = ""
for line in file:
    if line.endswith("|\n"):
        list.append(str + line[:-1])
    else:
        str += line
file.close()

def deal(sql):
    line = sql
    res = ""
    if "insert into" in line:
        res += "insert||" + line
    elif "INSERT INTO" in line:
        res += "insert||" + line
    elif "DELETE FROM" in line:
        res += "delete||" + line
    elif "delete from" in line:
        res += "delete||" + line
    elif "update" in line:
        res += "update||" + line
    elif "UPDATE" in line:
        res += "update||" + line
    elif "CREATE TABLE" in line:
        res += "create||" + line
    elif "create table" in line:
        res += "create||" + line
    elif "merge into" in line:
        res += "merge into||" + line
    elif "MERGE INTO" in line:
        res += "merge into||" + line
    elif "drop table" in line:
        res += "drop table||" + line
    elif "DROP TABLE" in line:
        res += "drop table||" + line
    return res

for i in range(len(list)):
    data = list[i].split("|")
    proc_name = data[0]
    step_seq = data[1]
    step_name = data[5]
    sql_text = data[8]
    res = deal(sql_text)
    if res != "":
        files.write(res)
