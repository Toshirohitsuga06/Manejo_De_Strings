"""
Nombre: Benjamin Balboa Acosta
Matrícula: 2630376
Ingeniería en Mecatrónica
Institución: Universidad Politécnica de Victoria
Materia: Metodologias de la programacion
Manejo de strings en Python
"""

# RESUMEN EJECUTIVO
"""
Un string  en Python es una secuencia de caracteres 
que se usan para representar información en forma de texto. Las cadenas son inmutables
lo que significa que una vez se crean no puede modificarse, la unica forma de cambiar 
el contenido de una string se pueden redefinir, tambien
cualquier operación que altere una cadena genera  un objeto nuevo en 
la memoria. Las operaciones son la concatenación con '+', la obtención 
de la longitud con 'len()', la extracción de subcadenas mediante slicing, la búsqueda 
de patrones con 'in' y el reemplazo de texto con 'replace()'. Validar y normalizar 
las entradas de texto —como correos, nombres y contraseñas— es importante para 
prevenir errores de entrada antes de analizar datos.
"""



# PRINCIPIOS Y BUENAS PRÁCTICAS

# 1. Inmutabilidad: Los strings no pueden modificarse , por lo que se consideran inmutables
#    solo pueden redefinirse.
# 2. Normalización: Es una buena práctica normalizar las entradas de usuario usando 
#    'strip()' y 'lower()' antes de compararlas para evitar discrepancias por espacios o mayúsculas.
# 3. Números mágicos: Evitar el uso de números fijos en los índices sin documentación; 
#    explicar claramente qué extrae cada segmento (slice).
# 4. Métodos integrados: Utilizar los métodos nativos de string en lugar de reescribir 
#    lógica básica de análisis.
# 5. Validaciones robustas: Validar secuencialmente: primero verificar que no esté vacío 
#    después de limpiar espacios, y luego verificar el formato estructural.
# 6. Legibilidad: Escribir código limpio utilizando nombres de variables en lower_snake_case 
#    y mensajes de error claros.

"""
Problema 1:  Full name formatter (name + initials)
Descripción:
    Dado el nombre completo de una persona en una sola cadena (por ejemplo: "juan carlos tovar"), el programa debe:
        1) Normalizar el texto (strip, espacios extra, mayúsculas/minúsculas).
        2) Mostrar el nombre formateado en Title Case y las iniciales (por ejemplo: J.C.T.).
"""
print("PROBLEMA 1:")
test_names = ["juan carlos tovar", "  benja   balboa  ", "   "]

for full_name in test_names:
    print(f"Entrada: \"{full_name}\"")
    cleaned_name = full_name.strip()
    
    if not cleaned_name:
        print("Error: entrada no válida\n")
        continue
        
    name_words = cleaned_name.split()
    
    if len(name_words) < 2:
        print("Error: entrada no válida\n")
        continue
        
    formatted_name = " ".join([word.title() for word in name_words])
    initials_list = [word[0].upper() for word in name_words]
    initials_str = "".join([f"{init}." for init in initials_list])
    
    print(f"Nombre formateado: {formatted_name}")
    print(f"Iniciales: {initials_str}\n")


"""
Problema 2: Simple email validator (structure + domain)
Valida si una dirección de correo tiene un formato básico correcto:
    - Contiene exactamente un '@'.
    - Después del '@' debe haber al menos un '.'.
    - No contiene espacios en blanco.
Si el correo es válido, también muestra el dominio (la parte después de '@').
"""
print("=== PROBLEMA 2: Validador simple de correo electrónico ===")
test_emails = ["test.user@example.com", "a@b.co", "correo-invalido.com"]

for email_text in test_emails:
    print(f"Entrada: \"{email_text}\"")
    cleaned_email = email_text.strip()
    
    if not cleaned_email or " " in cleaned_email or cleaned_email.count("@") != 1:
        print("Correo válido: false\n")
        continue
        
    at_index = cleaned_email.find("@")
    domain_part = cleaned_email[at_index + 1:]
    
    if "." not in domain_part or domain_part.startswith(".") or domain_part.endswith("."):
        print("Correo válido: false\n")
        continue
        
    print("Correo válido: true")
    print(f"Dominio: {domain_part}\n")


"""
7.3 Problema 3: Palindrome checker (ignoring spaces and case)

Descripción:
Determina si una frase es un palíndromo, es decir, se lee igual de izquierda 
a derecha y de derecha a izquierda, ignorando espacios y mayúsculas/minúsculas.

"""
print("=== PROBLEMA 3: Verificador de palíndromos ===")
test_phrases = ["Anita lava la tina", "Ab a", "Hi"]

for phrase in test_phrases:
    print(f"Entrada: \"{phrase}\"")
    cleaned_phrase = phrase.strip()
    
    if not cleaned_phrase:
        print("Error: entrada no válida\n")
        continue
        
    normalized = cleaned_phrase.lower().replace(" ", "")
    
    if len(normalized) < 3:
        print("Error: entrada no válida\n")
        continue
        
    reversed_text = normalized[::-1]
    is_pal = (normalized == reversed_text)
    
    print(f"Texto normalizado: {normalized}")
    print(f"Es palíndromo: {str(is_pal).lower()}\n")


