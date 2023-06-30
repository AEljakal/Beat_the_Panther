import itertools

def generate_words(letters):
    # Generar todas las permutaciones posibles de las letras
    permutations = list(itertools.permutations(letters))
    
    # Cargar un diccionario de palabras válidas (puedes ampliarlo con más palabras)
    valid_words = ['AITLAI', 'AMOR', 'NOITCAAV']
    
    # Verificar si cada permutación es una palabra válida
    valid_permutations = []
    for permutation in permutations:
        word = ''.join(permutation)
        if word in valid_words:
            valid_permutations.append(word)
    
    return valid_permutations

# Ejemplo de uso
letters = ['A', 'I', 'T', 'L', 'A', 'I']
valid_permutations = generate_words(letters)
print(valid_permutations)
