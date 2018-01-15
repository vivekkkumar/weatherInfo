from twilio.rest import Client

# Find these values at https://twilio.com/user/account

class messenger:
    '''Importing the twilio Library here for sending messages
    needs sending number, recieving number, acount ID and its auth token which can be taken
    from their webpage on registration'''

    def __init__(self, your_number, to_number, account_sid, auth_token):
        '''Creating a client to send messages'''

        self.your_number = your_number
        self.to_number = to_number
        self.client = Client(account_sid, auth_token)


    def send_message(self, message):
        '''This method actually sends messages, these api are well defined in their webpage'''
        if message != None:

            self.client.api.account.messages.create(
            to=self.to_number,                          # your phone number or other number
            from_=self.your_number,                     # Your sample number
            body=message)                               # Message about weather
        else:
            raise Exception('Message Body is empty, check the api calls result')

