import abc

class DataSource(abc.ABC):
    @abc.abstractmethod
    def __iter__(self):
        while False:
            yield None

    @property    
    @abc.abstractmethod
    def description(self):
        return None
    
    @abc.abstractmethod
    def sample(self, n):
        while False:
            yield None

    @abc.abstractmethod
    def where (self, **kwargs):
        return self