import tkinter as tk
from tkinter import ttk

class GoldPriceConverter:
    # Conversion constants
    GRAMS_PER_OUNCE = 31.1035
    
    def __init__(self, root):
        self.root = root
        self.root.title("黄金价格转换工具")
        self.root.geometry("400x250")
        
        # Exchange rate (you can update this)
        self.exchange_rate = 7.0  # 1 USD = 7 CNY (example)
        
        # USD/oz input
        ttk.Label(root, text="美元/盎司 (USD/oz):").grid(row=0, column=0, padx=10, pady=10)
        self.usd_oz_var = tk.DoubleVar()
        self.usd_oz_entry = ttk.Entry(root, textvariable=self.usd_oz_var, width=20)
        self.usd_oz_entry.grid(row=0, column=1, padx=10, pady=10)
        self.usd_oz_entry.bind("<KeyRelease>", self.convert_from_usd_oz)
        
        # CNY/gram input
        ttk.Label(root, text="人民币/克 (CNY/g):").grid(row=1, column=0, padx=10, pady=10)
        self.cny_gram_var = tk.DoubleVar()
        self.cny_gram_entry = ttk.Entry(root, textvariable=self.cny_gram_var, width=20)
        self.cny_gram_entry.grid(row=1, column=1, padx=10, pady=10)
        self.cny_gram_entry.bind("<KeyRelease>", self.convert_from_cny_gram)
        
        # Exchange rate setting
        ttk.Label(root, text="汇率 (1 USD = ? CNY):").grid(row=2, column=0, padx=10, pady=10)
        self.rate_var = tk.DoubleVar(value=self.exchange_rate)
        self.rate_entry = ttk.Entry(root, textvariable=self.rate_var, width=20)
        self.rate_entry.grid(row=2, column=1, padx=10, pady=10)
        self.rate_entry.bind("<KeyRelease>", self.update_exchange_rate)
        
        # Result display
        ttk.Label(root, text="转换结果:", font=("Arial", 10, "bold")).grid(row=3, column=0, columnspan=2, pady=10)
        self.result_var = tk.StringVar(value="输入数值即可转换")
        ttk.Label(root, textvariable=self.result_var, foreground="blue").grid(row=4, column=0, columnspan=2, pady=5)
    
    def update_exchange_rate(self, event=None):
        try:
            self.exchange_rate = self.rate_var.get()
        except:
            pass
    
    def convert_from_usd_oz(self, event=None):
        try:
            usd_oz = self.usd_oz_var.get()
            cny_gram = (usd_oz * self.exchange_rate) / self.GRAMS_PER_OUNCE
            self.cny_gram_var.set(round(cny_gram, 2))
            self.result_var.set(f"${usd_oz}/oz = ¥{cny_gram:.2f}/克")
        except:
            pass
    
    def convert_from_cny_gram(self, event=None):
        try:
            cny_gram = self.cny_gram_var.get()
            usd_oz = (cny_gram * self.GRAMS_PER_OUNCE) / self.exchange_rate
            self.usd_oz_var.set(round(usd_oz, 2))
            self.result_var.set(f"¥{cny_gram}/克 = ${usd_oz:.2f}/oz")
        except:
            pass

if __name__ == "__main__":
    root = tk.Tk()
    app = GoldPriceConverter(root)
    root.mainloop()