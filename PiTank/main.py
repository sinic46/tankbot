from requests import get



def light_the_beacon():

    response = get("https://robotapi.sinic.co.uk")

    print(f"beacons are lit. {response.text}")



if __name__ == "__main__":
    light_the_beacon()