class Computer:
    def __init__(self, name, brand, ram):
        self.name = name
        self.brand = brand
        self.ram = ram

    def show_detials(self):
        print("-----------")
        print(" Device: ", self.name)
        print(" brand: ", self.brand)
        print(" RAM: ", self.ram)
        print("-----------")

    def SetBrand(self, brand):
        self.brand = brand

    def GetBrand(self):
        return self.brand


class pc(Computer):
    def __init__(self, name, model, storage):
        super().__init__(name, model, "Not specified")
        self.model = model
        self.storage = 0

    def SetStorage(self, storage):
        self.storage = storage

    def GetStorage(self):
        return self.storage


laptop = Computer("laptop", "Dell", "8GB")
mobile = Computer("Mobile", "Vivo y19s", "4GB")
ipad = Computer("ipad", "Apple", "250GB")

laptop.show_detials()
mobile.show_detials()
ipad.show_detials()

print(laptop.brand)
laptop.SetBrand("LENOVO")
print(laptop.name + " has a brand {} ".format(laptop.GetBrand()))
print(laptop.GetBrand())
print("==========")

h = pc("system", "windows", "250GB")

print(h.GetStorage())  # 250GB

h.SetStorage("54GB")

print(h.GetStorage())  # 54GB