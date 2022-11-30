import json
import keyword


class ColorizeMixin():
    """Миксин для изменения цвета выводимого текста"""

    def __str__(self):
        return f' \033[3;{self.repr_color_code};33m {repr(self)}\033[0;0m'


class Location(ColorizeMixin):
    """Класс локаций"""

    def __init__(self, mapping):
        """Конструктор принимает все атрибуты словаря"""
        self.__dict__.update(mapping)
        #for key, value in mapping.items():
        for key in self.__dict__.keys():
            if type(self.__dict__[key]) == dict:
                self.__dict__[key] = Location(self.__dict__[key])


class Advert(ColorizeMixin):
    """Класс объявлений"""

    def __init__(self, mapping):
        """Конструктор принимает все атрибуты словаря"""
        self.repr_color_code = 32
        self.price = 0
        self.__dict__.update(mapping)
        #dict_of_keys = dict(self.__dict__.keys())
        #print(list_of_keys)
        for key in list(self.__dict__):
            if keyword.iskeyword(key):
                self.__dict__[key + '_'] = self.__dict__.pop(key)
        if self.price < 0:
            raise ValueError('must be >= 0')
        else:
            self.price = self.price
        if 'location' in self.__dict__:
            self.location = Location(self.location)

    def __str__(self):
        return super().__str__()

    def __repr__(self):
        return f'{self.price} {self.title}'


if __name__ == "__main__":
    lesson_str = """{
"title": "python",
"price": 10,
"class": "god help me",
"def": "11",
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
    print(lesson_ad.class_)
    print(lesson_ad.def_)
