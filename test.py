import hashlib

def sha256_hash(filename):
    sha256 = hashlib.sha256()
    with open(filename, 'rb') as f:
        while chunk := f.read(8192):
            sha256.update(chunk)
    return sha256.hexdigest()

filename = 'example_file.txt'
print(f"SHA-256 Hash: {sha256_hash(filename)}")