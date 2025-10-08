import sys
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtQml import QQmlApplication
Engineapp = QGuiApplication(sys.argv)
engine = QQmlApplicationEngine()
engine.quit.connect(app.quit)
engine.load('./UI/main.qml')
sys.exit(app.exec())
