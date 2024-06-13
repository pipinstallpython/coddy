def total_burning_time(c1, b1):
    total_time = 0
    current_candles = c1

    while current_candles > 0:
        total_time += 2 * current_candles # 6 

        new_candles = (current_candles // b1) * 2

        current_candles = new_candles

    return total_time


c1 = 5 
b1 = 3 

print(f"Общее время горения: {total_burning_time(c1, b1)} часов")
