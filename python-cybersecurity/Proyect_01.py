# Primer scaner 

import socket

host = input("Ingrese la IP o dominio: ")

print(f"\nEscaneando {host}\n")

for puerto in range(1,1025):

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.settimeout(0.5)

    resultado = s.connect_ex((host, puerto))

    if resultado == 0:
        print(f"Puerto {puerto} ABIERTO")

    s.close()
    
    