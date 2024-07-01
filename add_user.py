import requests
class AddUser:
    def __init__(self):
        self.list = []

    def user_info(self):
        print("Welcome to Flight Club")
        print("We find the best flight deals and email you.")
        end = False

        first_name = input("What is your first name ")
        last_name = input("What is your last name ")
        email = input("what is your email ")
        email_again = input("Type your email again ")

        if email != email_again:
            print("Emails do not match")
        else:
            print("You are in the club")

            api_endpoint = "https://api.sheety.co/ccbf039ec2020e00808f58654d46be1d/flightDetails/sheet2"
            params = {
                "sheet2": {
                    "firstName": first_name,
                    "lastName": last_name,
                    "email": email
                }
            }
            response = requests.post(url=api_endpoint, json=params)

    def email_list(self):
        api_end = "https://api.sheety.co/ccbf039ec2020e00808f58654d46be1d/flightDetails/sheet2"
        response = requests.get(url=api_end)
        data = response.json()
        for item in data["sheet2"]:
            email = item["email"]
            self.list.append(email)
        return self.list