from PyQt4 import QtGui, QtCore
from PyQt4.Qt import *
from thermostat_ui import *
import _thread
import random
import time
import schedule
import datetime
from switch_widget import *
from daily_schedule import *
from schedule_combobox_appear_hide import *
from synchronize_data import *

try:
    from environment_temp import *
except:
    pass
try:
    from curtemp_from_sensor_DS18B20 import *
except:
    pass
try:
    #from AC_running_main_function import *
    from Real_AC_Running import *
except:
    pass
mode_name_number=0
tem_set_number=1
sch_number=[0,4,4,4,4,4,4,4]
sch_1=[]
sch_2=[]
sch_3=[]
sch_4=[]
sch_5=[]
sch_6=[]
sch_7=[]
sch_run = 0
tem_position1=1
today=0
sch_label=' '

try:
    from PyQt4.QtCore import QString
except ImportError:
    # we are using Python3 so QString is not defined
    QString = type("")

        
class gettemp(QThread):
    def run(self):
        while True:
            global cur_temp
#            try:
#                cur_temp=get_temp_from_Arduino(cur_temp)
#                postdata('cur_temp',cur_temp)
#            except:
#                pass
                #continue
            
            try:
                cur_temp=get_temp_from_sensor()
                time.sleep(5)
                postdata('cur_temp',cur_temp)
            except:
                pass
            #    continue
            
class Sleep_Mode(QThread):
    def run(self):
              global set_temp,stop_it,mode_name_number,run_or_not_sleep,sleep_time
              mode_name_number=1
              set_temp= set_temp - 3
              postdata('set_temp',set_temp)
              sleep_time_here = sleep_time
              while (sleep_time_here>0):
                sleep_time_here = sleep_time_here - 1
                print("sleep mode running")
                print(sleep_time_here)
                time.sleep(1)                
                if(run_or_not_sleep==0):
                    sleep_time_here=0
                    break
              if(sleep_time_here<=0):
                 set_temp=set_temp+3
                 print("sleep mode finish")
                 run_or_not_sleep=0
                 mode_name_number=0
                 stop_it=0
                 postdata('run_or_not_sleep',0)
                 postdata('stop_it',0)
                 postdata('set_temp',set_temp)

class Pre_Cool_Mode(QThread):
    def run(self):
                global run_or_not_precool,set_temp,mode_name_number,precool_time,stop_it,cool_not
                temp_here=set_temp
                cool_not=0
                n=15
                mode_name_number=2
                precool_time_here=precool_time-15
                while (precool_time_here>0):# precool_time_here
                    time.sleep(1)
                    precool_time_here=precool_time_here-1                    
                    print("waiting")
                    print(precool_time_here)
                    if(run_or_not_precool==0):
                        n=0
                        break                       
                if(precool_time_here==0):
                    temp_here=set_temp                    
                    set_temp=set_temp-5
                    cool_not=1
                    postdata('set_temp',set_temp)
                while (n>0):
                    n = n - 1
                    print("running_precool")
                    print(n)
                    if(run_or_not_precool==0):
                        set_temp=temp_here
                        postdata('set_temp',set_temp)
                        print("break it from outside faction")
                        break
                    time.sleep(1)
                if(n<=0):
                    print("break")
                    set_temp=temp_here                     
                    stop_it=0
                    mode_name_number=0
                    run_or_not_precool=0
                    postdata('set_temp',set_temp)
                    postdata('run_or_not_precool',0)
                    postdata('stop_it',0)
                    
class Pre_Heat_Mode(QThread):
    def run(self):
                global run_or_not_preheat,set_temp,mode_name_number,precool_time,stop_it,heat_not
                temp_here=set_temp
                n=15
                heat_not=0
                mode_name_number=3
                preheat_time_here=preheat_time-15
                while (preheat_time_here>0):# precool_time_here
                    time.sleep(1)
                    preheat_time_here=preheat_time_here-1 
                    print("waiting")
                    print(preheat_time_here)
                    if(run_or_not_preheat==0):
                        n=0
                        break                        
                if(preheat_time_here==0):
                    temp_here=set_temp
                    set_temp=set_temp+5
                    heat_not=1
                    postdata('set_temp',set_temp)
                while (n>0):
                    n = n - 1
                    print("running_preheat")
                    print(n)
                    if(run_or_not_preheat==0):
                        set_temp=temp_here
                        print("break it from outside faction")
                        break
                    time.sleep(1)
                if(n<=0):
                    print("break")
                    stop_it=1
                    mode_name_number=0
                    run_or_not_preheat=0
                    set_temp=temp_here
                    postdata('run_or_not_preheat',0)
                    postdata('stop_it',0)
                    postdata('set_temp',set_temp)


class Save_Mode(QThread):
    def run(self):
                    global run_or_not_save,cool_or_heat,set_temp,mode_name_number,state_4,stop_it,fan_state
                    mode_name_number=4
                    if(cool_or_heat==1):
                        set_temp= set_temp +5
                        fan_state='Auto'
                    else:
                        set_temp= set_temp -5
                        fan_state='Auto'
                    postdata('set_temp',set_temp)
                    postdata('fan_cloud',1)
                    while True:
                        time.sleep(5)                
                        print("saving mode running")

                    
class synchronize(QThread):
    def run(self):
        while True:
            global mode_cloud,fan_cloud,fan_state,mode_state,mode_state_cloud,precool_time,preheat_time,run_or_not_precool,run_or_not_preheat,run_or_not_save,run_or_not_sleep,sch_cloud,set_temp,sleep_time,stop_it
            w=Widget()
            try:
                cloud=getcloud()
                if(cloud==1):
                    w.on_pushButton_onauto_pressed()
                    postdata('cloud',0)
                elif(cloud==2):
                    mode_cloud=mergedata(firebase.get('/00002/mode_cloud',None))
                    mode_state_cloud=mergedata(firebase.get('/00002/mode_state_cloud',None))
                    if(mode_cloud==0):
                        mode_state='off'
                    elif(mode_cloud==1):
                        mode_state='cool'
                    else:
                        mode_state='heat'
                    postdata('cloud',0)
                    #w.modechange(mode_cloud)
                elif(cloud==3):
                    precool_time=mergedata(firebase.get('/00002/precool_time',None))
                    postdata('cloud',0)
                elif(cloud==4):
                    preheat_time=mergedata(firebase.get('/00002/preheat_time',None))
                    postdata('cloud',0)
                elif(cloud==5):
                    w.on_pushButton_cool_pressed()
                    postdata('cloud',0)
                elif(cloud==6):
                    w.on_pushButton_heat_pressed()
                    postdata('cloud',0)
                elif(cloud==7):
                    w.on_pushButton_save_pressed()
                    postdata('cloud',0)
                elif(cloud==8):
                    w.on_pushButton_sleep_pressed()
                    postdata('cloud',0)
                elif(cloud==9):
                    w.on_pushButton_left_pressed()
                    postdata('cloud',0)
                elif(cloud==10):
                    w.on_pushButton_up_pressed()
                    postdata('cloud',0)
                elif(cloud==11):
                    w.on_pushButton_down_pressed()
                    postdata('cloud',0)
                elif(cloud==12):
                    sleep_time=mergedata(firebase.get('/00002/sleep_time',None))
                    postdata('cloud',0)
                elif(cloud==13):
                    w.on_pushButton_right_pressed()
                    postdata('cloud',0)
                #print('1') 
            except:
                pass
            
