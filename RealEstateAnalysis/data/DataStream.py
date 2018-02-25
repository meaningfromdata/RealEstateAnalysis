import requests
import random
from RealEstateAnalysis.data.DataModel import DataSource

class DataStream(DataSource):

    @property
    def description(self):
        return "Data Stream"
    
    def __iter__(self):
        return iter(self.__data)

    def __init__(self, url):
        self.__url = url
        self.__data = []
        self.__len = 0
        self.params = {}
    
    def __len__(self):
        return self.__len
    
    @property 
    def url(self):
        return self.__url
    
    @property
    def params(self):
        return self.__params

    @params.setter
    def params(self, newParams):
        self.__params = newParams

    def load(self):
        a = requests.get(self.url, self.params)
        self.__data = a.json()
        self.__len = len(a.json())
    
    def where(self, **kwargs):
        for key in kwargs:
            self.params[key] = kwargs[key]
        return self

    def sample(self, n):
        L = self.__data
        if n < len(self):
            self.__len = self.__len - n
            return [
                L.pop(random.randrange(len(L)))
                for _ in range(n)
            ]
            
        else:
            output = [item for item in self.__iter__()]
            self.__data = []
            self.__len = 0
            return output

