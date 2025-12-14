# Imports für tkinter und die AppGUI Klasse
import tkinter as tk
from gui import AppGUI
from models import Task


# Erstellung des Hauptfensters(root) und Konfiguration der Grundeinstellungen
root = tk.Tk()
root.title("Pyticker - Every second counts")
root.geometry("600x400")  # Pixeldimensionen
root.config(bg="#000000")  # Hintergrundfarbe

# Instanziierung der AppGUI-Klasse und Übergabe an das Root-Fenster
app = AppGUI(root)


# Start der Haupt-Ereignisschleife von Tkinter
root.mainloop()