class AC_Running(QThread):
    update_cur_temp = pyqtSignal(QString)
    def run(self):
        while True:
            global set_temp,cur_temp,mode_state, fan_state,today,sch_run,sch_cloud
#schedule
            today=datetime.datetime.now().weekday()+1
            #print(today)
            schedule.run_pending()
            if(sch_cloud==0):
                Widget.sch_change()
                sch_cloud=1
                postdata('sch_cloud',sch_cloud)
            self.update_cur_temp.emit(QString(str(cur_temp)))
            
            #try:
            #cur_temp=get_temp_from_sensor()
                #time.sleep(5)
            #postdata('cur_temp',cur_temp)
            #except:
                #pass           
#AC function            
 
            try:
                AC_Running_Function(mode_state, set_temp, cur_temp,fan_state)                    
            except:
                pass

            time.sleep(1)
#read temperature from txt
#            f=open('currentTemperature.txt')
#            cur_temp=(int)(f.readline())
#            f.close           
#            print(cur_temp)
                
              
              
class Widget(QtGui.QWidget, Ui_themostat):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self)

    def on_pushButton_up_pressed(self):
        global set_temp, cur_temp, mode_state,mode_name_number
        global run_or_not_save ,run_or_not_sleep,run_or_not_precool,run_or_not_preheat,stop_it
        Widget.on_pushButton_right_pressed(self)
        if(mode_state != 'off'):
            set_temp=set_temp+1
            self.label_settemp.setText(str(set_temp)+'°F')
            _thread.start_new_thread(postdata,('set_temp',set_temp))
        
    def on_pushButton_down_pressed(self):
        global set_temp, cur_temp, mode_state,mode_name_number
        global run_or_not_save ,run_or_not_sleep,run_or_not_precool,run_or_not_preheat,stop_it
        Widget.on_pushButton_right_pressed(self)
        if(mode_state != 'off'):
            set_temp-=1
            self.label_settemp.setText(str(set_temp)+'°F')
            _thread.start_new_thread(postdata,('set_temp',set_temp))

    def on_pushButton_onauto_pressed(self):
       global fan_state, fan_cloud
       if(fan_state=='On'):
            fan_state = 'Auto'
            fan_cloud=1
            _thread.start_new_thread(postdata,('fan_cloud',fan_cloud))
       else:
            fan_state='On'
            fan_cloud=0
            _thread.start_new_thread(postdata,('fan_cloud',fan_cloud))

    def modechange(self,mode_cloud):
        global mode_state,cur_temp, set_temp, cool_or_heat,mode_name_number
        global run_or_not_save,run_or_not_sleep,run_or_not_precool,run_or_not_preheat,stop_it
        mode_state = self.modebox.currentText()
        
        if(mode_state == 'off'):
            self.label_settemp.setVisible(False)
            Widget.on_pushButton_right_pressed(self)
            mode_cloud=0
        elif(mode_state=='cool'):
            self.label_settemp.setVisible(True)
            mode_cloud=1        
        else:
            self.label_settemp.setVisible(True)
            mode_cloud=2
        _thread.start_new_thread(postdata,('mode_cloud',mode_cloud))     

        if(mode_state == "cool"):
            cool_or_heat = 1
        else:
            cool_or_heat = 2

            
    def on_pushButton_left_pressed(self):
        Widget.sch_change()

    def sch_change():
        global sch_run, sch_label
        if(sch_run==0):
            sch_run=1
            sch_label='Hold'
            schedule.clear()
            print("stop")
            postdata('sch_state_cloud',0)
        else:
            sch_run=0
            create_schedule()
            sch_label=''
            postdata('sch_state_cloud',1)

    def on_pushButton_right_pressed(self):
        global run_or_not_save,run_or_not_sleep,run_or_not_precool,run_or_not_preheat,stop_it,set_temp
        global mode_name_number,cool_not,fan_state       
        stop_it=0        
        if(mode_name_number==1):

            Back1.terminate()
            set_temp=set_temp+3
            run_or_not_sleep=0
            _thread.start_new_thread(postdata,('run_or_not_sleep',0))
            _thread.start_new_thread(postdata,('set_temp',set_temp))
        elif(mode_name_number==2):
            if(cool_not==1):
                set_temp=set_temp+5
            run_or_not_precool=0
            _thread.start_new_thread(postdata,('run_or_not_precool',0))
            Back2.terminate()
            _thread.start_new_thread(postdata,('set_temp',set_temp))
        elif(mode_name_number==3):
            if(heat_not==1):
                set_temp=set_temp-5
            run_or_not_preheat=0
            _thread.start_new_thread(postdata,('run_or_not_preheat',0))
            Back3.terminate()
            _thread.start_new_thread(postdata,('set_temp',set_temp))
        elif(mode_name_number==4):
            Back4.terminate()
            run_or_not_save =0
            _thread.start_new_thread(postdata,('run_or_not_save',0))
            if(cool_or_heat==1):
                set_temp= set_temp -5
            else:
                set_temp= set_temp +5
            fan_state='On'
            _thread.start_new_thread(postdata,('set_temp',set_temp))        
        mode_name_number=0
           
    def curtempchange(self,cur_temp):
        global set_temp, fan_state, mode_name_number,sch_label,mode_state,cool_or_heat,mode_state_cloud
        self.label_curtemp.setText(str(cur_temp)+'°F')
        self.label_settemp.setText(str(set_temp)+'°F')
        self.label_mode_running.setText(mode_name[mode_name_number])
        self.label_fanstate.setText("Fan: "+fan_state)
        self.label_hold.setText(sch_label)
        self.label_modestate.setText(mode_state)
        if(mode_name_number==1):
            self.pushButton_sleep.setText("Stop")
        if(mode_name_number==2):
            self.pushButton_cool.setText("Stop")
        if(mode_name_number==3):
            self.pushButton_heat.setText("Stop")
        if(mode_name_number==4):
            self.pushButton_save.setText("Stop")
        if(mode_state_cloud==0):
            time.sleep(1)
            if(mode_cloud == 0):
                self.label_settemp.setVisible(False)
                Widget.on_pushButton_right_pressed(self)
                mode_state_cloud=1
            else:
                self.label_settemp.setVisible(True)
                mode_state_cloud=1
            postdata('mode_state_cloud',mode_state_cloud)
        if(mode_state == "cool"):
            cool_or_heat = 1
        else:
            cool_or_heat = 2

    def on_pushButton_setting_pressed(self):
        setting_to_middle(self)

    def update_settemp(self):
        global set_temp
        self.label_settemp.setText(str(set_temp)+'°F')
