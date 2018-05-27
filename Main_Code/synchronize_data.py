from firebase import firebase
import re
import time
firebase = firebase.FirebaseApplication('https://wifi-thermostat.firebaseio.com/')
listnum=[]
def getdata():
    listnum=[]
    listnum.append(firebase.get('/cur_temp',None))
    listnum.append(firebase.get('/fan_cloud',None))
    listnum.append(firebase.get('/mode_cloud',None))
    listnum.append(firebase.get('/mode_state_cloud',None))
    listnum.append(firebase.get('/precool_time',None))
    listnum.append(firebase.get('/preheat_time',None))
    listnum.append(firebase.get('/run_or_not_precool',None))
    listnum.append(firebase.get('/run_or_not_preheat',None))
    listnum.append(firebase.get('/run_or_not_save',None))
    listnum.append(firebase.get('/run_or_not_sleep',None))
    listnum.append(firebase.get('/sch_cloud',None))
    listnum.append(firebase.get('/set_temp',None))
    listnum.append(firebase.get('/sleep_time',None))
    listnum.append(firebase.get('/stop_it',None))
    for x in range (0,14):
        if(isinstance(listnum[x],int)):
            listnum[x]=listnum[x]
        else:
            sets=str(listnum[x])
            strlist = sets.split(':')
            #print(strlist[1])
            a=re.findall(r'\d',strlist[1])
            b=''
            b=b.join(a)
            listnum[x]=int(b)
    #print(listnum)
    return listnum[1],listnum[2],listnum[3],listnum[4],listnum[5],listnum[6],listnum[7],listnum[8],listnum[9],listnum[10],listnum[11],listnum[12],listnum[13]
            
def postdata(name,data):
    #time.sleep(1)
    firebase.delete('/'+name,None)
    firebase.post('/'+name,data)

def getcloud():
    result = firebase.get('/cloud',None)
    if(isinstance(result,int)):
        return result
    else:
        sets=str(result)
        strlist = sets.split(':') 
        a=re.findall(r'\d',strlist[1])
        b=''
        b=b.join(a)
        c=int(b)
        return c
#getdata()

def postdatabegin():
    firebase.delete('/fan_cloud',None)
    firebase.post('/fan_cloud',0)
    firebase.delete('/mode_cloud',None)
    firebase.post('/mode_cloud',1)
    firebase.delete('/mode_state_cloud',None)
    firebase.post('/mode_state_cloud',0)
    firebase.delete('/fan_cloud',None)
    firebase.post('/fan_cloud',0)
    firebase.delete('/precool_time',None)
    firebase.post('/precool_time',30)
    firebase.delete('/preheat_time',None)
    firebase.post('/preheat_time',30)
    firebase.delete('/run_or_not_precool',None)
    firebase.post('/run_or_not_precool',0)
    firebase.delete('/run_or_not_preheat',None)
    firebase.post('/run_or_not_preheat',0)
    firebase.delete('/run_or_not_save',None)
    firebase.post('/run_or_not_save',0)
    firebase.delete('/run_or_not_sleep',None)
    firebase.post('/run_or_not_sleep',0)
    firebase.delete('/sch_cloud',None)
    firebase.post('/sch_cloud',1)
    firebase.delete('/set_temp',None)
    firebase.post('/set_temp',80)
    firebase.delete('/sleep_time',None)
    firebase.post('/sleep_time',30)
    firebase.delete('/stop_it',None)
    firebase.post('/stop_it',0)
