import tkinter as tk
from tkinter import filedialog, messagebox
import hashlib

def choose_file():
    file_path = filedialog.askopenfilename()
    file_entry.delete(0, tk.END)
    file_entry.insert(0, file_path)

def hash_file(file_path, hash_type):
    hasher = hashlib.new(hash_type)
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hasher.update(chunk)
    return hasher.hexdigest()

def hash_button_click():
    file_path = file_entry.get()
    hash_type = hash_var.get()

    if not file_path:
        messagebox.showerror("Error", "Please choose a file.")
        return

    try:
        hash_value = hash_file(file_path, hash_type)
        messagebox.showinfo("Hash Result", f"The {hash_type} hash of the file is:\n{hash_value}")
        print(f"SHA-256 Hash: {hash_value}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Création de la fenêtre principale
root = tk.Tk()
root.title("File Hasher")
root.geometry("400x300")

# Entrée pour le fichier
file_label = tk.Label(root, text="File:")
file_label.pack(pady=5)
file_entry = tk.Entry(root, width=50)
file_entry.pack(pady=5)
file_button = tk.Button(root, text="Choose File", command=choose_file)
file_button.pack(pady=5)

# Sélection du type de hachage
hash_label = tk.Label(root, text="Hash Type:")
hash_label.pack(pady=5)
hash_var = tk.StringVar(value="md5")
hash_md5 = tk.Radiobutton(root, text="MD5", variable=hash_var, value="md5")
hash_md5.pack()
hash_sha1 = tk.Radiobutton(root, text="SHA-1", variable=hash_var, value="sha1")
hash_sha1.pack()
hash_sha256 = tk.Radiobutton(root, text="SHA-256", variable=hash_var, value="sha256")
hash_sha256.pack()

# Bouton pour hacher le fichier
hash_button = tk.Button(root, text="Hash File", command=hash_button_click)
hash_button.pack(pady=20)

# Lancer la boucle principale
root.mainloop() 