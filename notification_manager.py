from twilio.rest import Client
import smtplib
from add_user import AddUser

class NotificationManager:
    def __init__(self):
        self.ad = AddUser()
        self.auth_sid = "AC3cb72f33b7218d265dad7f8ec42a8e0c"
        self.auth_token="739caa3b6282b75ee4761a00eeb5a608"
        self.twilio_phone="+12058982424"
        self.my_phone = "+919971734360"
    def msg_me(self, code,country, date, price):
        client = Client(self.auth_sid, self.auth_token)

        message = client.messages.create(
            from_= self.twilio_phone,
            body=f"Low price alert ! Only €{price}  to fly from India-IND to"
                 f" {country}-{code}, on {date}.\n Thank You",
            to=self.my_phone
        )
    def send_email(self,code,country, date, price):
        email_list = self.ad.email_list()
        for email in email_list:
            message = f"Subject:Flight Deals Alert\n\nLow Price Alert ! Only €{price} to fly from India-IND {country}-{code}, on {date}.\n Thank You"
            connection = smtplib.SMTP("smtp.gmail.com")
            self.my_email = "aayushsethi007@gmail.com"
            self.password = "hqhl voxo rbyv aunw"
            connection.starttls()
            connection.login(user=self.my_email, password=self.password)
            connection.sendmail(from_addr=self.my_email, to_addrs=email, msg=message.encode('utf-8'))


        
