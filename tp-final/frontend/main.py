from backend.core.db import init_db
from frontend.ui.menu import menu_principal

def main():
    init_db()          # backend: prepara DB
    menu_principal()   # frontend: UI terminal

if __name__ == "__main__":
    main()
