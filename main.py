"""
艺术二维码生成器

@author  : zhouhuajian
@version : v1.0
"""
from PySide6.QtGui import QMouseEvent, Qt
from PySide6.QtWidgets import QWidget, QApplication, QFileDialog

from main_window_ui import Ui_MainWindow


class ArtisticQrcodeGenerator(QWidget):
    """艺术二维码生成器"""

    def __init__(self):
        """初始化"""
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.backgroundImageLabel.mousePressEvent = self.changeBackgroundImage

    def changeBackgroundImage(self, mouseEvent: QMouseEvent):
        """修改背景图片"""
        if mouseEvent.button() != Qt.MouseButton.LeftButton:
            return
        r = QFileDialog.getOpenFileName(parent=self,
                                        caption="选择背景图片",
                                        filter="图片 (*.jpg *.png *.gif)")
        # print(r)
        imagePath = r[0]
        if not imagePath:
            return
        print("背景图片修改为" + imagePath)

if __name__ == '__main__':
    # 应用
    app = QApplication()
    qrcodeGenerator = ArtisticQrcodeGenerator()
    qrcodeGenerator.show()
    # 进入消息循环
    app.exec()
