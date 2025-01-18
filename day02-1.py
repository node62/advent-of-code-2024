#!/usr/bin/env python3
print("Enter input:\n")
def is_safe_report(report):
    nums = list(map(int, report.split()))
    diff_list = [nums[i + 1] - nums[i] for i in range(len(nums) - 1)]

    if all(-3 <= diff <= -1 for diff in diff_list):
        return True
    if all(1 <= diff <= 3 for diff in diff_list):
        return True

    return False

reports_list = []
while True:
    try:
        line = input().strip()
        if line == "EOF":
            break
        reports_list.append(line)
    except EOFError:
        break

safe_count = 0
for report in reports_list:
    if is_safe_report(report):
        safe_count += 1

print(safe_count)