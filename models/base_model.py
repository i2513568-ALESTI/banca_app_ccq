from abc import ABC, abstractmethod

class BaseCredito(ABC):
    def _init_(self, monto, plazo, tasa):
        self.monto = monto
        self.plazo = plazo
        self.tasa = tasa
    
    @abstractmethod
    def calcular_cuota(self):
        pass