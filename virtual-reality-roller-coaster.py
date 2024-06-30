import tkinter as tk
import random

tracks = [
    "Loop-de-loop",
    "Corkscrew",
    "Drop Tower",
    "Twisty Turns",
    "High Speed",
    "Tunnel of Darkness",
    "Upside Down",
    "Wild Rapids",
    "Mountain Climb",
    "treking",
    "boating",
    "Sky Dive"
]

def generate_track():
    track = random.choice(tracks)
    track_label.config(text=f"Current Track: {track}")
    

root = tk.Tk()
root.title("Virtual Reality Roller Coaster Simulator")
root.geometry("400x200")

track_label = tk.Label(root, text="", font=("Helvetica", 16))
track_label.pack(pady=20)

generate_button = tk.Button(root, text="Generate Track", command=generate_track)
generate_button.pack(pady=20)


root.mainloop()
