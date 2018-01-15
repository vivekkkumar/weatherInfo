import requests
import collections

class weatherinfo:
    '''This class is used to creater an instance from openweather map which predicts weather information
    on a hourly basis (in this example), to call the API the app ID and the ID of the city is needed
    which is provided in the init method.'''

    def __init__(self ,id ,appid):
        '''Here ID mentions city which can be retrieved from their webpage
        and appid is the token for this tool'''

        self.id = id
        self.appid = appid

        # Since this attribute is not updated ever no need of any other methods to change this attribute or access.
        # no need of getter or setter methods.

        self.__url = 'http://api.openweathermap.org/data/2.5/weather?id={}&appid={}'.format(self.id, self.appid)

    def create_request(self):
        '''Creates a get request for the url to get hourly information of Bangalore city'''

        self.req = requests.get(self._url)

    def check_status(self):
        '''Returns the http status code if success or failure'''

        return self.req.status_code

    def parse_message(self):
        '''This method is to retreive the information needed which is in this case
        if its going to rain'''
                                                            # 3 for Loops not a good implementation, flatten_dict a better method.
        if self.check_status() == 200:                      # If we flatten the dict no need of too many comparisons
            for key in self.req.json():                     # static method is not used in this case
                if key == "weather":
                    for list_item in (self.req.json()[key]):       # Just this value is a list from response, that's how the API is.
                        for key, value in list_item.items():
                            if key == "description":
                                if value == "moderate rain" or value == "heavy rain":
                                    return True
                                else:
                                    return False

        else:
            raise Exception("Status code not 200")          # sending a message that request did not happen

    @staticmethod                                           # static method neither alters instance or class
    def flatten_dict(dictionary, parent_key='', sep='_'):   # restricted to just the data, doesnt take cls or self
        items = []                                          # just to namespace this method. This method is to flatten the dict
        for key, value in dictionary.items():               # for easy retrieval of information
            new_key = parent_key + sep + key if parent_key else key
            if isinstance(value, collections.MutableMapping):
                items.extend(weatherinfo.flatten_dict(value, new_key, sep=sep).items())
            else:
                items.append((new_key, value))                          # example l = [(1,4),(2,3),(4,5)]
                                                                        # dict(l) => {1: 4, 2: 3, 4: 5}
        return dict(items)