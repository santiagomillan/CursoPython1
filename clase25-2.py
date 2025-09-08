class Vehicle:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
        self.is_available = True
        
    def sell(self):
        if self.is_available:
            self.is_available = False
            print(f"El vehiculo {self.brand} {self.model} ha sido vendido.")
        else:
            print(f"El vehiculo {self.brand} {self.model} no esta disponible.")

    def check_availability(self):
        return self.is_available
    
    def get_price(self):
        return self.price
    
    def stert_engine(self):
        raise NotImplementedError("Este metodo debe ser implementado por la sub clase.")

    def stop_engine(self):
        raise NotImplementedError("Este metodo debe ser implementado por la sub clase.")

class Car(Vehicle):
    def stert_engine(self):
        if not self.is_available:
            return(f"El motor del coche {self.brand} {self.model} ha sido encendido.")
        else:
            return(f"El coche {self.brand} {self.model} no esta disponible para encender el motor.")
    def stop_engine(self):
        if not self.is_available:
            return(f"El motor del coche {self.brand} {self.model} ha sido apagado.")
        else:
            return(f"El coche {self.brand} {self.model} no esta disponible para apagar el motor.")