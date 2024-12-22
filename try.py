import tkinter as tk
from tkinter import font

# Function to calculate relationship percentage
def calculate_relationship():
    name1 = entry_name1.get().upper()  # Get Name1 input
    name2 = entry_name2.get().upper()  # Get Name2 input
    relation = entry_relation.get().upper()  # Get Relation input

    # Combine all inputs
    total = name1 + name2 + relation

    # Create a frequency map
    hashmap = {}
    for i in total:
        if i in hashmap:
            hashmap[i] += 1
        else:
            hashmap[i] = 1

    # Convert frequency map values into an array
    arr = list(hashmap.values())

    # Reduce the array until only 2 elements remain
    while len(arr) > 2:
        n = len(arr) // 2  
        for i in range(n):
            arr[i] = arr[i] + arr[-1]  
            arr.pop(-1)  

    # Final number calculation
    final_number = int("".join(map(str, arr)))
    
    # Display the result in the label
    label_result.config(text=f"Relationship: {final_number}%", fg="#3498db")

# Set up the Tkinter window
root = tk.Tk()
root.title("Relationship Calculator")

# Set window size and background color
root.geometry("400x350")
root.config(bg="#ecf0f1")

# Create a custom font for labels and buttons
custom_font = font.Font(family="Arial", size=12, weight="bold")

# Create and place labels and entry widgets for inputs
label_name1 = tk.Label(root, text="Enter Name1:", font=custom_font, bg="#ecf0f1", fg="#2c3e50")
label_name1.pack(pady=(30, 5))  # Added padding for spacing

entry_name1 = tk.Entry(root, font=custom_font, bd=2, relief="solid", width=25)
entry_name1.pack(pady=5, ipadx=10, ipady=5)

label_name2 = tk.Label(root, text="Enter Name2:", font=custom_font, bg="#ecf0f1", fg="#2c3e50")
label_name2.pack(pady=5)

entry_name2 = tk.Entry(root, font=custom_font, bd=2, relief="solid", width=25)
entry_name2.pack(pady=5, ipadx=10, ipady=5)

label_relation = tk.Label(root, text="Enter Relation:", font=custom_font, bg="#ecf0f1", fg="#2c3e50")
label_relation.pack(pady=5)

entry_relation = tk.Entry(root, font=custom_font, bd=2, relief="solid", width=25)
entry_relation.pack(pady=5, ipadx=10, ipady=5)

# Create a button to trigger the calculation
button_calculate = tk.Button(root, text="Calculate Relationship", font=custom_font, bg="#2ecc71", fg="white", command=calculate_relationship, bd=0, relief="raised")
button_calculate.pack(pady=20)

# Create a label to display the result
label_result = tk.Label(root, text="Relationship: ", font=custom_font, bg="#ecf0f1", fg="#2c3e50")
label_result.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()
