class Cookie:
    def __init__(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def set_color(self, color):
        self.color = color



cookie_one = Cookie("green")
cookie_two = Cookie("red")

print("Cookie one is", cookie_one.get_color())

cookie_one.set_color("pink")

print("Cookie one is", cookie_one.get_color())

