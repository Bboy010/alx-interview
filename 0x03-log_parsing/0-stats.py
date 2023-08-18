#!/usr/bin/env python3
"""
Log parsing interview
"""
import sys
import signal

class MetricsCalculator:
    def __init__(self):
        """ Initialize metric"""
        self.total_size = 0
        self.status_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
        self.line_count = 0

    def handle_line(self, line):
        """Handle line"""
        parts = line.split()
        if len(parts) != 10:
            return False

        try:
            status_code = int(parts[8])
            file_size = int(parts[9])
        except ValueError:
            return False

        self.total_size += file_size
        if status_code in self.status_counts:
            self.status_counts[status_code] += 1

        self.line_count += 1
        return True

    def print_metrics(self):
        """ Function to print metric """
        print(f"File size: {self.total_size}")
        for status_code in sorted(self.status_counts.keys()):
            if self.status_counts[status_code] > 0:
                print(f"{status_code}: {self.status_counts[status_code]}")
        print()  # Print an empty line after each set of metrics

def main():
    """ Check """
    calculator = MetricsCalculator()
    try:
        for line in sys.stdin:
            if calculator.handle_line(line):
                if calculator.line_count % 10 == 0:
                    calculator.print_metrics()
    except KeyboardInterrupt:
        calculator.print_metrics()

if __name__ == "__main__":
    main()
