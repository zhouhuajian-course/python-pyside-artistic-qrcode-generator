"""
艺术二维码生成器

@author: zhouhuajian
@version: v1.0
"""
import time

from PySide6.QtCore import QFile
from PySide6.QtGui import QMouseEvent, Qt, QMovie, QPixmap
from PySide6.QtWidgets import QWidget, QApplication, QFileDialog, QMessageBox
from amzqr import amzqr

from main_window_ui import Ui_MainWindow


class ArtisticQrcodeGenerator(QWidget):
    """艺术二维码生成器"""

    def __init__(self):
        """初始化"""
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # 修改背景图片
        self.ui.backgroundImageLabel.mousePressEvent = self.changeBackgroundImage
        self.backgroundImagePath = 'images/default_background.png'
        # 创建二维码
        self.ui.pushButton.clicked.connect(self.createQrcode)
        # 保持二维码
        self.ui.qrcodeLabel.mousePressEvent = self.saveQrcode
        self.qrcodePath = 'images/default_qrcode.png'
        self.file = QFile()

    def changeBackgroundImage(self, mouseEvent: QMouseEvent):
        """修改背景图片"""
        if mouseEvent.button() != Qt.MouseButton.LeftButton:
            return
        r = QFileDialog.getOpenFileName(parent=self,
                                        caption="选择背景图片",
                                        filter="图片 (*.png *.jpg *.gif)")
        imagePath = r[0]
        # 如果用户没有选择背景图片，直接返回，不做后续处理
        if not imagePath:
            return
        self.backgroundImagePath = imagePath
        # jpg png 静态图片
        if self.backgroundImagePath[-3:] != 'gif':
            self.ui.backgroundImageLabel.setPixmap(QPixmap(self.backgroundImagePath))
        else:
            movie = QMovie(self.backgroundImagePath)
            self.ui.backgroundImageLabel.setMovie(movie)
            movie.start()

    def createQrcode(self):
        """创建二维码"""
        words = self.ui.plainTextEdit.toPlainText()
        try:
            # 生成二维码
            r = amzqr.run(words=words,
                          picture=self.backgroundImagePath,
                          save_dir='./temp',
                          save_name='临时二维码.' + self.backgroundImagePath[-3:],
                          version=10,
                          colorized=True)
            self.qrcodePath = r[2]
            # jpg png 静态图片
            if self.qrcodePath[-3:] != 'gif':
                self.ui.qrcodeLabel.setPixmap(QPixmap(self.qrcodePath))
            else:
                movie = QMovie(self.qrcodePath)
                self.ui.qrcodeLabel.setMovie(movie)
                movie.start()
        except Exception as e:
            error = str(e)
            if error.startswith("Wrong words!"):
                error = "您输入了" + repr(words) + "，但目前仅支持以下字符\n0-9 A-Z a-z ·,.:;+-*/\~!@#$%^&`'=<>[]()?_{}|"
            QMessageBox.critical(self, "二维码创建失败", error)

    def saveQrcode(self, mouseEvent: QMouseEvent):
        """二维码标签鼠标按下事件"""
        if mouseEvent.button() != Qt.MouseButton.LeftButton:
            return
        ext = self.qrcodePath[-3:]
        r = QFileDialog.getSaveFileName(parent=self,
                                        dir=f'二维码{time.strftime("%Y%m%d_%H%M%S")}.{ext}',
                                        filter=f"图片 (*{ext})")
        imagePath = r[0]
        if not imagePath:
            return
        self.file.copy(self.qrcodePath, imagePath)
        QMessageBox.information(self, "提示", f"二维码保存成功")


if __name__ == '__main__':
    # 应用
    app = QApplication()
    qrcodeGenerator = ArtisticQrcodeGenerator()
    qrcodeGenerator.show()
    # 进入消息循环
    app.exec()
