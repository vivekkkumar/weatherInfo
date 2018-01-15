import lib.messenger as messenger
import lib.weatherInfo as weatherapp
import credentials
import datetime
import time

# This tool is useful for me to send messages on hourly information of the local weather for a specific purpose of mine.


# Initializing the instances

message = messenger.messenger(credentials.my_number, credentials.to_number, credentials.account_sid, credentials.auth_token)
app = weatherapp.weatherinfo(credentials.id_weather_app, credentials.appid_weather_app)

# Create a request every one hour and send messages appropriately.

while datetime.datetime.now().hour < 23:                        # Run till night 11 PM
    app.create_request()
    time.sleep(6)
    if app.check_status() == 200:
        if app.parse_message():                                 # If True the rain is in forecast.
            message.send_message(credentials.message_true)
        else:
            message.send_message(credentials.message_false)
    else:
        print("Weather server not reachable")
    time.sleep(6000)                                            # Checking every one hour


