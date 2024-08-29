#!/usr/bin/python3
"""Log parsing script for processing stdin and computing metrics."""

import sys
import re
from collections import defaultdict


def print_stats(total_size, status_codes):
    """Print current statistics for file size and status codes."""
    print(f"File size: {total_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")


def main():
    """Process log entries and compute statistics."""
    total_size = 0
    status_codes = defaultdict(int)
    line_count = 0
    pattern = (
        r'^(\d+\.\d+\.\d+\.\d+) - \[(.*?)\] '
        r'"GET /projects/260 HTTP/1.1" (\d+) (\d+)$'
    )

    try:
        for line in sys.stdin:
            line = line.strip()
            match = re.match(pattern, line)
            if match:
                status_code = int(match.group(3))
                file_size = int(match.group(4))

                total_size += file_size

                if status_code in [200, 301, 400, 401, 403, 404, 405, 500]:
                    status_codes[status_code] += 1

                line_count += 1

                if line_count % 10 == 0:
                    print_stats(total_size, status_codes)

    except KeyboardInterrupt:
        print_stats(total_size, status_codes)
        sys.exit(0)


if __name__ == "__main__":
    main()
