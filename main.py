import lex
import yacc

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
