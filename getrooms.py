# import the requests library so we can use it to make REST calls
import requests


# the main function
def main():
    # login to developer.ciscospark.com and copy your access token here
    # Never hard-code access token in production environment
    token = "Bearer [access token]"

    # add authorization to the header
    header = {"Authorization": "%s" % token}

    # disable warnings about using certificate verification
    requests.packages.urllib3.disable_warnings()

    # create request url
    get_rooms_url = "https://api.ciscospark.com/v1/rooms"

    # send GET request and do not verify SSL certificate for simplicity of this example
    api_response = requests.get(get_rooms_url, headers=header, verify=True)

    # parse the response in json
    response_json = api_response.json()

    # print the response
    print(response_json)


# run main function
main()
