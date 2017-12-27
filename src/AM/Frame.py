import os
import wx
import time

class AMFrame(wx.Frame):
    def __init__(self, parent, title):
        style = wx.STAY_ON_TOP
        wx.Frame.__init__(self, parent, title=title, style=style)
        self.CreateStatusBar() # A StatusBar in the bottom of the window

        self.Bind(wx.EVT_CLOSE, self.OnExit)
        
        # Forbid moving, minising program.
        #self.Bind(wx.EVT_ICONIZE, self.OnExit)
        self.Bind(wx.EVT_MOVE_END, self.Reposition)
        self.Maximize(True)

    def OnAbout(self,e):
        # A message dialog box with an OK button. wx.OK is a standard ID in wxWidgets.
        dlg = wx.MessageDialog( self, "A small text editor", "About Sample Editor", wx.OK)
        dlg.ShowModal() # Show it
        dlg.Destroy() # finally destroy it when finished.

    def OnExit(self,e):
        #self.Close(True)  # Close the frame.
        pass
    def Reposition(self,e):
        self.Maximize(True)

