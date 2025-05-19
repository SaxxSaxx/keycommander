#!/usr/bin/env python3

import time
from collections import defaultdict, deque
from datetime import datetime
import threading
import json
import os
import sys
import subprocess
from typing import Dict, List, Deque, Tuple
import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
from pynput import keyboard

class KeyCommanderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("KeyCommander - Keyboard Visualizer")
        self.root.geometry("800x600")
        self.root.resizable(False, False)

        self.key_data = defaultdict(int)
        self.build_ui()

    def build_ui(self):
        style = ttk.Style()
        style.configure("TButton", padding=6, font=("Segoe UI", 10))

        self.frame = ttk.Frame(self.root, padding=20)
        self.frame.pack(fill=tk.BOTH, expand=True)

        ttk.Label(self.frame, text="KeyCommander", font=("Segoe UI", 18, "bold")).pack(pady=10)

        button_frame = ttk.Frame(self.frame)
        button_frame.pack(pady=10)

        ttk.Button(button_frame, text="Start Logging", command=self.start_logging).grid(row=0, column=0, padx=5)
        ttk.Button(button_frame, text="Show Heatmap", command=self.show_heatmap).grid(row=0, column=1, padx=5)
        ttk.Button(button_frame, text="Stop", command=self.stop_logging).grid(row=0, column=2, padx=5)

        self.status_label = ttk.Label(self.frame, text="Status: Ready", font=("Segoe UI", 10))
        self.status_label.pack(pady=10)

        self.canvas_frame = ttk.Frame(self.frame)
        self.canvas_frame.pack(fill=tk.BOTH, expand=True)

        self.credit = ttk.Label(self.root, text="Made with ❤️ by saxx", font=("Segoe UI", 8))
        self.credit.pack(side=tk.BOTTOM, pady=5)

    def start_logging(self):
        self.status_label.config(text="Status: Logging started. Press ESC to stop.")
        self.listener = keyboard.Listener(on_press=self.on_press, on_release=self.on_release)
        self.listener.start()

    def stop_logging(self):
        self.status_label.config(text="Status: Logging stopped.")
        if hasattr(self, 'listener'):
            self.listener.stop()

    def on_press(self, key):
        try:
            k = key.char
        except:
            k = str(key)
        self.key_data[k] += 1

    def on_release(self, key):
        if key == keyboard.Key.esc:
            self.stop_logging()
            return False

    def show_heatmap(self):
        if not self.key_data:
            messagebox.showwarning("No Data", "No key data to visualize.")
            return

        for widget in self.canvas_frame.winfo_children():
            widget.destroy()

        fig, ax = plt.subplots(figsize=(10, 4))
        keys = list(self.key_data.keys())
        values = list(self.key_data.values())
        ax.bar(keys, values)
        ax.set_title("Key Usage Heatmap")
        ax.set_ylabel("Count")
        ax.set_xticklabels(keys, rotation=90)
        fig.tight_layout()

        canvas = FigureCanvasTkAgg(fig, master=self.canvas_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

if __name__ == "__main__":
    root = tk.Tk()
    app = KeyCommanderApp(root)
    root.mainloop()
