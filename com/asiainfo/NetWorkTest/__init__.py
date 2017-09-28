#coding=gbk
import wx
import sys
import socket

class mainFrame(wx.Frame):
    def __init__(self,parent,title):
        super(mainFrame,self).__init__(parent,title = title,size = (300,200))
        self.Start()

    def Start(self):
        panel = wx.Panel(self)
        self.label = wx.StaticText(panel,label="������ip��ַ���˿�:",pos = (10,15))
        self.readIP = wx.TextCtrl(panel,value = "10.113.133.240", pos = (10,50))
        self.read = wx.TextCtrl(panel,value = "13080",pos = (140,50),size = (50,25))
        self.button = wx.Button(panel,label = "��ʼ����",pos = (10,100))
        self.Bind(wx.EVT_BUTTON,self.NetTest)
        self.Centre()
        self.Show(True)

    def NetTest(self,e):
        #self.label1 = wx.StaticText(self.panel,label="�����У����Ժ󡭡�",pos = (50,100))
        #wx.MessageBox("���ڲ��ԣ����Ժ򡭡�","���Խ��",wx.OK | wx.ICON_INFORMATION)
        # progressMax = 1
        # dialog = wx.ProgressDialog("�����У����Ժ򡭡�","�����У����Ժ򡭡�",progressMax )
        # keep = True
        # count = 0
        IPstr = self.readIP.GetValue()
        str = self.read.GetValue()
        #
        # while keep and count < progressMax:
        #     count += 1
        #     wx.Sleep(1)
        #     keep = dialog.Update(count)
        # dialog.Destroy()

        try:
            skt = socket.socket()
            skt.connect((IPstr,int(str)))
            wx.MessageBox("����˿ڲ���ͨ����","���Խ��",wx.OK | wx.ICON_INFORMATION)
            skt.close()
        except socket.error,e:
            wx.MessageBox("����˿ڲ�������ʧ�ܣ�","���Խ��",wx.OK | wx.ICON_ERROR)

app = wx.App()
mainFrame(None,'����˿����Ӳ��Գ���')
app.MainLoop()