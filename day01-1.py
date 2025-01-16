#!/usr/bin/env python3
import sys

def main():
    left_list = []
    right_list = []
    
    for line in sys.stdin:
        if line.strip() == "EOF":
            break
        if not line.strip():
            continue
        columns = line.strip().split()
        if len(columns) != 2:
            continue
        left_val = int(columns[0])
        right_val = int(columns[1])
        left_list.append(left_val)
        right_list.append(right_val)
    
    left_list.sort()
    right_list.sort()
    total_distance = 0
    for i in range(len(left_list)):
        total_distance += abs(left_list[i] - right_list[i])
    
    print(total_distance)

if __name__ == "__main__":
    main()
