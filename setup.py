from distutils.core import setup,Extension
modulo = Extension('Compilacion', sources = ['main.cpp'])

setup(name = 'Compilacion',
        version = '1.0',
        author = 'Juan Marroquin',
        description = 'Analizador Lexico y Sintactico',
        ext_modules = [modulo])