# Limbreria lexica y sintactica
import ply.lex as lex
import ply.yacc as yacc
import tkinter as tk
from tkinter import filedialog

# Crear la ventana principal
ventana = tk.Tk()

# Función para manejar el botón "Seleccionar archivo"
def seleccionar_archivo():
    # Abrir un cuadro de diálogo para seleccionar un archivo
    archivo = filedialog.askopenfile()
    # Obtener la ruta del archivo seleccionado
    ruta_archivo = archivo.name
    # Imprimir la ruta en la consola (opcional)
    print("Archivo seleccionado:", ruta_archivo)

# Crear el botón "Seleccionar archivo"
boton_seleccionar = tk.Button(ventana, text="Seleccionar archivo", command=seleccionar_archivo)
boton_seleccionar.pack()

# Mostrar la ventana principal
ventana.mainloop()



# Definir las reglas de análisis léxico
tokens = ('NUMERO', 'MAS')

def t_NUMERO(token):
    r'\d+'
    token.value = int(token.value)
    return token

def t_MAS(token):
    r'\+'
    return token

t_ignore = ' \t\n'

# Definir las reglas de análisis sintáctico
def p_suma(p):
    'expresion : NUMERO MAS NUMERO'
    p[0] = p[1] + p[3]

# Crear el analizador léxico y sintáctico
analizador_lexico = lex.lex()
analizador_sintactico = yacc.yacc()

# Leer la expresión a compilar
expresion = input("Ingrese una expresión matemática simple: ")

# Analizar la expresión
resultado = analizador_sintactico.parse(expresion, lexer=analizador_lexico)

# Mostrar el resultado
print("El resultado de la expresión es:", resultado)

# Palabras reservadas
P_reservada = {
    'entero' : 'ENTERO',
    'decimal' : 'DECIMAL',
    'booleano' : 'BOOLEANO',
    'cadena' : 'CADENA',
    'si' : 'SI',
    'sino' : 'SINO',
    'mientras' : 'MIENTRAS',
    'hacer' : 'HACER',
    'verdadero' : 'VERDADERO',
    'falso' : 'FALSO'
}

operador = {
    'MAS',
    'MENOS',
    'POR',
    'DIVIDIDO',
    'PORCIENTO',
    'IGUAL',
    'COMPARACION',
    'MENORQUE',
    'MAYORQUE',
    'MENORIGUALQUE',
    'MAYORIGUALQUE',
}

signos = {
    'PARIZQ',
    'PARDER',
    'CORIZQ',
    'CORDER',
    'COMILLA'
    'PUNTOCOMA',
}

numeros = {
    0, 1, 2, 3, 4, 5, 6, 7, 8, 9
}

identificadores = {
    numeros, 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 
    'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
}

# Tokens
t_PARIZQ = r'\('
t_PARDER = r'\)'
t_CORIZQ = r'\['
t_CORDER = r'\]'
t_COMILLA = r'\"'
t_PUNTOCOMA = r'\;'
t_MAS = r'\+'
t_MENOS = r'\-'
t_POR = r'\*'
t_DIVIDIDO = r'/'
t_PORCIENTO = r'\%'
t_IGUAL = r'\='
