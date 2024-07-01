from data_manager import DataManager
from flight_search import FlightSearch
from add_user import AddUser


dt = DataManager()
fl = FlightSearch()
code_list = dt.codes()
ad = AddUser()


ad.user_info()
# dt.get_country()
for item in code_list:
    fl.search_flight(item)



