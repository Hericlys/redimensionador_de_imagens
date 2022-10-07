import sys
from designer import *
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from PyQt5.QtGui import QPixmap


class RedimencionarImagem(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.BtnEscolherarquivo.clicked.connect(self.abrir_imagem)
        self.btnRedimensionar.clicked.connect(self.redimencionar_imagem)
        self.btnSalvar.clicked.connect(self.salvar)

    def abrir_imagem(self):
        imagem, _ = QFileDialog.getOpenFileName(
            self.centralwidget,
            'Abrir Imagem',
            r"C:/Users/",
        )
        self.InputEndArquivo.setText(imagem)
        self.original_img = QPixmap(imagem)
        self.labelImg.setPixmap(self.original_img)
        self.inputLargura.setText(str(self.original_img.width()))
        self.inputAltura.setText(str(self.original_img.height()))

    def redimencionar_imagem(self):
        largura = int(self.inputLargura.text())
        self.nova_img = self.original_img.scaledToWidth(largura)
        self.labelImg.setPixmap(self.nova_img)
        self.inputLargura.setText(str(self.nova_img.width()))
        self.inputAltura.setText(str(self.nova_img.height()))

    def salvar(self):
        try:
            if self.nova_img:
                imagem, _ = QFileDialog.getSaveFileName(
                    self.centralwidget,
                    'Salvar Imagem',
                    r"C:/Users/",
                )
                self.nova_img.save(imagem, format='jpg')
        except Exception as e:
            pass


if __name__ == "__main__":
    qt= QApplication(sys.argv)
    ri = RedimencionarImagem()
    ri.show()
    qt.exec_()
