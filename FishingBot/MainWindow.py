import pygetwindow as gw
from PyQt5.QtCore import QRunnable, Qt, QThreadPool
from PyQt5 import QtCore, QtGui, QtWidgets
import functions
from time import sleep
import webbrowser


class Runnable(QRunnable):
    def __init__(self, n):
        super().__init__()
        self.n = n

    # Reads text file
    def get_title(self):
        MC_Title_Text_File = open("Title.txt", "r")
        value = MC_Title_Text_File.read()
        MC_Title_Text_File.close()
        return value

    # Runs main script
    def run(self):
        sleep(5)
        i = 0
        fish_count = 0
        # Gets title from
        title = self.get_title()
        while True:
            # Gets name of active window title
            active_window = gw.getActiveWindowTitle()
            if active_window == title:
                # Eats food after 300 catches
                if i > 300:
                    functions.eat_food(2, 1)
                    sleep(1)
                    i = 0
                # Calls main script
                functions.autofish(0.01, 0, 5)
                i += 1
                fish_count += 1
            else:
                print("Inactive")
                break


class Ui_Title(object):
    def setupUi(self, Title):
        Title.setObjectName("Title")
        Title.resize(412, 170)
        Title.setMaximumSize(QtCore.QSize(16777215, 16777215))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../../../Downloads/fishing_pole.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Title.setWindowIcon(icon)
        Title.setToolTipDuration(9)
        Title.setLayoutDirection(QtCore.Qt.LeftToRight)
        Title.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(94, 94, 94);")
        # Start Button
        self.StartButton = QtWidgets.QPushButton(Title)
        self.StartButton.setGeometry(QtCore.QRect(20, 100, 111, 41))
        self.StartButton.setObjectName("StartButton")
        # Stop Button
        self.StopButton = QtWidgets.QPushButton(Title)
        self.StopButton.setGeometry(QtCore.QRect(280, 100, 111, 41))
        self.StopButton.setObjectName("StopButton")
        # Minecraft Title Text
        self.MC_Select_T = QtWidgets.QLabel(Title)
        self.MC_Select_T.setGeometry(QtCore.QRect(30, 30, 91, 16))
        self.MC_Select_T.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.MC_Select_T.setTextFormat(QtCore.Qt.AutoText)
        self.MC_Select_T.setAlignment(QtCore.Qt.AlignCenter)
        self.MC_Select_T.setObjectName("MC_Select_T")
        # LCD Fish Counting Display
        self.Fish_Counter = QtWidgets.QLCDNumber(Title)
        self.Fish_Counter.setGeometry(QtCore.QRect(160, 120, 91, 41))
        self.Fish_Counter.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Fish_Counter.setAutoFillBackground(False)
        self.Fish_Counter.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Fish_Counter.setSmallDecimalPoint(False)
        self.Fish_Counter.setDigitCount(1)
        self.Fish_Counter.setMode(QtWidgets.QLCDNumber.Hex)
        self.Fish_Counter.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.Fish_Counter.setProperty("intValue", 0)
        self.Fish_Counter.setObjectName("Fish_Counter")
        # Fish Counting Text
        self.Fishing_Count_T = QtWidgets.QLabel(Title)
        self.Fishing_Count_T.setGeometry(QtCore.QRect(170, 100, 71, 16))
        self.Fishing_Count_T.setObjectName("Fishing_Count_T")
        # Test Button
        self.TestButton = QtWidgets.QPushButton(Title)
        self.TestButton.setGeometry(QtCore.QRect(280, 42, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.TestButton.setFont(font)
        self.TestButton.setIconSize(QtCore.QSize(12, 12))
        self.TestButton.setObjectName("TestButton")
        # Rod Slot Text
        self.Rod_Slot_T = QtWidgets.QLabel(Title)
        self.Rod_Slot_T.setEnabled(True)
        self.Rod_Slot_T.setGeometry(QtCore.QRect(150, 40, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.Rod_Slot_T.setFont(font)
        self.Rod_Slot_T.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Rod_Slot_T.setAlignment(QtCore.Qt.AlignCenter)
        self.Rod_Slot_T.setWordWrap(True)
        self.Rod_Slot_T.setObjectName("Rod_Slot_T")
        # Food Slot Text
        self.Food_Slot_T = QtWidgets.QLabel(Title)
        self.Food_Slot_T.setGeometry(QtCore.QRect(210, 40, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.Food_Slot_T.setFont(font)
        self.Food_Slot_T.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Food_Slot_T.setAlignment(QtCore.Qt.AlignCenter)
        self.Food_Slot_T.setObjectName("Food_Slot_T")
        # Rod Slot Number
        self.Rod_Slot_Number = QtWidgets.QLabel(Title)
        self.Rod_Slot_Number.setGeometry(QtCore.QRect(160, 60, 20, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.Rod_Slot_Number.setFont(font)
        self.Rod_Slot_Number.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Rod_Slot_Number.setAlignment(QtCore.Qt.AlignCenter)
        self.Rod_Slot_Number.setObjectName("Rod_Slot_Number")
        # Food Slot Number
        self.Food_Slot_Number = QtWidgets.QLabel(Title)
        self.Food_Slot_Number.setGeometry(QtCore.QRect(230, 60, 20, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.Food_Slot_Number.setFont(font)
        self.Food_Slot_Number.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Food_Slot_Number.setAlignment(QtCore.Qt.AlignCenter)
        self.Food_Slot_Number.setObjectName("Food_Slot_Number")
        # Help Button
        self.HelpButton = QtWidgets.QPushButton(Title)
        self.HelpButton.setGeometry(QtCore.QRect(370, 0, 41, 23))
        self.HelpButton.setStyleSheet("border-color: rgb(255, 255, 255);")
        self.HelpButton.setObjectName("HelpButton")
        # Minecraft Input Box
        self.MC_Title_String = QtWidgets.QLineEdit(Title)
        self.MC_Title_String.setText(self.get_title())
        self.MC_Title_String.setGeometry(QtCore.QRect(20, 50, 81, 31))
        self.MC_Title_String.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.MC_Title_String.setObjectName("MC_Title_String")
        # Minecraft Ok Button for Input Box
        self.McOkButton = QtWidgets.QPushButton(Title)
        self.McOkButton.setGeometry(QtCore.QRect(110, 52, 31, 31))
        self.McOkButton.setObjectName("McOkButton")
        self.retranslateUi(Title)
        QtCore.QMetaObject.connectSlotsByName(Title)
        # If Button is clicked these connect them with the functions
        self.StartButton.clicked.connect(self.start_buttonclicked)
        self.TestButton.clicked.connect(self.test_buttonclicked)
        self.HelpButton.clicked.connect(self.help_buttonclicked)
        self.McOkButton.clicked.connect(self.McOk_buttonclicked)
        self.StopButton.clicked.connect(self.stop_buttonclicked)

    def retranslateUi(self, Title):
        _translate = QtCore.QCoreApplication.translate
        Title.setWindowTitle(_translate("Title", "MC Fisher"))
        Title.setToolTip(_translate("Title", "Get Minecraft Title"))
        self.StartButton.setText(_translate("Title", "Start"))
        self.StopButton.setText(_translate("Title", "Stop"))
        self.MC_Select_T.setText(_translate("Title", "Minecraft Title"))
        self.Fishing_Count_T.setText(_translate("Title", "Fishing Count"))
        self.TestButton.setText(_translate("Title", "Test Fisher"))
        self.Rod_Slot_T.setText(_translate("Title", "Rod Slot"))
        self.Food_Slot_T.setText(_translate("Title", "Food Slot"))
        self.Rod_Slot_Number.setText(_translate("Title", "1"))
        self.Food_Slot_Number.setText(_translate("Title", "2"))
        self.HelpButton.setText(_translate("Title", "Help?"))
        self.McOkButton.setText(_translate("Title", "OK"))

    # Closes window
    def stop_buttonclicked(self):
        quit()

    # Reads text file
    def get_title(self):
        MC_Title_Text_File = open("Title.txt", "r")
        value = MC_Title_Text_File.read()
        MC_Title_Text_File.close()
        return value

    def McOk_buttonclicked(self):
        # Gets text from Minecraft Input Box
        value = self.MC_Title_String.text()
        MC_Title_Text_File = open("Title.txt", "w")
        self.MC_Title_String.setText(value)
        # Writes value from Minecraft Input Box
        MC_Title_Text_File.write(value)
        MC_Title_Text_File.close()

    def help_buttonclicked(self):
        # Opens help website
        webbrowser.open('http://google.com', new=2)

    def test_buttonclicked(self):
        # Calls function to test fisher
        i = 0
        while i < 15:
            print("test button")
            functions.autofish_test(0.01, 0, 5)

    def start_buttonclicked(self):
        # Initializes PyAutoGUI
        functions.initPyAutoGUI()
        # Gets text from Minecraft Input Box
        mc_title_value = self.MC_Title_String.text()
        # Gets windows title from mc_title
        MC_Window = gw.getWindowsWithTitle(f'{mc_title_value}')[0]
        # Resizes and moves window
        functions.manage_window(MC_Window)
        # Sets up threads
        threadCount = QThreadPool.globalInstance().maxThreadCount()
        pool = QThreadPool.globalInstance()
        runnable = Runnable(threadCount)
        # Call start()
        pool.start(runnable)