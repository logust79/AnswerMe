import sys
sys.path.append('src')
import wx
from AM import Frame,Panel
import random

def generate_question(grade):
    err = None
    if grade == 'reception':
        A = random.randint(0,10)
        S = random.randint(0,10)
        
        # make sure S >= A
        A,S = sorted([A,S])
        B = S - A
        
        ops = ('+','-')
        op = random.choice(ops)
        # get question and answer.
        if op == '-':
            A,S = S,A
        question = '{A} {op} {B}'.format(**locals())
        answer = str(S)
    else:
        err = 'I do not understand this grade: {}'.format(grade)
        return(None, None, err)
    return(question, answer, err)

if __name__ == '__main__':

    # get a question answer pair
    grade = 'reception'
    app = wx.App(False)
    frame = Frame.AMFrame(None,'AnswerMe')
    panel = Panel.AMPanel(frame, generate_question, grade)
    frame.Show()
    app.MainLoop()