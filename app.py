import sys
sys.path.append('src')
import wx
from AM import Frame,Panel
import random

def generate_question(grade):
    err = None
    if grade in (0,1):
        # + / -
        A = random.randint(0,10)
        B = random.randint(0,10)
        
        S = A + B
        
        if grade == 0:
            question = '{A} + {B}'.format(**locals())
            answer = str(S)
        else:
            question = '{S} - {A}'.format(**locals())
            answer = str(B)
    elif grade == 2:
        A = random.randint(0,10)
        B = random.randint(0,10)
        S = A * B
        question = '{A} * {B}'.format(**locals())
        answer = str(S)
    else:
        err = 'I do not understand this grade: {}'.format(grade)
        return(None, None, err)
    return(question, answer, err)

def time_down_func(x):
    # a function to timing the challenges
    return 30 / x
    
if __name__ == '__main__':

    # get a question answer pair
    grade = 0
    app = wx.App(False)
    frame = Frame.AMFrame(None,'AnswerMe')
    panel = Panel.AMPanel(frame, generate_question, grade, time_down_func)
    frame.Show()
    app.MainLoop()