#******************#
#schudule function
#******************#

    def on_pushButton_1_pressed(self):
        global day_number,sch_number,tem_1,tem_2,tem_3,tem_4,tem_5, tem_6
        global tem_set_number
        day_number=1
        tem_set_number=1
        schedule_temp_back(self)
        day_change(self,day_number)
        Monday_appear(self)
        Tuesday_hide(self)
        Wednesday_hide(self)
        Thursday_hide(self)
        Friday_hide(self)
        Saturday_hide(self)
        Sunday_hide(self)
        output_temp(self)
        if(sch_number[day_number]==4):
            self.comboBox_1_9.setVisible(False)
            self.comboBox_1_10.setVisible(False)
            self.comboBox_1_11.setVisible(False)
            self.comboBox_1_12.setVisible(False)
        if(sch_number[day_number]==5):
            self.comboBox_1_11.setVisible(False)
            self.comboBox_1_12.setVisible(False)
    def on_pushButton_2_pressed(self):
        global day_number,sch_number,tem_1,tem_2,tem_3,tem_4,tem_5, tem_6
        global tem_set_number
        day_number=2
        tem_set_number=1
        schedule_temp_back(self)
        day_change(self,day_number)
        Monday_hide(self)
        Tuesday_appear(self)
        Wednesday_hide(self)
        Thursday_hide(self)
        Friday_hide(self)
        Saturday_hide(self)
        Sunday_hide(self)
        output_temp(self)
        if(sch_number[day_number]==4):
            self.comboBox_2_9.setVisible(False)
            self.comboBox_2_10.setVisible(False)
            self.comboBox_2_11.setVisible(False)
            self.comboBox_2_12.setVisible(False)
        if(sch_number[day_number]==5):
            self.comboBox_2_11.setVisible(False)
            self.comboBox_2_12.setVisible(False)
    def on_pushButton_3_pressed(self):
        global day_number,sch_number,tem_1,tem_2,tem_3,tem_4,tem_5, tem_6
        global tem_set_number
        day_number=3
        tem_set_number=1
        schedule_temp_back(self)
        day_change(self,day_number)
        Monday_hide(self)
        Tuesday_hide(self)
        Wednesday_appear(self)
        Thursday_hide(self)
        Friday_hide(self)
        Saturday_hide(self)
        Sunday_hide(self)
        output_temp(self)
        if(sch_number[day_number]==4):
            self.comboBox_3_9.setVisible(False)
            self.comboBox_3_10.setVisible(False)
            self.comboBox_3_11.setVisible(False)
            self.comboBox_3_12.setVisible(False)
        if(sch_number[day_number]==5):
            self.comboBox_3_11.setVisible(False)
            self.comboBox_3_12.setVisible(False)
    def on_pushButton_4_pressed(self):
        global day_number,sch_number,tem_1,tem_2,tem_3,tem_4,tem_5, tem_6
        global tem_set_number
        day_number=4
        tem_set_number=1
        schedule_temp_back(self)
        day_change(self,day_number)
        Monday_hide(self)
        Tuesday_hide(self)
        Wednesday_hide(self)
        Thursday_appear(self)
        Friday_hide(self)
        Saturday_hide(self)
        Sunday_hide(self)
        output_temp(self)
        if(sch_number[day_number]==4):
            self.comboBox_4_9.setVisible(False)
            self.comboBox_4_10.setVisible(False)
            self.comboBox_4_11.setVisible(False)
            self.comboBox_4_12.setVisible(False)
        if(sch_number[day_number]==5):
            self.comboBox_4_11.setVisible(False)
            self.comboBox_4_12.setVisible(False)        
    def on_pushButton_5_pressed(self):
        global day_number,sch_number,tem_1,tem_2,tem_3,tem_4,tem_5, tem_6
        global tem_set_number
        day_number=5
        tem_set_number=1
        schedule_temp_back(self)
        day_change(self,day_number)
        Monday_hide(self)
        Tuesday_hide(self)
        Wednesday_hide(self)
        Thursday_hide(self)
        Friday_appear(self)
        Saturday_hide(self)
        Sunday_hide(self)
        output_temp(self)
        if(sch_number[day_number]==4):
            self.comboBox_5_9.setVisible(False)
            self.comboBox_5_10.setVisible(False)
            self.comboBox_5_11.setVisible(False)
            self.comboBox_5_12.setVisible(False)
        if(sch_number[day_number]==5):
            self.comboBox_5_11.setVisible(False)
            self.comboBox_5_12.setVisible(False)        
    def on_pushButton_6_pressed(self):
        global day_number,sch_number,tem_1,tem_2,tem_3,tem_4,tem_5, tem_6
        global tem_set_number
        day_number=6
        tem_set_number=1
        schedule_temp_back(self)
        day_change(self,day_number)
        Monday_hide(self)
        Tuesday_hide(self)
        Wednesday_hide(self)
        Thursday_hide(self)
        Friday_hide(self)
        Saturday_appear(self)
        Sunday_hide(self)
        output_temp(self)
        if(sch_number[day_number]==4):
            self.comboBox_6_9.setVisible(False)
            self.comboBox_6_10.setVisible(False)
            self.comboBox_6_11.setVisible(False)
            self.comboBox_6_12.setVisible(False)
        if(sch_number[day_number]==5):
            self.comboBox_6_11.setVisible(False)
            self.comboBox_6_12.setVisible(False)        
    def on_pushButton_7_pressed(self):
        global day_number,sch_number,tem_1,tem_2,tem_3,tem_4,tem_5, tem_6
        global tem_set_number
        day_number=7
        tem_set_number=1
        schedule_temp_back(self)
        day_change(self,day_number)
        Monday_hide(self)
        Tuesday_hide(self)
        Wednesday_hide(self)
        Thursday_hide(self)
        Friday_hide(self)
        Saturday_hide(self)
        Sunday_appear(self)
        output_temp(self)
        if(sch_number[day_number]==4):
            self.comboBox_7_9.setVisible(False)
            self.comboBox_7_10.setVisible(False)
            self.comboBox_7_11.setVisible(False)
            self.comboBox_7_12.setVisible(False)
        if(sch_number[day_number]==5):
            self.comboBox_7_11.setVisible(False)
            self.comboBox_7_12.setVisible(False)        
    def on_pushButton_add_pressed(self):
        global day_number, sch_number, tem_5, tem_6
        if(day_number==1):
            if(sch_number[day_number]==4):
                self.comboBox_1_9.setVisible(True)
                self.comboBox_1_10.setVisible(True)
                tem_5[day_number]=78
                self.label_tem5.setText(str(tem_5[day_number]))
            if(sch_number[day_number]==5):
                self.comboBox_1_11.setVisible(True)
                self.comboBox_1_12.setVisible(True)
                tem_6[day_number]=78
                self.label_tem6.setText(str(tem_6[day_number]))
            sch_number[day_number]+=1
        if(day_number==2):
            if(sch_number[day_number]==4):
                self.comboBox_2_9.setVisible(True)
                self.comboBox_2_10.setVisible(True)
                tem_5[day_number]=78
                self.label_tem5.setText(str(tem_5[day_number]))
            if(sch_number[day_number]==5):
                self.comboBox_2_11.setVisible(True)
                self.comboBox_2_12.setVisible(True)
                tem_6[day_number]=78
                self.label_tem6.setText(str(tem_6[day_number]))        
            sch_number[day_number]+=1
        if(day_number==3):
            if(sch_number[day_number]==4):
                self.comboBox_3_9.setVisible(True)
                self.comboBox_3_10.setVisible(True)
                tem_5[day_number]=78
                self.label_tem5.setText(str(tem_5[day_number]))
            if(sch_number[day_number]==5):
                self.comboBox_3_11.setVisible(True)
                self.comboBox_3_12.setVisible(True)
                tem_6[day_number]=78
                self.label_tem6.setText(str(tem_6[day_number]))        
            sch_number[day_number]+=1
        if(day_number==4):
            if(sch_number[day_number]==4):
                self.comboBox_4_9.setVisible(True)
                self.comboBox_4_10.setVisible(True)
                tem_5[day_number]=78
                self.label_tem5.setText(str(tem_5[day_number]))
            if(sch_number[day_number]==5):
                self.comboBox_4_11.setVisible(True)
                self.comboBox_4_12.setVisible(True)
                tem_6[day_number]=78
                self.label_tem6.setText(str(tem_6[day_number]))        
            sch_number[day_number]+=1
        if(day_number==5):
            if(sch_number[day_number]==4):
                self.comboBox_5_9.setVisible(True)
                self.comboBox_5_10.setVisible(True)
                tem_5[day_number]=78
                self.label_tem5.setText(str(tem_5[day_number]))
            if(sch_number[day_number]==5):
                self.comboBox_5_11.setVisible(True)
                self.comboBox_5_12.setVisible(True)
                tem_6[day_number]=78
                self.label_tem6.setText(str(tem_6[day_number]))        
            sch_number[day_number]+=1
        if(day_number==6):
            if(sch_number[day_number]==4):
                self.comboBox_6_9.setVisible(True)
                self.comboBox_6_10.setVisible(True)
                tem_5[day_number]=78
                self.label_tem5.setText(str(tem_5[day_number]))
            if(sch_number[day_number]==5):
                self.comboBox_6_11.setVisible(True)
                self.comboBox_6_12.setVisible(True)
                tem_6[day_number]=78
                self.label_tem6.setText(str(tem_6[day_number]))        
            sch_number[day_number]+=1
        if(day_number==7):
            if(sch_number[day_number]==4):
                self.comboBox_7_9.setVisible(True)
                self.comboBox_7_10.setVisible(True)
                tem_5[day_number]=78
                self.label_tem5.setText(str(tem_5[day_number]))
            if(sch_number[day_number]==5):
                self.comboBox_7_11.setVisible(True)
                self.comboBox_7_12.setVisible(True)
                tem_6[day_number]=78
                self.label_tem6.setText(str(tem_6[day_number]))        
            sch_number[day_number]+=1
        if(sch_number[day_number]>6):
            sch_number[day_number]=6

    def on_pushButton_minus_pressed(self):
        global day_number, sch_number, tem_5, tem_6
        if(day_number==1):
            if(sch_number[day_number]==6):
                self.comboBox_1_11.setVisible(False)
                self.comboBox_1_12.setVisible(False)
                tem_6[day_number]=''
                self.label_tem6.setText(str(tem_6[day_number]))
            if(sch_number[day_number]==5):
                self.comboBox_1_9.setVisible(False)
                self.comboBox_1_10.setVisible(False)
                tem_5[day_number]=''
                self.label_tem5.setText(str(tem_5[day_number]))
            sch_number[day_number]-=1
        if(day_number==2):
            if(sch_number[day_number]==6):
                self.comboBox_2_11.setVisible(False)
                self.comboBox_2_12.setVisible(False)
                tem_6[day_number]=''
                self.label_tem6.setText(str(tem_6[day_number]))
            if(sch_number[day_number]==5):
                self.comboBox_2_9.setVisible(False)
                self.comboBox_2_10.setVisible(False)
                tem_5[day_number]=''
                self.label_tem5.setText(str(tem_5[day_number]))
            sch_number[day_number]-=1
        if(day_number==3):
            if(sch_number[day_number]==6):
                self.comboBox_3_11.setVisible(False)
                self.comboBox_3_12.setVisible(False)
                tem_6[day_number]=''
                self.label_tem6.setText(str(tem_6[day_number]))
            if(sch_number[day_number]==5):
                self.comboBox_3_9.setVisible(False)
                self.comboBox_3_10.setVisible(False)
                tem_5[day_number]=''
                self.label_tem5.setText(str(tem_5[day_number]))
            sch_number[day_number]-=1
        if(day_number==4):
            if(sch_number[day_number]==6):
                self.comboBox_4_11.setVisible(False)
                self.comboBox_4_12.setVisible(False)
                tem_6[day_number]=''
                self.label_tem6.setText(str(tem_6[day_number]))
            if(sch_number[day_number]==5):
                self.comboBox_4_9.setVisible(False)
                self.comboBox_4_10.setVisible(False)
                tem_5[day_number]=''
                self.label_tem5.setText(str(tem_5[day_number]))
            sch_number[day_number]-=1
        if(day_number==5):
            if(sch_number[day_number]==6):
                self.comboBox_5_11.setVisible(False)
                self.comboBox_5_12.setVisible(False)
                tem_6[day_number]=''
                self.label_tem6.setText(str(tem_6[day_number]))
            if(sch_number[day_number]==5):
                self.comboBox_5_9.setVisible(False)
                self.comboBox_5_10.setVisible(False)
                tem_5[day_number]=''
                self.label_tem5.setText(str(tem_5[day_number]))
            sch_number[day_number]-=1
        if(day_number==6):
            if(sch_number[day_number]==6):
                self.comboBox_6_11.setVisible(False)
                self.comboBox_6_12.setVisible(False)
                tem_6[day_number]=''
                self.label_tem6.setText(str(tem_6[day_number]))
            if(sch_number[day_number]==5):
                self.comboBox_6_9.setVisible(False)
                self.comboBox_6_10.setVisible(False)
                tem_5[day_number]=''
                self.label_tem5.setText(str(tem_5[day_number]))
            sch_number[day_number]-=1
        if(day_number==7):
            if(sch_number[day_number]==6):
                self.comboBox_7_11.setVisible(False)
                self.comboBox_7_12.setVisible(False)
                tem_6[day_number]=''
                self.label_tem6.setText(str(tem_6[day_number]))
            if(sch_number[day_number]==5):
                self.comboBox_7_9.setVisible(False)
                self.comboBox_7_10.setVisible(False)
                tem_5[day_number]=''
                self.label_tem5.setText(str(tem_5[day_number]))
            sch_number[day_number]-=1
        if(sch_number[day_number]<4):
            sch_number[day_number]=4
                    
    def on_pushButton_up1_pressed(self):
        global day_number,tem_1, tem_2, tem_3, tem_4, tem_5, tem_6, tem_number,tem_set_number
        if(tem_set_number==1):
            tem_1[day_number]+=1
            self.label_tem1.setText(str(tem_1[day_number]))
        if(tem_set_number==2):
            tem_2[day_number]+=1
            self.label_tem2.setText(str(tem_2[day_number]))
        if(tem_set_number==3):
            tem_3[day_number]+=1
            self.label_tem3.setText(str(tem_3[day_number]))
        if(tem_set_number==4):
            tem_4[day_number]+=1
            self.label_tem4.setText(str(tem_4[day_number]))
        if(tem_set_number==5):
            tem_5[day_number]+=1
            self.label_tem5.setText(str(tem_5[day_number]))
        if(tem_set_number==6):
            tem_6[day_number]+=1
            self.label_tem6.setText(str(tem_6[day_number]))
            
    def on_pushButton_down1_pressed(self):
        global tem_1, tem_2, tem_3, tem_4,tem_5, tem_6, tem_number, tem_set_number
        if(tem_set_number==1):
            tem_1[day_number]-=1
            self.label_tem1.setText(str(tem_1[day_number]))
        if(tem_set_number==2):
            tem_2[day_number]-=1
            self.label_tem2.setText(str(tem_2[day_number]))
        if(tem_set_number==3):
            tem_3[day_number]-=1
            self.label_tem3.setText(str(tem_3[day_number]))
        if(tem_set_number==4):
            tem_4[day_number]-=1
            self.label_tem4.setText(str(tem_4[day_number]))
        if(tem_set_number==5):
            tem_5[day_number]-=1
            self.label_tem5.setText(str(tem_5[day_number]))
        if(tem_set_number==6):
            tem_6[day_number]-=1
            self.label_tem6.setText(str(tem_6[day_number]))

    def on_pushButton_left1_pressed(self):
        global tem_number, sch_number,tem_set_number      
        tem_number, sch_number[day_number],tem_set_number = schedule_temp_position_change_left(self,day_number,tem_number, sch_number[day_number], tem_set_number)    
    def on_pushButton_right1_pressed(self):
        global tem_number, sch_number,tem_set_number       
        tem_number, sch_number[day_number],tem_set_number = schedule_temp_position_change_right(self,day_number,tem_number, sch_number[day_number], tem_set_number)
    def on_pushButton_back_pressed(self):
        schedule_to_main_page(self,mode_state)
        global sch_run
        save_sch_time(self)
        schedule.clear()
        create_schedule()

