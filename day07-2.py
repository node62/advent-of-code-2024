import sys
from itertools import product

def main():
    total = 0
    for line in sys.stdin:
        line = line.strip()
        if line == 'EOF':
            break
        if not line:
            continue
        test_str, nums_str = line.split(': ')
        test_val = int(test_str)
        nums = list(map(int, nums_str.split()))
        if len(nums) == 1:
            if nums[0] == test_val:
                total += test_val
            continue
        num_ops = len(nums) - 1
        for ops in product(['+', '*', '||'], repeat=num_ops):
            current = nums[0]
            valid = True
            for i in range(num_ops):
                op = ops[i]
                next_num = nums[i+1]
                if op == '+':
                    current += next_num
                elif op == '*':
                    current *= next_num
                elif op == '||':
                    current = int(str(current) + str(next_num))
                else:
                    valid = False
                    break
            if valid and current == test_val:
                total += test_val
                break
    print(total)

if __name__ == "__main__":
    main()