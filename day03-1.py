import re

def main():
    print("Enter input: ")
    input_lines = []
    while True:
        line = input()
        if line.strip() == "EOF":
            break
        input_lines.append(line)
    input_data = "\n".join(input_lines)
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    matches = re.findall(pattern, input_data)
    total_sum = 0
    for match in matches:
        x, y = map(int, match)
        total_sum += x * y
    print(total_sum)

if __name__ == "__main__":
    main()