#***********#
#Middle page
#***********#
    def on_pushButton_back1_pressed(self):
        middle_to_mainpage(self,mode_state)

    def on_pushButton_schedule_pressed(self):
        global day_number,sch_number
        middle_to_schedule(self)
        output_temp(self)
        if(sch_number[day_number]==4):
            self.comboBox_1_9.setVisible(False)
            self.comboBox_1_10.setVisible(False)
            self.comboBox_1_11.setVisible(False)
            self.comboBox_1_12.setVisible(False)
        if(sch_number[day_number]==5):
            self.comboBox_1_11.setVisible(False)
            self.comboBox_1_12.setVisible(False)

    def on_pushButton_mode_pressed(self):
        middle_to_mode(self)
        global sleep_time
        global temp_set , temp_toset ,set_temp,run_or_not_save,run_or_not_sleep,cool_or_heat,run_or_not_precool,run_or_not_preheat    
              
 # cool       
        if(cool_or_heat==1):
            self.pushButton_cool.setEnabled(True)
            self.pushButton_heat.setEnabled(False)
            self.pushButton_sleep.setEnabled(True)
            self.pushButton_save.setEnabled(True)
            if(run_or_not_save ==1):
                self.pushButton_cool.setEnabled(False)
                self.pushButton_heat.setEnabled(False)
                self.pushButton_sleep.setEnabled(False)
                self.pushButton_save.setEnabled(True)
                self.label_mode_settemp.setText(" ")
                self.label_sleep_lowertemp.setText(" ")
                self.label_mode_pretemp.setText(" ")
                self.label_leaving_lowertemp.setText(str(set_temp)) 
            if(run_or_not_sleep ==1):
                self.pushButton_cool.setEnabled(False)
                self.pushButton_heat.setEnabled(False)
                self.pushButton_sleep.setEnabled(True)
                self.pushButton_save.setEnabled(False)
                
                self.label_mode_settemp.setText(str(set_temp+3))
                self.label_sleep_lowertemp.setText(str(set_temp))
                self.label_mode_pretemp.setText(" ")
                self.label_leaving_lowertemp.setText(" ") 
            if(run_or_not_precool ==1):
                self.pushButton_cool.setEnabled(True)
                self.pushButton_heat.setEnabled(False)
                self.pushButton_sleep.setEnabled(False)
                self.pushButton_save.setEnabled(False)
               
                self.label_mode_settemp.setText(" ")
                self.label_sleep_lowertemp.setText(" ")
                self.label_mode_pretemp.setText(str(set_temp-5))
                self.label_leaving_lowertemp.setText(" ") 
           
            else:
                if(run_or_not_precool ==0 and run_or_not_sleep ==0 and run_or_not_save ==0  ):
                    self.pushButton_cool.setEnabled(True)
                    self.pushButton_heat.setEnabled(False)
                    self.pushButton_sleep.setEnabled(True)
                    self.pushButton_save.setEnabled(True)
                   
                    self.label_mode_settemp.setText(str(set_temp))
                    self.label_sleep_lowertemp.setText(str(set_temp-3))
                    self.label_mode_pretemp.setText(str(set_temp-5))
                    self.label_leaving_lowertemp.setText(str(set_temp+5))
           
            if(run_or_not_save ==0):
               self.pushButton_save.setText("Run")                
            if(run_or_not_sleep ==0):
               self.pushButton_sleep.setText("Run") 
            if(run_or_not_precool==0):
               self.pushButton_cool.setText("Run") 
            if(run_or_not_preheat==0):
               self.pushButton_heat.setText("Run")
            
                
            
 # heat:
        if(cool_or_heat==2):
            self.pushButton_cool.setEnabled(False)
            self.pushButton_heat.setEnabled(True)
            self.pushButton_sleep.setEnabled(False)
            self.pushButton_save.setEnabled(True)
            if(run_or_not_save ==1):
                self.pushButton_cool.setEnabled(False)
                self.pushButton_heat.setEnabled(False)
                self.pushButton_sleep.setEnabled(False)
                self.pushButton_save.setEnabled(True)
                
                  
                self.label_mode_settemp.setText(" ")
                self.label_sleep_lowertemp.setText(" ")
                self.label_mode_pretemp.setText(" ")
                self.label_leaving_lowertemp.setText(str(set_temp-5)) 
                
                
            if(run_or_not_sleep ==1):
                self.pushButton_cool.setEnabled(False)
                self.pushButton_heat.setEnabled(False)
                self.pushButton_sleep.setEnabled(False)
                self.pushButton_save.setEnabled(False)
                
                  
                self.label_mode_settemp.setText(str(set_temp))
                self.label_sleep_lowertemp.setText(str(set_temp-3))
                self.label_mode_pretemp.setText(" ")
                self.label_leaving_lowertemp.setText(" ") 
            
            if(run_or_not_preheat ==1):
                self.pushButton_cool.setEnabled(False)
                self.pushButton_heat.setEnabled(True)
                self.pushButton_sleep.setEnabled(False)
                self.pushButton_save.setEnabled(False)
                
                self.label_mode_settemp.setText(" ")
                self.label_sleep_lowertemp.setText(" ")
                self.label_mode_pretemp.setText(str(set_temp+5))
                self.label_leaving_lowertemp.setText(" ") 
                               
            else:
                if(run_or_not_preheat ==0 and run_or_not_sleep ==0 and run_or_not_save ==0  ):
                    self.pushButton_cool.setEnabled(False)
                    self.pushButton_heat.setEnabled(True)
                    self.pushButton_sleep.setEnabled(False)
                    self.pushButton_save.setEnabled(True)
                    
                    self.label_mode_settemp.setText(str(set_temp))
                    self.label_sleep_lowertemp.setText(str(set_temp-3))
                    self.label_mode_pretemp.setText(str(set_temp+5))
                    self.label_leaving_lowertemp.setText(str(set_temp-5))               
            if(run_or_not_save ==0):
               self.pushButton_save.setText("Run")                 
            if(run_or_not_sleep ==0):
               self.pushButton_sleep.setText("Run") 
            if(run_or_not_precool==0):
               self.pushButton_cool.setText("Run") 
            if(run_or_not_preheat==0):
               self.pushButton_heat.setText("Run")
            if(mode_state == 'off'):
                self.pushButton_cool.setEnabled(False)
                self.pushButton_heat.setEnabled(False)
                self.pushButton_sleep.setEnabled(False)
                self.pushButton_save.setEnabled(False)
