# covid-aws-iot
Using IOT MQTT Broker and Nodered to publish data on AWS IOT Core with an Automatic Email System using AWS SNS to notify friends with Location and health details of friend using Android App if their friend’s body temperature is abnormal.
Approach:
The project essentially consists of four parts-

1.	Designing a node-red flow to plot the graph from the provided database
The initial JSON file contained four folders each consisting of the temperature data of the four friends respectively. However, there was a trouble accessing the file in Node-red. So we copied and concatenated all of the them into one single file separated by commas. We have attached the drive link of the concatenated JSON file.

https://drive.google.com/file/d/1jJUR99Bu-_t29sf8R0glwk0BaezEvTDi/view

In the flow we insert the file using the file in node and then separate the four different objects using split node. Furthermore, we split individual temperature data at specific hours using another split node and feed it to the chart nodes which then plots the chart on the node-red dashboard.

1.a.	NODE RED FLOW

 

1.c.	Dashboard




 
 







2.	Uploading the data to AWS IoT Core through AWS MQTT broker


In a separate flow we split the data in similar way to access individual temperature data which was then uploaded in different topics using AWS MQTT broker.
 
2.a.	NODE RED FLOW

We have added four function nodes (by the names Adi, Mohit, Rahul and Sumit) which will filter out the data of the one of the friends from the JSON file which contains all their temperature values. Again we used four more function nodes (by the names Adi Mqtt, Mohit Mqtt, Rahul Mqtt and Sumit Mqtt) to set different topics for each of their datas to be uploaded on to the AWS MQTT Broker.

We have also inserted four delay nodes. These nodes prevent whole of the data to be uploaded at a time on to the MQTT Broker. The delay nodes put a time gap of four hours between two consecutive temperature.


3.	Sending alert mails when one of the four friends has a fever


The task in this section was to send an alert mail to the other three friends whenever anyone of them had a high temperature. So we created four topics on Amazon SNS which were named after the four friends respectively. Each topic has to be subscribed by the other three friends.
 
3.a.	AWS SNS Screenshots







 
 


So as to automate the mail system we wrote four python programs, which were to run in the background on each of the four friends’ devices. The program subscribes to the MQTT topic of the user of the device. The program then compares the fetched temperature value of the user to the threshold(100ºF). In case the fetched value exceeded the threshold an alert mail was sent to the subscribers of the user’s SNS topic.








4.	Designing an app using MIT App Inventor to continuously save the user’s data in a local database

4.a.	LocSen (Location Sensor)
We created a simple android application using MIT App inventor that sends out the longitude and latitude of the user to a database. The chosen database here is a simple Google sheet file. The UI of the app is fairly simple consisting of a Current Geographical Co-ordinate display along with address and a list view that shows all the previously visited locations serially. The user can even choose to hide or show the list view according to his/her will.
 
1.	The Layout : LocSen consists only a single screen that displays all the relevant data. The home screen contains a text label displaying the current latitude , current longitude and relevant address . Below the address label, there are two buttons. One to Show the location list and another to Hide the location list. Finally the screen ends with a Listview. The screen also contains some hidden components such as a Location Sensor, two Web nodes. One web node is used to write the data into the database and another is used to read the data from the database and feed it into the Listview.
2.	The Code Blocks : On the coding side of the application, we have used various block to make sure the app functions as per the question demanded. The explanation of each block used are as follows :-
A)	when Screen1.Initialize - We configured this block to direct the app to fetch data from the	database the moment the app was turned on. We achieved this by joining a set Web.Url to block. This block was linked to the Google sheet database that fetched the data. The previous block was executed using a call Web.Get block.
B)	when LocationSensor1.LocationChanged - The application of this block is pretty obvious from the name itself. This block tells application to perform certain tasks when the location sensor senses a different location using the user’s phone’s GPS. We programmed it to feed the location, latitude and address data to their respective text labels. Also, this node performed the most important task of the entire application, it sends the location data to the database. It does so by utilization of the Web_2_For_Sending_Data node. Without this node, the application looses its	meaning.
C)	When Web_1_For_Reading.GotText - This block is linked to the first web node, I.e, Web_1_For_Reading. By using this block we derived the data from the URL, I.e, the data from the Google sheet, and programmed it to feed the data into the Listview of the application. We also	configured the node to remove the first column of the spread sheet that contains the field values.
D)	when Web_2_For_Sending_Data.GotText - When the data is entered into the database, simultaneously the second URL is also executed to read the data and feed it into the List View. This is the only for using the when Web_2_For_Sending_Data.GotText node. It enables this function and lets us see the location in the list view and upload it to the database at the same time.
 
E)	Global Variables - We have also used two Global variable nodes. The LocationList variable stores the	incoming data from the Google sheet in it making it easier to perform actions on the data.The second variable Empty is used to store an empty list that will be used to hide the	existing Location List.
F)	Buttons - Finally we have used two button nodes to program the Show List
and Hide List functions.


