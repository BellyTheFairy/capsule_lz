from graphic import SteamStats
from logger import loger

def run_logger_demo():
    print("Записано в logs.csv")

def build_steam_stats():
    statistyc = SteamStats('steam_players.csv')
    statistyc.plot(top_n=100)

def main():
    print("Выберите действие логгера:")
    print("  1 - тест логгера (run_logger)")
    print("  2 - построить статистику Steam (build_steam_stats)")
    print("  3 - выполнить оба действия")
    print("  0 - выход")

    choice = input("Ваш выбор: ").strip()

    match choice:
        case '1':
            run_logger()
        case '2':
            build_steam_stats()
        case '3':
            run_logger_demo()
            build_steam_stats()
        case '0':
            print("Выход.")
        case _:
            print("Неверный ввод. Выберите 0, 1, 2 или 3.")

if __name__ == '__main__':
    main()
