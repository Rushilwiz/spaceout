# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\login.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QPushButton, QVBoxLayout, QApplication, QSplashScreen 

import webbrowser
import requests
import keyring
from requests.auth import HTTPBasicAuth

API_ENDPOINT = 'http://localhost:8000/api/'

class LoginForm(object):
    def setupUi(self, Form):
        Form.setObjectName("SpaceOut Login")
        Form.resize(500, 756)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.widget.setStyleSheet(".QWidget{background-color: rgb(0,0,0);}")
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setContentsMargins(9, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setContentsMargins(-1, 15, -1, -1)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label, 0, QtCore.Qt.AlignHCenter)
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setContentsMargins(50, 35, 59, -1)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setStyleSheet("color: rgb(231, 231, 231);\n"
"font: 15pt \"Verdana\";")
        self.label_2.setObjectName("label_2")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.username = QtWidgets.QLineEdit(self.widget)
        self.username.setMinimumSize(QtCore.QSize(0, 40))
        self.username.setStyleSheet("QLineEdit {\n"
"      color: rgb(231, 231, 231);\n"
"      font: 15pt \"Verdana\";\n"
"      border: None;\n"
"      border-bottom-color: white;\n"
"      border-radius: 10px;\n"
"      padding: 0 8px;\n"
"      background: rgb(25, 25, 40);\n"
"      selection-background-color: darkgray;\n"
"}")
        self.username.setObjectName("lineEdit")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.username)
        self.line = QtWidgets.QFrame(self.widget)
        self.line.setStyleSheet("border: 2px solid white;")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.SpanningRole, self.line)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setStyleSheet("color: rgb(231, 231, 231);\n"
"font: 15pt \"Verdana\";")
        self.label_3.setObjectName("label_3")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.password = QtWidgets.QLineEdit(self.widget)
        self.password.setMinimumSize(QtCore.QSize(0, 40))
        self.password.setStyleSheet("QLineEdit {\n"
"      color: orange;\n"
"      font: 15pt \"Verdana\";\n"
"      border: None;\n"
"      border-bottom-color: white;\n"
"      border-radius: 10px;\n"
"      padding: 0 8px;\n"
"      background: rgb(25, 25, 40);\n"
"      selection-background-color: darkgray;\n"
"}")
        self.password.setObjectName("password")
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.password)
        self.line_2 = QtWidgets.QFrame(self.widget)
        self.line_2.setStyleSheet("border: 2px solid #03EEF3;")
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.SpanningRole, self.line_2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout_2.setItem(7, QtWidgets.QFormLayout.SpanningRole, spacerItem1)
        self.login = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.login.sizePolicy().hasHeightForWidth())
        self.login.setSizePolicy(sizePolicy)
        self.login.setMinimumSize(QtCore.QSize(0, 60))
        self.login.setAutoFillBackground(False)
        self.login.setStyleSheet("color: rgb(231, 231, 231);\n"
"font: 17pt \"Verdana\";\n"
"border: 2px solid #03EEF3;\n"
"padding: 5px;\n"
"border-radius: 3px;\n"
"opacity: 200;\n"
"")
        self.login.setAutoDefault(False)
        self.login.setDefault(False)
        self.login.setFlat(False)
        self.login.setObjectName("login")
        self.formLayout_2.setWidget(8, QtWidgets.QFormLayout.SpanningRole, self.login)
        self.register = QtWidgets.QPushButton(self.widget)
        self.register.setMinimumSize(QtCore.QSize(0, 60))
        self.register.setStyleSheet("color: rgb(231, 231, 231);\n"
"font: 17pt \"Verdana\";\n"
"border: 2px solid #03EEF3;\n"
"padding: 5px;\n"
"border-radius: 3px;\n"
"opacity: 200;\n"
"")
        self.register.setDefault(False)
        self.register.setFlat(False)
        self.register.setObjectName("register")

        self.register.clicked.connect(self.open_register_link)
        self.login.clicked.connect(self.check_password)

        self.formLayout_2.setWidget(9, QtWidgets.QFormLayout.SpanningRole, self.register)
        self.verticalLayout_3.addLayout(self.formLayout_2)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem2)
        self.verticalLayout_2.addLayout(self.verticalLayout_3)
        self.horizontalLayout_3.addWidget(self.widget)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def open_register_link(self):
        webbrowser.open('https://donot.space/out')

    def check_password (self):
        QApplication.setOverrideCursor(QtCore.Qt.WaitCursor)
        r = requests.get(f'{API_ENDPOINT}profile', auth=HTTPBasicAuth(str(self.username.text()), str(self.password.text()))) 
        QApplication.restoreOverrideCursor()

        if r.ok:
            keyring.set_password("spaceout", str(self.username.text()), str(self.password.text()))
            f = open('.userinfo', 'w')
            f.write(self.username.text())
            f.close()
            app.quit()
        else:
            msg = QtWidgets.QMessageBox()
            msg.setText('Incorrect Login')
            msg.exec_()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "<html><head/><body><p><img src=\":/src/spaceout.png\"/></p></body></html>"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p><img src=\":/src/user.png\"/></p></body></html>"))
        self.label_3.setText(_translate("Form", "<html><head/><body><p><img src=\":/src/password.png\"/></p></body></html>"))
        self.login.setText(_translate("Form", "Sign In"))
        self.register.setText(_translate("Form", "Register"))

import spaceout_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    try:
        f = open('.userinfo')
        username = f.read()
        f.close()
        password = keyring.get_password('spaceout', username)
        r = requests.get(f'{API_ENDPOINT}profile', auth=HTTPBasicAuth(username, password)) 
        if not r.ok:
            raise Exception

    except:
        Form = QtWidgets.QWidget()
        ui = LoginForm()
        ui.setupUi(Form)
        Form.show()


    sys.exit(app.exec_())