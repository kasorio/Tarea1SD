import grpc
import json
import time
import numpy as np
import cache_service_pb2
import cache_service_pb2_grpc
from find_car_by_id import find_car_by_id
import matplotlib.pyplot as plt

class CacheClient:
    def __init__(self, host="master", port=50051):
        self.channel = grpc.insecure_channel(f"{host}:{port}")
        self.stub = cache_service_pb2_grpc.CacheServiceStub(self.channel)

    def get(self, key, simulated=False):
        start_time = time.time()  # Inicio del temporizador

        response = self.stub.Get(cache_service_pb2.Key(key=key))
        
        if response.value:
            elapsed_time = time.time() - start_time  # Calcula el tiempo transcurrido
            return response.value
        else:
            # Simulamos un retraso aleatorio de 1 a 3 segundos, con una distribución normal en 2
            delay = np.random.normal(2, 0.5)

            if not simulated:
                time.sleep(delay)

            # Si no está en el caché, buscar en el JSON
            value = find_car_by_id(int(key))
            value = str(value)
            if value:
                # Agregando la llave-valor al caché
                self.stub.Put(cache_service_pb2.CacheItem(key=key, value=value))
                
                return value
            else:
                print("Key not found.")
                return None
            
    def simulate_searches(self, duration_seconds=60):
        start_time = time.time()
        time_elapsed = 0
        query_times = []
        
        while time_elapsed < duration_seconds:
            key = str(np.random.randint(1, 101))
            query_start_time = time.time()
            self.get(key)
            query_end_time = time.time()
            
            query_times.append(query_end_time - query_start_time)
            time_elapsed = query_end_time - start_time
        
        plt.plot(query_times)
        plt.xlabel("Query Number")
        plt.ylabel("Query Time (s)")
        plt.title("Query Time Distribution Over Time")
        plt.show()
        

if __name__ == '__main__':
    client = CacheClient()

    while True:
        print("\nChoose an operation:")
        print("1. Get")
        print("2. Simulate Searches")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            key = input("Enter key: ")
            value = client.get(key)
            if value is not None:
                print(f"Value: {value}")
        elif choice == "2":
            duration_seconds = int(input("Enter the duration of the simulation in seconds: "))
            client.simulate_searches(duration_seconds)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")
