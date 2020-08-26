import requests
import json

url = "https://api.rootnet.in/covid19-in/stats/latest"
r = requests.get(url)
r_text = r.text


def load_data(data1):
    convert = json.loads(data1)
    total_cases = convert["data"]["summary"]["total"]
    ap_cases = convert["data"]["regional"][1]["confirmedCasesIndian"]
    ap_deaths = convert["data"]["regional"][1]["deaths"]
    print("The total cases in India: {}".format(total_cases))
    print()
    for i in range(35):
        loc = convert["data"]["regional"][i]["loc"]
        cases = convert["data"]["regional"][i]["confirmedCasesIndian"]
        deaths = convert["data"]["regional"][i]["deaths"]
        print("The total confirmed cases in {} : {}".format(loc, cases))
        print("The total confirmed deaths in {} : {}".format(loc, deaths))
        print("")
    return None


def main():
    load_data(r_text)


if __name__ == "__main__":
    main()
