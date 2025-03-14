import multiprocessing
import time
import random
import numpy as np

def worker_function(data_chunk, result_queue):
    """A worker function that simulates processing of a data chunk."""
    print(f"Processing chunk: {data_chunk}")
    time.sleep(random.uniform(0.1, 1.0))  # Simulate processing time
    result = sum(data_chunk)  # Example operation: sum of the chunk
    result_queue.put(result)  # Put the result in the queue
    print(f"Finished chunk: {data_chunk}, Result: {result}")

def parallel_processing(data, num_workers):
    """Distribute data processing across multiple workers."""
    chunk_size = len(data) // num_workers
    processes = []
    result_queue = multiprocessing.Queue()

    # Create worker processes
    for i in range(num_workers):
        start_index = i * chunk_size
        end_index = None if i == num_workers - 1 else (i + 1) * chunk_size
        data_chunk = data[start_index:end_index]
        
        process = multiprocessing.Process(target=worker_function, args=(data_chunk, result_queue))
        processes.append(process)
        process.start()

    # Collect results from all workers
    for process in processes:
        process.join()

    results = []
    while not result_queue.empty():
        results.append(result_queue.get())
    
    return results

def main():
    """Main function to execute parallel processing."""
    print("Parallel Computing Project")
    
    data_size = 100000  # Define the size of data
    num_workers = 4     # Define the number of worker processes
    data = np.random.randint(1, 100, data_size)  # Generate random data

    print(f"Generated data: {data[:10]}...")  # Display first 10 elements
    results = parallel_processing(data.tolist(), num_workers)

    print(f"Results from parallel processing: {results}")
    print(f"Total sum: {sum(results)}")  # Sum of all results

if __name__ == "__main__":
    main()

# Example Call
# if __name__== '__main__':
#     main()

def additional_functionality(results):
    """Example of additional functionality using results."""
    # Example: Calculate and return average result from processed chunks
    return sum(results) / len(results) if results else 0

def test_parallel_processing():
    """Test function to validate parallel processing."""
    print("Testing parallel processing...")
    data = np.arange(1, 101)  # Sample data for testing
    expected_sum = sum(data)
    results = parallel_processing(data.tolist(), 4)
    total = sum(results)
    assert total == expected_sum, f"Expected {expected_sum}, got {total}"
    print("Test passed successfully!")

# Uncomment the following line to run tests
# test_parallel_processing()

def visualize_results(results):
    """Visualize results of parallel processing using matplotlib."""
    import matplotlib.pyplot as plt

    plt.bar(range(len(results)), results)
    plt.title("Results from Parallel Processing")
    plt.xlabel("Chunk Index")
    plt.ylabel("Sum of Chunk")
    plt.show()

# Uncomment the following line to visualize results after processing
# visualize_results(results)

class CustomParallel:
    """Custom class for parallel computing."""
    def __init__(self, data, num_workers):
        self.data = data
        self.num_workers = num_workers

    def run(self):
        """Run the parallel processing."""
        return parallel_processing(self.data, self.num_workers)

if __name__ == "__main__":
    # Running custom parallel class example
    custom_data = np.random.randint(1, 100, 1000).tolist()
    custom_parallel = CustomParallel(custom_data, 4)
    custom_results = custom_parallel.run()
    print(f"Custom parallel results: {custom_results}")

    # Additional tasks can be executed as needed
    avg_result = additional_functionality(custom_results)
    print(f"Average Result of Custom Parallel Processing: {avg_result}")