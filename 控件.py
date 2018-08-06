import win32com
from win32com.client import Dispatch,constants
def bar_get(lj):

    bar = win32com.client.Dispatch('bartender.Application')

    bar.Visible = True

    #mobans = bar.Format

    moban = bar.Formats.Open(lj,False,'')

lj = r'C:\Users\li\Desktop\模板\2401机身标.btw'

bar_get(lj)   