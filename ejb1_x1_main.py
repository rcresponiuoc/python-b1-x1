"""El objetivo general del ejercicio es crear una serie de funciones que nos permitan realizar operaciones 
sobre un texto.

Para este ejercicio, no se debe usar la función split de Python. En vez de ello, deberás  usar las 
siguientes funciones auxiliares que serán de gran ayuda al resolver el ejercicio. Asimismo, se pueden 
elegir crear nuevas funciones adicionales. A continuación, presentaremos una descripción de estos métodos:

* is_newline(character): Es una función que detecta el final de una oración. Deberás suponer que las frases 
están separadas por "\n" (nueva línea). Si el carácter es este símbolo, devolverá True.

* is_space(character): Es una función que detecta si un carácter es un espacio en blanco. Si el carácter es 
este símbolo, devolverá True.

* remove_punctuation_marks(cad): Una función que elimina los signos de puntuación de una palabra o un texto. 
Este método devuelve como resultado una cadena de caracteres sin signos de puntuación.

Las funciones descritas en el apartado anterior forman parte del módulo denominado 'text_manager.py', por lo tanto, 
es preciso importar estas en el módulo 'ejb1_x1_main.py', el cual es el módulo principal en el que desarrollaremos 
nuestra solución. 
En este ejercicio utilizaremos  la variable "TEXT" de tipo cadena de caracteres(definida en el módulo text_manager.py), 
la cual será empleada en cada una de las siguientes funciones como parámetro. Los métodos que se solicita 
desarrollar son:

* find_largest_word(text): Un método que permite detectar la palabra más larga en un texto. Este método debe 
devolver como resultado una cadena de caracteres correspondiente a la palabra más larga. Al evaluar la palabra
no debe contener signos de puntuación. 

* is_palindrome_word(word): Es una función recursiva que nos permitirá detectar si una palabra es palíndromo. 
Un palíndromo es una palabra que se lee igual en un sentido que en otro. Por ejemplo las siguientes palabras son 
palíndromos: Ata; Aviva; Azuza; Apa; Afromorfa. Para el ejercicio, el texto se encuentra en lengua inglesa, 
por lo que no se requiere realizar ningún tipo de acción en relación con tildes o acentos. Al evaluar la palabra 
no debe contener signos de puntuación. El valor que devuelve es de tipo booleano. Si es un palíndromo devolverá 
"True", y en el caso contrario "False". 

* count_palindrome_words(text): Se trata de una función que nos permitirá enumerar las apariciones de palíndromos 
en el texto, por lo tanto, esta retorna un número entero. Para esto debemos hacer uso de la anterior 
función is_palindrome_word(word).

* find_size_largest_sentence(text, filter): Se trata de una función que permite encontrar el tamaño de la oración 
más larga cuyo valor de filtro esté en esa sentencia. Si no existe una oración que coincida con el filtro deberá 
lanzar una excepción del tipo ValueError. El valor a retornar es un número entero que representa la longitud de 
la cadena en cuestión. 
Por ejemplo: si se invoca a la función con los parámetros text = "Hola, Pepe.\n¿Cómo estás, amigo?", el parámetro
filter = "a", este debe devolver 19, ya que en la segunda oración "¿Cómo estás, amigo?", se encuentra incluido 
el valor pasado como filtro y la oración tiene una longitud de la cadena de texto más larga. 
"""
# Add your imports here
from util_package import text_manager 
from util_package.text_manager import TEXT, is_newline, is_space, remove_punctuation_marks

def find_largest_word(text):
    palabra_mas_larga = ''
    palabra_actual = ''
    # iniciamos bucle para valorar si la i es un valor u otro para retener la palabra, limpiarla de signos de puntuación
    # y si es más largo, se valora. 
    for i in text:
        if(is_newline(i) or is_space(i)):
            palabra_actual = remove_punctuation_marks(palabra_actual)
            if(len(palabra_actual)>len(palabra_mas_larga)):
                palabra_mas_larga = palabra_actual
            palabra_actual = ''
        else:
            palabra_actual = f'{palabra_actual}{i}'
     
    # Al final se hace una ultima comprobacíon ya que si no hay salto o espacio, no entrará dentro del 
    # if else previo y el bucle terminó, pero debe valorarse esa ultima palabra generada una vez limpiada,
    # con la previa para determinar si es la más larga o no.
    palabra_actual = remove_punctuation_marks(palabra_actual)
    if len(palabra_actual) > len(palabra_mas_larga):
        palabra_mas_larga = palabra_actual
    return palabra_mas_larga     

