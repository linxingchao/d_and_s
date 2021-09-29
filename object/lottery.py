from abc import ABC, abstractmethod

class Lottery(ABC):
    
    @abstractmethod
    def search_data_from_net(): 
        pass

    @abstractmethod
    def search_data_from_csv(): 
        pass
