# Hash-Calculator

## Project Description 

A hash calculator is a tool used to generate hash values ​​from input data. These hash values ​​are fixed sequences of characters (usually in hexadecimal) that represent the unique digital fingerprint of the data.


This project aims to explain the principle of ransomware and I developed it as part of my studies, to learn how it works.

## Uses of a Hash Calculator :

- Data Integrity Checking: :lock:
- Secure Password Storage: :closed_lock_with_key:
- Digital Signature Generation: :black_nib:
- Data Deduplication: :card_index_dividers:
- Indexing and Fast Search: :clipboard:


## Screenshot 📸

![IHM](https://github.com/user-attachments/assets/ec299734-a341-41f0-a832-77021826d29c)

## Use

1. Clone the GitHub repository to your local machine <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/git/git-original.svg" height="15" alt="git logo" />:

    ```
    git clone https://github.com/Alexous-O/Hash-Calculatoir.git
    ```
    
2. Then launch the project
   - It's up to you to have fun

## Explanations

1. Importing modules:

```
import tkinter as tk
from tkinter import filedialog, messagebox
import hashlib
```

2. Utility functions:

**choose_file():** Opens a dialog box to choose a file and updates the text entry with the path of the selected file.

**hash_file(file_path, hash_type):** Reads the file in 4096-byte chunks, updates the hash, and returns the hashed value in hexadecimal.

**hash_button_click():** Retrieves the selected file path and hash type, and displays the hash result in a dialog box.

3. Creating the user interface:

- **file_label, file_entry**, file_button for file selection.
- **hash_label, hash_md5, hash_sha1**, hash_sha256 for hash type selection.
- **hash_button** to start the hash.


## Author 👨‍💻
The project was created by myself.
