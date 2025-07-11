import random

class Customer:
    def __init__(self, name, country, is_active, total_spent):
        self.name = name
        self.country = country
        self.is_active = is_active
        self.total_spent = total_spent

class CustomerQuery:
    def __init__(self, customers):
        self.customers = customers

    def active(self):
        self.customers = [c for c in self.customers if c.is_active]
        return self

    def from_country(self, country):
        self.customers = [c for c in self.customers if c.country == country]
        return self

    def with_min_spent(self, amount):
        self.customers = [c for c in self.customers if c.total_spent >= amount]
        return self

    def get(self):
        return self.customers


names = [
    "John Doe", "Jane Smith", "Alice Johnson", "Bob Brown", "Carlos Vega",
    "Daniela Ruiz", "Tom Lee", "Sarah King", "Hannah Scott", "Diego Torres",
    "Laura White", "Sofia Martinez", "Emma Davis", "William Clark", "Lucas Wilson",
    "Emily Hill", "Grace Lopez", "Henry Young", "Olivia Green", "Noah Hall",
    "Liam Adams", "Chloe Wright", "Zoe Walker", "Mia Harris", "Ella Allen",
    "Ethan Lewis", "Ava Robinson", "Leo Turner", "Camila Baker", "Nina Gonzalez"
]

countries = ["USA", "Canada", "Mexico", "Brazil", "Germany"]
customers = []

for name in names:
    country = random.choice(countries)
    is_active = random.choice([True, False])
    total_spent = round(random.uniform(500, 2000), 2)
    customers.append(Customer(name, country, is_active, total_spent))


query = CustomerQuery(customers)
filtered = query.active().from_country("USA").with_min_spent(1000).get()


for customer in filtered:
    print(f"{customer.name} - {customer.country} - ${customer.total_spent:.2f}")
