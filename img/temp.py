import socket
import threading
import time

# SET THIS TO YOUR SERVER'S IP AND PORT
SERVER_IP = '69.163.183.130'  # Localhost (your own computer)
SERVER_PORT = 443       # Change to your game server port

# How many fake players you want to simulate
NUM_CONNECTIONS = 50

# How often to send packets (in seconds)
PACKET_INTERVAL = 1

def fake_player(player_id):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((SERVER_IP, SERVER_PORT))
        print(f"[Player {player_id}] Connected!")

        while True:
            # Send a dummy message
            sock.sendall(b"Hello from fake player!\n")
            print(f"[Player {player_id}] Sent packet!")
            time.sleep(PACKET_INTERVAL)

    except Exception as e:
        print(f"[Player {player_id}] Error: {e}")
    finally:
        sock.close()
        print(f"[Player {player_id}] Disconnected.")

def main():
    threads = []

    for i in range(NUM_CONNECTIONS):
        t = threading.Thread(target=fake_player, args=(i,))
        t.start()
        threads.append(t)
        time.sleep(0.1)  # Small delay to not slam all at once

    # Optional: wait for all threads to finish (they won't unless your server kicks them)
    for t in threads:
        t.join()

if __name__ == "__main__":
    main()
