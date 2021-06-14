from pywebio.input import *
from pywebio.output import *
from flask import Flask,send_from_directory
import pickle
import pandas as pd
import numpy as np
from pywebio.platform.flask import webio_view
import argparse
from pywebio import STATIC_PATH,start_server
app=Flask(__name__)
model=pickle.load(open('model6.pkl','rb'))
def predict():
    put_markdown('Rainfall Prediction')
    location=select("Choose the location",['Canberra','Sydney','Perth','Darwin','Hobart','Brisbane','Adelaide','Bendigo',             
                    'Townsville','AliceSprings','MountGambier','Ballarat','Launceston','Albany','Albury','MelbourneAirport',    
                    'PerthAirport','Mildura','SydneyAirport','Nuriootpa','Sale','Watsonia','Tuggeranong','Portland','Woomera',             
                    'Cairns','Cobar','Wollongong','GoldCoast','WaggaWagga','NorfolkIsland','Penrith','Newcastle','SalmonGums',         
                    'CoffsHarbour','Witchcliffe','Richmond','Dartmoor','NorahHead','BadgerysCreek','MountGinini','Moree',               
                    'Walpole','PearceRAAF','Williamtown','Melbourne','Nhil','Katherine','Uluru'])
    if location=='Canberra':
        loc=9
    elif location=='Sydney':
        loc=37
    elif location=='Perth':
        loc=31
    elif location=='Darwin':
        loc=13
    elif location=='Hobart':
        loc=15
    elif location=='Brisbane':
        loc=7
    elif location=='Adelaide':
        loc=0
    elif location=='Bendigo':
        loc=6
    elif location=='Townsville':
        loc=39
    elif location=='AliceSprings':
        loc=3
    elif location=='MountGambier':
        loc=22
    elif location=='Ballarat':
        loc=5
    elif location=='Launceston':
        loc=17
    elif location=='Albany':
        loc=1
    elif location=='Albury':
        loc=2
    elif location=='MelbourneAirport':
        loc=19
    elif location=='PerthAirport':
        loc=32
    elif location=='Mildura':
        loc=20
    elif location=='SydneyAirport':
        loc=38
    elif location=='Nuriootpa':
        loc=28
    elif location=='Sale':
        loc=35
    elif location=='Watsonia':
        loc=44
    elif location=='Tuggeranong':
        loc=40
    elif location=='Portland':
        loc=33
    elif location=='Woomera':
        loc=48
    elif location=='Cairns':
        loc=8
    elif location=='Cobars':
        loc=10
    elif location=='Wollongong':
        loc=47
    elif location=='GoldCoast':
        loc=14
    elif location=='WaggaWagga':
        loc=42
    elif location=='NorfolkIsland':
        loc=27
    elif location=='Penrith':
        loc=30
    elif location=='Newcastle':
        loc=24
    elif location=='SalmomGums':
        loc=36
    elif location=='CoffsHarbour':
        loc=11
    elif location=='Witchcliffe':
        loc=46
    elif location=='Richmond':
        loc=34
    elif location=='Dartmoor':
        loc=12
    elif location=='NorahHead':
        loc=26
    elif location=='BadgerysCreek':
        loc=4
    elif location=='MountGinini':
        loc=23
    elif location=='Moree':
        loc=21
    elif location=='Walpole':
        loc=43
    elif location=='PearceRAAF':
        loc=29
    elif location=='Williamtown':
        loc=45
    elif location=='Melbourne':
        loc=18
    elif location=='Nhil':
        loc=25
    elif location=='Katherine':
        loc=16
    elif location=='Uluru':
        loc=41
    else:
        loc=-1
        
    min_temp=input("Enter the minimum temperature",type=FLOAT)
    max_temp=input("Enter the maximum temperature",type=FLOAT)
    rainfall=input("Enter rainfall in cm",type=FLOAT)
    evaporation =input("Enter evaporation in your area")
    sunshine=input("Enter sunshine in your area",type=FLOAT)
    direc=radio("Choose the direction of the wind",['W','SE','E','N','SSE','S','WSW','SW','SSW','WNW','NW','ENE','ESE','NE'
                                                    ,'NNW','NNE'])
    if direc=='W':
        d=13
    elif direc=='SE':
        d=9
    elif direc=='E':
        d=0
    elif direc=='N':
        d=3
    elif direc=='SSE':
        d=10
    elif direc=='S':
        d=8
    elif direc=='WSW':
        d=15
    elif direc=='SW':
        d=12
    elif direc=='SSW':
        d=11
    elif direc=='WNW':
        d=14
    elif direc=='NW':
        d=7
    elif direc=='ENE':
        d=1
    elif direc=='ESE':
        d=2
    elif direc=='NE':
        d=4
    elif direc=='NNW':
        d=6
    elif direc=='NNE':
        d=5
    else:
        d=-1
        
    speed=input("Enter the wind speed",type=FLOAT)
    direc_9=radio("Enter the direction at 9 am",['N','SE','E','SSE','NW','S','W','SW','NNE','NNW','ENE','ESE','NE','SSW','WNW','WSW'])
    if direc_9=='N':
        d_9=3
    elif direc_9=='SE':
        d_9=9
    elif direc_9=='E':
        d_9=0
    elif direc_9=='SSE':
        d_9=10
    elif direc_9=='NW':
        d_9=7
    elif direc_9=='S':
        d_9=8
    elif direc_9=='W':
        d_9=13
    elif direc_9=='SW':
        d_9=12
    elif direc_9=='NNE':
        d_9=5
    elif direc_9=='NNW':
        d_9=6
    elif direc_9=='ENE':
        d_9=1
    elif direc_9=='ESE':
        d_9=2
    elif direc_9=='NE':
        d_9=4
    elif direc_9=='SSW':
        d_9=11
    elif direc_9=='WNW':
        d_9=14
    elif direc_9=='WSW':
        d_9=15
    else:
        d_9=-1
        
    direc_3=radio("Enter the direction at 3 pm",['SE','W','S','WSW','SW','SSE','N','WNW','NW','ESE','E','NE','SSW','NNW','ESE','NNE'])
    if direc_3=='SE':
        d_3=9
    elif direc_3=='W':
        d_3=13
    elif direc_3=='S':
        d_3=8
    elif direc_3=='WSW':
        d_3=5
    elif direc_3=='SW':
        d_3=12
    elif direc_3=='SSE':
        d_3=10
    elif direc_3=='N':
        d_3=3
    elif direc_3=='WNW':
        d_3=4
    elif direc_3=='NW':
        d_3=7
    elif direc_3=='ESE':
        d_3=2
    elif direc_3=='E':
        d_3=0
    elif direc_3=='NE':
        d_3=4
    elif direc_3=='SSW':
        d_3=11
    elif direc_3=='NNW':
        d_3=6
    elif direc_3=='ESE':
        d_3=1
    elif direc_3=='NNE':
        d_3=5
    else:
        d_3=-1
    
    speed_9=input("Enter the speed at 9 am",type=FLOAT)
    speed_3=input("Enter the speed at 3 pm",type=FLOAT)
    hum_9=input("Enter humidity at 9 am",type=FLOAT)
    hum_3=input("Enter humidity at 3 pm",type=FLOAT)
    pre_9=input("Enter pressure at 9 am",type=FLOAT)
    pre_3=input("Enter pressure at 3 pm",type=FLOAT)
    cl_9=input("Enter cloud at 9 am",type=FLOAT)
    cl_3=input("Enter cloud at 3 pm",type=FLOAT)
    temp_9=input("Enter temperature at 9 am in Celsius",type=FLOAT)
    temp_3=input("Enter temperature at 3 pm in Celsius",type=FLOAT)
    today=radio("Choose whether it rained today or not",["Yes","No"])
    if today=="Yes":
        to=1
    else:
        to=0
    risk=input("Enter the risk mm",type=FLOAT)
    datee=input("Enter the date for which you want to predict the date",type=DATE)
    date=int(pd.to_datetime(datee).day)
    month=int(pd.to_datetime(datee).month)
    output=model.predict([[loc,min_temp,max_temp,rainfall,evaporation,sunshine,d,speed,d_9,d_3,speed_9,speed_3,hum_9,hum_3,pre_9,
                           pre_3,cl_9,cl_3,temp_9,temp_3,to,risk,date,month]])
    prediction=int(output)
    if prediction =="1":
        put_text("It will rain in your location")
    else:
        put_text("It won't rain in your location")
app.add_url_rule('/tool', 'webio_view',webio_view(predict),methods=['GET','POST','OPTIONS'])

if __name__=='__main__':
    arg=argparse.ArgumentParser()
    arg.add_argument("-p","--port",default=8080)
    args=arg.parse_args()
    start_server(predict,port=args.port)
    #predict()