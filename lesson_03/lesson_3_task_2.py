from smartphone import Smartphone

catalog = [
    Smartphone('Samsung', 'Galaxy M31', '+79991234567'),
    Smartphone('Xiaomi', 'Redmi 9A', '+79876543210'),
    Smartphone('Apple', 'iPhone 15', '+7901234678'),
    Smartphone('Infinix', 'GT 30 Pro', '+79032145698'),
    Smartphone('Honor', 'Magic V2', '+79874563210')
]

for smartphone in catalog:
    print(f"{smartphone.brand} - {smartphone.model}. "
          f"{smartphone.number}")
