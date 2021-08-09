import socket
import threading
import random
import string
import pandas as pd
import numpy as np
df1 = pd.DataFrame(pd.read_csv("Booking1.csv"))
df2=pd.DataFrame(pd.read_csv("Booking.csv"))
food=pd.DataFrame(pd.read_csv("Test.csv"))
#df1-->booking.csv
#df2-->billing.csv
#df3-->inventory.csv
print("This is a SERVER program")
print("--------------------------------")



s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 5001               # Reserve a port for your service.
print('Server started!')
print('Waiting for clients...\n')

s.bind((host, port))        # Bind to the port
s.listen(5)



def Booking(clientsocket,df_df):
    data=[]

    n=len(df_df)-1
    last_column_id = df_df.iloc[n, 0]
    last_column_rn = df_df.iloc[n, 13]
    j=int(last_column_id)
    cid=j+1
    print(last_column_rn)

    ro=int(last_column_rn)
    roomn=ro+1
    print(cid)
    data.append(cid)
    j1 = "Inside bookingfn"
    clientsocket.send(j1.encode())
    msg="HOTEL TGR WELCOMES YOU!!!\n\nENTER NAME: "
    clientsocket.send(msg.encode())
    name=msg = clientsocket.recv(1024).decode()
    data.append(name)
    msg="ENTER PHONE NUMBER: "
    clientsocket.send(msg.encode())
    ph= clientsocket.recv(1024).decode()
    data.append(ph)
    msg = "ENTER DOOR NUMBER: "
    clientsocket.send(msg.encode())
    dnum = clientsocket.recv(1024).decode()
    data.append(dnum)
    msg = "ENTER address line 1: "
    clientsocket.send(msg.encode())
    ad1 = clientsocket.recv(1024).decode()
    data.append(ad1)

    msg = "ENTER address line 2: "
    clientsocket.send(msg.encode())
    ad2 = clientsocket.recv(1024).decode()
    data.append(ad2)

    msg = "ENTER City: "
    clientsocket.send(msg.encode())
    city = clientsocket.recv(1024).decode()
    data.append(city)

    msg = "ENTER Checkin date: "
    clientsocket.send(msg.encode())
    cin = clientsocket.recv(1024).decode()
    data.append(cin)

    msg = "ENTER Checkout date: "
    clientsocket.send(msg.encode())
    cout = clientsocket.recv(1024).decode()
    data.append(cout)
    data=room(clientsocket,data)
    data.append(roomn)
    print(data)
    l1 = len(df_df)
    df_df.loc[l1] = data
    #j2 = df_df.to_string()
    #clientsocket.send(j1.encode())
    j3="---------------------------BOOKING CONFIRMED!!!---------------------\nCUSTOMER ID:"+str(data[0])+"\nNAME         :"+name+"\nPHONE        :"+ph+"\nCHECKIN DATE :"+cin+ "\nCHECKOUT DATE:"+cout+ "\nROOM TYPE    :"+str(data[9])+"\nNO OF DAYS   :"+str(data[11])+"\nCOST PER DAY :"+ str(data[10])+"\n----------------------------\n        TOTAL:"+str(data[12])+"\n----------------------------\n ROOM NO.:"+str(data[13])+"\n---------------------THANK YOU---------------------"
    #print(j3)
    clientsocket.send(j3.encode())
    df_df.to_csv('Booking1.csv', index=False)


def room(clientsocket,data):
    msg = "ENTER Room type:\n1. Standard Non-AC ---> Rs.500/day\n2. Standard AC --->Rs.1000/day\n3. 3-Bed Non-AC --->Rs.1500\n4. 3-Bed AC --->Rs.2000/day "
    clientsocket.send(msg.encode())
    rt= clientsocket.recv(1024).decode()
    a=int(rt)
    msg = "ENTER number of days : "
    clientsocket.send(msg.encode())
    temp = clientsocket.recv(1024).decode()
    n = int(temp)
    if a==1:
        k1='Standard Non-AC'
        k2=500*n
        data.append(k1)
        data.append('500')
        data.append(n)
        data.append(k2)
    elif a==2:
        k1 = 'Standard AC'
        k2= 1000*n
        data.append(k1)
        data.append('1000')
        data.append(n)
        data.append(k2)
    elif a==3:
        k1='3-Bed Non-AC'
        k2=1500*n
        data.append(k1)
        data.append('1500')
        data.append(n)
        data.append(k2)
    elif a==4:
        k1 = '3-Bed AC'
        data.append(k1)
        k2=2000*n
        data.append('2000')
        data.append(n)
        data.append(k2)
    return data

def Billing(clientsocket,df_df,m_df):
    total=0
    count=1
    temp=""
    bill=[]
    x="inside billing function!"
    print(x)
    j=df_df.to_string()
    msg = "HOTEL TGR WELCOMES YOU!!!\n\n----------------MENU CARD-----------------\n "+j+"\nPRESS e FOR EXIT\nEnter Option:"
    clientsocket.send(msg.encode())
    msg1= clientsocket.recv(1024).decode()
    print("before while")
    while msg1!="e":
        print("inside while")
        print(bill)
        for i in range(len(df_df)):
            print("inside for")
            print(df_df.iloc[i , 0])
            print(df_df.iloc[i , 0] == msg1)
            if str(df_df.iloc[i , 0]) == msg1:
                print("inside if")
                clientsocket.send("Qty:".encode())
                ip=clientsocket.recv(1024).decode()
                qty=int(ip)
                cost=(qty*int(df_df.iloc[i,2]))
                total+=cost
                lin=str(count)+" "+str(df_df.iloc[i,1])+" "+str(df_df.iloc[i,2])+" "+ip+" "+str(cost)
                print(lin)
                bill.append(lin)
                count+=1
        clientsocket.send("PRESS e FOR EXIT\nEnter next option:".encode())
        msg1 = clientsocket.recv(1024).decode()
    print(bill)

    print(total)






def on_new_client(clientsocket,addr,host):
    msg = clientsocket.recv(1024).decode()
    print(msg," connected")
    if "1" in msg:
        Booking(clientsocket,df1)
    elif "2" in msg:
        Billing(clientsocket,food,df2)
    else:
        a = "Trouble in server! Please try again later!"
        clientsocket.send(a.encode())

    clientsocket.close()


c, addr = s.accept()  # Establish connection with client.
t = threading.Thread(target=on_new_client, args=(c, addr, host))  # df[0:5] #########
t.start()
t.join()
