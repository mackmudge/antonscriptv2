"""Configuration constants"""

import configparser
import os

LOCAL_SETTINGS_PATH = os.path.dirname(os.getcwd()) + '/resources/lolbot.cfg'
config = configparser.RawConfigParser()
if os.path.exists(LOCAL_SETTINGS_PATH):
    config.read(LOCAL_SETTINGS_PATH)
else:
    config['Paths'] = {"LeaguePath": "C:/Riot Games/League of Legends"}
    config['Game'] = {
        "Maxlevel": "30",
        "GameMode": "840"
    }
    config['Graphical'] = {"TextColor": "None"}
    with open(LOCAL_SETTINGS_PATH, 'w') as outfile:
        config.write(outfile)

# PATHS
LEAGUE_CLIENT_DIR = config.get('Paths', 'LeaguePath')
LEAGUE_CLIENT_PATH = LEAGUE_CLIENT_DIR + '/LeagueClient'
LEAGUE_GAME_CONFIG_PATH = LEAGUE_CLIENT_DIR + '/Config/game.cfg'
LEAGUE_CLIENT_LOCKFILE_PATH = LEAGUE_CLIENT_DIR + "/lockfile"
LOCAL_ACCOUNTS_PATH = os.path.dirname(os.getcwd()) + '/resources/accounts.json'
LOCAL_GAME_CONFIG_PATH = os.path.dirname(os.getcwd()) + '/resources/game.cfg'
RIOT_CLIENT_LOCKFILE_PATH = os.getenv('LOCALAPPDATA') + '/Riot Games/Riot Client/Config/lockfile'
LOCAL_LOG_PATH = os.path.dirname(os.getcwd()) + '/logs'

# API INFO
LCU_HOST = '127.0.0.1'
RCU_HOST = '127.0.0.1'
LCU_USERNAME = 'riot'
RCU_USERNAME = 'riot'

# WINDOW NAMES
RIOT_CLIENT_WINNAME = "Riot Client Main"
LEAGUE_CLIENT_WINNAME = "League of Legends"
LEAGUE_GAME_CLIENT_WINNAME = "League of Legends (TM) Client"

# PROCESS NAMES
LEAGUE_PROCESS_NAMES = ["LeagueClient.exe", "League of Legends.exe"]
RIOT_CLIENT_PROCESS_NAMES = ["RiotClientUx.exe"]

# COMMANDS
KILL_LEAGUE_CLIENT = 'TASKKILL /F /IM LeagueClient.exe'
KILL_LEAGUE = 'TASKKILL /F /IM "League of Legends.exe"'
KILL_RIOT_CLIENT = 'TASKKILL /F /IM RiotClientUx.exe'

# GAME DATA
ACCOUNT_MAX_LEVEL = int(config.get('Game', 'MaxLevel'))
GAME_LOBBY_ID = int(config.get('Game', 'GameMode'))
EARLY_GAME_END_TIME = 630
MAX_GAME_TIME = 2400
ASK_4_MID_DIALOG = ["mid ples",
                    "plannin on goin mid team",
                    "mid por favor",
                    "bienvenidos, mid",
                    "howdy, mid",
                    "goin mid",
                    "mid"]

# GAME BUTTON RATIOS
GAME_MINI_MAP_UNDER_TURRET = (0.8760, 0.8846)
GAME_MINI_MAP_CENTER_MID = (0.8981, 0.8674)
GAME_MINI_MAP_ENEMY_NEXUS = (0.9628, 0.7852)
GAME_ULT_RATIO = (0.7298, 0.2689)
GAME_AFK_OK_RATIO = (0.4981, 0.4647)
GAME_CENTER_OF_SCREEN = (0.5, 0.5)
GAME_SYSTEM_MENU_X = (0.7729, 0.2488)

# CLIENT BUTTON RATIOS
POST_GAME_OK_RATIO = (0.4996, 0.9397)
POST_GAME_SELECT_CHAMP_RATIO = (0.4977, 0.5333)
POPUP_SEND_EMAIL_X_RATIO = (0.6960, 0.1238)

# RANDOM
MAX_CLIENT_ERRORS = 5
MAX_PHASE_ERRORS = 20
TEXT_COLOR = config.get('Graphical', 'TextColor')
VERSION = 'v1.3.1'

def persist():
    """Persists game settings"""
    config['Paths']['LeaguePath'] = LEAGUE_CLIENT_DIR
    config['Game']['MaxLevel'] = str(ACCOUNT_MAX_LEVEL)
    config['Game']['GameMode'] = str(GAME_LOBBY_ID)
    config['Graphical']['TextColor'] = TEXT_COLOR
    with open(LOCAL_SETTINGS_PATH, 'w') as configfile:
        config.write(configfile)