import sys
import ply.lex as lex

from distutils.core import setup,Extension
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog, QPushButton, QTextEdit, QVBoxLayout, QMessageBox


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
    def initUI(self):
        self.setGeometry(100, 100, 400, 300)
        self.setWindowTitle('Analizador Lexico')
        
        # Crear un botón para seleccionar un archivo de texto
        select_file_button = QPushButton('Seleccionar archivo', self)
        select_file_button.clicked.connect(self.select_file)
        
        # Crear un botón para compilar el archivo de texto
        compile_button = QPushButton('Compilar', self)
        compile_button.clicked.connect(self.compile_file)
        
        # Crear una caja de texto para mostrar el contenido del archivo
        self.file_contents = QTextEdit(self)
        self.file_contents.setReadOnly(True)
        
        # Crear un layout vertical para los elementos de la interfaz
        layout = QVBoxLayout()
        layout.addWidget(select_file_button)
        layout.addWidget(self.file_contents)
        layout.addWidget(compile_button)
        
        self.setLayout(layout)
        
    def select_file(self):
        # Abrir un diálogo para seleccionar un archivo de texto
        file_dialog = QFileDialog(self)
        file_dialog.setNameFilter('Archivos de texto (*.txt)')
        
        if file_dialog.exec_() == QFileDialog.Accepted:
            file_path = file_dialog.selectedFiles()[0]
            
            # Leer el contenido del archivo seleccionado y mostrarlo en la caja de texto
            with open(file_path, 'r') as f:
                file_contents = f.read()
                self.file_contents.setText(file_contents)
        
    def compile_file(self):
        modulo = Extension('Compilacion', sources = ['main.cpp'])

        setup(name = 'Compilacion',
                version = '1.0',
                author = 'Juan Marroquin',
                description = 'Analizador Lexico y Sintactico',
                ext_modules = [modulo])
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
