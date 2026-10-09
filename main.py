"""File deduplication utility: find duplicate files in a directory."""
import os, sys, hashlib, argparse

def hash_file(path, chunk_size=65536):
    h=hashlib.sha256()
    with open(path,'rb') as f:
        for chunk in iter(lambda: f.read(chunk_size), b''):
            h.update(chunk)
    return h.hexdigest()

def find_duplicates(root):
    hashes={}
    for dirpath, _, files in os.walk(root):
        for name in files:
            path=os.path.join(dirpath,name)
            try:
                h=hash_file(path)
            except Exception:
                continue
            hashes.setdefault(h,[]).append(path)
    return {h:paths