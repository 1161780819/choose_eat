#coding=gbk
import wx
import random
import logging

class mainFrame(wx.Frame):
    time = ""
    aa = "���ѡ������"
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
        str = "���ѡ��Է�ѡ�" + self.readChoose()
        panel = wx.Panel(self)
        self.label = wx.StaticText(panel,label = "��ѡ��Է�ʱ��",pos = (10,10))
        self.button1 = wx.RadioButton(panel,1,label = '����',pos = (10,40),style = wx.RB_GROUP)
        self.button2 = wx.RadioButton(panel,2,label = '����',pos = (60,40))
        self.chooses = wx.StaticText(panel,label = str,pos = (10,70),size = (400,20))
        self.buto = wx.Button(panel,label = "��ʼ���",pos = (10,100))
        self.Bind(wx.EVT_RADIOBUTTON,self.OnRadiogroup)
        self.Bind(wx.EVT_BUTTON,self.startchoose)
        self.Centre()
        self.Show(True)

    def OnRadiogroup(self,e):
        rb = e.GetEventObject()
        self.time = rb.GetLabel()

    def readChoose(self):
        try:
            file = open("�˵�.txt",'r')
            Clist = ""
            for i in file:
                Clist = Clist + i
            file.close()
            return Clist
        except IOError,e:
            wx.MessageBox("�˵��ļ�û�ҵ���","������Ϣ",wx.OK| wx.ICON_ERROR)

    def startchoose(self,e):
        str = self.readChoose()
        result = str.split("|")
        num = random.randint(0,len(result)-1)
        wx.MessageBox(result[num],"���ѡ����",wx.OK | wx.ICON_INFORMATION)
        self.logger.info(result[num])

app = wx.App()
mainFrame(None,'���ѡ��Է���ʽ')
app.MainLoop()