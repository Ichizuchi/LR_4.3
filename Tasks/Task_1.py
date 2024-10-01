class Liquid:
    def __init__(self, name: str, density: float):
        self.name = name
        self.density = density

    def set_name(self, new_name: str):
        self.name = new_name

    def set_density(self, new_density: float):
        if new_density > 0:
            self.density = new_density
        else:
            print("Плотность должна быть положительным числом.")

    def get_info(self):
        return f"Название: {self.name}, Плотность: {self.density} кг/м³"


class Alcohol(Liquid):
    def __init__(self, name: str, density: float, strength: float):
        super().__init__(name, density)
        self.strength = strength

    def set_strength(self, new_strength: float):
        if 0 <= new_strength <= 100:
            self.strength = new_strength
        else:
            print("Крепость должна быть в диапазоне от 0 до 100 процентов.")

    def get_info(self):
        base_info = super().get_info()
        return f"{base_info}, Крепость: {self.strength}%"


if __name__ == '__main__':
    water = Liquid(name="Вода", density=1000)
    print(water.get_info())
    
    water.set_name("Пресная вода")
    water.set_density(998)
    print(water.get_info())

    ethanol = Alcohol(name="Этанол", density=789, strength=96)
    print(ethanol.get_info())
    
    ethanol.set_strength(70)
    ethanol.set_density(800)
    print(ethanol.get_info())
