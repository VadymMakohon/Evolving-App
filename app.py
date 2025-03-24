import tkinter as tk
from tkinter import messagebox

class SimpleApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Evolving App")
        self.root.geometry("350x250")
        self.root.resizable(False, False)

        self.label = tk.Label(root, text="Enter something:", font=("Arial", 12))
        self.label.pack(pady=5)

        self.entry = tk.Entry(root, font=("Arial", 12))
        self.entry.pack(pady=5)
        self.entry.bind("<KeyRelease>", self.update_character_count)  # Update count on key release

        self.counter_label = tk.Label(root, text="Character count: 0", font=("Arial", 10))
        self.counter_label.pack(pady=5)

        self.button_frame = tk.Frame(root)
        self.button_frame.pack(pady=10)

        self.submit_button = tk.Button(self.button_frame, text="Submit", command=self.on_submit, font=("Arial", 12))
        self.submit_button.grid(row=0, column=0, padx=5)

        self.clear_button = tk.Button(self.button_frame, text="Clear", command=self.on_clear, font=("Arial", 12))
        self.clear_button.grid(row=0, column=1, padx=5)

        self.exit_button = tk.Button(self.button_frame, text="Exit", command=self.on_exit, font=("Arial", 12), fg="red")
        self.exit_button.grid(row=0, column=2, padx=5)

    def on_submit(self):
        user_input = self.entry.get().strip()
        if user_input:
            messagebox.showinfo("Message", f"You entered: {user_input}")
            self.entry.delete(0, tk.END)
            self.update_character_count()
        else:
            messagebox.showwarning("Warning", "Please enter something!")

    def on_clear(self):
        self.entry.delete(0, tk.END)
        self.update_character_count()

    def on_exit(self):
        self.root.destroy()

    def update_character_count(self, event=None):
        count = len(self.entry.get())
        self.counter_label.config(text=f"Character count: {count}")

if __name__ == "__main__":
    root = tk.Tk()
    app = SimpleApp(root)
    root.mainloop()
