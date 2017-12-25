import wx
import time
class AMPanel(wx.Panel):
    def __init__(self, parent, question, answer):
        wx.Panel.__init__(self, parent)
        self.__answer = None
        self.parent = parent
        self.__trueAnswer = answer
        self.question = wx.StaticText(self, label="Your question : {}".format(question), pos=(20, 30))

        # A multiline TextCtrl - This is here to show how the events work in this program, don't pay too much attention to it
        self.logger = wx.TextCtrl(self, pos=(300,20), size=(200,300), style=wx.TE_MULTILINE | wx.TE_READONLY)

        # A button
        self.button =wx.Button(self, label="Submit", pos=(200, 90))
        self.Bind(wx.EVT_BUTTON, self.OnClick,self.button)

        # the edit control - one line version.
        self.lblanswer = wx.StaticText(self, label="Your answer :", pos=(20,60))
        self.editanswer = wx.TextCtrl(self, value="", pos=(105, 60), size=(140,-1))
        self.Bind(wx.EVT_TEXT, self.EvtText, self.editanswer)
        #self.Bind(wx.EVT_CHAR, self.EvtChar, self.editanswer)


    def OnClick(self,event):
        #self.logger.AppendText(" Click on object with Id %d\n" %event.GetId())
        if str(self.__answer) == self.__trueAnswer:
            self.logger.AppendText(" Correct!!")
            time.sleep(1)
            self.parent.Hide()
            time.sleep(10*60)
            self.parent.Maximize(True)
        else:
            self.logger.AppendText(" Wrong!!, do it again!")
    def EvtText(self, event):
        self.logger.AppendText('EvtText: %s\n' % event.GetString())
        self.__answer = event.GetString()


