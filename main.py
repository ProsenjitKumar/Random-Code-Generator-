from PyQt5 import QtWidgets, uic
import string, random



def id_8(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def id_4_1(size=4, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def id_4_2(size=4, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def id_4_3(size=4, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def id_12(size=12, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def tinder():
    a_8 = id_8()
    b_4 = id_4_1()
    c_4 = id_4_2()
    d_4 = id_4_3()
    e_12 = id_12()


    name = dlg.lineEdit.text()
    age = int(dlg.lineEdit_2.text())

    if name and age >= 14:
        dlg.label_5.setText("Hello, "+name)
        dlg.label_6.setText("Your Token ")
        dlg.textBrowser.setText(a_8+'-'+b_4+'-'+c_4+'-'+d_4+'-'+e_12)
    else:
        dlg.label_5.setText("Something Went Wrong,")
        dlg.label_5.setText("Sorry, Try Again.")

def random_code():
    code = ""

    for n in range(10):
        x = random.randint(0, 99)
        code += string.printable[x]

    return code
#random_code(15)

app = QtWidgets.QApplication([])
dlg = uic.loadUi("tinder_color.ui")

dlg.pushButton.clicked.connect(tinder)

dlg.show()
app.exec()
