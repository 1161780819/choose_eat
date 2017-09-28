#coding=gbk
import wx
import random
import logging

class mainFrame(wx.Frame):
    time = ""
    aa = "随机选择结果："
    log_file = 'chooseinfo.txt'
    logger = logging.getLogger('mainFrame')
    logger.setLevel(logging.INFO)
    hander = logging.FileHandler(log_file)
    hander.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s-%(message)s')
    hander.setFormatter(formatter)
    logger.addHandler(hander)
    def __init__(self,parent,title):
        super(mainFrame,self).__init__(parent,title = title,size = (400,200))
        self.Start()

    def Start(self):
        str = "随机选择吃饭选项：" + self.readChoose()
        panel = wx.Panel(self)
        self.label = wx.StaticText(panel,label = "请选择吃饭时间",pos = (10,10))
        self.button1 = wx.RadioButton(panel,1,label = '中午',pos = (10,40),style = wx.RB_GROUP)
        self.button2 = wx.RadioButton(panel,2,label = '晚上',pos = (60,40))
        self.chooses = wx.StaticText(panel,label = str,pos = (10,70),size = (400,20))
        self.buto = wx.Button(panel,label = "开始随机",pos = (10,100))
        self.Bind(wx.EVT_RADIOBUTTON,self.OnRadiogroup)
        self.Bind(wx.EVT_BUTTON,self.startchoose)
        self.Centre()
        self.Show(True)

    def OnRadiogroup(self,e):
        rb = e.GetEventObject()
        self.time = rb.GetLabel()

    def readChoose(self):
        try:
            file = open("菜单.txt",'r')
            Clist = ""
            for i in file:
                Clist = Clist + i
            file.close()
            return Clist
        except IOError,e:
            wx.MessageBox("菜单文件没找到！","错误信息",wx.OK| wx.ICON_ERROR)

    def startchoose(self,e):
        str = self.readChoose()
        result = str.split("|")
        num = random.randint(0,len(result)-1)
        wx.MessageBox(result[num],"随机选择结果",wx.OK | wx.ICON_INFORMATION)
        self.logger.info(result[num])

app = wx.App()
mainFrame(None,'随机选择吃饭方式')
app.MainLoop()