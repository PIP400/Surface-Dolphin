import sys, os, platform, threading, time, requests, webbrowser
import tkinter as tk
from tkinter import ttk, messagebox

# --- UNIVERSAL PC FIX: STDN / CONSOLE REDIRECTION ---
if sys.executable.endswith("pythonw.exe") or getattr(sys, 'frozen', False):
    sys.stdout = open(os.devnull, "w")
    sys.stderr = open(os.devnull, "w")

# --- PROFESSIONAL HARDWARE LIBRARIES ---
import psutil
import wmi
import pythoncom 

class SurfingDolphinPro:
    def __init__(self, root):
        self.root = root
        self.root.title("Surfing Dolphin PE v5.1.0 Dev. REZ360")
        self.root.geometry("900x980")
        self.root.configure(bg="#050505")
        
        self.setup_style()
        self.create_widgets()
        self.update_live_data()

    def setup_style(self):
        style = ttk.Style()
        style.theme_use('clam')
        style.configure("TFrame", background="#050505")
        style.configure("TLabelframe", background="#111111", foreground="#00ffcc")
        style.configure("TLabelframe.Label", background="#111111", foreground="#00ffcc", font=("Arial", 11, "bold"))
        style.configure("TLabel", background="#111111", foreground="#ffffff", font=("Consolas", 9))
        style.configure("Live.TLabel", background="#111111", foreground="#00ffcc", font=("Consolas", 10, "bold"))
        style.configure("Buy.TLabel", background="#111111", foreground="#ffcc00", font=("Consolas", 10, "bold"))
        style.configure("Horizontal.TProgressbar", thickness=15, troughcolor='#222', background='#00ffcc')

    def open_link(self, url):
        webbrowser.open_new(url)

    def create_widgets(self):
        # --- HEADER ---
        header = tk.Frame(self.root, bg="#111", height=70)
        header.pack(side="top", fill="x")
        ttk.Label(header, text="🐬 IDENTITY & LIVE ADVISOR", font=("Arial", 14, "bold")).pack(side="left", padx=20, pady=20)
        ttk.Button(header, text="🔍 RUN DEEP AUDIT", command=self.start_audit_thread).pack(side="right", padx=20)

        # --- BOTTOM FOOTER (ROOT STYLE) ---
        footer = tk.Frame(self.root, bg="#111", height=30)
        footer.pack(side="bottom", fill="x")
        
        # Simple Footer Text
        tk.Label(footer, text="Dev. REZ360 |", bg="#111", fg="#666", font=("Arial", 8)).pack(side="left", padx=(20, 5), pady=5)
        
        # Patreon Link
        p_lnk = tk.Label(footer, text="Patreon", bg="#111", fg="#00ffcc", font=("Arial", 8, "bold"), cursor="hand2")
        p_lnk.pack(side="left", pady=5)
        p_lnk.bind("<Button-1>", lambda e: self.open_link("https://www.patreon.com/your_link"))

        tk.Label(footer, text="|", bg="#111", fg="#666", font=("Arial", 8)).pack(side="left", padx=5)

        # Github Link
        g_lnk = tk.Label(footer, text="GitHub", bg="#111", fg="#00ffcc", font=("Arial", 8, "bold"), cursor="hand2")
        g_lnk.pack(side="left", pady=5)
        g_lnk.bind("<Button-1>", lambda e: self.open_link("https://github.com/REZ368"))

        tk.Label(footer, text="|", bg="#111", fg="#666", font=("Arial", 8)).pack(side="left", padx=5)

        # Github Link
        g_lnk = tk.Label(footer, text="Portfolio", bg="#111", fg="#00ffcc", font=("Arial", 8, "bold"), cursor="hand2")
        g_lnk.pack(side="left", pady=5)
        g_lnk.bind("<Button-1>", lambda e: self.open_link("https://drive.google.com/drive/folders/1Wc7hAKtkbaZ7miG00uqkYFgN5SGxCKnP?usp=sharing"))

        # --- MAIN CANVAS & BODY ---
        self.canvas = tk.Canvas(self.root, bg="#050505", highlightthickness=0)
        scroll = ttk.Scrollbar(self.root, orient="vertical", command=self.canvas.yview)
        self.f = ttk.Frame(self.canvas)
        
        self.f.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
        self.canvas.create_window((0, 0), window=self.f, anchor="nw")
        self.canvas.configure(yscrollcommand=scroll.set)
        self.canvas.pack(side="left", fill="both", expand=True)
        scroll.pack(side="right", fill="y")
        self.canvas.bind_all("<MouseWheel>", lambda e: self.canvas.yview_scroll(int(-1*(e.delta/120)), "units"))

        self.sections = ["Processor (CPU)", "Memory (RAM)", "Storage (SSD/HDD)", "Graphics (GPU)", "Motherboard & BIOS"]
        self.ui = {}

        for name in self.sections:
            frame = ttk.LabelFrame(self.f, text=f" {name} ")
            frame.pack(fill="x", pady=10, padx=25)
            lbl = ttk.Label(frame, text="Identifying brands...", justify="left", wraplength=800)
            lbl.pack(anchor="w", padx=15, pady=10)
            live_lbl = ttk.Label(frame, text="Live Load: --%", style="Live.TLabel")
            live_lbl.pack(anchor="w", padx=15, pady=2)
            buy_lbl = ttk.Label(frame, text="", style="Buy.TLabel", wraplength=800)
            buy_lbl.pack(anchor="w", padx=15, pady=5)
            bar = ttk.Progressbar(frame, length=750, mode="determinate", style="Horizontal.TProgressbar")
            bar.pack(pady=10, padx=15)
            self.ui[name] = {"static": lbl, "live": live_lbl, "buy": buy_lbl, "bar": bar}

    def update_live_data(self):
        try:
            # CPU LIVE
            cpu_load = psutil.cpu_percent()
            self.ui["Processor (CPU)"]["live"].config(text=f"LIVE LOAD: {cpu_load}%")
            self.ui["Processor (CPU)"]["bar"]['value'] = cpu_load

            # RAM LIVE
            mem = psutil.virtual_memory()
            self.ui["Memory (RAM)"]["live"].config(text=f"LIVE USAGE: {mem.percent}% ({round(mem.used/1e9,2)}GB Used)")
            self.ui["Memory (RAM)"]["bar"]['value'] = mem.percent

            # STORAGE LIVE
            stg = psutil.disk_usage('/')
            self.ui["Storage (SSD/HDD)"]["live"].config(text=f"DISK FILLED: {stg.percent}%")
            self.ui["Storage (SSD/HDD)"]["bar"]['value'] = stg.percent

            # GPU LIVE (Status)
            self.ui["Graphics (GPU)"]["live"].config(text="GPU STATUS: ACTIVE")
            
            # MOTHERBOARD LIVE (Uptime)
            uptime = int((time.time() - psutil.boot_time()) // 3600)
            self.ui["Motherboard & BIOS"]["live"].config(text=f"SYSTEM UPTIME: {uptime} Hours")
            self.ui["Motherboard & BIOS"]["bar"]['value'] = min(uptime, 100)

        except: pass
        self.root.after(2000, self.update_live_data)

    def start_audit_thread(self):
        threading.Thread(target=self._deep_audit_worker, daemon=True).start()

    def _deep_audit_worker(self):
        pythoncom.CoInitialize() 
        try:
            local_wmi = wmi.WMI()

            # --- CPU ---
            cpu = local_wmi.Win32_Processor()[0]
            self.ui["Processor (CPU)"]["static"].config(text=f"NAME: {cpu.Name}\nBRAND: {cpu.Manufacturer}\nSOCKET: {cpu.SocketDesignation}")
            self.ui["Processor (CPU)"]["buy"].config(text=f"ADVICE: Your socket is {cpu.SocketDesignation}. Look for high core counts in this socket.")

            # --- RAM ---
            ram_list = local_wmi.Win32_PhysicalMemory()
            ram_full_report = ""
            total_gb = 0
            speed = 0
            for i, m in enumerate(ram_list):
                brand = m.Manufacturer.strip() if m.Manufacturer else ""
                if not brand or brand.startswith("00") or "Unknown" in brand:
                    brand = m.Caption.strip()
                if not brand or "Physical Memory" in brand:
                    brand = "Generic/OEM"
                
                cap = int(m.Capacity)//1073741824
                total_gb += cap
                speed = m.Speed
                ram_full_report += f"SLOT {i} | BRAND: {brand} | PN: {m.PartNumber.strip()}\nSPECS: {cap}GB @ {m.Speed}MHz\n"
                ram_full_report += "-"*30 + "\n"

            self.ui["Memory (RAM)"]["static"].config(text=ram_full_report)
            advice = f"ADVICE: You have {total_gb}GB total. Buy another {speed}MHz stick to upgrade."
            if total_gb < 16: advice += " 16GB is the 2026 sweet spot."
            self.ui["Memory (RAM)"]["buy"].config(text=advice)

            # --- STORAGE ---
            disk_text = ""
            for d in local_wmi.Win32_DiskDrive():
                disk_text += f"DRIVE: {d.Caption}\nMODEL: {d.Model}\nINTERFACE: {d.InterfaceType}\n"
                disk_text += "-"*30 + "\n"
            self.ui["Storage (SSD/HDD)"]["static"].config(text=disk_text)
            self.ui["Storage (SSD/HDD)"]["buy"].config(text="ADVICE: Upgrade to NVMe if your interface is SATA for 10x speed.")

            # --- GPU ---
            gpu = local_wmi.Win32_VideoController()[0]
            vram = int(gpu.AdapterRAM)//1048576 if gpu.AdapterRAM else 0
            self.ui["Graphics (GPU)"]["static"].config(text=f"GPU: {gpu.Caption}\nVRAM: {vram}MB")
            self.ui["Graphics (GPU)"]["buy"].config(text="ADVICE: If VRAM is below 8000MB, consider an upgrade for modern games.")

            # --- MOTHERBOARD ---
            board = local_wmi.Win32_BaseBoard()[0]
            self.ui["Motherboard & BIOS"]["static"].config(text=f"BRAND: {board.Manufacturer}\nPRODUCT: {board.Product}")
            self.ui["Motherboard & BIOS"]["buy"].config(text=f"ADVICE: Check {board.Manufacturer} website for the latest BIOS.")

        except Exception as e:
            pass 
        finally:
            pythoncom.CoUninitialize()

if __name__ == "__main__":
    root = tk.Tk()
    app = SurfingDolphinPro(root)
    root.mainloop()