import requests
import json
import time

print("<----------Welcome to Ali Weather Page---------->")
time.sleep(1.0)
city = str(input("Enter the city name: "))

url = "http://api.weatherstack.com/current?access_key=db6b3c5b4a7ff6a94b907a54a72ce2a7&query={}".format(city)



# for i in "LOADING...":
#     print(i, end=" ")
#     time.sleep(0.2)
# print("")


r = requests.get(url)
r_text = r.text


# print(r.text)

def load_info(text_data):
    convert = json.loads(text_data)
    query = convert["request"]["query"]
    city_name = convert["location"]["name"]
    country_name = convert["location"]["country"]
    time_zone = convert["location"]["localtime"]
    temperature = convert["current"]["temperature"]
    wind_speed = convert["current"]["wind_speed"]
    w_suggestion = convert["current"]["weather_descriptions"][0]
    print("The requested query is {}".format(query))

    # for i in "RETRIEVING":
    #     print(i, end=" ")
    #     time.sleep(0.2)
    print("")

    print("City        : {}".format(city_name))
    print("Country Name: {}".format(country_name))
    print("Current Time: {}".format(time_zone))
    print()
    print("******Weather condition in {}, {} ******".format(city_name, country_name))
    print()
    print("Temperature        : {}".format(temperature))
    print("Wind Speed         : {}".format(wind_speed))
    print("Weather Description: {}".format(w_suggestion))


if __name__ == "__main__":
    try:
        load_info(r_text)
    except:
        print("The given city: {} is not in API list currently, Please try again later".format(city))
