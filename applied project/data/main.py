from . import setup, tools
from .chapter import main_menu, level1, load_screen, game_over, time_out, coin_room
from . import constants as c


def main():
    run_it = tools.Control(setup.ORIGINAL_CAPTION)
    state_dict = {
        c.MAIN_MENU: main_menu.Menu(),
        c.LOAD_SCREEN: load_screen.LoadScreen(),
        c.GAME_OVER: game_over.GameOver(),
        c.TIME_OUT: time_out.TimeOut(),
        c.LEVEL1: level1.Level1(),
        c.COIN_ROOM: coin_room.CoinRoom(),
    }

    run_it.setup_states(state_dict, c.MAIN_MENU)
    run_it.main()
