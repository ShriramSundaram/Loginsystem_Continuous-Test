import sys

sys.path.append(r'C:\\Shriram\Personal\\08_RobotFramework')

from PyQt5.QtWidgets import QMainWindow
from LoginSystem.LoginSystem import LoginSystem
import pytest


@pytest.fixture()
def login_system(qtbot):
    test_login = LoginSystem()
    qtbot.addWidget(test_login)
    return test_login


def test_user_input(login_system):
    assert login_system.label_2.text() == "Username"


def test_password(login_system):
    assert login_system.label_2.text() == "Password"


def test_headline(login_system):
    assert login_system.label_5.text() == "LoginSystem"


def test_Log(login_system):
    assert login_system.label_6.text() == "Log"


def test_sign_up(login_system):
    assert login_system.label_7.text() == "SignUp"


def test_new_username(login_system):
    assert login_system.label_9.text() == "New Username"


def test_label_12(login_system):
    assert login_system.label_12.text() == "Confirm Password"
