"""
艺术二维码生成器

@author  : zhouhuajian
@version : v1.0
"""
from PySide6.QtWidgets import QWidget, QApplication


class ArtisticQrcodeGenerator(QWidget):
    """艺术二维码生成器"""

    def __init__(self):
        """初始化"""
        super().__init__()


if __name__ == '__main__':
    # 应用
    app = QApplication()
    qrcodeGenerator = ArtisticQrcodeGenerator()
    qrcodeGenerator.show()
    # 进入消息循环
    app.exec()