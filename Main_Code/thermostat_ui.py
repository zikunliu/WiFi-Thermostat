#list_time=['12:00am','1:00am','2:00am','3:00am','4:00am','5:00am','6:00am','7:00am','8:00am','9:00am','10:00am','11:00am','12:00pm','1:00pm','2:00pm','3:00pm','4:00pm','5:00pm','6:00pm','7:00pm','8:00pm','9:00pm','10:00pm','11:00pm']
list_time=['0:00','1:00','2:00','3:00','4:00','5:00','6:00','7:00','8:00','9:00','10:00','11:00','12:00','13:00','14:00','15:00','16:00','17:00','18:00','19:00','20:00','21:00','22:00','23:00']
#cur_temp = 77
f=open('currentTemperature.txt')
cur_temp=(int)(f.readline())
f.close
set_temp = 80
fan_state = 'On'
mode_state = 'cool'
mode_name=['','Sleep mode running','Pre cool mode running','pre heat mode running','Save mode running']
tem_1=[0,78,78,78,78,78,78,78]
tem_2=[0,78,78,78,78,78,78,78]
tem_3=[0,78,78,78,78,78,78,78]
tem_4=[0,78,78,78,78,78,78,78]
tem_5=[0,'','','','','','','']
tem_6=[0,'','','','','','','']
tem_number=1
day_number=1
sch_cloud=1
#mode#
run_or_not_save = 0
run_or_not_sleep = 0
run_or_not_precool = 0
run_or_not_preheat =0
state_1 = 1
state_4=1
cool_or_heat=1
sleep_time=15
precool_time = 30
preheat_time = 30
stop_it=0
mode_state_cloud=1
#############
from PyQt4 import QtCore, QtGui
from schedule_combobox_appear_hide import *
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)
#create interface class
class Ui_themostat(object):

    def setupUi(self, themostat):
#interface setting
        themostat.setObjectName(_fromUtf8("themostat"))
        themostat.resize(800, 480)
#pushButton_up
        self.pushButton_up = QtGui.QPushButton(themostat)
        self.pushButton_up.setGeometry(QtCore.QRect(560, 70, 50, 50))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        self.pushButton_up.setFont(font)
        self.pushButton_up.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_up.setAutoFillBackground(True)
        self.pushButton_up.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.pushButton_up.setObjectName(_fromUtf8("pushButton_up"))
