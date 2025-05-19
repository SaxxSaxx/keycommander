# 🎹 KeyCommander

**KeyCommander** is a modern, cross-platform desktop tool that tracks and visualizes your keyboard usage in real time. It includes a heatmap, typing speed tracker, and export options — all built with Python and Tkinter.

---

## ✨ Features

- 📊 Real-time key usage heatmap
- ⚡ Typing speed chart (keys per minute)
- 💾 Export visuals as PNG or PDF
- 🔄 Reset and restart tracking anytime
- 🖥️ Beautiful, native GUI with `Tkinter`
- 🧠 Fully local — no data leaves your machine

---

## 📦 Installation

Clone the repo:

```bash
git clone https://github.com/yourusername/keycommander.git
cd keycommander
```

Install dependencies from `requirements.txt`:

```bash
pip install -r requirements.txt
```

> If `Tkinter` is missing:
> - On Linux: `sudo apt install python3-tk`
> - On Windows/macOS: included with Python

---

## 🚀 Usage

Run the tool:

```bash
python keycommander.py
```

Then:

1. Click **Start Logging**
2. Type anything
3. Press **ESC** to stop
4. View heatmap or typing speed
5. Optionally export charts to image/PDF

---

## 📁 File Structure

```
keycommander/
├── keycommander.py         # Main app
├── requirements.txt        # Dependencies
├── README.md               # Project info
├── keycommander_data.json  # Stored data (auto-created)
```

---

## 🔒 Privacy

KeyCommander runs fully offline. Your keyboard data is never sent anywhere.

---

## 📄 License

MIT License — free to use, modify, and distribute.

---

## 🙌 Credits

Made with ❤️ by [**@saxx**](https://github.com/saxxsaxx)
