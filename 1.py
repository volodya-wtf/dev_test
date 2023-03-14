# 1.
class Technic:
    def __init__(self, name: str, price: float, availability: bool):
        self.name = name
        self.price = price
        self.availability = availability

    def __repr__(self):
        return self.name


products = list()

products.append(Technic("Samsung c100", 3500.00, True))
products.append(Technic("Dexp URSUS K48", 6499.00, True))
products.append(Technic("Dexp URSUS C18 Kid's", 4299.00, True))

cost_criterion = 5000  # Критерий дороговизны

expensive = list()
cheap = list()

for product in products:
    expensive.append(product) if product.price > cost_criterion else cheap.append(
        product
    )

# print(expensive)  # [Dexp URSUS K48]
# print(cheap)  # [Samsung c100, Dexp URSUS C18 Kid's]

# 2.
class Technic:
    def __init__(self, name: str, price: float, availability: bool):
        self.name = name
        self.price = price
        self.availability = availability

    def __repr__(self):
        return self.name

    def __lt__(self, other):
        if isinstance(other, Technic):
            return len(self.name) < len(other.name)
        else:
            raise TypeError

    def __gt__(self, other):
        if isinstance(other, Technic):
            return len(self.name) > len(other.name)
        else:
            raise TypeError

    def __eq__(self, other):
        if isinstance(other, Technic):
            return len(self.name) == len(other.name)
        else:
            raise TypeError


# foo = Technic("foo", 1000.00, True)
# bar = Technic("bar", 1000.00, True)
# foobar = Technic("foobar", 1000.00, True)

# print(f"foo > bar: {foo > bar}") # False
# print(f"foo < bar: {foo < bar}") # False
# print(f"foo == bar: {foo == bar}") # True

# print(f"foo > foobar: {foo > foobar}") # False
# print(f"foo < foobar: {foo < foobar}") # True
# print(f"foo == foobar: {foo == foobar}") # False

# print(foo > 10)  # TypeError
