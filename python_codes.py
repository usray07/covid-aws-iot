#The Python code on Adi’s system –

import paho.mqtt.client as pmc import ssl
import random import time import boto3
rootca=r"C:\Users\Anshuman\Desktop\AWS Keys\AmazonRootCA1.pem.txt"	#r indicates that the compiler must use the raw string cert=r"C:\Users\Anshuman\Desktop\AWS Keys\fcce3c98d4-certificate.pem.crt" pkey=r"C:\Users\Anshuman\Desktop\AWS Keys\fcce3c98d4-private.pem.key" c=pmc.Client()
c.tls_set(rootca, certfile=cert, keyfile=pkey, cert_reqs=ssl.CERT_REQUIRED, tls_version=ssl.PROTOCOL_TLSv1_2, ciphers=None) c.connect('a1dufe2albfsbg-ats.iot.us-east-2.amazonaws.com', 8883)

client = boto3.client( "sns",
aws_access_key_id="AKIAX75ZIIZZK6HDECQK", aws_secret_access_key="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",
 
region_name='us-east-2'
)
def onc(c, userdata,flag,rc): print("CONNECTED", rc) c.subscribe("project/temp/Sheet1")
def onm(c, userdata, msg): mg=msg.payload.decode() print(mg)
mg=int(mg) if mg > 100:
print("Inside Adi's if block")
response = client.publish(TopicArn='arn:aws:sns:us-east- 2:549607458418:Adi_Temp_Data',Message='Adi has fever')
print("mail") elif mg <= 100:
print("no mail")
c.on_connect=onc	#These coommands help us declare shortforms for the functions c.on_message=onm
c.loop_forever()	#This commands keeps the program in an infinite loop


The Python code on Mohit’s system –

import paho.mqtt.client as pmc import ssl
import random import time import boto3
rootca=r"C:\Users\Anshuman\Desktop\AWS Keys\AmazonRootCA1.pem.txt"	#r indicates that the compiler must use the raw string cert=r"C:\Users\Anshuman\Desktop\AWS Keys\fcce3c98d4-certificate.pem.crt" pkey=r"C:\Users\Anshuman\Desktop\AWS Keys\fcce3c98d4-private.pem.key" c=pmc.Client()
c.tls_set(rootca, certfile=cert, keyfile=pkey, cert_reqs=ssl.CERT_REQUIRED, tls_version=ssl.PROTOCOL_TLSv1_2, ciphers=None) c.connect('a1dufe2albfsbg-ats.iot.us-east-2.amazonaws.com', 8883)

client = boto3.client( "sns",
aws_access_key_id="AKIAX75ZIIZZK6HDECQK", aws_secret_access_key="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", region_name='us-east-2'
)
def onc(c, userdata,flag,rc): print("CONNECTED", rc)
 
c.subscribe("project/temp/Mohit") def onm(c, userdata, msg):
mg=msg.payload.decode() print(mg)
mg=int(mg) if mg > 100:
print("Inside Mohit's if block")
response = client.publish(TopicArn='arn:aws:sns:us-east- 2:549607458418:Mohit_Temp_Data',Message='Mohit has fever')
print("mail") elif mg <= 100:
print("no mail")
c.on_connect=onc	#These coommands help us declare shortforms for the functions c.on_message=onm
c.loop_forever()	#This commands keeps the program in an infinite loop


#The Python code on Rahul’s system –

import paho.mqtt.client as pmc import ssl
import random import time import boto3
rootca=r"C:\Users\Anshuman\Desktop\AWS Keys\AmazonRootCA1.pem.txt"	#r indicates that the compiler must use the raw string cert=r"C:\Users\Anshuman\Desktop\AWS Keys\fcce3c98d4-certificate.pem.crt" pkey=r"C:\Users\Anshuman\Desktop\AWS Keys\fcce3c98d4-private.pem.key" c=pmc.Client()
c.tls_set(rootca, certfile=cert, keyfile=pkey, cert_reqs=ssl.CERT_REQUIRED, tls_version=ssl.PROTOCOL_TLSv1_2, ciphers=None) c.connect('a1dufe2albfsbg-ats.iot.us-east-2.amazonaws.com', 8883)

client = boto3.client( "sns",
aws_access_key_id="AKIAX75ZIIZZK6HDECQK", aws_secret_access_key="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", region_name='us-east-2'
)
def onc(c, userdata,flag,rc): print("CONNECTED", rc) c.subscribe("project/temp/Rahul")
def onm(c, userdata, msg): mg=msg.payload.decode() print(mg)
 
mg=int(mg) if mg > 100:
print("Inside Rahul's if block")
response = client.publish(TopicArn='arn:aws:sns:us-east- 2:549607458418:Rahul_Temp_Data',Message='Rahul has fever')
print("mail") elif mg <= 100:
print("no mail")
c.on_connect=onc	#These coommands help us declare shortforms for the functions c.on_message=onm
c.loop_forever()	#This commands keeps the program in an infinite loop


#The Python code on Sumit’s system –

import paho.mqtt.client as pmc import ssl
import random import time import boto3
rootca=r"C:\Users\Anshuman\Desktop\AWS Keys\AmazonRootCA1.pem.txt"	#r indicates that the compiler must use the raw string cert=r"C:\Users\Anshuman\Desktop\AWS Keys\fcce3c98d4-certificate.pem.crt" pkey=r"C:\Users\Anshuman\Desktop\AWS Keys\fcce3c98d4-private.pem.key" c=pmc.Client()
c.tls_set(rootca, certfile=cert, keyfile=pkey, cert_reqs=ssl.CERT_REQUIRED, tls_version=ssl.PROTOCOL_TLSv1_2, ciphers=None) c.connect('a1dufe2albfsbg-ats.iot.us-east-2.amazonaws.com', 8883)

client = boto3.client( "sns",
aws_access_key_id="AKIAX75ZIIZZK6HDECQK", aws_secret_access_key="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", region_name='us-east-2'
)
def onc(c, userdata,flag,rc): print("CONNECTED", rc) c.subscribe("project/temp/Sumit")
def onm(c, userdata, msg): mg=msg.payload.decode() print(mg)
mg=int(mg) if mg > 100:
print("Inside Sumit's if block")
 
response = client.publish(TopicArn='arn:aws:sns:us-east- 2:549607458418:Sumit_Temp_Data',Message='Sumit has fever')
print("mail") elif mg <= 100:
print("no mail")
c.on_connect=onc	#These coommands help us declare shortforms for the functions c.on_message=onm
c.loop_forever()	#This commands keeps the program in an infinite loop
