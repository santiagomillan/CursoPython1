class Vehicle:
    def __init__(self, brand, model, price):
        #Encapsulamiento
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

    #Abstraccion
    def check_availability(self):
        return self.is_available
    
    #Abstraccion
    def get_price(self):
        return self.price
    
    def stert_engine(self):
        raise NotImplementedError("Este metodo debe ser implementado por la sub clase.")

    def stop_engine(self):
        raise NotImplementedError("Este metodo debe ser implementado por la sub clase.")

#Herencia
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
        
#Herencia
class Bike(Vehicle):
    #Polimorfismo 
    def stert_engine(self):
        if not self.is_available:
            return(f"La bicileta {self.brand} {self.model} esta en marcha.")
        else:
            return(f"La bicileta  {self.brand} {self.model} no esta disponible para parar.")
    #Polimorfismo 
    def stop_engine(self):
        if not self.is_available:
            return(f"La bicileta  {self.brand} {self.model} ha parado.")
        else:
            return(f"La bicileta  {self.brand} {self.model} no esta disponible para parar.")
        
#Herencia
class Truck(Vehicle):
    #Polimorfismo 
    def stert_engine(self):
        if not self.is_available:
            return(f"El camion {self.brand} {self.model} ha sido encendido.")
        else:
            return(f"El camion {self.brand} {self.model} no esta disponible para encender el motor.")
    #Polimorfismo 
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

    def add_vehicles(self, vehicle: Vehicle):
        self.inventory.append(vehicle)
        print(f"El {vehicle.brand} ha sido aÃ±adido al inventario")

    def register_customers(self, customer: Customer):
        self.customers.append(customer)
        print(f"El cliente {customer.name} ha sido aÃ±adido")

    def show_available_vehicle(self):
        print("Vehiculos disponibles en la tienda")
        for vehicle in self.inventory:
            if vehicle.check_availability():
                print(f"- {vehicle.brand} por {vehicle.get_price()}")

car1 = Car("Toyota", "Corolla", 20000)
bike1 = Bike("Yamaha", "MT-07", 7000)
truck1 = Truck("Volvo", "FH16", 80000)

customer1 = Customer("Carlos")

dealership = Dealership()
dealership.add_vehicles(car1)
dealership.add_vehicles(bike1)
dealership.add_vehicles(truck1)

#Mostrar vehiculos disponibles
dealership.show_available_vehicle()

#Cliente consultar un vehiculo
customer1.inquire_vehicle(car1)

#Cliente comprar un vehiculo
customer1.buy_vehicle(car1)

#Mostrar vehiculos disponibles
dealership.show_available_vehicle()


# Encapsulamiento:* Agrupa datos y métodos relacionados en una clase.
# Oculta los detalles internos y controla el acceso a los datos.
# Ejemplo: Una clase "Coche" que encapsula propiedades como "color" y métodos como "arrancar".
# Abstracción:* Simplifica sistemas complejos ocultando detalles innecesarios.
# Permite centrarse en las características esenciales de un objeto.
# Ejemplo: Una interfaz "Vehículo" con método "mover", sin especificar cómo se implementa.
# Herencia:* Permite que una clase (hija) herede propiedades y métodos de otra (padre).
# Promueve la reutilización de código y la jerarquía de clases.
# Ejemplo: "Coche" y "Moto" heredan de "Vehículo".
# Polimorfismo:* Permite que objetos de diferentes clases respondan al mismo método de manera única.
# Facilita el uso de una interfaz común para tipos de datos diversos.
# Ejemplo: Diferentes tipos de "Vehículo" implementan el método "mover" de forma distinta.