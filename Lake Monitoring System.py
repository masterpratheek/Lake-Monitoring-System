import csv

CSV_FILE = "lakes.csv"

# ---------- Write Sample Data at Program Start ----------
def create_sample_data():
    sample_lakes = [
        ["Varthur Lake", "Bangalore, Karnataka", 7.2, 24.5, "Medium", "2025-08-01 10:30:00"],
        ["Bellandur Lake", "Bangalore, Karnataka", 6.8, 26.0, "High", "2025-08-02 09:15:00"],
        ["Ulsoor Lake", "Bangalore, Karnataka", 7.0, 22.8, "Low", "2025-08-03 14:45:00"],
        ["Hebbal Lake", "Bangalore, Karnataka", 7.5, 23.1, "Low", "2025-08-04 08:20:00"],
        ["Sankey Tank", "Bangalore, Karnataka", 6.9, 25.4, "Medium", "2025-08-05 16:00:00"],
        ["Agara Lake", "Bangalore, Karnataka", 7.1, 24.2, "Low", "2025-08-06 11:10:00"]
    ]
    with open(CSV_FILE, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(sample_lakes)

# ---------- AI Chatbot Data ----------
chatbot_responses = {
    "what is ph": "pH is a measure of how acidic or basic the water is. A pH of 7 is neutral.",
    "what is pollution level": "Pollution level describes the contamination of water. It can be Low, Medium, or High.",
    "ideal temperature": "For most freshwater lakes, the ideal temperature is between 20°C and 25°C.",
    "how to clean a lake": "Cleaning a lake involves removing pollutants, controlling waste disposal, and using aeration."
}

# ---------- View Lakes ----------
def view_lakes():
    with open(CSV_FILE, "r", newline="") as f:
        reader = csv.reader(f)
        lakes = list(reader)

    if not lakes:
        print("\n⚠ No lakes found.")
        return

    print("\n--- List of Lakes ---")
    for i, lake in enumerate(lakes, start=1):
        print(f"{i}. {lake[0]} ({lake[1]})")  # Lake name + location

    try:
        choice = int(input("\nEnter Lake Number to view details (0 to go back): "))
    except ValueError:
        print("⚠ Invalid input!")
        return

    if choice == 0:
        return

    if 1 <= choice <= len(lakes):
        lake = lakes[choice - 1]
        print(f"\nLake Name: {lake[0]}")
        print(f"Location: {lake[1]}")
        print(f"pH: {lake[2]}")
        print(f"Temperature: {lake[3]} °C")
        print(f"Pollution Level: {lake[4]}")
        print(f"Date & Time: {lake[5]}")
    else:
        print("⚠ No lake found with that number.")

# ---------- AI Chatbot ----------
def ai_chatbot():
    print("\n💬 AI Chatbot Activated! Type 'exit' to go back.")
    while True:
        query = input("You: ").lower()
        if query == "exit":
            break
        elif query in chatbot_responses:
            print("Bot:", chatbot_responses[query])
        else:
            print("Bot: Sorry, I don't have an answer for that.")

# ---------- Main Screen ----------
def main_screen():
    while True:
        print("\n====== Smart Lake Monitoring System ======")
        print("1. View Lakes")
        print("2. AI Chatbot")
        print("3. Back to Home Screen")
        choice = input("Enter your choice: ")

        if choice == "1":
            view_lakes()
        elif choice == "2":
            ai_chatbot()
        elif choice == "3":
            print("Returning to Home Screen...\n")
            break
        else:
            print("⚠ Invalid choice! Try again.")

# ---------- Program Start ----------
create_sample_data()  # Write sample data on startup
main_screen()