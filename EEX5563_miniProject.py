class BestFitMemoryAllocator:
    def __init__(self, memory_blocks):
        """
        Initialize the allocator with a list of memory blocks.
        :param memory_blocks: List of integers representing memory block sizes.
        """
        self.memory_blocks = [(size, True) for size in memory_blocks]  # True indicates the block is free

    def allocate_request(self, process_no, request):
        """
        Allocate memory for a given request using the Best Fit algorithm.
        :here the (param) process_no: The process number requesting memory.
        :(param)request: Size of memory requested.
        :return: Allocation result (block number or -1 if failed).
        """
        best_index = -1 "best_index tracks the index of the best-suited memory block. Initialized to -1 (indicating no suitable block found yet)."
        
        for i, (block_size, is_free) in enumerate(self.memory_blocks):
            "Iterates over all memory blocks using enumerate():i:
            "Current index of the block.block_size: Size of the memory block.is_free: Boolean indicating if the block is free.
            
            if is_free and block_size >= request:"Checks if the block is free (is_free) and can accommodate the requested size (block_size >= request).
            
                if best_index == -1 or self.memory_blocks[best_index][0] > block_size:
                    best_index = i "Updates best_index:If no suitable block is found yet (best_index == -1), or
                    "If the current block is smaller than the previously chosen best block (self.memory_blocks[best_index][0] > block_size).

        if best_index != -1:
            remaining_size = self.memory_blocks[best_index][0] - request
            self.memory_blocks[best_index] = (remaining_size, False if remaining_size == 0 else True)
            return best_index + 1  # Return block number (1-indexed)
        "If a suitable block is found:Calculate remaining_size (block size after allocation).
        "Update the block's tuple:Set the new size to remaining_size.
        "Mark the block as not free (False) if remaining_size == 0; otherwise, it remains free.
        "Return the block number (1-indexed for user clarity).
        
        else:
            return -1 "If no block is found, return -1 to indicate allocation failure.

    def display_allocation(self, processes):
        """
        Display the allocation of processes in a tabular format.
        :param processes: List of tuples with process number and size.
        """
        print("\n================ Memory Allocation =================") 

        print(f"{'Process No.':<15}{'Process Size':<15}{'Block No.':<10}") "Prints a formatted header for the memory allocation table:Process No., Process Size, and Block No.

        for process_no, size in processes:
            block_no = self.allocate_request(process_no, size)
            print(f"{process_no:<15}{size:<15}{(block_no if block_no != -1 else 'Not Allocated'):<10}")
            "Calls allocate_request() to allocate memory for the process.
            "Prints the results:
            "If allocated: Displays the block number.
            "If not allocated: Displays "Not Allocated".

    def display_memory_status(self):
        """
        Displays the remaining size and status of each memory block after allocation.

        """
        print("\nMemory Blocks Status:")
        for i, (size, is_free) in enumerate(self.memory_blocks):
            status = "Free" if is_free else "Allocated"
            print(f"Block {i + 1}: Size = {size}, Status = {status}")
            "Loops through all memory blocks:
            "size: Remaining size of the block.
            "is_free: Status of the block (Free or Allocated).
            "Prints the status of each block.

# Example usage
if __name__ == "__main__":
    # Initialize memory blocks
    memory_blocks = [200, 300, 400, 100, 150]
    allocator = BestFitMemoryAllocator(memory_blocks)
    "Creates an instance of BestFitMemoryAllocator with predefined block sizes: [200, 300, 400, 100, 150].
    
    # Define processes with their sizes
    processes = [(1, 120), (2, 250), (3, 50)]  # (Process No., Process Size)

    # Display allocation results
    allocator.display_allocation(processes)
    "Calls display_allocation() to print the allocation results for each process.

    # Display final memory status
    print("\nFinal Memory State:")
    allocator.display_memory_status()
    
    "for an extra information
    "pocess 1: Allocated to Block 5 (120 fits in 150; remaining size is 30).
    "Process 2: Allocated to Block 2 (250 fits exactly; no remaining space).
    "Process 3: Allocated to Block 2 (reallocated because Block 2 is now full).
