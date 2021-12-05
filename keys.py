from cryptography.hazmat.primitives import serialization as crypto_serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend as crypto_default_backend
import os
import sys

print("Choisissez la longueur en bits de la clé")
bit_length = int(input())

if bit_length % 8 != 0:
    print("La longueur du bit doit être un multiple de 8")
    sys.exit()

if bit_length < 2048:
    print("La longueur en bits doit être supérieure à 2048")
    sys.exit()

if bit_length > 8192:
    print("Vous avez sélectionné une longueur supérieure à 8192 la génération peut-être plus longue")

key = rsa.generate_private_key(
    backend=crypto_default_backend(),
    public_exponent=65537,
    key_size=bit_length
)

private_key = key.private_bytes(
    crypto_serialization.Encoding.PEM,
    crypto_serialization.PrivateFormat.PKCS8,
    crypto_serialization.NoEncryption()
)

public_key = key.public_key().public_bytes(
    crypto_serialization.Encoding.OpenSSH,
    crypto_serialization.PublicFormat.OpenSSH
)


f = open('./save_keys/private.pem', "w+")
f.write(private_key.decode('utf-8'))

f = open('./save_keys/public.pem', "w+")
f.write(public_key.decode('utf-8'))

print("La génération de la clé est effectué, les clés ont été sauvegarder dans le répertoire ./save_keys")