import re
from collections import defaultdict

def analyze_log(file_path):
    error_count = 0
    warning_count = 0
    info_count = 0
    ip_counter = defaultdict(int)

    try:
        with open(file_path, 'r') as file:
            for line in file:
                # Count log levels
                if "ERROR" in line:
                    error_count += 1
                elif "WARNING" in line:
                    warning_count += 1
                elif "INFO" in line:
                    info_count += 1

                # Extract IP addresses
                ip_match = re.search(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b', line)
                if ip_match:
                    ip_counter[ip_match.group()] += 1

        print("\n=== Log Analysis Report ===")
        print(f"Errors   : {error_count}")
        print(f"Warnings : {warning_count}")
        print(f"Info     : {info_count}")

        print("\nTop IP Addresses:")
        for ip, count in sorted(ip_counter.items(), key=lambda x: x[1], reverse=True)[:5]:
            print(f"{ip} → {count} requests")

    except FileNotFoundError:
        print("Log file not found!")

def main():
    print("=== Smart Log Analyzer ===")
    path = input("Enter log file path: ")
    analyze_log(path)

if __name__ == "__main__":
    main()