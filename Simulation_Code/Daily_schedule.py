from thermostat import *
sch_1=[]
sch_2=[]
sch_3=[]
sch_4=[]
sch_5=[]
sch_6=[]
sch_7=[]

def day_change(self,day_number):
    if(day_number==1):
        self.pushButton_1.setStyleSheet('color:red')
        self.pushButton_2.setStyleSheet('color:black')
        self.pushButton_3.setStyleSheet('color:black')
        self.pushButton_4.setStyleSheet('color:black')
        self.pushButton_5.setStyleSheet('color:black')
        self.pushButton_6.setStyleSheet('color:black')
        self.pushButton_7.setStyleSheet('color:black')
    elif(day_number==2):
        self.pushButton_1.setStyleSheet('color:black')
        self.pushButton_2.setStyleSheet('color:red')
        self.pushButton_3.setStyleSheet('color:black')
        self.pushButton_4.setStyleSheet('color:black')
        self.pushButton_5.setStyleSheet('color:black')
        self.pushButton_6.setStyleSheet('color:black')
        self.pushButton_7.setStyleSheet('color:black')
        
    elif(day_number==3):
        self.pushButton_1.setStyleSheet('color:black')
        self.pushButton_2.setStyleSheet('color:black')
        self.pushButton_3.setStyleSheet('color:red')
        self.pushButton_4.setStyleSheet('color:black')
        self.pushButton_5.setStyleSheet('color:black')
        self.pushButton_6.setStyleSheet('color:black')
        self.pushButton_7.setStyleSheet('color:black')
    elif(day_number==4):
        self.pushButton_1.setStyleSheet('color:black')
        self.pushButton_2.setStyleSheet('color:black')
        self.pushButton_3.setStyleSheet('color:black')
        self.pushButton_4.setStyleSheet('color:red')
        self.pushButton_5.setStyleSheet('color:black')
        self.pushButton_6.setStyleSheet('color:black')
        self.pushButton_7.setStyleSheet('color:black')
    elif(day_number==5):
        self.pushButton_1.setStyleSheet('color:black')
        self.pushButton_2.setStyleSheet('color:black')
        self.pushButton_3.setStyleSheet('color:black')
        self.pushButton_4.setStyleSheet('color:black')
        self.pushButton_5.setStyleSheet('color:red')
        self.pushButton_6.setStyleSheet('color:black')
        self.pushButton_7.setStyleSheet('color:black')
    elif(day_number==6):
        self.pushButton_1.setStyleSheet('color:black')
        self.pushButton_2.setStyleSheet('color:black')
        self.pushButton_3.setStyleSheet('color:black')
        self.pushButton_4.setStyleSheet('color:black')
        self.pushButton_5.setStyleSheet('color:black')
        self.pushButton_6.setStyleSheet('color:red')
        self.pushButton_7.setStyleSheet('color:black')
    else:
        self.pushButton_1.setStyleSheet('color:black')
        self.pushButton_2.setStyleSheet('color:black')
        self.pushButton_3.setStyleSheet('color:black')
        self.pushButton_4.setStyleSheet('color:black')
        self.pushButton_5.setStyleSheet('color:black')
        self.pushButton_6.setStyleSheet('color:black')
        self.pushButton_7.setStyleSheet('color:red')
def schedule_temp_position_change_right(self,day_number,tem_number, sch_number, tem_set_number):
    tem_number+=1;
    if(tem_number==1):
            tem_set_number=1
            self.label_tem1.setStyleSheet('color:red')
            self.label_tem2.setStyleSheet('color:black')
            self.label_tem3.setStyleSheet('color:black')
            self.label_tem4.setStyleSheet('color:black')
            self.label_tem5.setStyleSheet('color:black')
            self.label_tem6.setStyleSheet('color:black')
    if(tem_number==2):
            tem_set_number=2
            self.label_tem1.setStyleSheet('color:black')
            self.label_tem2.setStyleSheet('color:red')
            self.label_tem3.setStyleSheet('color:black')
            self.label_tem4.setStyleSheet('color:black')
            self.label_tem5.setStyleSheet('color:black')
            self.label_tem6.setStyleSheet('color:black')
    if(tem_number==3):
            tem_set_number=3
            self.label_tem1.setStyleSheet('color:black')
            self.label_tem2.setStyleSheet('color:black')
            self.label_tem3.setStyleSheet('color:red')
            self.label_tem4.setStyleSheet('color:black')
            self.label_tem5.setStyleSheet('color:black')
            self.label_tem6.setStyleSheet('color:black')
    if(tem_number==4):
            tem_set_number=4
            self.label_tem1.setStyleSheet('color:black')
            self.label_tem2.setStyleSheet('color:black')
            self.label_tem3.setStyleSheet('color:black')
            self.label_tem4.setStyleSheet('color:red')
            self.label_tem5.setStyleSheet('color:black')
            self.label_tem6.setStyleSheet('color:black')
            if(sch_number==4):
                tem_set_number=4
                tem_number=0;
    if(tem_number==5):
            tem_set_number=5
            self.label_tem1.setStyleSheet('color:black')
            self.label_tem2.setStyleSheet('color:black')
            self.label_tem3.setStyleSheet('color:black')
            self.label_tem4.setStyleSheet('color:black')
            self.label_tem5.setStyleSheet('color:red')
            self.label_tem6.setStyleSheet('color:black')
            if(sch_number==5):
                tem_set_number=5
                tem_number=0
    if(tem_number==6):
            tem_set_number=6
            self.label_tem1.setStyleSheet('color:black')
            self.label_tem2.setStyleSheet('color:black')
            self.label_tem3.setStyleSheet('color:black')
            self.label_tem4.setStyleSheet('color:black')
            self.label_tem5.setStyleSheet('color:black')
            self.label_tem6.setStyleSheet('color:red')
    if(tem_number==7):
            tem_set_number=1
            tem_number=1;
            self.label_tem1.setStyleSheet('color:red')
            self.label_tem2.setStyleSheet('color:black')
            self.label_tem3.setStyleSheet('color:black')
            self.label_tem4.setStyleSheet('color:black')
            self.label_tem5.setStyleSheet('color:black')
            self.label_tem6.setStyleSheet('color:black')
    #print(tem_number)
    return  tem_number, sch_number, tem_set_number
