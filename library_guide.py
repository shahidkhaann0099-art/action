import os
import subprocess
import sys

def run_app():
    print("Launching the Library Management System GUI...")
    subprocess.run([sys.executable, "library_management_system.py"])

def run_tests():
    print("Running unit tests...")
    subprocess.run([sys.executable, "-m", "unittest", "discover", "-s", ".", "-p", "test_*.py"])

def main():
    while True:
        print("""\nLibrary Guide Menu
1. Run Library Management System (GUI)
2. Run Unit Tests
3. Exit""")
        choice = input("Enter your choice: ").strip()
        if choice == "1":
            run_app()
        elif choice == "2":
            run_tests()
        elif choice == "3":
            print("Exiting Library Guide.")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
