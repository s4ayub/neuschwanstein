def totalActiveTime(note):
    count = 1
    curr_time = note[0]["time"]
    total_active_time = 0

    for line in range(1, len(note)):
        if note[line]["type"] == "d": # a task ended
            count -= 1
        else: # a new task started
            count += 1
        
        if count == 0: 
            # don't increment count in here, the next loop will take care of it
            total_active_time += (note[line]["time"] - curr_time)

            if line < len(note) - 1:
                curr_time = note[line+1]["time"]
    
    return total_active_time

note = [
    {"type": "p", "time": 1},
    {"type": "p", "time": 2},
    {"type": "p", "time": 3},
    {"type": "d", "time": 4},
    {"type": "d", "time": 5},
    {"type": "d", "time": 5.5},
    {"type": "p", "time": 10},
    {"type": "d", "time": 11}
]

print(totalActiveTime(note))