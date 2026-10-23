import tkinter as tk
from tkinter import ttk, messagebox

class StationeryOrderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Stationery Order Management App")
        self.root.geometry("600x500")
        
        self.is_usd = True
        
        self.stationery_items = [
            {"name": "Notebook", "usd": 2.50, "inr": 200},
            {"name": "Gel Pen (Pack of 5)", "usd": 1.50, "inr": 120},
            {"name": "Graph Paper Pad", "usd": 3.00, "inr": 250},
            {"name": "Desk Organizer", "usd": 8.00, "inr": 650},
            {"name": "Highlighters (Set)", "usd": 4.00, "inr": 320}
        ]
        
        self.quantity_entries = {}
        
        self.canvas = tk.Canvas(root, width=600, height=500)
        self.canvas.pack(fill="both", expand=True)
        
        try:
            self.bg_image = tk.PhotoImage(file="background.png")
            self.canvas.create_image(0, 0, image=self.bg_image, anchor="nw")
        except tk.TclError:
            self.canvas.create_rectangle(0, 0, 600, 500, fill="#f0f4f8", width=0)
            self.canvas.create_text(300, 25, text="[Background Image Placeholder]", fill="#b0bec5")

        self.main_frame = tk.Frame(self.canvas, bg="#ffffff", bd=2, relief="groove")
        self.canvas.create_window(300, 250, window=self.main_frame, width=540, height=420)
        
        self.style = ttk.Style()
        self.style.theme_use("clam")
        
        title_label = ttk.Label(self.main_frame, text="Stationery Order Manager", font=("Arial", 16, "bold"))
        title_label.grid(row=0, column=0, columnspan=4, pady=15)
        
        self.currency_btn = ttk.Button(self.main_frame, text="Switch to INR (₹)", command=self.toggle_currency)
        self.currency_btn.grid(row=1, column=3, padx=10, pady=5, sticky="e")
        
        ttk.Label(self.main_frame, text="Item Name", font=("Arial", 10, "bold")).grid(row=2, column=0, padx=10, pady=5, sticky="w")
        ttk.Label(self.main_frame, text="Price", font=("Arial", 10, "bold")).grid(row=2, column=1, padx=10, pady=5, sticky="w")
        ttk.Label(self.main_frame, text="Quantity", font=("Arial", 10, "bold")).grid(row=2, column=2, padx=10, pady=5, sticky="w")
        
        self.price_labels = []
        for index, item in enumerate(self.stationery_items):
            grid_row = index + 3 
            
            name_lbl = ttk.Label(self.main_frame, text=item["name"], font=("Arial", 10))
            name_lbl.grid(row=grid_row, column=0, padx=10, pady=5, sticky="w")
            
            price_lbl = ttk.Label(self.main_frame, text="", font=("Arial", 10))
            price_lbl.grid(row=grid_row, column=1, padx=10, pady=5, sticky="w")
            self.price_labels.append(price_lbl)
            
            qty_entry = ttk.Entry(self.main_frame, width=8)
            qty_entry.insert(0, "0")  
            qty_entry.grid(row=grid_row, column=2, padx=10, pady=5, sticky="w")
            
            self.quantity_entries[item["name"]] = qty_entry
            
        self.update_price_display()
        
        btn_frame = tk.Frame(self.main_frame, bg="#ffffff")
        btn_frame.grid(row=9, column=0, columnspan=4, pady=20)
        
        calculate_btn = ttk.Button(btn_frame, text="Calculate Total", command=self.calculate_total)
        calculate_btn.pack(side="left", padx=10)
        
        self.total_label = ttk.Label(self.main_frame, text="Total Bill: $0.00", font=("Arial", 12, "bold"))
        self.total_label.grid(row=10, column=0, columnspan=4, pady=10)

    def update_price_display(self):
        for index, item in enumerate(self.stationery_items):
            price_text = f"${item['usd']:.2f}" if self.is_usd else f"₹{item['inr']:.2f}"
            self.price_labels[index].config(text=price_text)

    def toggle_currency(self):
        self.is_usd = not self.is_usd
        btn_text = "Switch to INR (₹)" if self.is_usd else "Switch to USD ($)"
        self.currency_btn.config(text=btn_text)
        self.update_price_display()
        self.calculate_total()

    def calculate_total(self):
        total = 0.0
        for item in self.stationery_items:
            qty_str = self.quantity_entries[item["name"]].get().strip()
            
            if not qty_str.isdigit():
                messagebox.showerror(
                    "Invalid Input", 
                    f"Please enter a valid positive integer quantity for '{item['name']}'."
                )
                return
            
            quantity = int(qty_str)
            item_price = item["usd"] if self.is_usd else item["inr"]
            total += item_price * quantity
            
        total_text = f"Total Bill: ${total:.2f}" if self.is_usd else f"Total Bill: ₹{total:.2f}"
        self.total_label.config(text=total_text)

if __name__ == "__main__":
    root = tk.Tk()
    app = StationeryOrderApp(root)
    root.mainloop()
