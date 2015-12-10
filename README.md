# Cisco Spark Webhooks Sample App

**Description**: Scripts for creating a Spark webhook to get notified of new messages in a Spark room, filter the messages, trigger a request to get data from APIC-EM's controller, and then post the data in a Spark room.

- **Technology stack**: Python 3.4
- **Status**:  First release v1.1 [CHANGELOG](CHANGELOG.md).
- **Live Demo**: This sample code accompanies the 'Spark - Webhooks Intermdiate' learning lab at https://learninglabs.cisco.com

Our sample app uses the following Python files which you can download on Github:
  * getrooms.py
  * postwebhook.py
  * webhookapp.py
  * getmessage.py
  * gethosts.py
  * postmessage.py

> These files are for your reference. You won't be able to run the app unless you host the app on a publicly reachable IP address or domain. For this reason we are hosting the app in the Cisco Sandbox at 10.10.10.10.

If you are running Mac or Linux, place the files in the following folder structure:
* /bin
  * getrooms.py
  * postwebhook.py
  * webhookapp.py
* /lib/pythonX.X/site-packages/
  * getmessage.py
  * gethosts.py
  * postmessage.py

If you are running Windows, place the files in the following folder structure:
  * /Scripts
    * getrooms.py
    * postwebhook.py
    * webhookapp.py
  * /Lib/site-packages
    * getmessage.py
    * gethosts.py
    * postmessage.py

![Webhook diagram](spark-apicem.jpg "Webhook diagram")
