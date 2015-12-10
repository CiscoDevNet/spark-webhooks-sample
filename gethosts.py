# import the requests library so we can use it to make REST calls
import requests, json

# disable warnings about using certificate verification
requests.packages.urllib3.disable_warnings()

# get APIC-EM ticket before making APIC-EM requests
def getServiceTicket():
    # specify the username and password which will be included in the data
    payload = {"username":"admin","password":"1vtG@lw@y"}

    # This is the URL to get the service ticket.
    # The base IP call is https://[Controller IP]/api/v1
    url = "https://sandboxapic.cisco.com:9443/api/v1/ticket"

    # Content type must be included in the header
    header = {"content-type": "application/json"}

    # Format the payload to JSON and add to the data.  Include the header in the call.
    # SSL certification is turned off, but should be active in production environments
    response= requests.post(url,data=json.dumps(payload), headers=header, verify=False)

    # Check if a response was received. If not, print an error message.
    if(not response):
        print ("No data returned!")
    else:
        # Data received.  Get the ticket and print to screen.
        r_json=response.json()
        ticket = r_json["response"]["serviceTicket"]
        print ("ticket: ", ticket)
    return ticket

# the main function
def main():

    # get a new authenictation ticket from APIC-EM
    ticket = getServiceTicket()

    # If ticket received, get the hosts
    if ticket:
        # add authorization to the header
        header = {"X-Auth-Token": "%s" % ticket}

        # create request URL using the always-on APIC-EM GA Sandbox
        get_hosts_url = "https://sandboxapic.cisco.com:9443/api/v1/host"

        # create GET request and do not verify SSL certificate for simplicity of this example
        api_response = requests.get(get_hosts_url, headers=header, verify=False)

        # parse the response in json
        response_json = api_response.json()

        # create variable
        string = ""

        # loop through response and list the MAC and IP address of each host
        for host in response_json["response"]:
            string += "[hostMac: " + host["hostMac"] + ", hostIp: " + host["hostIp"] + "] "

        # return list of hosts
        print(string)
        return string

    else:
        print("No service ticket was received.  Ending program!")