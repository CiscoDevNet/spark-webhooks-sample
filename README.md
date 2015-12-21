# Cisco Spark Webhooks Sample App

**Description**: Scripts for creating a Spark webhook to get notified of new messages in a Spark room, filter the messages, trigger a request to get data from APIC-EM's controller, and then post the data in a Spark room.

- **Technology stack**: Python 3.4 and Flask 0.10.1
- **Status**:  First release v1.1 [CHANGELOG](CHANGELOG.md).
- **Tutorial**: This sample code accompanies the 'Spark - Webhooks Intermediate' learning lab at https://learninglabs.cisco.com

![Webhook diagram](spark-apicem.jpg "Webhook diagram")


## Installation

You will need to install [Python 3.4](https://www.python.org/downloads/), the [Requests](http://docs.python-requests.org/en/latest/user/install/) library, and [Flask](http://flask.pocoo.org/) to run the application.

This sample app consists of the following Python files:
  * **webhookapp.py** - *the main app*
  * **getrooms.py** - *get the Spark room id*
  * **postwebhook.py** - *create a Spark webhook*
  * **getmessage.py** - *get the text of the new message*
  * **gethosts.py** - *get hosts from APIC-EM*
  * **postmessage.py** - *post message to Spark room*

> These files are for your reference. You won't be able to run the app unless you host the app on a publicly reachable IP address or domain.

## Usage

* Retrieve your Spark API Access Token.  This token is your developer token, and can be used to access **Spark** APIs during exploration and development:
  * Open a browser tab, navigate to the [developer.ciscospark.com](https://developer.ciscospark.com/?utm_source=Llab4&utm_medium=readme&utm_campaign=spark), and **Login**
  * Click on your profile image
  * Click **Copy** to copy your access token to the clipboard
<div align="center">![Access Token](token.jpg)</div>

## Getting help

Cisco DevNet support is available here: https://developer.cisco.com/site/devnet/support/

## Getting involved

Suggestions and enhancements welcome, see [CONTRIBUTING](CONTRIBUTING.md).


----

## Open source licensing info
[LICENSE](LICENSE)
