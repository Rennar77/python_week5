# Base Class: Smartphone
class Smartphone:
    # Constructor to initialize attributes
    def __init__(self, brand, model, storage, battery):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.battery = battery

    # Method to display details
    def phone_info(self):
        return f"{self.brand} {self.model} | Storage: {self.storage}GB | Battery: {self.battery}mAh"

    # Method to simulate charging
    def charge(self):
        return f"{self.model} is charging 🔋..."

    # Method to simulate calling
    def call(self, contact):
        return f"Calling {contact} from {self.model} 📞"


# Derived Class: AndroidPhone (inherits from Smartphone)
class AndroidPhone(Smartphone):
    def __init__(self, brand, model, storage, battery, android_version):
        # Call parent constructor
        super().__init__(brand, model, storage, battery)
        self.android_version = android_version

    # Overriding method (polymorphism example)
    def phone_info(self):
        return f"{self.brand} {self.model} (Android {self.android_version}) | Storage: {self.storage}GB | Battery: {self.battery}mAh"


# Derived Class: iPhone (inherits from Smartphone)
class iPhone(Smartphone):
    def __init__(self, model, storage, battery, ios_version):
        # iPhones only need model, since brand is always Apple
        super().__init__("Apple", model, storage, battery)
        self.ios_version = ios_version

    # Overriding method
    def phone_info(self):
        return f"{self.brand} {self.model} (iOS {self.ios_version}) | Storage: {self.storage}GB | Battery: {self.battery}mAh"


# --- Testing our classes ---

# Creating a base Smartphone
phone1 = Smartphone("Nokia", "3310", 2, 900)
print(phone1.phone_info())
print(phone1.call("Alice"))
print(phone1.charge())

print("\n--- Inheritance and Polymorphism ---")

# Creating an Android phone
android = AndroidPhone("Samsung", "Galaxy S22", 128, 4500, "13")
print(android.phone_info())   # Overridden method
print(android.call("Bob"))

# Creating an iPhone
iphone = iPhone("14 Pro Max", 256, 4352, "16")
print(iphone.phone_info())    # Overridden method
print(iphone.call("Charlie"))
