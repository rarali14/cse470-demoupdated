from snake import Snake

import tkinter

class SnakeTkinterView:

    KEY_MAP = {
    "Up": Snake.UP,
    "Down": Snake.DOWN,
    "Left": Snake.LEFT,
    "Right": Snake.RIGHT
    }

    def __init__(self, canvas, side, game):
        self.c = canvas
        self.side = side
        self.game = game
        self.listeners = []

    def draw(self):
        self.c.delete(tkinter.ALL)
        self.draw_numbers()
        self.draw_snakes()

    def draw_numbers(self):
        num = self.game.get_numbers()
        if num.is_valid():
            x = num.get_x() * self.side
            y = num.get_y() * self.side
            ch = chr(ord('0') + num.get_number())
            self.c.create_text(x, y,
                    text=ch, anchor="nw", fill="white")

    def draw_snakes(self):
        for snake in self.game.get_snakes():
            for cell in snake.get_cells():
                x = cell[0] * self.side
                y = cell[1] * self.side
            self.c.create_oval(x, y, x + self.side, y + self.side,
                    outline="white", fill="white")

    def add_action_listener(self, listener):
        self.listeners.append(listener)

    def got_key(self, event):
    #print "Got key (%s)" % (event.keysym)
        direction = SnakeTkinterView.KEY_MAP[event.keysym]
        for listener in self.listeners:
            listener.turn_action(direction)
