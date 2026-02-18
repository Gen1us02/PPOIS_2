from PySide6.QtWidgets import QApplication
from src.db.settings import engine
from src.db.models import Base
from src.windows.main_window import MainWindow
import sys


if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
