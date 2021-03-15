# -*- coding: utf-8 -*-

###########################################################################
# Python code generated with wxFormBuilder (version Oct 26 2018)
# http://www.wxformbuilder.org/
##
# PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
# Class MyFrame2
###########################################################################


class MyFrame2 (wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition, size=wx.Size(
            500, 300), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        sbSizer2 = wx.StaticBoxSizer(wx.StaticBox(
            self, wx.ID_ANY, u"HELLO WX"), wx.VERTICAL)

        fgSizer3 = wx.FlexGridSizer(0, 2, 0, 0)
        fgSizer3.SetFlexibleDirection(wx.BOTH)
        fgSizer3.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_staticText3 = wx.StaticText(sbSizer2.GetStaticBox(
        ), wx.ID_ANY, u"Nama :", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText3.Wrap(-1)

        fgSizer3.Add(self.m_staticText3, 0, wx.ALL, 5)

        self.m_staticText4 = wx.StaticText(sbSizer2.GetStaticBox(
        ), wx.ID_ANY, u"Ricky Marcellyno Sabastian", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText4.Wrap(-1)

        fgSizer3.Add(self.m_staticText4, 0, wx.ALL, 5)

        self.m_staticText5 = wx.StaticText(sbSizer2.GetStaticBox(
        ), wx.ID_ANY, u"NIM :", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText5.Wrap(-1)

        fgSizer3.Add(self.m_staticText5, 0, wx.ALL, 5)

        self.m_staticText6 = wx.StaticText(sbSizer2.GetStaticBox(
        ), wx.ID_ANY, u"192410101137", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText6.Wrap(-1)

        fgSizer3.Add(self.m_staticText6, 0, wx.ALL, 5)

        sbSizer2.Add(fgSizer3, 1, wx.EXPAND, 5)

        self.SetSizer(sbSizer2)
        self.Layout()

        self.Centre(wx.BOTH)

    def __del__(self):
        pass
