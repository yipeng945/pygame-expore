from . import setup, tools
from .chapter import main_menu, level1
from . import constants as c


def main():
    run_it = tools.Control(setup.ORIGINAL_CAPTION)
    state_dict = {
        c.MAIN_MENU: main_menu.Menu(),
        c.LEVEL1: level1.Level1(),
    }

    run_it.setup_states(state_dict, c.MAIN_MENU)
    run_it.main()
