import os

def start_menu():
    print("--- HELMET DETECTION SYSTEM ---")
    print("1. Run Live Webcam Detection")
    print("2. Run Traffic Video Test")
    print("3. Exit")
    
    choice = input("Select an option (1-3): ")

    if choice == '1':
        print("Starting Webcam...")
        os.system("python webcam_test1.py") # Calls your webcam file
    elif choice == '2':
        print("Starting Video Test...")
        os.system("python trafficVideo_test.py") # Calls your video file
    elif choice == '3':
        print("Exiting...")
    else:
        print("Invalid choice, try again.")
        start_menu()

if __name__ == "__main__":
    start_menu()