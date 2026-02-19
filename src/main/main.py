from PySide6.QtWidgets import QApplication
from src.db.settings import engine
from src.db.models import Base
from src.windows.main_window import MainWindow
from src.db.db_manager import DBManager
import sys


if __name__ == "__main__":
    db_manager = DBManager()
    Base.metadata.create_all(bind=engine)
    app = QApplication(sys.argv)
    window = MainWindow(db_manager)
    window.show()
    sys.exit(app.exec())
