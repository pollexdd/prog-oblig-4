


class filmer:
    def __init__(self, name, year, score):
        self.name = name
        self.year = year
        self.score = score
    def get_description(self):
        return f"{self.name} was released in {self.year} and currently has a score of {self.year}"

film_1 = filmer("Inception","2010","Score: 8.8")
film_2 = filmer("The Martian","2015","Score: 8.0")
film_3 = filmer("Joker","2019","Score: 8.4")

print(f"{film_1.name} was released in {film_1.year} and currently has a score of {film_1.year}")
print(f"{film_2.name} was released in {film_2.year} and currently has a score of {film_2.year}")
print(f"{film_3.name} was released in {film_3.year} and currently has a score of {film_3.year}")

print()

print(film_1.get_description())
print(film_2.get_description())
print(film_3.get_description())