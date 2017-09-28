#coding=utf-8

class people():
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def instr(self):
        print "我的名字是" + self.name + "我的年龄是" + self.age

people(name = "杨",age = "21").instr()