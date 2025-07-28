import tkinter as tk

class SimpleCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")
        self.root.geometry("350x500")
        self.root.configure(bg="#2c3e50")  # Dark theme background
        self.root.resizable(False, False)

        # Display (Entry widget)
        self.entry = tk.Entry(root, font=("Arial", 24), borderwidth=5, relief="ridge", justify="right", bg="#ecf0f1")
        self.entry.pack(pady=20, padx=10, fill="x")

        # Bind keyboard keys
        self.root.bind("<Return>", lambda e: self.on_button_click("="))
        self.root.bind("<Escape>", lambda e: self.on_button_click("C"))
        self.root.bind("<BackSpace>", lambda e: self.backspace())

        # Button frame
        btn_frame = tk.Frame(root, bg="#2c3e50")
        btn_frame.pack()

        self.create_buttons(btn_frame)

    def create_buttons(self, frame):
        """Creates calculator buttons with colors and layout."""
        buttons = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
            ("0", 4, 0), (".", 4, 1), ("C", 4, 2), ("+", 4, 3),
            ("=", 5, 0, 4)  # Spans across 4 columns
        ]

        for (text, row, col, *span) in buttons:
            btn = tk.Button(
                frame, text=text, font=("Arial", 18, "bold"),
                width=5, height=2, relief="raised", bg="#34495e", fg="white",
                activebackground="#1abc9c", activeforeground="black",
                command=lambda t=text: self.on_button_click(t)
            )
            if text == "=":
                btn.grid(row=row, column=col, columnspan=span[0], sticky="nsew", padx=3, pady=3)
            else:
                btn.grid(row=row, column=col, padx=3, pady=3)

        # Make columns expand equally
        for i in range(4):
            frame.grid_columnconfigure(i, weight=1)

    def backspace(self):
        """Deletes last character in entry."""
        current = self.entry.get()
        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, current[:-1])

    def on_button_click(self, char):
        """Handles calculator logic."""
        if char == "C":
            self.entry.delete(0, tk.END)
        elif char == "=":
            try:
                expression = self.entry.get()
                result = eval(expression)
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
            except Exception:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")
        else:
            self.entry.insert(tk.END, char)

if __name__ == "__main__":
    root = tk.Tk()
    app = SimpleCalculator(root)
    root.mainloop()
