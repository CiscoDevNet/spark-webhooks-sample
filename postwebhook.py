# import the requests and json library so we can use it to make REST calls
import requests, json


# the main function
def main():
    # define a variable for the hostname of Spark
    hostname = "api.ciscospark.com"

    # login to developer.ciscospark.com and copy your access token here
    # Never hard-code access token in production environment
    token = "Bearer [access token]"

    # add authorization to the header
    header = {"Authorization": "%s" % token, "content-type": "application/json"}

    # disable warnings about using certificate verification
    requests.packages.urllib3.disable_warnings()

    # create request url
    post_message_url = "https://" + hostname + "/v1/webhooks"

    # create request body
    payload = {
        "resource": "messages",
        "event": "created",
        "filter": "roomId=[room_id]",
        "targetUrl": "http://10.10.10.10/webhook",
        "name": "[webhook_name]"
    }

    # send the POST request resource and do not verify SSL certificate for simplicity of this example
    api_response = requests.post(post_message_url, json=payload, headers=header, verify=False)

    # get the response status code
    response_status = api_response.status_code

    # print the status code
    print(response_status)


# run the function
main()