#******************#
#mode function
#******************#       
    def on_pushButton_back2_pressed(self):
         mode_to_main_page(self,mode_state)
         
    def changeValue1(self):
        global sleep_time
        pos = self.horizontalSlider_time1.value()
        if pos <= 50:
            sleep_time = 15
            self.label_slider_1.setText(str(sleep_time)+"min")
        elif pos <= 95  :
            sleep_time = 30
            self.label_slider_1.setText(str(sleep_time)+"min")            
        else:
            sleep_time = 60
            self.label_slider_1.setText(str(sleep_time)+"min")
        postdata('sleep_time',sleep_time)

    def changeValue2(self):
        global precool_time,preheat_time 
        pos = self.horizontalSlider_time2.value()
        if pos <= 50:
            precool_time = 30
            preheat_time = 30
            self.label_slider_2.setText("30min")
        elif pos <= 95:
            precool_time = 60
            preheat_time = 60
            self.label_slider_2.setText("60min")
        else:
            precool_time = 90
            preheat_time = 90
            self.label_slider_2.setText("90min")
        postdata('precool_time',precool_time)
        postdata('preheat_time',preheat_time)
        

    
    
    

                      
    def on_pushButton_sleep_pressed(self):
        global set_temp,stop_it,mode_name_number,Back1
        global run_or_not_save, run_or_not_sleep,run_or_not_precool,run_or_not_preheat
        mode_to_main_page(self,mode_state)
        if(stop_it==0):
            run_or_not_sleep = 1
            stop_it=1
            postdata('run_or_not_sleep',1)
            Back1 =Sleep_Mode()
            Back1.start()
        else:
           Widget.on_pushButton_right_pressed(self)
           

    def on_pushButton_cool_pressed(self):
        global set_temp , stop_it,mode_name_number,mode_state,Back2
        global run_or_not_save, run_or_not_sleep,run_or_not_precool,run_or_not_preheat
        mode_to_main_page(self,mode_state)
        if(stop_it==0):
            run_or_not_precool =1     
            stop_it=1
            postdata('run_or_not_precool',1)
            Back2=Pre_Cool_Mode()
            Back2.start()
        else:
            Widget.on_pushButton_right_pressed(self)
            
    def on_pushButton_heat_pressed(self):
        global set_temp,stop_it,mode_name_number,Back3
        global run_or_not_save, run_or_not_sleep,run_or_not_precool,run_or_not_preheat
        mode_to_main_page(self,mode_state)
        if(stop_it==0):
            run_or_not_preheat =1
            stop_it = 1
            postdata('run_or_not_preheat',1)
            Back3=Pre_Heat_Mode()
            Back3.start()
        else:
            Widget.on_pushButton_right_pressed(self)
            
    def on_pushButton_save_pressed(self):
        global set_temp,stop_it,mode_name_number,Back4
        global run_or_not_save, run_or_not_sleep,run_or_not_precool,run_or_not_preheat
        mode_to_main_page(self,mode_state)
        if(stop_it==0):
            run_or_not_save = 1
            stop_it=1
            mode_name_number=4
            postdata('run_or_not_save',1)
            Back4=Save_Mode()
            Back4.start()
        else:
            Widget.on_pushButton_right_pressed(self)
            #Back4.terminate()
    def sch1(self):
        global set_temp, tem_1,tem_2,tem_3,tem_4,tem_5, tem_6, today
        if(today==1):
            set_temp=tem_1[1]
        if(today==2):
            set_temp=tem_1[2]
        if(today==3):
            set_temp=tem_1[3]
        if(today==4):
            set_temp=tem_1[4]
        if(today==5):
            set_temp=tem_1[5]
        if(today==6):
            set_temp=tem_1[6]
        if(today==7):
            set_temp=tem_1[7]
        _thread.start_new_thread(postdata,('set_temp',set_temp))

    def sch2(self):
        global set_temp, tem_1,tem_2,tem_3,tem_4,tem_5, tem_6, today
        if(today==1):
            set_temp=tem_2[1]
        if(today==2):
            set_temp=tem_2[2]
        if(today==3):
            set_temp=tem_2[3]
        if(today==4):
            set_temp=tem_2[4]
        if(today==5):
            set_temp=tem_2[5]
        if(today==6):
            set_temp=tem_2[6]
        if(today==7):
            set_temp=tem_2[7]
        _thread.start_new_thread(postdata,('set_temp',set_temp))
            
    def sch3(self):
        global set_temp, tem_1,tem_2,tem_3,tem_4,tem_5, tem_6, today
        if(today==1):
            set_temp=tem_3[1]
        if(today==2):
            set_temp=tem_3[2]
        if(today==3):
            set_temp=tem_3[3]
        if(today==4):
            set_temp=tem_3[4]
        if(today==5):
            set_temp=tem_3[5]
        if(today==6):
            set_temp=tem_3[6]
        if(today==7):
            set_temp=tem_3[7]
        _thread.start_new_thread(postdata,('set_temp',set_temp))
            
    def sch4(self):
        global set_temp, tem_1,tem_2,tem_3,tem_4,tem_5, tem_6, today
        if(today==1):
            set_temp=tem_4[1]
        if(today==2):
            set_temp=tem_4[2]
        if(today==3):
            set_temp=tem_4[3]
        if(today==4):
            set_temp=tem_4[4]
        if(today==5):
            set_temp=tem_4[5]
        if(today==6):
            set_temp=tem_4[6]
        if(today==7):
            set_temp=tem_4[7]
        _thread.start_new_thread(postdata,('set_temp',set_temp))
            
    def sch5(self):
        global set_temp, tem_1,tem_2,tem_3,tem_4,tem_5, tem_6, today
        if(today==1):
            set_temp=tem_5[1]
        if(today==2):
            set_temp=tem_5[2]
        if(today==3):
            set_temp=tem_5[3]
        if(today==4):
            set_temp=tem_5[4]
        if(today==5):
            set_temp=tem_5[5]
        if(today==6):
            set_temp=tem_5[6]
        if(today==7):
            set_temp=tem_5[7]
        _thread.start_new_thread(postdata,('set_temp',set_temp))
            
    def sch6(self):
        global set_temp, tem_1,tem_2,tem_3,tem_4,tem_5, tem_6, today
        if(today==1):
            set_temp=tem_6[1]
        if(today==2):
            set_temp=tem_6[2]
        if(today==3):
            set_temp=tem_6[3]
        if(today==4):
            set_temp=tem_6[4]
        if(today==5):
            set_temp=tem_6[5]
        if(today==6):
            set_temp=tem_6[6]
        if(today==7):
            set_temp=tem_6[6]
        _thread.start_new_thread(postdata,('set_temp',set_temp))
            
