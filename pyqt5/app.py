from PyQt5 import QtWidgets, uic
import sys

def parenth(Start=0,End=0,numb=0,a=[]):
    numb=int(u.TnumEl.text())
    if End == numb:
        u.Lw.addItem(''.join(a))
        
    else:
        
        if Start<numb:
            a.append('(')
            parenth(Start+1,End,numb,a)
            a.pop()
        if Start>End:
            a.append(')')
            parenth(Start,End+1,numb,a)
            a.pop()

    

app=QtWidgets.QApplication(sys.argv)
u=uic.loadUi("app1.ui")
u.show()


u.Val.clicked.connect(parenth)
sys.exit(app.exec_())