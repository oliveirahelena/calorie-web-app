from temperature import Temperature


class Calorie:
    """Represents optimal calorie amount a person needs to take today"""

    def __init__(
        self, weight: float, height: float, age: int, temperature: float
    ) -> None:
        self.weight = weight
        self.height = height
        self.age = age
        self.temperature = temperature

    def calculate(self) -> float:
        result = 10 * self.weight + 6.5 * self.height + 5 - self.temperature * 10
        return result


if __name__ == "__main__":
    temperature = Temperature(country="brazil", city="belo-horizonte").get()
    calorie = Calorie(weight=70, height=164, age=37, temperature=temperature)
    print(calorie.calculate())