"""
7.4 Problem 4: Sentence word stats (lengths and first/last word)
--------------------------------------------------

Descripción:
Dada una oración, el programa debe:
1) Normalizar espacios (quitar espacios al principio y al final).
2) Separar las palabras por espacios.
3) Mostrar:
   - Número total de palabras.
   - Primera palabra.
   - Última palabra.
   - Palabra más corta y más larga (por longitud).

"""
print("=== PROBLEMA 4: Estadísticas de palabras ===")
test_sentences = ["Python programming is extremely fun", "Hola", ""]

for sentence in test_sentences:
    print(f"Entrada: \"{sentence}\"")
    cleaned_sentence = sentence.strip()
    
    if not cleaned_sentence:
        print("Error: entrada no válida\n")
        continue
        
    words = cleaned_sentence.split()
    
    if not words:
        print("Error: entrada no válida\n")
        continue
        
    word_count = len(words)
    first_word = words[0]
    last_word = words[-1]
    shortest_word = min(words, key=len)
    longest_word = max(words, key=len)
    
    print(f"Conteo de palabras: {word_count}")
    print(f"Primera palabra: {first_word}")
    print(f"Última palabra: {last_word}")
    print(f"Palabra más corta: {shortest_word}")
    print(f"Palabra más larga: {longest_word}\n")


"""
Problema 5 Password strength classifier
Descripción:
Clasifica una contraseña como "weak", "medium" o "strong" según reglas mínimas (puedes afinarlas, pero documéntalas en los comentarios).

Ejemplo de reglas:
- Weak: longitud < 8 o todo en minúsculas o muy simple.
- Medium: longitud >= 8 y mezcla de letras (mayúsculas/minúsculas) o dígitos.
- Strong: longitud >= 8 y contiene al menos:
  - una letra mayúscula,
  - una letra minúscula,
  - un dígito,
  - un símbolo no alfanumérico (por ejemplo, !, @, #, etc.).
"""
print("=== PROBLEMA 5: Clasificador de contraseñas ===")
test_passwords = ["SecurePass123!", "password", ""]

for password_input in test_passwords:
    print(f"Entrada: \"{password_input}\"")
    if not password_input:
        print("Error: entrada no válida\n")
        continue
        
    length = len(password_input)
    has_upper = any(c.isupper() for c in password_input)
    has_lower = any(c.islower() for c in password_input)
    has_digit = any(c.isdigit() for c in password_input)
    has_symbol = any(not c.isalnum() for c in password_input)
    
    if length >= 8 and has_upper and has_lower and has_digit and has_symbol:
        strength = "fuerte"
    elif length >= 8 and ((has_upper and has_lower) or has_digit):
        strength = "media"
    else:
        strength = "débil"
        
    print(f"Fortaleza de contraseña: {strength}\n")


"""
7.6 Problema 6: Product label formatter (fixed-width text)

Descripción:
Dado el nombre de un producto y su precio, genera una etiqueta en una sola línea con el siguiente formato:

Product: <NAME> | Price: $<PRICE>

La cadena completa debe tener exactamente 30 caracteres:
- Si es más corta, rellena con espacios al final.
- Si es más larga, recorta hasta 30 caracteres.

"""
print("=== PROBLEMA 6: Formateador de etiquetas ===")
test_products = [("Café", 45.50), ("A", 1.0), ("", -5)]

for product_name, price_value in test_products:
    print(f"Entrada: Producto=\"{product_name}\", Precio={price_value}")
    cleaned_name = product_name.strip()
    
    if not cleaned_name:
        print("Error: entrada no válida\n")
        continue
        
    try:
        numeric_price = float(price_value)
        if numeric_price < 0:
            print("Error: entrada no válida\n")
            continue
    except ValueError:
        print("Error: entrada no válida\n")
        continue
        
    base_label = f"Product: {cleaned_name} | Price: ${numeric_price}"
    
    if len(base_label) > 30:
        final_label = base_label[:30]
    else:
        final_label = base_label.ljust(30, " ")
        
    print(f"Etiqueta: \"{final_label}\"\n")


"""
Los strings son fundamentales para realizar operaciones de entrada
y salida de datos usando metodos como 'lower()', 
'strip()', 'split()' y 'join()' ayudan a agilizar las aplicaciones de cambios
a los strings ahorrando tiempo. Normalizar el texto antes de compararlo previene errores 
de espacios en blanco o diferencias de mayúsculas. Las validaciones rigurosas 
garantizan que las aplicaciones descarten datos que no sirven,
comprender la inmutabilidad de los strings y los slices permiten 
una gestión eficiente de la memoria.
"""


#Referencias:

# 1) Python Software Foundation - Text Sequence Type — str: https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str
# 2) Real Python - Python Strings and String Methods: https://realpython.com/python-strings/
# 3) W3Schools - Python String Methods: https://www.w3schools.com/python/python_strings_methods.asp
# 4) Programiz - Python String Methods: https://www.programiz.com/python-programming/methods/string
# 5) GeeksforGeeks - Python Strings: https://www.geeksforgeeks.org/python-strings/


# REPOSITORIO DE GITHUB

# Repositorio de GitHub: 
