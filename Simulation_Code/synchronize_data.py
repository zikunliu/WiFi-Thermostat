from firebase import firebase
import re
import time
try:
    firebase = firebase.FirebaseApplication('https://wifi-thermostat.firebaseio.com/')
except:
    pass
listnum=[]
base='00001'
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
    try:
        firebase.delete('/'+base+'/'+name,None)
        firebase.post('/'+base+'/'+name,data)
    except:
        pass

def getcloud():
    result = firebase.get('/'+base+'/cloud',None)
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
  try:
    firebase.delete('/'+base+'/cloud',None)
    firebase.post('/'+base+'/cloud',0)
    firebase.delete('/'+base+'/'+base+'/mode_cloud',None)
    firebase.post('/'+base+'/mode_cloud',1)
    firebase.delete('/'+base+'/mode_state_cloud',None)
    firebase.post('/'+base+'/mode_state_cloud',0)
    firebase.delete('/'+base+'/fan_cloud',None)
    firebase.post('/'+base+'/fan_cloud',0)
    firebase.delete('/'+base+'/precool_time',None)
    firebase.post('/'+base+'/precool_time',30)
    firebase.delete('/'+base+'/preheat_time',None)
    firebase.post('/'+base+'/preheat_time',30)
    firebase.delete('/'+base+'/run_or_not_precool',None)
    firebase.post('/'+base+'/run_or_not_precool',0)
    firebase.delete('/'+base+'/run_or_not_preheat',None)
    firebase.post('/'+base+'/run_or_not_preheat',0)
    firebase.delete('/'+base+'/run_or_not_save',None)
    firebase.post('/'+base+'/run_or_not_save',0)
    firebase.delete('/'+base+'/run_or_not_sleep',None)
    firebase.post('/'+base+'/run_or_not_sleep',0)
    firebase.delete('/'+base+'/sch_cloud',None)
    firebase.post('/'+base+'/sch_cloud',1)
    firebase.delete('/'+base+'/set_temp',None)
    firebase.post('/'+base+'/set_temp',80)
    firebase.delete('/'+base+'/sleep_time',None)
    firebase.post('/'+base+'/sleep_time',30)
    firebase.delete('/'+base+'/stop_it',None)
    firebase.post('/'+base+'/stop_it',0)
  except:
      pass

def mergedata(data):
  try:
    if(isinstance(data,int)):
        return data
    else:
        sets=str(data)
        strlist = sets.split(':') 
        a=re.findall(r'\d',strlist[1])
        b=''
        b=b.join(a)
        c=int(b)
        return c
  except:
        pass
