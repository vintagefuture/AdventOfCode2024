reports = []
safe_reports = []

def is_safe(report):
    max_iterations = len(report)-1
    increasing = report[1] > report[0]

    strike = False
    bad_index = 0

    for i in range(max_iterations):
        if not abs(report[i] - report[i+1]) in [1, 2, 3]:
            bad_index = i
            strike = True
            break

        if (report[i + 1] > report[i]) != increasing:
            bad_index = i
            strike = True
            break

    if strike:
        print(f'Initial report was {report}')
        fixed_report1 = [i for i in report]
        fixed_report1.pop(bad_index)
        print(f'Report is now {fixed_report1}')

        first_option_failed = False

        max_iterations = len(fixed_report1) - 1
        increasing = fixed_report1[1] > fixed_report1[0]
        for i in range(max_iterations):
            if not abs(fixed_report1[i] - fixed_report1[i+1]) in [1, 2, 3]:
                first_option_failed = True

            if (report[i + 1] > report[i]) != increasing:
                first_option_failed = True

        if first_option_failed:
            print(f'The first option failed, try second')
            fixed_report2 = [i for i in report]
            fixed_report2.pop(bad_index+1)
            print(f'New report is {fixed_report2}')

            increasing = fixed_report2[1] > fixed_report2[0]
            for i in range(max_iterations):
                if not abs(fixed_report2[i] - fixed_report2[i + 1]) in [1, 2, 3]:
                    return False

                if (report[i + 1] > report[i]) != increasing:
                    return False

    return True


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