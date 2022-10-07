class Search:
    def __init__(self, brand: str, model: str, from_year: int, until_year: int, quantity: int):
        self._brand = brand.lower()
        self._model = model.lower()
        self._from_year = from_year
        self._until_year = until_year
        self._quantity = quantity

    @classmethod
    def input_attributes(cls):
        brand = input("Marca: ")
        model = input("Modelo: ")
        from_year = int(input("Anio inicial: "))
        until_year = int(input("Anio final: "))
        quantity = int(input("Cantidad de resultados: "))
        return cls(brand, model, from_year, until_year, quantity)

    def get_search(self):
        print(f"Marca: {self._brand},\nModelo: {self._model},\nAnios: {self._from_year} - {self._until_year}"
              f"\nCantidad: {self._quantity}")

