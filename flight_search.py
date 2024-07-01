import requests
from datetime import datetime
from datetime import timedelta
from data_manager import DataManager
from notification_manager import NotificationManager
class FlightSearch:
    def __init__(self):
        self.nt = NotificationManager()
        self.dt = DataManager()
        self.api_key ="e--INj_0vZ7c_Ct5lmdXXZXGxjVvak0k"
        self.flight_endpoint = "https://api.tequila.kiwi.com"
        self.headers = {
            "apikey":
                self.api_key
        }
    def iata_codes(self,country):
        self.iata = {
            "term": country
        }
        response = requests.get(url=f"{self.flight_endpoint}/locations/query", params=self.iata, headers=self.headers)
        data = response.json()["locations"][0]["code"]

        return data
    def search_flight(self,code):
        today = datetime.now()
        tomm = today + timedelta(days=1)
        mod_tomm = tomm.strftime("%d/%m/%Y")
        date = int(tomm.strftime("%d"))
        month = int(tomm.strftime("%m"))
        year = int(tomm.strftime("%Y"))
        month = month + 6
        if (month > 12):
            month -= 12
            year += 1
        date_6 = datetime(day=date, month=month, year=year)

        mod_6_mon = date_6.strftime("%d/%m/%Y")

        self.param = {
            "date_from":mod_tomm,
            "date_to":mod_6_mon,
            "fly_from":"IND",
            "fly_to":code
        }
        self.response = requests.get(url=f"{self.flight_endpoint}/v2/search",params=self.param,headers=self.headers)
        self.data = self.response.json()["data"]

        for item in self.data:
            code = item["cityCodeTo"]
            country = item["cityTo"]
            price = item["price"]
            target = self.dt.check(code,price)
            if(target):
                departure_date =item["route"][0]["utc_departure"]
                departure_date=departure_date.split('T')[0]
                print("found one")
                # self.nt.msg_me(code,country,departure_date,price)
                self.nt.send_email(code,country,departure_date,price)
                break














