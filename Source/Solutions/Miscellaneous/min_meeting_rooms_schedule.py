# Given n meetings with start and end times. 
# Return the minimum number of rooms required to schedule all meetings without conflict.

import heapq

def min_meeting_rooms_with_schedule(meetings):
    if not meetings:
        return 0, {}

    # Step 1: Sort by start time with indexing
    indexed_meetings = sorted(enumerate(meetings), key=lambda x: x[1][0])
    
    # indexed_meetings = list(enumerate(meetings))
    # indexed_meetings.sort(key=lambda x: x[1][0])
    # [(0, (0, 30)), (1, (5, 10)), (2, (15, 20))]
    
    # Heap of (end_time, room_id)
    heap = []
    
    # Room assignment and schedule
    room_id_counter = 0
    # meeting_to_room = {}
    room_schedule = {}

    for idx, (start, end) in indexed_meetings:
        if heap and heap[0][0] <= start: # if heap has at least one element and heap[0] =(0.5, "post A") and heap[0][0] = 0.5, the first heap element.
            # Reuse a room
            earliest_end, room_id = heapq.heappop(heap)
        else:
            # Need new room
            room_id = room_id_counter
            room_schedule[room_id] = []
            room_id_counter += 1

        # Assign meeting to the room
        heapq.heappush(heap, (end, room_id))
        # meeting_to_room[idx] = room_id
        room_schedule[room_id].append((start, end))

    return room_id_counter, room_schedule #, meeting_to_room

meetings = [(5, 10), (0, 30), (15, 20)]
rooms_required, schedule = min_meeting_rooms_with_schedule(meetings)

print("Rooms required:", rooms_required)
print("Schedule:")
for room, times in schedule.items():
    print(f"Room {room}: {times}")

meetings = [(15, 40), (5, 10), (0, 30), (0, 45), (35, 45)]
rooms_required, schedule = min_meeting_rooms_with_schedule(meetings)

print("Rooms required:", rooms_required)
print("Schedule:")
for room, times in schedule.items():
    print(f"Room {room}: {times}")