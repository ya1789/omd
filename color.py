class Color:
    END = '\033[0'
    START = '\033[1;38;2'
    MOD = 'm'

    def __init__(self, red_ch, green_ch, blue_ch):
        self.red_ch = red_ch
        self.green_ch = green_ch
        self.blue_ch = blue_ch

    def __repr__(self):
        return f'{self.START};{self.red_ch};{self.green_ch};{self.blue_ch}{self.MOD}●{self.END}{self.MOD}'

    @staticmethod
    def _is_correct_ch(channel):
        if not isinstance(channel, int):
            raise ValueError(f"{type(channel)} != int")

        if not 0 <= channel <= 255:
            raise ValueError("channel > 255 or channel < 0")

    @property
    def red_ch(self):
        return self.red_ch_

    @property
    def green_ch(self):
        return self.green_ch_

    @property
    def blue_ch(self):
        return self.blue_ch_

    @red_ch.setter
    def red_ch(self, channel):
        Color._is_correct_ch(channel)
        self.red_ch_ = channel

    @blue_ch.setter
    def blue_ch(self, channel):
        Color._is_correct_ch(channel)
        self.blue_ch_ = channel

    @green_ch.setter
    def green_ch(self, channel):
        Color._is_correct_ch(channel)
        self.green_ch_ = channel

    def __eq__(self, other_color):
        if self is other_color:
            return True

        return self.red_ch == other_color.red_ch and \
            self.green_ch == other_color.green_ch and \
            self.blue_ch == other_color.blue_ch

    def __add__(self, other_color):
        return Color(
            min(self.red_ch + other_color.red_ch, 255),
            min(self.green_ch + other_color.green_ch, 255),
            min(self.blue_ch + other_color.blue_ch, 255)
        )

    def __hash__(self):
        color_tuple = (self.red_ch, self.green_ch, self.blue_ch)
        return hash(color_tuple)

    def __mul__(self, coef):
        if not (isinstance(coef, float) or isinstance(coef, int)):
            raise TypeError(f"{type(coef)} != float")

        if not 0 <= coef <= 1:
            raise ValueError(f"Coef should be between 0 and 1, got {coef}")

        cl = -256 * (1 - coef)
        f = 259 * (cl + 255) / (255 * (259 - cl))

        new_red_ch = round(f * (self.red_ch - 128)) + 128
        new_green_ch = round(f * (self.green_ch - 128)) + 128
        new_blue_ch = round(f * (self.blue_ch - 128)) + 128

        return Color(new_red_ch, new_green_ch, new_blue_ch)

    def __rmul__(self, coef):
        return self.__mul__(coef)


orange1 = Color(255, 165, 0)
red = Color(255, 0, 0)
green = Color(0, 255, 0)
orange2 = Color(255, 165, 0)
color_list = [orange1, red, green, orange2]
set(color_list)
print(0.5 * red)
