"""
Главный модуль приложения (конечный автомат главного меню).
"""

import logging
from messages import MESSAGES
from task_1 import task1_menu
from task_4 import task4_menu
from task_5 import task5_menu

# Настройка логирования
logger = logging.getLogger(__name__)

def show_help():
    """Показывает справку."""
    print("\n=== СПРАВКА ===")
    print("1 - Обработка двух массивов (сортировка и поэлементное сложение)")
    print("4 - Арифметические операции над числами в виде массивов")
    print("5 - Поиск подмассивов с заданной суммой")
    print("h - Показать эту справку")
    print("l - Изменить уровень логирования")
    print("0 - Выйти из программы")
    logger.info("Показана справка")


def change_logging_level():
    """Изменяет уровень логирования."""
    print("\n=== Изменение уровня логирования ===")
    print("Доступные уровни:")
    print("1. DEBUG - все сообщения")
    print("2. INFO - информационные сообщения")
    print("3. WARNING - только предупреждения")
    print("4. ERROR - только ошибки")
    print("5. CRITICAL - только критические ошибки")
    
    choice = input("Выберите уровень (1-5): ").strip()
    
    level_map = {
        '1': logging.DEBUG,
        '2': logging.INFO,
        '3': logging.WARNING,
        '4': logging.ERROR,
        '5': logging.CRITICAL
    }
    
    if choice in level_map:
        new_level = level_map[choice]
        logging.getLogger().setLevel(new_level)
        level_name = logging.getLevelName(new_level)
        print(f"Уровень логирования изменен на: {level_name}")
        logger.info(f"Уровень логирования изменен на: {level_name}")
    else:
        print("Неверный выбор уровня")
        logger.warning("Неверный выбор уровня логирования")


# FSM главного меню

MAIN_FSM = {
    "MAIN": {
        "1": {"action": "task1"},
        "4": {"action": "task4"},
        "5": {"action": "task5"},
        "h": {"action": "help"},
        "l": {"action": "logging"},
        "0": {"action": "exit"},
    }
}

# Обработчики действий
def do_task1():
    logger.info("→ Переход в task_1")
    task1_menu()

def do_task4():
    logger.info("→ Переход в task_4")
    task4_menu()

def do_task5():
    logger.info("→ Переход в task_5")
    task5_menu()

def do_help():
    show_help()

def do_logging():
    change_logging_level()

def do_exit():
    print("Выход из программы...")
    logger.info("Приложение завершено пользователем")
    return False  # сигнал для выхода из главного цикла

# Словарь обработчиков
ACTION_MAP = {
    "task1": do_task1,
    "task4": do_task4,
    "task5": do_task5,
    "help": do_help,
    "logging": do_logging,
    "exit": do_exit,
}

# Главный цикл программы
def main():
    """
    Основной цикл обработки меню через конечный автомат.
    """
    # Настройка логирования
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[logging.FileHandler("app.log", encoding='utf-8')]
    )
    
    state = "MAIN"
    msgs = MESSAGES["main_menu"]
    
    logger.info("Программа запущена")
    print("=" * 60)
    print("ПРОГРАММА ДЛЯ ВЫПОЛНЕНИЯ ЗАДАНИЙ ПО РАБОТЕ С МАССИВАМИ")
    print("=" * 60)

    while True:
        print("\n" + msgs["title"])
        for opt in msgs["options"]:
            print(opt)

        choice = input(msgs["prompt"]).strip().lower()
        logger.info(f"Главное меню: ввод пользователя → {choice}")

        entry = MAIN_FSM[state].get(choice)
        if not entry:
            print(msgs["invalid"])
            logger.warning("Main: неверный пункт меню")
            continue

        action_name = entry["action"]
        handler = ACTION_MAP[action_name]
        
        result = handler()
        if result is False:  # если обработчик сигнализировал выход
            break


if __name__ == "__main__":
    main()