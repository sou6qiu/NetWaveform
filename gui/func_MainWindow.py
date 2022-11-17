from ui_MainWindow import Ui_MainWindow

# 在这里实现程序的功能，和UI界面分开，避免耦合
class FuncMainWindow:
    def __init__(self, UI):
        # self.ui = UI
        self.ui = Ui_MainWindow()

    def setup_function(self):
        self.ui.serverbutton.clicked.connect(self.handle_server)
        pass

    def handle_server(self):
        self.ui.ip
