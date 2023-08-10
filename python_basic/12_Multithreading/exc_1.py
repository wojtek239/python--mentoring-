#  Amdahl's Law jest zasadą, która mówi nam, że nawet jeśli zwiększamy liczbę wątków,
#  część operacji nadal będzie wykonywana sekwencyjnie i nie będzie można osiągnąć
#  liniowej skali przyspieszenia.

import random
import time
import threading
import multiprocessing


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def threaded_bubble_sort(arr, num_threads=2):
    chunk_size = len(arr) // num_threads
    threads = []

    for i in range(num_threads):
        start_idx = i * chunk_size
        end_idx = (i + 1) * chunk_size if i < num_threads - 1 else len(arr)
        thread = threading.Thread(target=bubble_sort, args=([arr[start_idx:end_idx]]))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()


def process_bubble_sort(arr, num_processes=2):
    chunk_size = len(arr) // num_processes
    processes = []

    for i in range(num_processes):
        start_idx = i * chunk_size
        end_idx = (i + 1) * chunk_size if i < num_processes - 1 else len(arr)

        pool = multiprocessing.Pool(processes=num_processes)

        pool.apply_async(func=bubble_sort, args=([arr[start_idx:end_idx]]))
        pool.close()
        pool.join()


if __name__ == "__main__":
    array_size = 100
    num_arrays = 10

    arrays = []
    for _ in range(num_arrays):
        random_array = [random.randint(0, 1000) for _ in range(array_size)]
        arrays.append(random_array)

    start_time = time.time()
    for array in arrays[:]:
        threaded_bubble_sort(array)
    end_time = time.time()
    print(f"Multithread sorting: {end_time - start_time} seconds")

    start_time = time.time()
    for array in arrays[:]:
        process_bubble_sort(array)

    end_time = time.time()
    print(f"Multiprocess sorting: {end_time - start_time} seconds")