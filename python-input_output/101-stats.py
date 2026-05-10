#!/usr/bin/python3
"""This modules is about files manipulation"""


import sys

def print_stats(occurrences, total_size):
    print(f"File size: {total_size}")
    for code in sorted(occurrences.keys()):
        if occurrences[code] > 0:
            print(f"{code}: {occurrences[code]}")

def run_stats():
    http_codes = ["200", "301", "400", "401", "403", "404", "405", "500"]
    occurrences = {k: 0 for k in http_codes}
    total_size = 0
    line_count = 0
    try:
        for line in sys.stdin:
            tokens = line.split()
            if len(tokens) > 1:
                try:
                    filesize = tokens[-1]
                    status_code = tokens[-2]
                    if status_code in occurrences.keys():
                        occurrences[status_code] += 1
                        total_size += int(filesize)
                        line_count += 1
                except (ValueError, IndexError):
                    continue
                if line_count % 10 == 0:
                    print_stats(occurrences, total_size)

    except KeyboardInterrupt:
        raise

    finally:
        print_stats(occurrences, total_size)

if __name__ == "__main__":
    run_stats()
