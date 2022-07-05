"""
艺术二维码生成器

@author  : zhouhuajian
@version : v1.0
"""
from PySide6.QtWidgets import QWidget, QApplication

from main_window_ui import Ui_MainWindow


class ArtisticQrcodeGenerator(QWidget):
    """艺术二维码生成器"""

    def __init__(self):
        """初始化"""
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


if __name__ == '__main__':
    # 应用
    app = QApplication()
    qrcodeGenerator = ArtisticQrcodeGenerator()
    qrcodeGenerator.show()
    # 进入消息循环
    app.exec()