###################
#outclass function#
###################   
def output_temp(self):
        global day_number,sch_number,tem_1,tem_2,tem_3,tem_4,tem_5, tem_6
        self.label_tem1.setText(str(tem_1[day_number]))
        self.label_tem2.setText(str(tem_2[day_number]))        
        self.label_tem3.setText(str(tem_3[day_number]))
        self.label_tem4.setText(str(tem_4[day_number]))        
        self.label_tem5.setText(str(tem_5[day_number]))
        self.label_tem6.setText(str(tem_6[day_number]))

def schedule_temp_back(self):
        self.label_tem1.setStyleSheet('color:red')
        self.label_tem2.setStyleSheet('color:black')
        self.label_tem3.setStyleSheet('color:black')
        self.label_tem4.setStyleSheet('color:black')
        self.label_tem5.setStyleSheet('color:black')
        self.label_tem6.setStyleSheet('color:black')

def save_sch_time(self):
        global sch_1,sch_2,sch_3,sch_4,sch_5,sch_6,sch_7
        sch_1=[]
        sch_1.append(self.comboBox_1_1.currentText())
        sch_1.append(self.comboBox_1_2.currentText())
        sch_1.append(self.comboBox_1_3.currentText())
        sch_1.append(self.comboBox_1_4.currentText())
        sch_1.append(self.comboBox_1_5.currentText())
        sch_1.append(self.comboBox_1_6.currentText())
        sch_1.append(self.comboBox_1_7.currentText())
        sch_1.append(self.comboBox_1_8.currentText())
        sch_1.append(self.comboBox_1_9.currentText())
        sch_1.append(self.comboBox_1_10.currentText())
        sch_1.append(self.comboBox_1_11.currentText())
        sch_1.append(self.comboBox_1_12.currentText())
    
        sch_2=[]
        sch_2.append(self.comboBox_2_1.currentText())
        sch_2.append(self.comboBox_2_2.currentText())
        sch_2.append(self.comboBox_2_3.currentText())
        sch_2.append(self.comboBox_2_4.currentText())
        sch_2.append(self.comboBox_2_5.currentText())
        sch_2.append(self.comboBox_2_6.currentText())
        sch_2.append(self.comboBox_2_7.currentText())
        sch_2.append(self.comboBox_2_8.currentText())
        sch_2.append(self.comboBox_2_9.currentText())
        sch_2.append(self.comboBox_2_10.currentText())
        sch_2.append(self.comboBox_2_11.currentText())
        sch_2.append(self.comboBox_2_12.currentText())
        
        sch_3=[]
        sch_3.append(self.comboBox_3_1.currentText())
        sch_3.append(self.comboBox_3_2.currentText())
        sch_3.append(self.comboBox_3_3.currentText())
        sch_3.append(self.comboBox_3_4.currentText())
        sch_3.append(self.comboBox_3_5.currentText())
        sch_3.append(self.comboBox_3_6.currentText())
        sch_3.append(self.comboBox_3_7.currentText())
        sch_3.append(self.comboBox_3_8.currentText())
        sch_3.append(self.comboBox_3_9.currentText())
        sch_3.append(self.comboBox_3_10.currentText())
        sch_3.append(self.comboBox_3_11.currentText())
        sch_3.append(self.comboBox_3_12.currentText())

        sch_4=[]
        sch_4.append(self.comboBox_4_1.currentText())
        sch_4.append(self.comboBox_4_2.currentText())
        sch_4.append(self.comboBox_4_3.currentText())
        sch_4.append(self.comboBox_4_4.currentText())
        sch_4.append(self.comboBox_4_5.currentText())
        sch_4.append(self.comboBox_4_6.currentText())
        sch_4.append(self.comboBox_4_7.currentText())
        sch_4.append(self.comboBox_4_8.currentText())
        sch_4.append(self.comboBox_4_9.currentText())
        sch_4.append(self.comboBox_4_10.currentText())
        sch_4.append(self.comboBox_4_11.currentText())
        sch_4.append(self.comboBox_4_12.currentText())        

        sch_5=[]
        sch_5.append(self.comboBox_5_1.currentText())
        sch_5.append(self.comboBox_5_2.currentText())
        sch_5.append(self.comboBox_5_3.currentText())
        sch_5.append(self.comboBox_5_4.currentText())
        sch_5.append(self.comboBox_5_5.currentText())
        sch_5.append(self.comboBox_5_6.currentText())
        sch_5.append(self.comboBox_5_7.currentText())
        sch_5.append(self.comboBox_5_8.currentText())
        sch_5.append(self.comboBox_5_9.currentText())
        sch_5.append(self.comboBox_5_10.currentText())
        sch_5.append(self.comboBox_5_11.currentText())
        sch_5.append(self.comboBox_5_12.currentText())

        sch_6=[]
        sch_6.append(self.comboBox_6_1.currentText())
        sch_6.append(self.comboBox_6_2.currentText())
        sch_6.append(self.comboBox_6_3.currentText())
        sch_6.append(self.comboBox_6_4.currentText())
        sch_6.append(self.comboBox_6_5.currentText())
        sch_6.append(self.comboBox_6_6.currentText())
        sch_6.append(self.comboBox_6_7.currentText())
        sch_6.append(self.comboBox_6_8.currentText())
        sch_6.append(self.comboBox_6_9.currentText())
        sch_6.append(self.comboBox_6_10.currentText())
        sch_6.append(self.comboBox_6_11.currentText())
        sch_6.append(self.comboBox_6_12.currentText())

        sch_7=[]
        sch_7.append(self.comboBox_7_1.currentText())
        sch_7.append(self.comboBox_7_2.currentText())
        sch_7.append(self.comboBox_7_3.currentText())
        sch_7.append(self.comboBox_7_4.currentText())
        sch_7.append(self.comboBox_7_5.currentText())
        sch_7.append(self.comboBox_7_6.currentText())
        sch_7.append(self.comboBox_7_7.currentText())
        sch_7.append(self.comboBox_7_8.currentText())
        sch_7.append(self.comboBox_7_9.currentText())
        sch_7.append(self.comboBox_7_10.currentText())
        sch_7.append(self.comboBox_7_11.currentText())
        sch_7.append(self.comboBox_7_12.currentText())

            