def is_palindrome_word(word):
    ''' 
    Nota 1- Tras hacer varias pruebas, he detectado que ' ' es en sí mismo un palindromo según
    la función definida inicialmente, entendiendo que en una palabra, un caracter debería ser una letra
    como mínimo y por definición palindromo. Entonces, en una palabra, aviva o digamos anna, que al reducir
    letras se queda en valor len 1 o 0, funciona, pero si lo que pasa es ' ' (o múltiples espacios),
    se detecta valor = 1 y también da true, por lo tanto, hago un bucle previo para ver si por error
    llegan espacios, limpio y valoro esa opción para devoler false y luego entrará la función de verdad
    NOTA 2: '' también da erroneo pero no tengo como limpiar esto en la recursión, el mismo ejemplo
    de Anna es el caso, primera prueba = true, segunda = true, tercera = '', si protego ese potencial input
    dará falso, pero claramente debería dar true en este caso, pero no tengo como diferenciarlo aquí sin
    hacer algo más avanzado, por parámetro adicional o algo así.
    '''
    word = remove_punctuation_marks(word).lower()
    # bucle para determinar limpiar potenciales espacios continuados y al menos, meter esta protección
    while '  ' in word:
        word = word.replace('  ', ' ')
    if word == ' ':
        return False
    '''
    word = word.strip()
    -->  aplicaría esta pero conceptualmente, entiendo que la palabra viene limpia sin espacios 
    por detrás o delante
    '''
    if len(word) <= 1:
        return True
    if word[0] == word[-1]:
        return is_palindrome_word(word[1:-1])
    else:
        return False

def count_palindrome_words(text):
    palabra_actual = ''
    x = 0
    for i in text:
        if(is_newline(i) or is_space(i)):
            palabra_actual = remove_punctuation_marks(palabra_actual)
            # Protegemos el potencial error detectado previamente bloqueando posible True del ''
            # creo que sería más limpio si en el anterior pudiese meter un parametro al recursivo para
            # no tenerlo que proteger aquí
            if(palabra_actual != '' and is_palindrome_word(palabra_actual)):
                x += 1
            palabra_actual = ''
        else:
            palabra_actual = f'{palabra_actual}{i}'
    # hacemos la misma jugada apra la ultima evaluacíon, ya que si no es newline o space no evaluaría en
    # el propio bucle.
    palabra_actual = remove_punctuation_marks(palabra_actual)
    if(palabra_actual != '' and is_palindrome_word(palabra_actual)):
        x += 1
    return x
    
def find_size_largest_sentence(text, filter):
    oracion_larga = ''
    actual = ''
    for i in text:
        if is_newline(i):
            if filter in actual:
                if(len(actual)>len(oracion_larga)):
                    oracion_larga = actual
            actual = ''
        else:
            actual = f'{actual}{i}'

    # actual = remove_punctuation_marks(actual)
    # comento ya que entiendo que forma parte integro cada carácter de la oración
    # tampoco se pide.
    if filter in actual:
        if len(actual) > len(oracion_larga):
            oracion_larga = actual
    if oracion_larga == '':
        raise ValueError("No se encontró el filtro en ninguna oración")
    return len(oracion_larga)

# Si quieres probar tu código, descomenta las siguientes líneas y ejecuta el script
#print("La palabra mas larga es:", find_largest_word(TEXT))
#print("'aa' es un palíndromo su resultado es:", is_palindrome_word("aa"))
#print("'abx' no un palíndromo su resultado es:", is_palindrome_word("abx"))
#print("'a' es un palíndromo su resultado es:", is_palindrome_word("a"))
#print("'Ababa' es palíndromo su resultado es:", is_palindrome_word("Ababa"))
#print("El número de palabras identificadas como palíndromos es:", count_palindrome_words(TEXT))
#print("El tamaño de la oración más larga con el filtro='a', es :", find_size_largest_sentence(TEXT, "melon"))

