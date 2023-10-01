from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

# Texto que queremos hashear
texto_original = "Ejemplo de cifrado con HASH SHA-256."

# Creamos un objeto de hash SHA-256
digest = hashes.Hash(hashes.SHA256())

# Actualizamos el objeto de hash con el texto
digest.update(texto_original.encode('utf-8'))

# Finalizamos el cálculo dle hash y obtenemos el valor hash en formato bytes
hash_result = digest.finalize()

# Convertimos el valor hash en formato bytes a una representación hexadecimal
hash_hex = hash_result.hex()

# Imprimimos el resultado
print("Texto Original:  ", texto_original)
print("Texto SHA-256:   ", hash_hex)