#pushButton_setting
        self.pushButton_setting = QtGui.QPushButton(themostat)
        self.pushButton_setting.setGeometry(QtCore.QRect(390, 310, 81, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        self.pushButton_setting.setFont(font)
        self.pushButton_setting.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_setting.setAutoFillBackground(True)
        self.pushButton_setting.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.pushButton_setting.setObjectName(_fromUtf8("pushButton_setting"))
#label_curtemp
        self.label_curtemp = QtGui.QLabel(themostat)
        self.label_curtemp.setGeometry(QtCore.QRect(215, 190, 55, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(20)
        self.label_curtemp.setFont(font)
        self.label_curtemp.setObjectName(_fromUtf8("label_curtemp"))
#label_current 
        self.label_current = QtGui.QLabel(themostat)
        self.label_current.setGeometry(QtCore.QRect(200, 80, 101, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(20)
        self.label_current.setFont(font)
        self.label_current.setObjectName(_fromUtf8("label_current"))
#pushbutton_left
        self.pushButton_left = QtGui.QPushButton(themostat)
        self.pushButton_left.setGeometry(QtCore.QRect(500, 130, 50, 50))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        self.pushButton_left.setFont(font)
        self.pushButton_left.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_left.setAutoFillBackground(True)
        self.pushButton_left.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.pushButton_left.setObjectName(_fromUtf8("pushButton_left"))
#pushbutton_down
        self.pushButton_down = QtGui.QPushButton(themostat)
        self.pushButton_down.setGeometry(QtCore.QRect(560, 190, 50, 50))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        self.pushButton_down.setFont(font)
        self.pushButton_down.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton_down.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_down.setAutoFillBackground(True)
        self.pushButton_down.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.pushButton_down.setObjectName(_fromUtf8("pushButton_down"))
#label_set
        self.label_set = QtGui.QLabel(themostat)
        self.label_set.setGeometry(QtCore.QRect(380, 80, 51, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(20)
        self.label_set.setFont(font)
        self.label_set.setAutoFillBackground(True)
        self.label_set.setObjectName(_fromUtf8("label_set"))
#pushButton_onauto
        self.pushButton_onauto = QtGui.QPushButton(themostat)
        self.pushButton_onauto.setGeometry(QtCore.QRect(160, 310, 81, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        self.pushButton_onauto.setFont(font)
        self.pushButton_onauto.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_onauto.setAutoFillBackground(True)
        self.pushButton_onauto.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.pushButton_onauto.setObjectName(_fromUtf8("pushButton_onauto"))
#pushButton_right
        self.pushButton_right = QtGui.QPushButton(themostat)
        self.pushButton_right.setGeometry(QtCore.QRect(620, 130, 50, 50))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        self.pushButton_right.setFont(font)
        self.pushButton_right.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_right.setAutoFillBackground(True)
        self.pushButton_right.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.pushButton_right.setObjectName(_fromUtf8("pushButton_right"))
#label_settemp
        self.label_settemp = QtGui.QLabel(themostat)
        self.label_settemp.setGeometry(QtCore.QRect(375, 190, 55, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(20)
        self.label_settemp.setFont(font)
        self.label_settemp.setObjectName(_fromUtf8("label_settemp"))
#label_fanstate
        self.label_fanstate = QtGui.QLabel(themostat)
        self.label_fanstate.setGeometry(QtCore.QRect(170, 260, 80, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(14)
        self.label_fanstate.setFont(font)
        self.label_fanstate.setObjectName(_fromUtf8("label_fanstate"))
#label_modestate
        self.label_modestate = QtGui.QLabel(themostat)
        self.label_modestate.setGeometry(QtCore.QRect(300, 260, 41, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(14)
        self.label_modestate.setFont(font)
        self.label_modestate.setObjectName(_fromUtf8("label_modestate"))
#modebox
        self.modebox = QtGui.QComboBox(themostat)
        self.modebox.setGeometry(QtCore.QRect(280, 310, 81, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(14)
        self.modebox.setFont(font)
        self.modebox.setObjectName(_fromUtf8("modebox"))
#label_hold
        self.label_hold = QtGui.QLabel(themostat)
        self.label_hold.setGeometry(QtCore.QRect(390, 160, 31, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_hold.setFont(font)
        self.label_hold.setObjectName(_fromUtf8("label_hold"))
#label_mode_running
        self.label_mode_running = QtGui.QLabel(themostat)
        self.label_mode_running.setGeometry(QtCore.QRect(170, 380, 281, 61))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(20)
        self.label_mode_running.setFont(font)
        self.label_mode_running.setObjectName(_fromUtf8("label_mode_running"))
#********************#
#schedule interface
#********************#
#Title_schedule
        self.Title_schedule = QtGui.QLabel(themostat)
        self.Title_schedule.setGeometry(QtCore.QRect(260, 0, 281, 81))
        self.Title_schedule.setObjectName(_fromUtf8("Title_schedule"))
##############Monday
#comboBox_1_1
        self.comboBox_1_1 = QtGui.QComboBox(themostat)
        self.comboBox_1_1.setGeometry(QtCore.QRect(250, 130, 69, 22))
        self.comboBox_1_1.setObjectName(_fromUtf8("comboBox_1_1"))        
#comboBox_1_2      
        self.comboBox_1_2 = QtGui.QComboBox(themostat)
        self.comboBox_1_2.setGeometry(QtCore.QRect(390, 130, 69, 22))
        self.comboBox_1_2.setObjectName(_fromUtf8("comboBox_1_2"))
#comboBox_1_3
        self.comboBox_1_3 = QtGui.QComboBox(themostat)
        self.comboBox_1_3.setGeometry(QtCore.QRect(250, 170, 69, 22))
        self.comboBox_1_3.setObjectName(_fromUtf8("comboBox_1_3"))
#comboBox_1_4
        self.comboBox_1_4 = QtGui.QComboBox(themostat)
        self.comboBox_1_4.setGeometry(QtCore.QRect(390, 170, 69, 22))
        self.comboBox_1_4.setObjectName(_fromUtf8("comboBox_1_4"))
#comboBox_1_5
        self.comboBox_1_5 = QtGui.QComboBox(themostat)
        self.comboBox_1_5.setGeometry(QtCore.QRect(250, 210, 69, 22))
        self.comboBox_1_5.setObjectName(_fromUtf8("comboBox_1_5"))
#comboBox_1_6
        self.comboBox_1_6 = QtGui.QComboBox(themostat)
        self.comboBox_1_6.setGeometry(QtCore.QRect(390, 210, 69, 22))
        self.comboBox_1_6.setObjectName(_fromUtf8("comboBox_1_6"))
#comboBox_1_7
        self.comboBox_1_7 = QtGui.QComboBox(themostat)
        self.comboBox_1_7.setGeometry(QtCore.QRect(250, 250, 69, 22))
        self.comboBox_1_7.setObjectName(_fromUtf8("comboBox_1_7"))
#comboBox_1_8
        self.comboBox_1_8 = QtGui.QComboBox(themostat)
        self.comboBox_1_8.setGeometry(QtCore.QRect(390, 250, 69, 22))
        self.comboBox_1_8.setObjectName(_fromUtf8("comboBox_1_8"))
#comboBox_1_9
        self.comboBox_1_9 = QtGui.QComboBox(themostat)
        self.comboBox_1_9.setGeometry(QtCore.QRect(250, 290, 69, 22))
        self.comboBox_1_9.setObjectName(_fromUtf8("comboBox_1_9"))
#comboBox_1_10
        self.comboBox_1_10 = QtGui.QComboBox(themostat)
        self.comboBox_1_10.setGeometry(QtCore.QRect(390, 290, 69, 22))
        self.comboBox_1_10.setObjectName(_fromUtf8("comboBox_1_10"))
#comboBox_1_11
        self.comboBox_1_11 = QtGui.QComboBox(themostat)
        self.comboBox_1_11.setGeometry(QtCore.QRect(250, 330, 69, 22))
        self.comboBox_1_11.setObjectName(_fromUtf8("comboBox_1_11"))
#comboBox_1_12
        self.comboBox_1_12 = QtGui.QComboBox(themostat)
        self.comboBox_1_12.setGeometry(QtCore.QRect(390, 330, 69, 22))
        self.comboBox_1_12.setObjectName(_fromUtf8("comboBox_1_12"))
##############Tuesday
#comboBox_2_1
        self.comboBox_2_1 = QtGui.QComboBox(themostat)
        self.comboBox_2_1.setGeometry(QtCore.QRect(250, 130, 69, 22))
        self.comboBox_2_1.setObjectName(_fromUtf8("comboBox_2_1"))        
#comboBox_2_2      
        self.comboBox_2_2 = QtGui.QComboBox(themostat)
        self.comboBox_2_2.setGeometry(QtCore.QRect(390, 130, 69, 22))
        self.comboBox_2_2.setObjectName(_fromUtf8("comboBox_2_2"))
#comboBox_2_3
        self.comboBox_2_3 = QtGui.QComboBox(themostat)
        self.comboBox_2_3.setGeometry(QtCore.QRect(250, 170, 69, 22))
        self.comboBox_2_3.setObjectName(_fromUtf8("comboBox_2_3"))
#comboBox_2_4
        self.comboBox_2_4 = QtGui.QComboBox(themostat)
        self.comboBox_2_4.setGeometry(QtCore.QRect(390, 170, 69, 22))
        self.comboBox_2_4.setObjectName(_fromUtf8("comboBox_2_4"))
#comboBox_2_5
        self.comboBox_2_5 = QtGui.QComboBox(themostat)
        self.comboBox_2_5.setGeometry(QtCore.QRect(250, 210, 69, 22))
        self.comboBox_2_5.setObjectName(_fromUtf8("comboBox_2_5"))
#comboBox_2_6
        self.comboBox_2_6 = QtGui.QComboBox(themostat)
        self.comboBox_2_6.setGeometry(QtCore.QRect(390, 210, 69, 22))
        self.comboBox_2_6.setObjectName(_fromUtf8("comboBox_2_6"))
#comboBox_2_7
        self.comboBox_2_7 = QtGui.QComboBox(themostat)
        self.comboBox_2_7.setGeometry(QtCore.QRect(250, 250, 69, 22))
        self.comboBox_2_7.setObjectName(_fromUtf8("comboBox_2_7"))
#comboBox_2_8
        self.comboBox_2_8 = QtGui.QComboBox(themostat)
        self.comboBox_2_8.setGeometry(QtCore.QRect(390, 250, 69, 22))
        self.comboBox_2_8.setObjectName(_fromUtf8("comboBox_2_8"))
#comboBox_2_9
        self.comboBox_2_9 = QtGui.QComboBox(themostat)
        self.comboBox_2_9.setGeometry(QtCore.QRect(250, 290, 69, 22))
        self.comboBox_2_9.setObjectName(_fromUtf8("comboBox_2_9"))
#comboBox_2_10
        self.comboBox_2_10 = QtGui.QComboBox(themostat)
        self.comboBox_2_10.setGeometry(QtCore.QRect(390, 290, 69, 22))
        self.comboBox_2_10.setObjectName(_fromUtf8("comboBox_2_10"))
#comboBox_2_11
        self.comboBox_2_11 = QtGui.QComboBox(themostat)
        self.comboBox_2_11.setGeometry(QtCore.QRect(250, 330, 69, 22))
        self.comboBox_2_11.setObjectName(_fromUtf8("comboBox_2_11"))
#comboBox_2_12
        self.comboBox_2_12 = QtGui.QComboBox(themostat)
        self.comboBox_2_12.setGeometry(QtCore.QRect(390, 330, 69, 22))
        self.comboBox_2_12.setObjectName(_fromUtf8("comboBox_2_12"))
##############Wednesday
#comboBox_3_1
        self.comboBox_3_1 = QtGui.QComboBox(themostat)
        self.comboBox_3_1.setGeometry(QtCore.QRect(250, 130, 69, 22))
        self.comboBox_3_1.setObjectName(_fromUtf8("comboBox_3_1"))        
#comboBox_3_2      
        self.comboBox_3_2 = QtGui.QComboBox(themostat)
        self.comboBox_3_2.setGeometry(QtCore.QRect(390, 130, 69, 22))
        self.comboBox_3_2.setObjectName(_fromUtf8("comboBox_3_2"))
#comboBox_3_3
        self.comboBox_3_3 = QtGui.QComboBox(themostat)
        self.comboBox_3_3.setGeometry(QtCore.QRect(250, 170, 69, 22))
        self.comboBox_3_3.setObjectName(_fromUtf8("comboBox_3_3"))
#comboBox_3_4
        self.comboBox_3_4 = QtGui.QComboBox(themostat)
        self.comboBox_3_4.setGeometry(QtCore.QRect(390, 170, 69, 22))
        self.comboBox_3_4.setObjectName(_fromUtf8("comboBox_3_4"))
#comboBox_3_5
        self.comboBox_3_5 = QtGui.QComboBox(themostat)
        self.comboBox_3_5.setGeometry(QtCore.QRect(250, 210, 69, 22))
        self.comboBox_3_5.setObjectName(_fromUtf8("comboBox_3_5"))
#comboBox_3_6
        self.comboBox_3_6 = QtGui.QComboBox(themostat)
        self.comboBox_3_6.setGeometry(QtCore.QRect(390, 210, 69, 22))
        self.comboBox_3_6.setObjectName(_fromUtf8("comboBox_3_6"))
#comboBox_3_7
        self.comboBox_3_7 = QtGui.QComboBox(themostat)
        self.comboBox_3_7.setGeometry(QtCore.QRect(250, 250, 69, 22))
        self.comboBox_3_7.setObjectName(_fromUtf8("comboBox_3_7"))
#comboBox_3_8
        self.comboBox_3_8 = QtGui.QComboBox(themostat)
        self.comboBox_3_8.setGeometry(QtCore.QRect(390, 250, 69, 22))
        self.comboBox_3_8.setObjectName(_fromUtf8("comboBox_3_8"))
#comboBox_3_9
        self.comboBox_3_9 = QtGui.QComboBox(themostat)
        self.comboBox_3_9.setGeometry(QtCore.QRect(250, 290, 69, 22))
        self.comboBox_3_9.setObjectName(_fromUtf8("comboBox_3_9"))
#comboBox_3_10
        self.comboBox_3_10 = QtGui.QComboBox(themostat)
        self.comboBox_3_10.setGeometry(QtCore.QRect(390, 290, 69, 22))
        self.comboBox_3_10.setObjectName(_fromUtf8("comboBox_3_10"))
#comboBox_3_11
        self.comboBox_3_11 = QtGui.QComboBox(themostat)
        self.comboBox_3_11.setGeometry(QtCore.QRect(250, 330, 69, 22))
        self.comboBox_3_11.setObjectName(_fromUtf8("comboBox_3_11"))
#comboBox_3_12
        self.comboBox_3_12 = QtGui.QComboBox(themostat)
        self.comboBox_3_12.setGeometry(QtCore.QRect(390, 330, 69, 22))
        self.comboBox_3_12.setObjectName(_fromUtf8("comboBox_3_12"))
##############Thursday
#comboBox_4_1
        self.comboBox_4_1 = QtGui.QComboBox(themostat)
        self.comboBox_4_1.setGeometry(QtCore.QRect(250, 130, 69, 22))
        self.comboBox_4_1.setObjectName(_fromUtf8("comboBox_4_1"))        
#comboBox_4_2      
        self.comboBox_4_2 = QtGui.QComboBox(themostat)
        self.comboBox_4_2.setGeometry(QtCore.QRect(390, 130, 69, 22))
        self.comboBox_4_2.setObjectName(_fromUtf8("comboBox_4_2"))
#comboBox_4_3
        self.comboBox_4_3 = QtGui.QComboBox(themostat)
        self.comboBox_4_3.setGeometry(QtCore.QRect(250, 170, 69, 22))
        self.comboBox_4_3.setObjectName(_fromUtf8("comboBox_4_3"))
#comboBox_4_4
        self.comboBox_4_4 = QtGui.QComboBox(themostat)
        self.comboBox_4_4.setGeometry(QtCore.QRect(390, 170, 69, 22))
        self.comboBox_4_4.setObjectName(_fromUtf8("comboBox_4_4"))
#comboBox_4_5
        self.comboBox_4_5 = QtGui.QComboBox(themostat)
        self.comboBox_4_5.setGeometry(QtCore.QRect(250, 210, 69, 22))
        self.comboBox_4_5.setObjectName(_fromUtf8("comboBox_4_5"))
#comboBox_4_6
        self.comboBox_4_6 = QtGui.QComboBox(themostat)
        self.comboBox_4_6.setGeometry(QtCore.QRect(390, 210, 69, 22))
        self.comboBox_4_6.setObjectName(_fromUtf8("comboBox_4_6"))
#comboBox_4_7
        self.comboBox_4_7 = QtGui.QComboBox(themostat)
        self.comboBox_4_7.setGeometry(QtCore.QRect(250, 250, 69, 22))
        self.comboBox_4_7.setObjectName(_fromUtf8("comboBox_4_7"))
#comboBox_4_8
        self.comboBox_4_8 = QtGui.QComboBox(themostat)
        self.comboBox_4_8.setGeometry(QtCore.QRect(390, 250, 69, 22))
        self.comboBox_4_8.setObjectName(_fromUtf8("comboBox_4_8"))
#comboBox_4_9
        self.comboBox_4_9 = QtGui.QComboBox(themostat)
        self.comboBox_4_9.setGeometry(QtCore.QRect(250, 290, 69, 22))
        self.comboBox_4_9.setObjectName(_fromUtf8("comboBox_4_9"))
#comboBox_4_10
        self.comboBox_4_10 = QtGui.QComboBox(themostat)
        self.comboBox_4_10.setGeometry(QtCore.QRect(390, 290, 69, 22))
        self.comboBox_4_10.setObjectName(_fromUtf8("comboBox_4_10"))
#comboBox_4_11
        self.comboBox_4_11 = QtGui.QComboBox(themostat)
        self.comboBox_4_11.setGeometry(QtCore.QRect(250, 330, 69, 22))
        self.comboBox_4_11.setObjectName(_fromUtf8("comboBox_4_11"))
#comboBox_4_12
        self.comboBox_4_12 = QtGui.QComboBox(themostat)
        self.comboBox_4_12.setGeometry(QtCore.QRect(390, 330, 69, 22))
        self.comboBox_4_12.setObjectName(_fromUtf8("comboBox_4_12"))
###############Friday
#comboBox_5_1
        self.comboBox_5_1 = QtGui.QComboBox(themostat)
        self.comboBox_5_1.setGeometry(QtCore.QRect(250, 130, 69, 22))
        self.comboBox_5_1.setObjectName(_fromUtf8("comboBox_5_1"))        
#comboBox_5_2      
        self.comboBox_5_2 = QtGui.QComboBox(themostat)
        self.comboBox_5_2.setGeometry(QtCore.QRect(390, 130, 69, 22))
        self.comboBox_5_2.setObjectName(_fromUtf8("comboBox_5_2"))
#comboBox_5_3
        self.comboBox_5_3 = QtGui.QComboBox(themostat)
        self.comboBox_5_3.setGeometry(QtCore.QRect(250, 170, 69, 22))
        self.comboBox_5_3.setObjectName(_fromUtf8("comboBox_5_3"))
#comboBox_5_4
        self.comboBox_5_4 = QtGui.QComboBox(themostat)
        self.comboBox_5_4.setGeometry(QtCore.QRect(390, 170, 69, 22))
        self.comboBox_5_4.setObjectName(_fromUtf8("comboBox_5_4"))
#comboBox_5_5
        self.comboBox_5_5 = QtGui.QComboBox(themostat)
        self.comboBox_5_5.setGeometry(QtCore.QRect(250, 210, 69, 22))
        self.comboBox_5_5.setObjectName(_fromUtf8("comboBox_5_5"))
#comboBox_5_6
        self.comboBox_5_6 = QtGui.QComboBox(themostat)
        self.comboBox_5_6.setGeometry(QtCore.QRect(390, 210, 69, 22))
        self.comboBox_5_6.setObjectName(_fromUtf8("comboBox_5_6"))
#comboBox_5_7
        self.comboBox_5_7 = QtGui.QComboBox(themostat)
        self.comboBox_5_7.setGeometry(QtCore.QRect(250, 250, 69, 22))
        self.comboBox_5_7.setObjectName(_fromUtf8("comboBox_5_7"))
#comboBox_5_8
        self.comboBox_5_8 = QtGui.QComboBox(themostat)
        self.comboBox_5_8.setGeometry(QtCore.QRect(390, 250, 69, 22))
        self.comboBox_5_8.setObjectName(_fromUtf8("comboBox_5_8"))
#comboBox_5_9
        self.comboBox_5_9 = QtGui.QComboBox(themostat)
        self.comboBox_5_9.setGeometry(QtCore.QRect(250, 290, 69, 22))
        self.comboBox_5_9.setObjectName(_fromUtf8("comboBox_5_9"))
#comboBox_5_10
        self.comboBox_5_10 = QtGui.QComboBox(themostat)
        self.comboBox_5_10.setGeometry(QtCore.QRect(390, 290, 69, 22))
        self.comboBox_5_10.setObjectName(_fromUtf8("comboBox_5_10"))
#comboBox_5_11
        self.comboBox_5_11 = QtGui.QComboBox(themostat)
        self.comboBox_5_11.setGeometry(QtCore.QRect(250, 330, 69, 22))
        self.comboBox_5_11.setObjectName(_fromUtf8("comboBox_5_11"))
#comboBox_5_12
        self.comboBox_5_12 = QtGui.QComboBox(themostat)
        self.comboBox_5_12.setGeometry(QtCore.QRect(390, 330, 69, 22))
        self.comboBox_5_12.setObjectName(_fromUtf8("comboBox_5_12"))
###############Saturday
#comboBox_6_1
        self.comboBox_6_1 = QtGui.QComboBox(themostat)
        self.comboBox_6_1.setGeometry(QtCore.QRect(250, 130, 69, 22))
        self.comboBox_6_1.setObjectName(_fromUtf8("comboBox_6_1"))        
#comboBox_6_2      
        self.comboBox_6_2 = QtGui.QComboBox(themostat)
        self.comboBox_6_2.setGeometry(QtCore.QRect(390, 130, 69, 22))
        self.comboBox_6_2.setObjectName(_fromUtf8("comboBox_6_2"))
#comboBox_6_3
        self.comboBox_6_3 = QtGui.QComboBox(themostat)
        self.comboBox_6_3.setGeometry(QtCore.QRect(250, 170, 69, 22))
        self.comboBox_6_3.setObjectName(_fromUtf8("comboBox_6_3"))
#comboBox_6_4
        self.comboBox_6_4 = QtGui.QComboBox(themostat)
        self.comboBox_6_4.setGeometry(QtCore.QRect(390, 170, 69, 22))
        self.comboBox_6_4.setObjectName(_fromUtf8("comboBox_6_4"))
#comboBox_6_5
        self.comboBox_6_5 = QtGui.QComboBox(themostat)
        self.comboBox_6_5.setGeometry(QtCore.QRect(250, 210, 69, 22))
        self.comboBox_6_5.setObjectName(_fromUtf8("comboBox_6_5"))
#comboBox_6_6
        self.comboBox_6_6 = QtGui.QComboBox(themostat)
        self.comboBox_6_6.setGeometry(QtCore.QRect(390, 210, 69, 22))
        self.comboBox_6_6.setObjectName(_fromUtf8("comboBox_6_6"))
#comboBox_6_7
        self.comboBox_6_7 = QtGui.QComboBox(themostat)
        self.comboBox_6_7.setGeometry(QtCore.QRect(250, 250, 69, 22))
        self.comboBox_6_7.setObjectName(_fromUtf8("comboBox_6_7"))
#comboBox_6_8
        self.comboBox_6_8 = QtGui.QComboBox(themostat)
        self.comboBox_6_8.setGeometry(QtCore.QRect(390, 250, 69, 22))
        self.comboBox_6_8.setObjectName(_fromUtf8("comboBox_6_8"))
#comboBox_6_9
        self.comboBox_6_9 = QtGui.QComboBox(themostat)
        self.comboBox_6_9.setGeometry(QtCore.QRect(250, 290, 69, 22))
        self.comboBox_6_9.setObjectName(_fromUtf8("comboBox_6_9"))
#comboBox_6_10
        self.comboBox_6_10 = QtGui.QComboBox(themostat)
        self.comboBox_6_10.setGeometry(QtCore.QRect(390, 290, 69, 22))
        self.comboBox_6_10.setObjectName(_fromUtf8("comboBox_6_10"))
#comboBox_6_11
        self.comboBox_6_11 = QtGui.QComboBox(themostat)
        self.comboBox_6_11.setGeometry(QtCore.QRect(250, 330, 69, 22))
        self.comboBox_6_11.setObjectName(_fromUtf8("comboBox_6_11"))
#comboBox_6_12
        self.comboBox_6_12 = QtGui.QComboBox(themostat)
        self.comboBox_6_12.setGeometry(QtCore.QRect(390, 330, 69, 22))
        self.comboBox_6_12.setObjectName(_fromUtf8("comboBox_6_12"))
##############Sunday
#comboBox_7_1
        self.comboBox_7_1 = QtGui.QComboBox(themostat)
        self.comboBox_7_1.setGeometry(QtCore.QRect(250, 130, 69, 22))
        self.comboBox_7_1.setObjectName(_fromUtf8("comboBox_7_1"))        
#comboBox_7_2      
        self.comboBox_7_2 = QtGui.QComboBox(themostat)
        self.comboBox_7_2.setGeometry(QtCore.QRect(390, 130, 69, 22))
        self.comboBox_7_2.setObjectName(_fromUtf8("comboBox_7_2"))
#comboBox_7_3
        self.comboBox_7_3 = QtGui.QComboBox(themostat)
        self.comboBox_7_3.setGeometry(QtCore.QRect(250, 170, 69, 22))
        self.comboBox_7_3.setObjectName(_fromUtf8("comboBox_7_3"))
#comboBox_7_4
        self.comboBox_7_4 = QtGui.QComboBox(themostat)
        self.comboBox_7_4.setGeometry(QtCore.QRect(390, 170, 69, 22))
        self.comboBox_7_4.setObjectName(_fromUtf8("comboBox_7_4"))
#comboBox_7_5
        self.comboBox_7_5 = QtGui.QComboBox(themostat)
        self.comboBox_7_5.setGeometry(QtCore.QRect(250, 210, 69, 22))
        self.comboBox_7_5.setObjectName(_fromUtf8("comboBox_7_5"))
#comboBox_7_6
        self.comboBox_7_6 = QtGui.QComboBox(themostat)
        self.comboBox_7_6.setGeometry(QtCore.QRect(390, 210, 69, 22))
        self.comboBox_7_6.setObjectName(_fromUtf8("comboBox_7_6"))
#comboBox_7_7
        self.comboBox_7_7 = QtGui.QComboBox(themostat)
        self.comboBox_7_7.setGeometry(QtCore.QRect(250, 250, 69, 22))
        self.comboBox_7_7.setObjectName(_fromUtf8("comboBox_7_7"))
#comboBox_7_8
        self.comboBox_7_8 = QtGui.QComboBox(themostat)
        self.comboBox_7_8.setGeometry(QtCore.QRect(390, 250, 69, 22))
        self.comboBox_7_8.setObjectName(_fromUtf8("comboBox_7_8"))
#comboBox_7_9
        self.comboBox_7_9 = QtGui.QComboBox(themostat)
        self.comboBox_7_9.setGeometry(QtCore.QRect(250, 290, 69, 22))
        self.comboBox_7_9.setObjectName(_fromUtf8("comboBox_7_9"))
#comboBox_7_10
        self.comboBox_7_10 = QtGui.QComboBox(themostat)
        self.comboBox_7_10.setGeometry(QtCore.QRect(390, 290, 69, 22))
        self.comboBox_7_10.setObjectName(_fromUtf8("comboBox_7_10"))
#comboBox_7_11
        self.comboBox_7_11 = QtGui.QComboBox(themostat)
        self.comboBox_7_11.setGeometry(QtCore.QRect(250, 330, 69, 22))
        self.comboBox_7_11.setObjectName(_fromUtf8("comboBox_7_11"))
#comboBox_7_12
        self.comboBox_7_12 = QtGui.QComboBox(themostat)
        self.comboBox_7_12.setGeometry(QtCore.QRect(390, 330, 69, 22))
        self.comboBox_7_12.setObjectName(_fromUtf8("comboBox_7_12"))
#######################        
#pushButton_add
        self.pushButton_add = QtGui.QPushButton(themostat)
        self.pushButton_add.setGeometry(QtCore.QRect(260, 400, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.pushButton_add.setFont(font)
        self.pushButton_add.setObjectName(_fromUtf8("pushButton_add"))
#pushButton_minus
        self.pushButton_minus = QtGui.QPushButton(themostat)
        self.pushButton_minus.setGeometry(QtCore.QRect(400, 400, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.pushButton_minus.setFont(font)
        self.pushButton_minus.setObjectName(_fromUtf8("pushButton_minus"))
#label_tem1
        self.label_tem1 = QtGui.QLabel(themostat)
        self.label_tem1.setGeometry(QtCore.QRect(520, 130, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_tem1.setFont(font)
        self.label_tem1.setObjectName(_fromUtf8("label_tem1"))
        self.label_tem1.setStyleSheet('color:red')
#label_tem2
        self.label_tem2 = QtGui.QLabel(themostat)
        self.label_tem2.setGeometry(QtCore.QRect(520, 170, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_tem2.setFont(font)
        self.label_tem2.setObjectName(_fromUtf8("label_tem2"))
#label_tem3
        self.label_tem3 = QtGui.QLabel(themostat)
        self.label_tem3.setGeometry(QtCore.QRect(520, 210, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_tem3.setFont(font)
        self.label_tem3.setObjectName(_fromUtf8("label_tem3"))
#label_tem4
        self.label_tem4 = QtGui.QLabel(themostat)
        self.label_tem4.setGeometry(QtCore.QRect(520, 250, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_tem4.setFont(font)
        self.label_tem4.setObjectName(_fromUtf8("label_tem4"))
#label_day
        self.label_day = QtGui.QLabel(themostat)
        self.label_day.setGeometry(QtCore.QRect(90, 80, 51, 31))
        self.label_day.setObjectName(_fromUtf8("label_day"))
#label_time_range
        self.label_time_range = QtGui.QLabel(themostat)
        self.label_time_range.setGeometry(QtCore.QRect(300, 80, 121, 31))
        self.label_time_range.setObjectName(_fromUtf8("label_time_range"))
#label_set1
        self.label_set1 = QtGui.QLabel(themostat)
        self.label_set1.setGeometry(QtCore.QRect(520, 80, 51, 31))
        self.label_set1.setObjectName(_fromUtf8("label_set"))
#pushButton_up1
        self.pushButton_up1 = QtGui.QPushButton(themostat)
        self.pushButton_up1.setGeometry(QtCore.QRect(650, 100, 50, 50))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        self.pushButton_up1.setFont(font)
        self.pushButton_up1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_up1.setAutoFillBackground(True)
        self.pushButton_up1.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.pushButton_up1.setObjectName(_fromUtf8("pushButton_up1"))
#pushButton_left1
        self.pushButton_left1 = QtGui.QPushButton(themostat)
        self.pushButton_left1.setGeometry(QtCore.QRect(590, 160, 50, 50))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        self.pushButton_left1.setFont(font)
        self.pushButton_left1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_left1.setAutoFillBackground(True)
        self.pushButton_left1.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.pushButton_left1.setObjectName(_fromUtf8("pushButton_left1"))
#pushButton_right1
        self.pushButton_right1 = QtGui.QPushButton(themostat)
        self.pushButton_right1.setGeometry(QtCore.QRect(710, 160, 50, 50))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        self.pushButton_right1.setFont(font)
        self.pushButton_right1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_right1.setAutoFillBackground(True)
        self.pushButton_right1.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.pushButton_right1.setObjectName(_fromUtf8("pushButton_right1"))
#pushButton_down1
        self.pushButton_down1 = QtGui.QPushButton(themostat)
        self.pushButton_down1.setGeometry(QtCore.QRect(650, 230, 50, 50))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        self.pushButton_down1.setFont(font)
        self.pushButton_down1.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton_down1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_down1.setAutoFillBackground(True)
        self.pushButton_down1.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.pushButton_down1.setObjectName(_fromUtf8("pushButton_down1"))
#pushButton_1
        self.pushButton_1 = QtGui.QPushButton(themostat)
        self.pushButton_1.setGeometry(QtCore.QRect(70, 120, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_1.setFont(font)
        self.pushButton_1.setObjectName(_fromUtf8("pushButton_1"))
        self.pushButton_1.setStyleSheet('color:red')
#pushButton_2
        self.pushButton_2 = QtGui.QPushButton(themostat)
        self.pushButton_2.setGeometry(QtCore.QRect(70, 170, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
#pushButton_5
        self.pushButton_5 = QtGui.QPushButton(themostat)
        self.pushButton_5.setGeometry(QtCore.QRect(70, 320, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
#pushButton_4
        self.pushButton_4 = QtGui.QPushButton(themostat)
        self.pushButton_4.setGeometry(QtCore.QRect(70, 270, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
#pushButton_3
        self.pushButton_3 = QtGui.QPushButton(themostat)
        self.pushButton_3.setGeometry(QtCore.QRect(70, 220, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
#pushButton_6
        self.pushButton_6 = QtGui.QPushButton(themostat)
        self.pushButton_6.setGeometry(QtCore.QRect(70, 370, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
#pushButton_7
        self.pushButton_7 = QtGui.QPushButton(themostat)
        self.pushButton_7.setGeometry(QtCore.QRect(70, 420, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))
#pushButton_back
        self.pushButton_back = QtGui.QPushButton(themostat)
        self.pushButton_back.setGeometry(QtCore.QRect(590, 390, 91, 61))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.pushButton_back.setFont(font)
        self.pushButton_back.setObjectName(_fromUtf8("pushButton_back"))
#label_tem5
        self.label_tem5 = QtGui.QLabel(themostat)
        self.label_tem5.setGeometry(QtCore.QRect(520, 290, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_tem5.setFont(font)
        self.label_tem5.setObjectName(_fromUtf8("label_tem5"))
#label_tem6
        self.label_tem6 = QtGui.QLabel(themostat)
        self.label_tem6.setGeometry(QtCore.QRect(520, 330, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_tem6.setFont(font)
        self.label_tem6.setObjectName(_fromUtf8("label_tem6"))
#************#
#middle setting page
#************#

#pushButton_back1
        self.pushButton_back1 = QtGui.QPushButton(themostat)
        self.pushButton_back1.setGeometry(QtCore.QRect(590, 390, 91, 61))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.pushButton_back1.setFont(font)
        self.pushButton_back1.setObjectName(_fromUtf8("pushButton_back1"))
#pushButton_schedule
        self.pushButton_schedule = QtGui.QPushButton(themostat)
        self.pushButton_schedule.setGeometry(QtCore.QRect(100, 180, 211, 81))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.pushButton_schedule.setFont(font)
        self.pushButton_schedule.setObjectName(_fromUtf8("pushButton_schedule"))
#pushButton_mode
        self.pushButton_mode = QtGui.QPushButton(themostat)
        self.pushButton_mode.setGeometry(QtCore.QRect(440, 180, 211, 81))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.pushButton_mode.setFont(font)
        self.pushButton_mode.setObjectName(_fromUtf8("pushButton_mode"))   
#*************#
#mode interface
#*************#
#Title_mode
        self.Title_mode = QtGui.QLabel(themostat)
        self.Title_mode.setGeometry(QtCore.QRect(250, 0, 281, 81))
        self.Title_mode.setObjectName(_fromUtf8("Title_mode"))
#label_mode_sleep
        self.label_mode_sleep = QtGui.QLabel(themostat)
        self.label_mode_sleep.setGeometry(QtCore.QRect(90, 80, 121, 31))
        self.label_mode_sleep.setObjectName(_fromUtf8("label_mode_sleep"))
#label_mode_save
        self.label_mode_save = QtGui.QLabel(themostat)
        self.label_mode_save.setGeometry(QtCore.QRect(630, 80, 141, 31))
        self.label_mode_save.setObjectName(_fromUtf8("label_mode_save"))
#label_mode_precool
        self.label_mode_precool = QtGui.QLabel(themostat)
        self.label_mode_precool.setGeometry(QtCore.QRect(260, 80, 151, 31))
        self.label_mode_precool.setObjectName(_fromUtf8("label_mode_precool"))
#pushButton_back2
        self.pushButton_back2 = QtGui.QPushButton(themostat)
        self.pushButton_back2.setGeometry(QtCore.QRect(600, 380, 91, 61))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.pushButton_back2.setFont(font)
        self.pushButton_back2.setObjectName(_fromUtf8("pushButton_back2"))
#pushButton_sleep
        self.pushButton_sleep = QtGui.QPushButton(themostat)
        self.pushButton_sleep.setGeometry(QtCore.QRect(90, 300, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_sleep.setFont(font)
        self.pushButton_sleep.setObjectName(_fromUtf8("pushButton_sleep"))
#pushButton_cool
        self.pushButton_cool = QtGui.QPushButton(themostat)
        self.pushButton_cool.setGeometry(QtCore.QRect(280, 300, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_cool.setFont(font)
        self.pushButton_cool.setObjectName(_fromUtf8("pushButton_cool"))
#pushButton_save
        self.pushButton_save = QtGui.QPushButton(themostat)
        self.pushButton_save.setGeometry(QtCore.QRect(650, 300, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_save.setFont(font)
        self.pushButton_save.setObjectName(_fromUtf8("pushButton_save"))
#label_mode_time
        self.label_mode_time = QtGui.QLabel(themostat)
        self.label_mode_time.setGeometry(QtCore.QRect(10, 180, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_mode_time.setFont(font)
        self.label_mode_time.setObjectName(_fromUtf8("label_mode_time"))
#horizontalSlider_time1
        self.horizontalSlider_time1 = QtGui.QSlider(themostat)
        self.horizontalSlider_time1.setGeometry(QtCore.QRect(80, 190, 160, 22))
        self.horizontalSlider_time1.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_time1.setObjectName(_fromUtf8("horizontalSlider_time1"))

        self.connect(self.horizontalSlider_time1, QtCore.SIGNAL('valueChanged(int)'),self.changeValue1)
       

#label_slider_1
        self.label_slider_1 = QtGui.QLabel(themostat)
        self.label_slider_1.setGeometry(QtCore.QRect(240, 180, 70, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_slider_1.setFont(font)
        self.label_slider_1.setObjectName(_fromUtf8("label_slider_1"))
        self.label_slider_1.setText("15min")
     #  self.horizontalSlider_time1.setMinimum(10)
      #  self.horizontalSlider_time1.setMaximum(30)
      #  self.horizontalSlider_time1.setValue(20)
       # self.horizontalSlider_time1.setTickPosition(QSlider.TicksBelow)
       # self.horizontalSlider_time1.setTickInterval(5)
        
#label_mode_set
        self.label_mode_set = QtGui.QLabel(themostat)
        self.label_mode_set.setGeometry(QtCore.QRect(10, 120, 51, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(16)
        self.label_mode_set.setFont(font)
        self.label_mode_set.setAutoFillBackground(True)
        self.label_mode_set.setObjectName(_fromUtf8("label_mode_set"))
#label_mode_settemp
        self.label_mode_settemp = QtGui.QLabel(themostat)
        self.label_mode_settemp.setGeometry(QtCore.QRect(120, 120, 41, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(20)
        self.label_mode_settemp.setFont(font)
        self.label_mode_settemp.setObjectName(_fromUtf8("label_mode_settemp"))
#label_mode_toset
        self.label_mode_toset = QtGui.QLabel(themostat)
        self.label_mode_toset.setGeometry(QtCore.QRect(10, 240, 71, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(16)
        self.label_mode_toset.setFont(font)
        self.label_mode_toset.setAutoFillBackground(True)
        self.label_mode_toset.setObjectName(_fromUtf8("label_mode_toset"))
#label_sleep_lowertemp
        self.label_sleep_lowertemp = QtGui.QLabel(themostat)
        self.label_sleep_lowertemp.setGeometry(QtCore.QRect(120, 240, 41, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(20)
        self.label_sleep_lowertemp.setFont(font)
        self.label_sleep_lowertemp.setObjectName(_fromUtf8("label_sleep_lowertemp"))
#label_mode_preheat
        self.label_mode_preheat = QtGui.QLabel(themostat)
        self.label_mode_preheat.setGeometry(QtCore.QRect(440, 80, 151, 31))
        self.label_mode_preheat.setObjectName(_fromUtf8("label_mode_preheat"))
#label_mode_pretemp
        self.label_mode_pretemp = QtGui.QLabel(themostat)
        self.label_mode_pretemp.setGeometry(QtCore.QRect(400, 120, 41, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(20)
        self.label_mode_pretemp.setFont(font)
        self.label_mode_pretemp.setObjectName(_fromUtf8("label_mode_pretemp"))
#horizontalSlider_time2
        self.horizontalSlider_time2 = QtGui.QSlider(themostat)
        self.horizontalSlider_time2.setGeometry(QtCore.QRect(340, 190, 160, 22))
        self.horizontalSlider_time2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_time2.setObjectName(_fromUtf8("horizontalSlider_time2"))
        self.connect(self.horizontalSlider_time2, QtCore.SIGNAL('valueChanged(int)'),self.changeValue2)

#label_slider_2:
        self.label_slider_2 = QtGui.QLabel(themostat)
        self.label_slider_2.setGeometry(QtCore.QRect(500, 180, 70, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_slider_2.setFont(font)
        self.label_slider_2.setObjectName(_fromUtf8("label_slider_2"))
        self.label_slider_2.setText("30min")


#pushButton_heat
        self.pushButton_heat = QtGui.QPushButton(themostat)
        self.pushButton_heat.setGeometry(QtCore.QRect(470, 300, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_heat.setFont(font)
        self.pushButton_heat.setObjectName(_fromUtf8("pushButton_heat"))
#label_mode_fanauto
        self.label_mode_fanauto = QtGui.QLabel(themostat)
        self.label_mode_fanauto.setGeometry(QtCore.QRect(640, 120, 101, 31))
        self.label_mode_fanauto.setObjectName(_fromUtf8("label_mode_fanauto"))
#label_leaving_lowertemp
        self.label_leaving_lowertemp = QtGui.QLabel(themostat)
        self.label_leaving_lowertemp.setGeometry(QtCore.QRect(670, 240, 41, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(20)
        self.label_leaving_lowertemp.setFont(font)
        self.label_leaving_lowertemp.setObjectName(_fromUtf8("label_leaving_lowertemp"))

#define ratranstateUi function
        self.retranslateUi(themostat)   
        QtCore.QMetaObject.connectSlotsByName(themostat)

    def retranslateUi(self, themostat):
        themostat.setWindowTitle(_translate("themostat", "wifi themostat", None))
        self.pushButton_up.setText(_translate("themostat", "Up", None))
        self.pushButton_setting.setText(_translate("themostat", "Setting", None))
        self.label_curtemp.setText(_translate("themostat", str(cur_temp)+'°F', None))
        self.label_current.setText(_translate("themostat", "Current", None))
        self.pushButton_left.setText(_translate("themostat", "Hold/\nRun", None))
        self.pushButton_down.setText(_translate("themostat", "Down", None))   
        self.label_set.setText(_translate("themostat", "Set", None))
        self.pushButton_onauto.setText(_translate("themostat", "On/Auto", None))
        self.pushButton_right.setText(_translate("themostat", "Stop", None))
        self.label_settemp.setText(_translate("themostat", str(set_temp)+'°F', None))
        self.label_fanstate.setText(_translate("themostat", "Fan: "+fan_state, None))
        self.label_modestate.setText(_translate("themostat", mode_state, None))
        self.modebox.addItem('cool')
        self.modebox.addItem('off')
        self.modebox.addItem('heat')
        self.modebox.currentIndexChanged.connect(self.modechange)
#******************#
#schudule function
#******************#
        self.Title_schedule.setText(_translate("Schedule", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt;\">Daily Schedule</span></p></body></html>", None))
        self.pushButton_add.setText(_translate("themostat", "+", None))
        self.pushButton_minus.setText(_translate("themostat", "-", None))
        self.pushButton_1.setText(_translate("themostat", "Mon", None))
        self.label_tem1.setText(_translate("themostat", str(tem_1[day_number]), None))
        self.label_tem2.setText(_translate("themostat", str(tem_2[day_number]), None))
        self.label_tem3.setText(_translate("themostat", str(tem_3[day_number]), None))
        self.label_tem4.setText(_translate("themostat", str(tem_4[day_number]), None))
        self.label_day.setText(_translate("themostat", "<html><head/><body><p><span style=\" font-size:16pt;\">Day</span></p></body></html>", None))
        self.label_time_range.setText(_translate("themostat", "<html><head/><body><p><span style=\" font-size:16pt;\">Time Range</span></p></body></html>", None))
        self.label_set1.setText(_translate("themostat", "<html><head/><body><p><span style=\" font-size:16pt;\">Set</span></p></body></html>", None))
        self.pushButton_up1.setText(_translate("themostat", "Up", None))
        self.pushButton_left1.setText(_translate("themostat", "<--", None))
        self.pushButton_right1.setText(_translate("themostat", "-->", None))
        self.pushButton_down1.setText(_translate("themostat", "Down", None))
        self.pushButton_2.setText(_translate("themostat", "Tues", None))
        self.pushButton_5.setText(_translate("themostat", "Fri", None))
        self.pushButton_4.setText(_translate("themostat", "Thurs", None))
        self.pushButton_3.setText(_translate("themostat", "Wed", None))
        self.pushButton_6.setText(_translate("themostat", "Sat", None))
        self.pushButton_7.setText(_translate("themostat", "Sun", None))      
        self.pushButton_back.setText(_translate("themostat", "Back", None))
        self.pushButton_back1.setText(_translate("themostat", "Back", None))
        self.pushButton_schedule.setText(_translate("themostat", "Schedule", None))
        self.pushButton_mode.setText(_translate("themostat", "Mode", None))
        for x in range (0,24):
            self.comboBox_1_1.addItem(list_time[x])
            self.comboBox_1_2.addItem(list_time[x])
            self.comboBox_1_3.addItem(list_time[x])
            self.comboBox_1_4.addItem(list_time[x])
            self.comboBox_1_5.addItem(list_time[x])
            self.comboBox_1_6.addItem(list_time[x])
            self.comboBox_1_7.addItem(list_time[x])
            self.comboBox_1_8.addItem(list_time[x])
            self.comboBox_1_9.addItem(list_time[x])
            self.comboBox_1_10.addItem(list_time[x])
            self.comboBox_1_11.addItem(list_time[x])
            self.comboBox_1_12.addItem(list_time[x])

            self.comboBox_2_1.addItem(list_time[x])
            self.comboBox_2_2.addItem(list_time[x])
            self.comboBox_2_3.addItem(list_time[x])
            self.comboBox_2_4.addItem(list_time[x])
            self.comboBox_2_5.addItem(list_time[x])
            self.comboBox_2_6.addItem(list_time[x])
            self.comboBox_2_7.addItem(list_time[x])
            self.comboBox_2_8.addItem(list_time[x])
            self.comboBox_2_9.addItem(list_time[x])
            self.comboBox_2_10.addItem(list_time[x])
            self.comboBox_2_11.addItem(list_time[x])
            self.comboBox_2_12.addItem(list_time[x])

            self.comboBox_3_1.addItem(list_time[x])
            self.comboBox_3_2.addItem(list_time[x])
            self.comboBox_3_3.addItem(list_time[x])
            self.comboBox_3_4.addItem(list_time[x])
            self.comboBox_3_5.addItem(list_time[x])
            self.comboBox_3_6.addItem(list_time[x])
            self.comboBox_3_7.addItem(list_time[x])
            self.comboBox_3_8.addItem(list_time[x])
            self.comboBox_3_9.addItem(list_time[x])
            self.comboBox_3_10.addItem(list_time[x])
            self.comboBox_3_11.addItem(list_time[x])
            self.comboBox_3_12.addItem(list_time[x])

            self.comboBox_4_1.addItem(list_time[x])
            self.comboBox_4_2.addItem(list_time[x])
            self.comboBox_4_3.addItem(list_time[x])
            self.comboBox_4_4.addItem(list_time[x])
            self.comboBox_4_5.addItem(list_time[x])
            self.comboBox_4_6.addItem(list_time[x])
            self.comboBox_4_7.addItem(list_time[x])
            self.comboBox_4_8.addItem(list_time[x])
            self.comboBox_4_9.addItem(list_time[x])
            self.comboBox_4_10.addItem(list_time[x])
            self.comboBox_4_11.addItem(list_time[x])
            self.comboBox_4_12.addItem(list_time[x])

            self.comboBox_5_1.addItem(list_time[x])
            self.comboBox_5_2.addItem(list_time[x])
            self.comboBox_5_3.addItem(list_time[x])
            self.comboBox_5_4.addItem(list_time[x])
            self.comboBox_5_5.addItem(list_time[x])
            self.comboBox_5_6.addItem(list_time[x])
            self.comboBox_5_7.addItem(list_time[x])
            self.comboBox_5_8.addItem(list_time[x])
            self.comboBox_5_9.addItem(list_time[x])
            self.comboBox_5_10.addItem(list_time[x])
            self.comboBox_5_11.addItem(list_time[x])
            self.comboBox_5_12.addItem(list_time[x])

            self.comboBox_6_1.addItem(list_time[x])
            self.comboBox_6_2.addItem(list_time[x])
            self.comboBox_6_3.addItem(list_time[x])
            self.comboBox_6_4.addItem(list_time[x])
            self.comboBox_6_5.addItem(list_time[x])
            self.comboBox_6_6.addItem(list_time[x])
            self.comboBox_6_7.addItem(list_time[x])
            self.comboBox_6_8.addItem(list_time[x])
            self.comboBox_6_9.addItem(list_time[x])
            self.comboBox_6_10.addItem(list_time[x])
            self.comboBox_6_11.addItem(list_time[x])
            self.comboBox_6_12.addItem(list_time[x])

            self.comboBox_7_1.addItem(list_time[x])
            self.comboBox_7_2.addItem(list_time[x])
            self.comboBox_7_3.addItem(list_time[x])
            self.comboBox_7_4.addItem(list_time[x])
            self.comboBox_7_5.addItem(list_time[x])
            self.comboBox_7_6.addItem(list_time[x])
            self.comboBox_7_7.addItem(list_time[x])
            self.comboBox_7_8.addItem(list_time[x])
            self.comboBox_7_9.addItem(list_time[x])
            self.comboBox_7_10.addItem(list_time[x])
            self.comboBox_7_11.addItem(list_time[x])
            self.comboBox_7_12.addItem(list_time[x])
            
        Monday_hide(self)
        Tuesday_hide(self)
        Wednesday_hide(self)
        Thursday_hide(self)
        Friday_hide(self)
        Saturday_hide(self)
        Sunday_hide(self)
        
        self.pushButton_add.setVisible(False)
        self.pushButton_minus.setVisible(False)
        self.label_tem1.setVisible(False)
        self.label_tem2.setVisible(False)
        self.label_tem3.setVisible(False)
        self.label_tem4.setVisible(False)
        self.label_day.setVisible(False)
        self.label_time_range.setVisible(False)
        self.label_set1.setVisible(False)
        self.pushButton_up1.setVisible(False)
        self.pushButton_left1.setVisible(False)
        self.pushButton_right1.setVisible(False)
        self.pushButton_down1.setVisible(False)
        self.pushButton_1.setVisible(False)
        self.pushButton_2.setVisible(False)
        self.pushButton_5.setVisible(False)
        self.pushButton_4.setVisible(False)
        self.pushButton_3.setVisible(False)
        self.pushButton_6.setVisible(False)
        self.pushButton_7.setVisible(False)
        self.label_tem5.setVisible(False)
        self.label_tem6.setVisible(False)
        self.pushButton_back.setVisible(False)
        self.Title_schedule.setVisible(False)
        self.pushButton_back1.setVisible(False)
        self.pushButton_schedule.setVisible(False)
        self.pushButton_mode.setVisible(False)

#******************#
#mode function
#******************#
        self.Title_mode.setText(_translate("themostat", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt;\">Mode Function</span></p></body></html>", None))
        self.label_mode_sleep.setText(_translate("themostat", "<html><head/><body><p><span style=\" font-size:16pt;\">Sleep Mode</span></p></body></html>", None))
        self.label_mode_save.setText(_translate("themostat", "<html><head/><body><p><span style=\" font-size:16pt;\">Save Mode</span></p></body></html>", None))
        self.label_mode_precool.setText(_translate("themostat", "<html><head/><body><p><span style=\" font-size:16pt;\">Pre Cool Mode</span></p></body></html>", None))
        self.pushButton_back2.setText(_translate("themostat", "Back", None))
        self.pushButton_sleep.setText(_translate("themostat", "Run", None))
        self.pushButton_cool.setText(_translate("themostat", "Run", None))
        self.pushButton_save.setText(_translate("themostat", "Run", None))
        self.label_mode_time.setText(_translate("themostat", "<html><head/><body><p><span style=\" font-size:16pt;\">Time</span></p></body></html>", None))
        self.label_mode_set.setText(_translate("themostat", "Set", None))
        #self.label_mode_settemp.setText(_translate("themostat", "80", None))
        self.label_mode_toset.setText(_translate("themostat", "To set", None))
        #self.label_sleep_lowertemp.setText(_translate("themostat", "77", None))
        self.label_mode_preheat.setText(_translate("themostat", "<html><head/><body><p><span style=\" font-size:16pt;\">Pre Heat Mode</span></p></body></html>", None))
        #self.label_mode_pretemp.setText(_translate("themostat", "80", None))
        self.pushButton_heat.setText(_translate("themostat", "Run", None))
        self.label_mode_fanauto.setText(_translate("themostat", "<html><head/><body><p><span style=\" font-size:16pt;\">Fan Auto</span></p></body></html>", None))
        #self.label_leaving_lowertemp.setText(_translate("themostat", "85", None))

        self.Title_mode.setVisible(False)
        self.label_mode_sleep.setVisible(False)
        self.label_mode_save.setVisible(False)
        self.label_mode_precool.setVisible(False)
        self.pushButton_back2.setVisible(False)
        self.pushButton_sleep.setVisible(False)
        self.pushButton_cool.setVisible(False)
        self.pushButton_save.setVisible(False)
        self.label_mode_time.setVisible(False)
        self.label_mode_set.setVisible(False)
        self.label_mode_settemp.setVisible(False)
        self.label_mode_toset.setVisible(False)
        self.label_sleep_lowertemp.setVisible(False)
        self.label_mode_preheat.setVisible(False)
        self.label_mode_pretemp.setVisible(False)
        self.pushButton_heat.setVisible(False)
        self.label_mode_fanauto.setVisible(False)
        self.label_leaving_lowertemp.setVisible(False)
        self.horizontalSlider_time1.setVisible(False)
        self.horizontalSlider_time2.setVisible(False)
        self.label_slider_1.setVisible(False)
        self.label_slider_2.setVisible(False)
        
        
def run():
    import sys
    app=QtGui.QApplication(sys.argv)
    widget=QtGui.QWidget()
    ui=Ui_themostat()
    ui.setupUi(widget)
    widget.show()
    sys.exit(app.exec_())

'''run()'''
