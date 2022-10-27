import json


class Location():
    """Класс локаций"""

    def __init__(self, mapping):
        """Конструктор принимает все атрибуты словаря"""
        self.__dict__.update(mapping)
        for key in self.__dict__.keys():
            if type(self.__dict__[key]) == dict:
                self.__dict__[key] = Location(self.__dict__[key])


class ColorizeMixin():
    """Миксин для изменения цвета выводимого текста"""

    def colorize(self):
        return f' \033[3;{self.repr_color_code};46m {self} \n'


class Advert(ColorizeMixin):
    """Класс объявлений"""

    def __init__(self, mapping):
        """Конструктор принимает все атрибуты словаря"""
        self.repr_color_code = 32
        self.__dict__.update(mapping)
        if 'price' in self.__dict__:
            if self.price < 0:
                raise ValueError('must be >= 0')
        else:
            self.price = 0
        if 'location' in self.__dict__:
            self.location = Location(self.location)

    def __repr__(self):
        return f'{self.title} | {self.price} ₽'


if __name__ == "__main__":
    lesson_str = """{
"title": "python",
"price": 10,
"location": {
"address": "город Москва, Лесная, 7",
"metro_stations": ["Белорусская"],
"some_dict" : {"a" : "a", "asd1" : {"asd2" : "qwe"}}
}
}"""

    lesson = json.loads(lesson_str)
    lesson_ad = Advert(lesson)
    print(lesson_ad.location.address)
    print(lesson_ad.location.metro_stations)
    print(lesson_ad.location.some_dict.asd1.asd2)
    print(lesson_ad)
    print(lesson_ad.colorize())
