from PyQt5 import QtCore
from LoginSystem.LoginSystem import LoginSystem
import pytest


@pytest.fixture()
def login_system(qtbot):
    test_login = LoginSystem()
    qtbot.addWidget(test_login)
    return test_login


def test_user_input(login_system):
    assert login_system.label_username.text() == "Username"


def test_password(login_system):
    assert login_system.label_password.text() == "Password"


def test_headline(login_system):
    assert login_system.label_login_system.text() == "LoginSystem"


def test_Log(login_system):
    assert login_system.label_log.text() == "Log:"


def test_sign_up(login_system):
    assert login_system.label_sign_up.text() == "SignUp"


def test_new_username(login_system):
    assert login_system.label_new_username.text() == "New Username"


def test_label_confirm_password(login_system):
    assert login_system.label_confirm_password.text() == "Confirm Password"


def test_new_password(login_system):
    assert login_system.label_new_password.text() == "New Password"


def test_button(login_system, qtbot):
    def on_timeout():
        qtbot.keyClicks(login_system.lineEdit_username, "")
        qtbot.mouseClick(login_system.button_login, QtCore.Qt.LeftButton)

    QtCore.QTimer.singleShot(0, on_timeout)
    qtbot.mouseClick(login_system.button_login, QtCore.Qt.LeftButton)
    assert login_system.label_log != ""