def schedule_temp_position_change_left(self,day_number,tem_number, sch_number, tem_set_number):
        tem_number-=1;
        if(tem_number<0):
            self.label_tem1.setStyleSheet('color:black')
            self.label_tem2.setStyleSheet('color:black')
            self.label_tem3.setStyleSheet('color:black')
            self.label_tem4.setStyleSheet('color:black')
            self.label_tem5.setStyleSheet('color:black')
            self.label_tem6.setStyleSheet('color:black')
            if(sch_number==4):
                tem_set_number=3
                tem_number=3;
                self.label_tem3.setStyleSheet('color:red')
            if(sch_number==5):
                tem_set_number=4
                tem_number=4;
                self.label_tem4.setStyleSheet('color:red')
        if(tem_number==1):
            self.label_tem1.setStyleSheet('color:red')
            self.label_tem2.setStyleSheet('color:black')
            self.label_tem3.setStyleSheet('color:black')
            self.label_tem4.setStyleSheet('color:black')
            self.label_tem5.setStyleSheet('color:black')
            self.label_tem6.setStyleSheet('color:black')
            tem_set_number=1
        if(tem_number==2):
            tem_set_number=2
            self.label_tem1.setStyleSheet('color:black')
            self.label_tem2.setStyleSheet('color:red')
            self.label_tem3.setStyleSheet('color:black')
            self.label_tem4.setStyleSheet('color:black')
            self.label_tem5.setStyleSheet('color:black')
            self.label_tem6.setStyleSheet('color:black')
        if(tem_number==3):
            tem_set_number=3
            self.label_tem1.setStyleSheet('color:black')
            self.label_tem2.setStyleSheet('color:black')
            self.label_tem3.setStyleSheet('color:red')
            self.label_tem4.setStyleSheet('color:black')
            self.label_tem5.setStyleSheet('color:black')
            self.label_tem6.setStyleSheet('color:black')
        if(tem_number==4):
            tem_set_number=4
            self.label_tem1.setStyleSheet('color:black')
            self.label_tem2.setStyleSheet('color:black')
            self.label_tem3.setStyleSheet('color:black')
            self.label_tem4.setStyleSheet('color:red')
            self.label_tem5.setStyleSheet('color:black')
            self.label_tem6.setStyleSheet('color:black')
            if(sch_number==4):
                tem_number=0;         
        if(tem_number==5):
            tem_set_number=5
            self.label_tem1.setStyleSheet('color:black')
            self.label_tem2.setStyleSheet('color:black')
            self.label_tem3.setStyleSheet('color:black')
            self.label_tem4.setStyleSheet('color:black')
            self.label_tem5.setStyleSheet('color:red')
            self.label_tem6.setStyleSheet('color:black')
        if(tem_number==6):
            tem_set_number=6
            self.label_tem1.setStyleSheet('color:black')
            self.label_tem2.setStyleSheet('color:black')
            self.label_tem3.setStyleSheet('color:black')
            self.label_tem4.setStyleSheet('color:black')
            self.label_tem5.setStyleSheet('color:black')
            self.label_tem6.setStyleSheet('color:red')
        if(tem_number==0):
            tem_set_number=6
            tem_number=6;
            self.label_tem1.setStyleSheet('color:black')
            self.label_tem2.setStyleSheet('color:black')
            self.label_tem3.setStyleSheet('color:black')
            self.label_tem4.setStyleSheet('color:black')
            self.label_tem5.setStyleSheet('color:black')
            self.label_tem6.setStyleSheet('color:red')
            if(sch_number==4):
                tem_set_number=4
                tem_number=0;
                self.label_tem4.setStyleSheet('color:red')
            if(sch_number==5):
                tem_set_number=5
                tem_number=0;
                self.label_tem5.setStyleSheet('color:red')
        
        #print(tem_number)
        return  tem_number, sch_number, tem_set_number

