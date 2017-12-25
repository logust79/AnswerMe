import wx
import time
class AMPanel(wx.Panel):
    def __init__(self, parent, question_generator, grade):
        wx.Panel.__init__(self, parent)
        self.__answer = None
        self.parent = parent
        
        # generate question and answer
        self.question_generator = question_generator
        self.grade = grade
        question, answer, err = question_generator(grade)
        if err:
            raise ValueError(err)
        self.__trueAnswer = answer
        self.question = wx.StaticText(self, label="Your question : {}".format(question), pos=(20, 30))

        # A log
        self.logger = wx.TextCtrl(self, pos=(300,20), size=(200,300), style=wx.TE_MULTILINE | wx.TE_READONLY)

        # A submit button
        self.button =wx.Button(self, label="Submit", pos=(200, 90))
        self.Bind(wx.EVT_BUTTON, self.OnClick,self.button)

        # the edit control - one line version.
        self.lblanswer = wx.StaticText(self, label="Your answer :", pos=(20,60))
        self.editanswer = wx.TextCtrl(self, value="", pos=(105, 60), size=(140,-1))
        self.Bind(wx.EVT_TEXT, self.EvtText, self.editanswer)


    def OnClick(self,event):
        #self.logger.AppendText(" Click on object with Id %d\n" %event.GetId())
        if str(self.__answer) == self.__trueAnswer:
            self.logger.AppendText(" Correct!!")
            time.sleep(0.5)
            self.parent.Hide()
            time.sleep(15*60)
            # clear answer
            self.editanswer.Clear()
            # change question
            question, answer, err = self.question_generator(self.grade)
            self.question.SetLabel(question)
            self.__trueAnswer = answer
            # show
            self.parent.Show(True)
        else:
            self.logger.AppendText(" Wrong!!, do it again!")
    def EvtText(self, event):
        self.logger.AppendText('AM: %s\n' % event.GetString())
        self.__answer = event.GetString()


