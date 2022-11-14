from abc import ABC, abstractmethod
class ControleRemoto(ABC):
    @abstractmethod
    def ligar(self):
        pass
    @abstractmethod
    def desligar(self):
        pass

class ControleTV(ControleRemoto):
    def ligar(self):
        return "liga tv"

    def desligar(self):
        return "desliga"

a= ControleTV()

print(a.desligar(), a.ligar())


