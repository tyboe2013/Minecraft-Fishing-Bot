import pygetwindow as gw
from PyQt5 import QtCore, QtGui, QtWidgets
import functions
from time import sleep
import webbrowser


class Ui_Title(object):
    def setupUi(self, Title):
        Title.setObjectName("Title")
        Title.resize(471, 197)
        Title.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Microsoft Yi Baiti")
        font.setPointSize(15)
        Title.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/fishing_pole.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Title.setWindowIcon(icon)
        Title.setToolTipDuration(9)
        Title.setLayoutDirection(QtCore.Qt.LeftToRight)
        Title.setStyleSheet("background-color: rgb(30, 30, 36);")
        # Start Button
        self.StartButton = QtWidgets.QPushButton(Title)
        self.StartButton.setGeometry(QtCore.QRect(30, 120, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.StartButton.setFont(font)
        self.StartButton.setStyleSheet("QPushButton {"
                                       "color: rgb(255, 248, 240);"
                                       "background-color: rgb(146, 20, 12);"
                                       "border-radius: 2px"
                                       "}"

                                       "QPushButton:hover{"
                                       "color: rgb(255, 248, 240);"
                                       "background-color: rgb(255, 32, 21);"
                                       "border-radius: 2px"
                                       "}")
        self.StartButton.setObjectName("StartButton")
        # Stop Button
        self.StopButton = QtWidgets.QPushButton(Title)
        self.StopButton.setGeometry(QtCore.QRect(330, 120, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.StopButton.setFont(font)
        self.StopButton.setStyleSheet("QPushButton {"
                                      "color: rgb(255, 248, 240);"
                                      "background-color: rgb(146, 20, 12);"
                                      "border-radius: 2px"
                                      "}"

                                      "QPushButton:hover{"
                                      "color: rgb(255, 248, 240);"
                                      "background-color: rgb(255, 32, 21);"
                                      "border-radius: 2px"
                                      "}")
        self.StopButton.setObjectName("StopButton")
        # Minecraft Select Label Text
        self.MC_Select_T = QtWidgets.QLabel(Title)
        self.MC_Select_T.setGeometry(QtCore.QRect(40, 40, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.MC_Select_T.setFont(font)
        self.MC_Select_T.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.MC_Select_T.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                       "color: rgb(255, 248, 240);")
        self.MC_Select_T.setTextFormat(QtCore.Qt.AutoText)
        self.MC_Select_T.setAlignment(QtCore.Qt.AlignCenter)
        self.MC_Select_T.setObjectName("MC_Select_T")
        # Fishing Count Text
        self.Fishing_Count_T = QtWidgets.QLabel(Title)
        self.Fishing_Count_T.setGeometry(QtCore.QRect(190, 110, 111, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Fishing_Count_T.setFont(font)
        self.Fishing_Count_T.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                           "color: rgb(255, 255, 255);")
        self.Fishing_Count_T.setAlignment(QtCore.Qt.AlignCenter)
        self.Fishing_Count_T.setObjectName("Fishing_Count_T")
        # Test Button
        self.TestButton = QtWidgets.QPushButton(Title)
        self.TestButton.setGeometry(QtCore.QRect(330, 50, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.TestButton.setFont(font)
        self.TestButton.setStyleSheet("QPushButton {"
                                      "color: rgb(255, 248, 240);"
                                      "background-color: rgb(146, 20, 12);"
                                      "border-radius: 2px"
                                      "}"

                                      "QPushButton:hover{"
                                      "color: rgb(255, 248, 240);"
                                      "background-color: rgb(255, 32, 21);"
                                      "border-radius: 2px"
                                      "}")
        self.TestButton.setIconSize(QtCore.QSize(12, 12))
        self.TestButton.setObjectName("TestButton")
        # Rod Slot Text
        self.Rod_Slot_T = QtWidgets.QLabel(Title)
        self.Rod_Slot_T.setEnabled(True)
        self.Rod_Slot_T.setGeometry(QtCore.QRect(190, 40, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.Rod_Slot_T.setFont(font)
        self.Rod_Slot_T.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Rod_Slot_T.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                      "color: rgb(255, 248, 240);")
        self.Rod_Slot_T.setAlignment(QtCore.Qt.AlignCenter)
        self.Rod_Slot_T.setWordWrap(True)
        self.Rod_Slot_T.setObjectName("Rod_Slot_T")
        # Food Slot Text
        self.Food_Slot_T = QtWidgets.QLabel(Title)
        self.Food_Slot_T.setGeometry(QtCore.QRect(250, 40, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.Food_Slot_T.setFont(font)
        self.Food_Slot_T.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Food_Slot_T.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                       "color: rgb(255, 248, 240);")
        self.Food_Slot_T.setAlignment(QtCore.Qt.AlignCenter)
        self.Food_Slot_T.setObjectName("Food_Slot_T")
        # Rod Slot Number
        self.Rod_Slot_Number = QtWidgets.QLabel(Title)
        self.Rod_Slot_Number.setGeometry(QtCore.QRect(200, 60, 20, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.Rod_Slot_Number.setFont(font)
        self.Rod_Slot_Number.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Rod_Slot_Number.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                           "color: rgb(255, 248, 240);")
        self.Rod_Slot_Number.setAlignment(QtCore.Qt.AlignCenter)
        self.Rod_Slot_Number.setObjectName("Rod_Slot_Number")
        # Food Slot Number
        self.Food_Slot_Number = QtWidgets.QLabel(Title)
        self.Food_Slot_Number.setGeometry(QtCore.QRect(270, 60, 20, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.Food_Slot_Number.setFont(font)
        self.Food_Slot_Number.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Food_Slot_Number.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                            "color: rgb(255, 248, 240);")
        self.Food_Slot_Number.setAlignment(QtCore.Qt.AlignCenter)
        self.Food_Slot_Number.setObjectName("Food_Slot_Number")
        # Help Button
        self.HelpButton = QtWidgets.QPushButton(Title)
        self.HelpButton.setGeometry(QtCore.QRect(430, 0, 41, 23))
        self.HelpButton.setStyleSheet("QPushButton {"
                                      "color: rgb(255, 248, 240);"
                                      "background-color: rgb(146, 20, 12);"
                                      "border-radius: 2px"
                                      "}"

                                      "QPushButton:hover{"
                                      "color: rgb(255, 248, 240);"
                                      "background-color: rgb(255, 32, 21);"
                                      "border-radius: 2px"
                                      "}")
        self.HelpButton.setObjectName("HelpButton")
        # Minecraft Input Box
        self.MC_Title_String = QtWidgets.QLineEdit(Title)
        self.MC_Title_String.setGeometry(QtCore.QRect(30, 60, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.MC_Title_String.setFont(font)
        self.MC_Title_String.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                           "color: rgb(0, 0, 0);")
        self.MC_Title_String.setText(self.get_title())
        self.MC_Title_String.setObjectName("MC_Title_String")
        # Ok Button
        self.McOkButton = QtWidgets.QPushButton(Title)
        self.McOkButton.setGeometry(QtCore.QRect(130, 60, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.McOkButton.setFont(font)
        self.McOkButton.setStyleSheet("QPushButton {"
                                      "color: rgb(255, 248, 240);"
                                      "background-color: rgb(146, 20, 12);"
                                      "border-radius: 2px"
                                      "}"

                                      "QPushButton:hover{"
                                      "color: rgb(255, 248, 240);"
                                      "background-color: rgb(255, 32, 21);"
                                      "border-radius: 2px"
                                      "}")
        self.McOkButton.setObjectName("McOkButton")
        # Fish Counter Numbers
        self.Fish_Counter = QtWidgets.QLabel(Title)
        self.Fish_Counter.setGeometry(QtCore.QRect(190, 130, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(27)
        self.Fish_Counter.setFont(font)
        self.Fish_Counter.setStyleSheet("color: rgb(255, 248, 240);\n"
                                        "background-color: rgba(255, 255, 255, 0);\n"
                                        "")
        self.Fish_Counter.setAlignment(QtCore.Qt.AlignCenter)
        self.Fish_Counter.setObjectName("Fish_Counter")
        # Active & Inactive Text
        self.active = QtWidgets.QLabel(Title)
        self.active.setGeometry(QtCore.QRect(0, 180, 71, 20))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.active.setFont(font)
        self.active.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                  "color: rgb(255, 248, 240);")
        self.active.setTextFormat(QtCore.Qt.AutoText)
        self.active.setAlignment(QtCore.Qt.AlignCenter)
        self.active.setObjectName("active")

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
        self.StopButton.setText(_translate("Title", "Quit"))
        self.MC_Select_T.setText(_translate("Title", "Minecraft Title"))
        self.Fishing_Count_T.setText(_translate("Title", "Fishing Count"))
        self.TestButton.setText(_translate("Title", "Test Fisher"))
        self.Rod_Slot_T.setText(_translate("Title", "Rod Slot"))
        self.Food_Slot_T.setText(_translate("Title", "Food Slot"))
        self.Rod_Slot_Number.setText(_translate("Title", "1"))
        self.Food_Slot_Number.setText(_translate("Title", "2"))
        self.HelpButton.setText(_translate("Title", "Help?"))
        self.McOkButton.setText(_translate("Title", "Enter"))
        self.Fish_Counter.setText(_translate("Title", "0"))
        self.active.setText(_translate("Title", "Inactive"))

    # Gets Title
    def get_title(self):
        MC_Title_Text_File = open("Title.txt", "r")
        value = MC_Title_Text_File.read()
        MC_Title_Text_File.close()
        return value

    # Quit Button
    def stop_buttonclicked(self):
        quit()

    # Writes Text File with Text inside Input Label
    def McOk_buttonclicked(self):
        # Gets text from Minecraft Input Box
        value = self.MC_Title_String.text()
        MC_Title_Text_File = open("Title.txt", "w")
        self.MC_Title_String.setText(value)
        # Writes value from Minecraft Input Box
        MC_Title_Text_File.write(value)
        MC_Title_Text_File.close()

    # Opens Readme
    def help_buttonclicked(self):
        # Opens help website
        webbrowser.open('https://github.com/tyboe2013/Minecraft-Fishing-Bot/blob/master/README.md', new=2)

    # Tests Main Script with few catches
    def test_buttonclicked(self):
        # Calls function to test fisher
        i = 0
        while i <= 2:
            functions.autofish(0.01, 0, 5)
            i += 1

    # Main Script For Bot
    def start_buttonclicked(self):
        # Sets Text as Active
        self.active.setText("Active")
        self.StartButton.setStyleSheet("background-color: rgb(112, 112, 112);\n"
                                       "border-radius: 2px;")
        # Initializes PyAutoGUI
        functions.initPyAutoGUI()
        # Gets text from Minecraft Input Box
        mc_title_value = self.MC_Title_String.text()
        # Gets windows title from mc_title
        MC_Window = gw.getWindowsWithTitle(f'{mc_title_value}')[0]
        # Resizes and moves window
        functions.manage_window(MC_Window)
        i = 0
        fish_count = 0
        # Gets title from
        title = self.get_title()
        sleep(8)
        while True:
            # Gets name of active window title
            active_window = gw.getActiveWindowTitle()
            # Stops Script If Minecraft Isn't Active
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
                string = str(fish_count)
                self.Fish_Counter.setText(string)
            else:
                # Sets Text as Inactive
                self.active.setText("Inactive")
                self.StartButton.setStyleSheet("QPushButton {"
                                               "color: rgb(255, 248, 240);"
                                               "background-color: rgb(146, 20, 12);"
                                               "border-radius: 2px"
                                               "}"

                                               "QPushButton:hover{"
                                               "color: rgb(255, 248, 240);"
                                               "background-color: rgb(255, 32, 21);"
                                               "border-radius: 2px"
                                               "}")
                break
