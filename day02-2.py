#!/usr/bin/env python3
print("Enter input:")
def is_safe_report(report):
    nums = list(map(int, report.split()))
    diff_list = [nums[i + 1] - nums[i] for i in range(len(nums) - 1)]

    if all(-3 <= diff <= -1 for diff in diff_list):
        return True
    if all(1 <= diff <= 3 for diff in diff_list):
        return True

    return False

def is_safe_with_dampener(report):
    nums = list(map(int, report.split()))
    for i in range(len(nums)):
        modified_nums = nums[:i] + nums[i+1:]
        diff_list = [modified_nums[j + 1] - modified_nums[j] for j in range(len(modified_nums) - 1)]

        if all(-3 <= diff <= -1 for diff in diff_list):
            return True
        if all(1 <= diff <= 3 for diff in diff_list):
            return True

    return is_safe_report(report)

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
    if is_safe_with_dampener(report):
        safe_count += 1

print(safe_count)
