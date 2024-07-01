import requests
# from flight_search import FlightSearch
class DataManager:
    def __init__(self):
        # self.fl = FlightSearch()
        self.end_point = "https://api.sheety.co/ccbf039ec2020e00808f58654d46be1d/flightDetails/sheet1"
        self.country_list = []
        self.response = requests.get(url=self.end_point)
        self.data = self.response.json()
        # print(self.data)
    def get_country(self):

        for i in range(0,10):
            country = self.data["sheet1"][i]["city"]
            self.country_list.append(country)
        self.iata()

    def iata(self):
        i=2

        while(i<=11):
            api = f"{self.end_point}/{i}"
            country = self.country_list[i-2]
            code = self.fl.iata_codes(country)
            param = {
                "sheet1":{
                    "iataCode":code
                }
            }
            response = requests.put(url=api,json=param)
            i+=1

    def codes(self):
        self.code_list = []
        for item in self.data["sheet1"]:
            code = item["iataCode"]
            self.code_list.append(code)
        return self.code_list


    def check(self,code,price):
        list = self.data["sheet1"]
        for items in list:
            if(items["iataCode"]==code):
                if(items["lowestPrice"] > price):
                    return True
                else:
                    return False







