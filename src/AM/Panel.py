import wx
import time
class AMPanel(wx.Panel):
    def __init__(self, parent, question_generator, grade, time_down_func):
        wx.Panel.__init__(self, parent)
        self.__answer = None
        self.parent = parent
        self.count = 0
        self.wrong_count = 0
        self.time_down_func = time_down_func
        # generate question and answer
        self.question_generator = question_generator
        self.grade = grade
        question, answer, err = question_generator(grade)
        if err:
            raise ValueError(err)
        self.__trueAnswer = answer
        self.question = wx.StaticText(self, label="Your question : {}".format(question), pos=(20, 30))
        font = wx.Font(18, wx.DECORATIVE, wx.NORMAL, wx.NORMAL)
        self.question.SetFont(font)

        # A submit button
        self.button =wx.Button(self, label="Submit", pos=(200, 90))
        self.Bind(wx.EVT_BUTTON, self.OnClick,self.button)

        # the edit control - one line version.
        self.lblanswer = wx.StaticText(self, label="Your answer :", pos=(20,60))
        self.lblanswer.SetFont(font)
        self.editanswer = wx.TextCtrl(self, value="", pos=(20, 90), size=(140,-1))
        self.editanswer.SetFont(font)
        self.editanswer.SetFocus()
        self.Bind(wx.EVT_TEXT, self.EvtText, self.editanswer)
        # A log
        self.logger = wx.TextCtrl(self, pos=(300,20), size=(200,300), style=wx.TE_MULTILINE | wx.TE_READONLY)

    def OnClick(self,event):
        #self.logger.AppendText(" Click on object with Id %d\n" %event.GetId())
        if str(self.__answer) == self.__trueAnswer:
            # clear wrong count
            self.wrong_count = 0
            self.logger.AppendText("AM: Correct!!\n")
            self.count += 1
            time.sleep(0.5)
            self.parent.Hide()
            time_to_sleep = self.time_down_func(self.count) * 60
            time.sleep(time_to_sleep)
            # clear answer
            self.editanswer.Clear()
            self.editanswer.SetFocus()        
            # change question
            question, answer, err = self.question_generator(self.grade + self.count//5)
            self.question.SetLabel('Your question : {}'.format(question))
            self.__trueAnswer = answer
            # show
            self.parent.Show(True)
        else:
            self.wrong_count += 1
            if not self.wrong_count % 9:
                # anti spam
                self.logger.AppendText(
                    "AM: You are spamming too much! Wait for 2 mins.\n"
                    )
                self.editanswer.Hide()
                time.sleep(2*60)
                self.editanswer.Show(True)
            if not self.wrong_count % 3:
                # get a new question
                self.logger.AppendText(
                    "AM: Wrong again!! Time to crack a new question.\n"
                    )
                question, answer, err = self.question_generator(self.grade + self.count//3)
                self.question.SetLabel('Your question : {}'.format(question))
                self.__trueAnswer = answer
            else:
                self.logger.AppendText("AM: Wrong!!, do it again!\n")
            self.editanswer.Clear()
            self.editanswer.SetFocus()
            
    def EvtText(self, event):
        self.logger.AppendText('AM: %s\n' % event.GetString())
        self.__answer = event.GetString()


