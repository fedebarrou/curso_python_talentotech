from colorama import init
from backend.core.db import init_db
from frontend.ui.menu import menu_principal

def main():
    init(autoreset=True)
    init_db()
    menu_principal()

if __name__ == "__main__":
    main()
