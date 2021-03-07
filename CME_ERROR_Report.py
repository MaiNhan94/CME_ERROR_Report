import AWSIoTPythonSDK.MQTTLib as AWSIoTPyMQTT
import json
import datetime
import os

def customCallback(client, userdata, message):
        topic = message.topic
        payload = message.payload.decode("utf-8")
        payload_json = json.loads(payload)
        if(payload_json["eventType"] == "connected"):
            print(str(datetime.datetime.utcnow()) + " - connected")
            File_Connect = open("Connected.log", "a")
            File_Connect.write(str(datetime.datetime.utcnow()))
            File_Connect.write(" - ")
            File_Connect.writelines(payload)
            File_Connect.close()
        if(payload_json["eventType"] == "disconnected"):
            print(str(datetime.datetime.utcnow()) + " - disconnected")
            File_DisConnect = open("Disconnected.log", "a")
            File_DisConnect.write(str(datetime.datetime.utcnow()))
            File_DisConnect.write(" - ")
            File_DisConnect.writelines(payload)
            File_DisConnect.close()

ENDPOINT = "a1q3rplqhm9yv-ats.iot.ap-northeast-1.amazonaws.com"
            
CLIENT_ID = "CME_ERROR_Report_Python_ID"
#PATH_TO_CERT = "C:\\Users\\NhanIMIC\\Desktop\\IoT_iMIC\\31fc29c16a-certificate.pem.crt"
#PATH_TO_KEY = "C:\\Users\\NhanIMIC\\Desktop\\IoT_iMIC\\31fc29c16a-private.pem.key"
#PATH_TO_CA = "C:\\Users\\NhanIMIC\\Desktop\\IoT_iMIC\\AmazonRootCA1.pem"

PATH_TO_CERT = str(os.getcwd()) + "\\certificate\\986a9699b8-certificate.pem.crt"
PATH_TO_KEY = str(os.getcwd()) + "\\certificate\\986a9699b8-private.pem.key"
PATH_TO_CA = str(os.getcwd()) + "\\certificate\\AmazonRootCA1.pem"

DisConnect_Topic = "$aws/events/presence/disconnected/+"
Connect_Topic = "$aws/events/presence/connected/+"

myAWSIoTMQTTClient = AWSIoTPyMQTT.AWSIoTMQTTClient(CLIENT_ID)
myAWSIoTMQTTClient.configureEndpoint(ENDPOINT, 8883)
myAWSIoTMQTTClient.configureCredentials(PATH_TO_CA, PATH_TO_KEY, PATH_TO_CERT)

myAWSIoTMQTTClient.connect()
myAWSIoTMQTTClient.subscribe(DisConnect_Topic, 0,customCallback)
myAWSIoTMQTTClient.subscribe(Connect_Topic, 0,customCallback)

while(1):
    if(input() == "Q"):
        break
