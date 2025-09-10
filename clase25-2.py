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
        
class Bike(Vehicle):
    def stert_engine(self):
        if not self.is_available:
            return(f"La bicileta {self.brand} {self.model} esta en marcha.")
        else:
            return(f"La bicileta  {self.brand} {self.model} no esta disponible para parar.")
    def stop_engine(self):
        if not self.is_available:
            return(f"La bicileta  {self.brand} {self.model} ha parado.")
        else:
            return(f"La bicileta  {self.brand} {self.model} no esta disponible para parar.")
        
class Truck(Vehicle):
    def stert_engine(self):
        if not self.is_available:
            return(f"El camion {self.brand} {self.model} ha sido encendido.")
        else:
            return(f"El camion {self.brand} {self.model} no esta disponible para encender el motor.")
    def stop_engine(self):
        if not self.is_available:
            return(f"El camion {self.brand} {self.model} ha sido apagado.")
        else:
            return(f"El camion {self.brand} {self.model} no esta disponible para apagar el motor.")
        
class Customer:
    def __init__(self, name):
        self.name = name
        self.purchased_vehicles = []
        
    def buy_vehicle(self, vehicle: Vehicle):
        if vehicle.check_availability():
            vehicle.sell()
            self.purchased_vehicles.append(vehicle)
        else:
            print(f"Lo siento, {vehicle.brand} {vehicle.model} no esta disponible.")
            
    def inquire_vehicle(self, vehicle: Vehicle):
        if vehicle.check_availability():
            availability = "Disponible"
        else:
            availability = "No disponible"
        print(f"El vehiculo {vehicle.brand} {vehicle.model} esta {availability} y cuesta {vehicle.get_price()}.")

class Dealership:
    def __init__(self):
        self.inventory = []
        self.customers = []
        
    def add_vehicle(self, vehicle: Vehicle):
        self.inventory.append(vehicle)
        print(f"El vehiculo {vehicle.brand} {vehicle.model} ha sido anadido al inventario.")
        
    def register_customer(self, customer: Customer):
        self.customers.append(customer)
        print(f"El cliente {customer.name} ha sido registrado en la concesionaria.")
        
    def show_available_vehicles(self):
        print("Vehiculos disponibles en la concesionaria:")
        for vehicle in self.inventory:
            if vehicle.check_availability():
                print(f"- {vehicle.brand} {vehicle.model} por {vehicle.get_price()}")