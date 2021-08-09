import os
import pygame as pyg

keybinding = {
    "action": pyg.K_j,
    "jump": pyg.K_k,
    "left": pyg.K_a,
    "right": pyg.K_d,
    "down": pyg.K_s,
}


class Control(object):
    def __init__(self, caption):
        self.screen = pyg.display.get_surface()
        self.done = False  # quit cross
        self.clock = pyg.time.Clock()  # frame rate
        self.caption = caption
        self.fps = 60
        self.show_fps = False
        self.current_time = 0.0
        self.keys = pyg.key.get_pressed()
        self.state_dict = {}
        self.state_name = None
        self.state = None

    def setup_states(self, state_dict, start_state):
        self.state_dict = state_dict
        self.state_name = start_state
        self.state = self.state_dict[self.state_name]

    def main(self):
        while not self.done:
            self.event_loop()
            self.update()
            pyg.display.update()
            self.clock.tick(self.fps)
            if self.show_fps:
                fps = self.clock.get_fps()
                caption_with_fps = "{} ----- {:.2f} FPS".format(self.caption, fps)
                pyg.display.set_caption(caption_with_fps)

    def update(self):
        self.current_time = pyg.time.get_ticks()
        if self.state.done:
            self.flip_state()
        elif self.state.quit:
            self.done = True

        self.state.update(self.screen, self.keys, self.current_time)

    def flip_state(self):
        previous, self.state_name = self.state_name, self.state.next
        persist = self.state.cleanup()
        self.state = self.state_dict[self.state_name]
        self.state.startup(self.current_time, persist)
        self.state.previous = previous

    def event_loop(self):
        for event in pyg.event.get():
            if event.type == pyg.QUIT:
                self.done = True
            elif event.type == pyg.KEYUP:
                self.keys = pyg.key.get_pressed()
            elif event.type == pyg.KEYDOWN:
                self.keys = pyg.key.get_pressed()
                self.toggle_show_fps(event.key)
            self.state.get_event(event)

    def toggle_show_fps(self, key):
        if key == pyg.K_F1:
            self.show_fps = not self.show_fps
            if not self.show_fps:
                pyg.display.set_caption(self.caption)


class _State(object):
    def __init__(self):
        self.start_time = 0.0
        self.current_time = 0.0
        self.done = False
        self.quit = False
        self.next = None
        self.previous = None
        self.persist = {}

    def get_event(self, event):
        pass

    def startup(self, current_time, persistant):
        self.persist = persistant
        self.start_time = current_time

    def cleanup(self):
        self.done = False
        return self.persist

    def update(self, surface, keys, current_time):
        pass


def load_all_images(directory, colorkey=(255, 0, 255), accept=(".png", "jpyg", "bmp")):
    graphics = {}
    for pic in os.listdir(directory):
        name, ext = os.path.splitext(pic)
        if ext.lower() in accept:
            img = pyg.image.load(os.path.join(directory, pic))
            if img.get_alpha():  # transparent
                img = img.convert_alpha()
            else:
                img = img.convert()
                img.set_colorkey(colorkey)
            graphics[name] = img
    return graphics
