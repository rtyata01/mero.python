# Given bridge size, max bridge weight and list of vehicle weights [unsorted positive integer]
    # A list of vehicle weights (weights), which are positive integers and not sorted.
    # A maximum bridge weight capacity (max_weight).
    # A bridge size (bridge_size), indicating the maximum number of vehicles the bridge can hold at once.

# Find the max vehicles, which can pass through bridge.
    # For max, if the new vehicle weight is smaller than the last in the bridge, then replace the last one with new vehicle.


from collections import deque

def find_weighted_vehicles(weights, max_weight, bridge_size=2):
    n = len(weights)
    results = []
    bridge_queue = deque()

    for i in range(n):
        # print(f"processing: {i}, queue: {bridge_queue}, results: {results}")
        
        # Check if current vehicle can be added
        if len(bridge_queue) < bridge_size:
            current_weight = weights[i]
            total_weight = sum(weights[idx] for idx in bridge_queue) + current_weight
            
            if total_weight <= max_weight:
                bridge_queue.append(i)
                
            if total_weight > max_weight and bridge_queue:
                previous_weight = weights[bridge_queue[-1]]
                # [note] this only checks the last vehicle in brige, but it should ideally check all vehicles in bridge. 
                if previous_weight > current_weight: 
                    bridge_queue.pop()
                    bridge_queue.append(i)
                
        # If bridge is full or we can't add the current vehicle, remove the oldest
        if len(bridge_queue) == bridge_size:
            results.append(weights[bridge_queue.popleft()])
            
    # Clear remaining vehicles on the bridge
    while bridge_queue:
        results.append(weights[bridge_queue.popleft()])

    return results

# Time complexity: O(n * bridge_size) = O(n) as bridge_size is constant = 2, 3.
# Space complexity: O(n) + O(bridge_size) = O(n) as bridge_size is constant = 2, 3.

# Test cases
test_cases = [
    (7, [7, 1, 2, 7, 6, 5, 2, 3, 4, 8], 2),
    (7, [7, 1, 2, 7, 6, 5, 2, 3, 4, 8], 3), 
    (6, [1, 8, 9, 6, 5, 2, 3, 4, 2], 2), 
    (6, [1, 8, 9, 6, 5, 2, 3, 4, 2], 3), 
]

for test_case in test_cases:
    max_weight, weights, bridge_size = test_case
    print(f"Input: {weights}, Max_weight={max_weight}, Bridge Capacity: {bridge_size}")
    results = find_weighted_vehicles(weights, max_weight, bridge_size)
    print(f"Results: {results}, count: {len(results)}")
                     

                     
             
                
            
        
        