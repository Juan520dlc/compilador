import sys
import ply.lex as lex

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
        # Obtener el contenido del archivo de la caja de texto y compilarlo aquí
        file_contents = self.file_contents.toPlainText()
        
        # Código para compilar el archivo
        reservadas = {
            'entero':'ENTERO',
            'decimal':'DECIMAL',
            'booleano':'BOOLEANO',
            'cadena':'CADENA',
            'si':'SI',
            'sino':'SINO',
            'mientras':'MIENTRAS',
            'hacer':'HACER',
            'verdadero':'VERDADERO',
            'falso':'FALSO'
        }

        tokens = ['ID', 'NUMERO', 'ENTERO', 'DECIMAL', 'BOOLEANO', 'CADENA', 'SI', 'SINO', 'MIENTRAS', 'HACER', 'VERDADERO', 'FALSO', 'MAS', 'MENOS', 'POR', 'DIVIDIDO',
                'PORCIENTO', 'IGUAL', 'COMPARACION', 'MENORQUE', 'MAYORQUE', 'MAYORIGUALQUE', 'MENORIGUALQUE', 'PARIZQ', 'PARDER','CORIZQ', 'CORDER',
                'COMILLA', 'PUNTOYCOMA', 'ACTUALIZAR']
        
        tokens = tokens + list(reservadas.values())
        
        t_ignore = '\t'
        t_MAS = r'\+'
        t_MENOS = r'\-'
        t_POR = r'\*'
        t_DIVIDIDO = r'/'
        t_PORCIENTO = r'\%'
        t_IGUAL = r'='
        t_COMPARACION = r'=='
        t_MENORQUE = '<'
        t_MAYORQUE = '>'
        t_MAYORIGUALQUE = '>='
        t_MENORIGUALQUE = '<='
        t_PARIZQ = r'\('
        t_PARDER = r'\)'
        t_CORIZQ = r'\{'
        t_CORDER = r'\}'
        t_COMILLA = r'"'
        t_PUNTOYCOMA = r';'
        t_ACTUALIZAR = ':='

        def t_ID(t):
            r'[a-zA-Z_] [a-zA-Z0-9_]*'
            if t.value.upper() in reservadas:
                t.value = t.value.upper()
                reservadas.get(t.value, 'ID')
                t.type = t.value
            
            return  t
        
        def t_lineanueva(t):
            r'\n+'
            t.lexer.lineno += len(t.value)

        def t_NUMERO(t):
            r'\d+'
            t.value = int(t.value)
            t.type = 'NUMERO'
            return t
        
        def t_error(t):
            message = "Error: Caracter inesperado '%s'" % t.value[0]
            return message


        cadena = file_contents

        analizador = lex.lex()

        analizador.input(cadena)

        while True:
            tok = analizador.token()
            if not tok : break
            print(tok)

        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
