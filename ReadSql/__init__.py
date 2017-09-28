#coding=utf-8

def main():
    file = open("sql.txt")
    outfile = open("res.txt",'w')
    for line in file:
        if "insert into" in line:
            outfile.write("insert||" + line)
        elif "INSERT INTO" in line:
            outfile.write("insert||" + line)
        elif "DELETE FROM" in line:
            outfile.write("delete||" + line)
        elif "delete from" in line:
            outfile.write("delete||" + line)
        elif "update" in line:
            outfile.write("update||" + line)
        elif "UPDATE" in line:
            outfile.write("update||" + line)
        elif "CREATE TABLE" in line:
            outfile.write("create||" + line)
        elif "create table" in line:
            outfile.write("create||" + line)
        elif "merge into" in line:
            outfile.write("merge into||" + line)
        elif "MERGE INTO" in line:
            outfile.write("merge into||" + line)
main()

        # proc_name = lis[0]
        # step_seq = lis[1]
        # s_step = lis[2]
        # f_step = lis[3]
        # n_step = lis[4]
        # step_name = lis[5]
        # step_type = lis[6]
        # step_code = lis[7]
        # sql_text = lis[8]
        # dbname = lis[9]
        # areacode = lis[10]