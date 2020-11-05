class Button:
    global x
    x = 0

    def click(self):
        global x
        x += 1

    def click_count(self):
        global x
        print(x)

    def reset(self):
        global x
        x = 0
