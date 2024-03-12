
import socket

def Banniere():
    print("#########################################")
    print("#         SCRIPT SCANNER PORT           #")
    print("#########################################")

def scan_port(host, port):
    try:
        # Créer un objet socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # Définir un délai pour la connexion (en secondes)
        sock.settimeout(1)
        
        # Tentative de connexion au port spécifié
        result = sock.connect_ex((host, port))
        
        # Si la connexion est réussie, le port est ouvert
        if result == 0:
            print(f"Port {port} sur {host} : Ouvert")
        else:
            print(f"Port {port} sur {host} : Fermé")
        
        # Fermer la connexion
        sock.close()
    except socket.error:
        print(f"Impossible de se connecter à {host}:{port}")

def main():

    Banniere()
    print()
    host = input("Entrez l'adresse IP ou le nom de domaine de la cible : ")
    port = int(input("Entrez le numéro de port à scanner : "))

    scan_port(host, port)

if __name__ == "__main__":
    main()
