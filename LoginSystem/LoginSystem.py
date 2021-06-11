"""
Python LoginSystem System
Generic and very simple login system.
version 1.1
Created by Shriram Sundaram

The term lineEdit indicates the user input box(where the user type the input)
"""
import os
import platform

from PyQt5.QtWidgets import QMainWindow


class LoginSystem(QMainWindow):

    def __init__(self):
        self.username_info = ""
        self.password_info = ""
        self.new_input_formatted_username = ""
        self.new_input_formatted_password = ""
        self.New_UserName = ""
        self.New_Password = ""
        self.Confirm_Password = ""
        dir = os.path.curdir
        if str(platform.system()) == "Windows":
            file = open(dir + ".//LoginInfo")
        elif str(platform.system()) == "Linux":
            file = open(dir + "/LoginInfo")
        self.already_saved = file.readlines()
        file.close()

        super(LoginSystem, self).__init__()
        self.setObjectName("MainWindow")
        self.resize(543, 453)
        self.setWindowTitle("Welcome To LoginSystem Panel")
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("central_widget")
        self.label_username = QtWidgets.QLabel(self.centralwidget)
        self.label_username.setGeometry(QtCore.QRect(70, 90, 101, 31))
        self.label_username.setStyleSheet("font: 18pt \"Microsoft Himalaya\";")
        self.label_username.setObjectName("label_log")
        self.label_password = QtWidgets.QLabel(self.centralwidget)
        self.label_password.setGeometry(QtCore.QRect(70, 160, 101, 21))
        self.label_password.setStyleSheet("font: 18pt \"Microsoft Himalaya\";")
        self.label_password.setObjectName("label_row_size")
        self.button_login = QtWidgets.QPushButton(self.centralwidget)
        self.button_login.setGeometry(QtCore.QRect(80, 240, 111, 41))
        self.button_login.setObjectName("button_login")
        self.label_login_system = QtWidgets.QLabel(self.centralwidget)
        self.label_login_system.setGeometry(QtCore.QRect(200, 0, 211, 41))
        self.label_login_system.setStyleSheet("font: 20pt \"Modern No. 20\";")
        self.label_login_system.setObjectName("label_login_system")
        self.label_log = QtWidgets.QLabel(self.centralwidget)
        self.label_log.setGeometry(QtCore.QRect(40, 300, 301, 21))
        self.label_log.setObjectName("label_log")
        self.label_sign_up = QtWidgets.QLabel(self.centralwidget)
        self.label_sign_up.setGeometry(QtCore.QRect(330, 60, 81, 21))
        self.label_sign_up.setStyleSheet("font: 18pt \"Microsoft Himalaya\";")
        self.label_sign_up.setObjectName("label_sign_up")
        self.label_new_username = QtWidgets.QLabel(self.centralwidget)
        self.label_new_username.setGeometry(QtCore.QRect(330, 90, 131, 31))
        self.label_new_username.setStyleSheet("font: 18pt \"Microsoft Himalaya\";")
        self.label_new_username.setObjectName("label_new_username")
        self.label_new_password = QtWidgets.QLabel(self.centralwidget)
        self.label_new_password.setGeometry(QtCore.QRect(330, 160, 131, 21))
        self.label_new_password.setStyleSheet("font: 18pt \"Microsoft Himalaya\";")
        self.label_new_password.setObjectName("label_new_password")
        self.button_sign_up = QtWidgets.QPushButton(self.centralwidget)
        self.button_sign_up.setGeometry(QtCore.QRect(340, 310, 111, 41))
        self.button_sign_up.setObjectName("button_sign_up")
        self.label_confirm_password = QtWidgets.QLabel(self.centralwidget)
        self.label_confirm_password.setGeometry(QtCore.QRect(330, 230, 161, 21))
        self.label_confirm_password.setStyleSheet("font: 18pt \"Microsoft Himalaya\";")
        self.label_confirm_password.setObjectName("label_confirm_password")
        self.lineEdit_username = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_username.setGeometry(QtCore.QRect(70, 120, 151, 21))
        self.lineEdit_username.setObjectName("lineEdit_username")
        self.lineEdit_password = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_password.setGeometry(QtCore.QRect(70, 190, 151, 22))
        self.lineEdit_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_password.setObjectName("line_edit_row_size")
        self.lineEdit_new_username = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_new_username.setGeometry(QtCore.QRect(330, 120, 151, 22))
        self.lineEdit_new_username.setObjectName("lineEdit_new_username")
        self.lineEdit_new_password = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_new_password.setGeometry(QtCore.QRect(330, 190, 151, 22))
        self.lineEdit_new_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_new_password.setObjectName("lineEdit_new_password")
        self.lineEdit_confirm_password = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_confirm_password.setGeometry(QtCore.QRect(330, 260, 151, 22))
        self.lineEdit_confirm_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_confirm_password.setObjectName("lineEdit_confirm_password")
        self.label_login = QtWidgets.QLabel(self.centralwidget)
        self.label_login.setGeometry(QtCore.QRect(70, 60, 81, 21))
        self.label_login.setStyleSheet("font: 18pt \"Microsoft Himalaya\";")
        self.label_login.setObjectName("label_login")
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 543, 26))
        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)
        self.UserName = ""
        self.Password = ""

        self.retranslateUi()
        self.initLogin()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.label_username.setText(_translate("MainWindow", "Username"))
        self.label_password.setText(_translate("MainWindow", "Password"))
        self.label_login_system.setText(_translate("MainWindow", "LoginSystem"))
        self.label_log.setText(_translate("MainWindow", "Log:"))
        self.label_sign_up.setText(_translate("MainWindow", "SignUp"))
        self.label_new_username.setText(_translate("MainWindow", "New Username"))
        self.label_new_password.setText(_translate("MainWindow", "New Password"))
        self.button_sign_up.setText(_translate("MainWindow", "SignUp"))
        self.label_confirm_password.setText(_translate("MainWindow", "Confirm Password"))
        self.label_login.setText(_translate("MainWindow", "Login"))
        self.button_login.setText(_translate("MainWindow", "Login"))

    def initLogin(self):
        self.button_login.setText("Login")
        self.button_login.clicked.connect(self.inputsFromUser)
        self.button_sign_up.clicked.connect(self.signUp)

    def inputsFromUser(self):
        if self.UserName is not None:
            self.UserName = str(self.lineEdit.text())
            self.Password = str(self.lineEdit_password.text())
            self.openSource()

    def openSource(self):
        """Open the source file and save it in the format"""
        self.new_input_formatted_username = str("Username =" + " " + self.UserName)
        self.new_input_formatted_password = str("Password =" + " " + self.Password)
        self.checkDatabase()

    def checkDatabase(self):
        """
        Verifying with the source code or Database

        """
        for i, users in enumerate(self.already_saved):
            if self.new_input_formatted_username == str(self.already_saved[i].rstrip("\n")):
                self.username_info = str(self.already_saved[i].rstrip("\n"))
            if self.new_input_formatted_password == str(self.already_saved[i]).rstrip("\n"):
                self.password_info = str(self.already_saved[i]).rstrip("\n")

        if self.new_input_formatted_username == self.username_info.rstrip("\n"):
            if self.new_input_formatted_password == self.password_info.rstrip("\n"):
                self.label_log.setText("Successfully Logged in")
            else:
                self.label_log.setText("Username and Password is incorrect")
        else:
            self.label_log.setText("The system couldn't "
                                   "find the Username, Please sign up")

    def signUp(self):
        """
        Sign Up Logic

        """
        if self.lineEdit_new_username is not None:
            self.New_UserName = str(str("Username = ") +
                                    str(self.lineEdit_new_username.text()))
            # print(self.New_UserName)
        if self.lineEdit_new_password is not None:
            self.New_Password = str(str("Password = ") +
                                    str(self.lineEdit_new_password.text()))
            # print(self.New_Password)
        if self.lineEdit_confirm_password is not None:
            self.Confirm_Password = str(str("Password = ") +
                                        self.lineEdit_confirm_password.text())

        if self.New_Password == self.Confirm_Password:
            if self.New_UserName + "\n" in self.already_saved:
                self.label_log.setText("The Username already exist!!!")
            else:
                self.label_log.setText("Sign Up Successful")
                if str(platform.system()) == "Linux":
                    New_Login = open("/LoginInfo", 'a')
                elif str(platform.system()) == "Windows":
                    New_Login = open("./LoginInfo", 'a')
                New_UserName = str(self.New_UserName)
                New_Password = str(self.New_Password)

                New_UsersList = [New_UserName, New_Password]
                for users in New_UsersList:
                    New_Login.writelines(users)
                    New_Login.writelines("\n")
                New_Login.close()
        else:
            self.label_log.setText("New Password and Confirm Password doesnt Match")


if __name__ == "__main__":
    import sys
    from PyQt5 import QtGui, QtWidgets, QtCore

    app = QtWidgets.QApplication(sys.argv)
    Login = LoginSystem()
    Login.show()
    sys.exit(app.exec_())
