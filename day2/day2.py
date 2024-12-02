reports = []
safe_reports = []

def is_safe(report):
    max_iterations = len(report) - 1
    increasing = report[1] > report[0]
    strikes = 0
    print(f'This is report {report}')
    for i in range(max_iterations):
        too_much_interval = False
        not_ordered = False
        if not abs(report[i] - report[i+1]) in [1, 2, 3]:
            too_much_interval = True

        if (report[i + 1] > report[i]) != increasing:
            not_ordered = True

        non_compliant = too_much_interval or not_ordered
        print(f'{report[i]} and {report[i+1]}: {non_compliant}')
        if non_compliant:
            strikes += 1
    print(strikes)
    if strikes < 2:
        print(f'This report is safe')
        return True
    else:
        print(f'This report is not safe')
        return False

def main():
    with open("input.txt") as f:
        for line in f:
            reports.append([int(x) for x in line.split()])

    for report in reports:
        if is_safe(report):
            safe_reports.append(report)

    print(f'Answer to A: {len(safe_reports)}')


if __name__ == '__main__':
    main()