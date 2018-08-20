import hashlib as hl
import json

def hash_string_256(string):
    return hl.sha256(string).hexdigest()

def hash_block(block):
    # json.dumps turns the block into a readable string, which hl.sha256() requires. hexdigest() returns the hash with normal characters
    # Sort_keys takes the dictionary, which is unordered, and orders it so that the same input always returns the same output.
    return hl.sha256(json.dumps(block, sort_keys=True).encode()).hexdigest()