def create_schedule():        
    global sch_1,sch_2,sch_3,sch_4,sch_5,sch_6,sch_7
    w = Widget()
    try:
        schedule.every().monday.at(sch_1[0]).do(w.sch1)
        schedule.every().monday.at(sch_1[2]).do(w.sch2)
        schedule.every().monday.at(sch_1[4]).do(w.sch3)
        schedule.every().monday.at(sch_1[6]).do(w.sch4)
        schedule.every().monday.at(sch_1[8]).do(w.sch5)
        schedule.every().monday.at(sch_1[10]).do(w.sch6)

        schedule.every().tuesday.at(sch_2[0]).do(w.sch1)
        schedule.every().tuesday.at(sch_2[2]).do(w.sch2)
        schedule.every().tuesday.at(sch_2[4]).do(w.sch3)
        schedule.every().tuesday.at(sch_2[6]).do(w.sch4)
        schedule.every().tuesday.at(sch_2[8]).do(w.sch5)
        schedule.every().tuesday.at(sch_2[10]).do(w.sch6)

        schedule.every().wednesday.at(sch_3[0]).do(w.sch1)
        schedule.every().wednesday.at(sch_3[2]).do(w.sch2)
        schedule.every().wednesday.at(sch_3[4]).do(w.sch3)
        schedule.every().wednesday.at(sch_3[6]).do(w.sch4)
        schedule.every().wednesday.at(sch_3[8]).do(w.sch5)
        schedule.every().wednesday.at(sch_3[10]).do(w.sch6)

        schedule.every().thursday.at(sch_4[0]).do(w.sch1)
        schedule.every().thursday.at(sch_4[2]).do(w.sch2)
        schedule.every().thursday.at(sch_4[4]).do(w.sch3)
        schedule.every().thursday.at(sch_4[6]).do(w.sch4)
        schedule.every().thursday.at(sch_4[8]).do(w.sch5)
        schedule.every().thursday.at(sch_4[10]).do(w.sch6)

        schedule.every().friday.at(sch_5[0]).do(w.sch1)
        schedule.every().friday.at(sch_5[2]).do(w.sch2)
        schedule.every().friday.at(sch_5[4]).do(w.sch3)
        schedule.every().friday.at(sch_5[6]).do(w.sch4)
        schedule.every().friday.at(sch_5[8]).do(w.sch5)
        schedule.every().friday.at(sch_5[10]).do(w.sch6)
        
        schedule.every().saturday.at(sch_6[0]).do(w.sch1)
        schedule.every().saturday.at(sch_6[2]).do(w.sch2)
        schedule.every().saturday.at(sch_6[4]).do(w.sch3)
        schedule.every().saturday.at(sch_6[6]).do(w.sch4)
        schedule.every().saturday.at(sch_6[8]).do(w.sch5)
        schedule.every().saturday.at(sch_6[10]).do(w.sch6)

        schedule.every().sunday.at(sch_7[0]).do(w.sch1)
        schedule.every().sunday.at(sch_7[2]).do(w.sch2)
        schedule.every().sunday.at(sch_7[4]).do(w.sch3)
        schedule.every().sunday.at(sch_7[6]).do(w.sch4)
        schedule.every().sunday.at(sch_7[8]).do(w.sch5)
        schedule.every().sunday.at(sch_7[10]).do(w.sch6)
    except:
        pass
    
if __name__ == '__main__':
    import sys 
    _thread.start_new_thread(postdatabegin,())
    app = QtGui.QApplication(sys.argv)
    widget = Widget()
    widget.show()
    Back10=gettemp()    
    Back10.start()
    Back20=synchronize()
    Back20.start()
    Back = AC_Running()
    Back.update_cur_temp.connect(widget.curtempchange) 
    Back.start()
    #Back1 =Sleep_Mode()
    #Back2=Pre_Cool_Mode()
    #Back3=Pre_Heat_Mode()
    #Back4=Save_Mode()
    sys.exit(app.exec_())

   



