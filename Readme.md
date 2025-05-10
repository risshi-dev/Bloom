# Bloom Filter Implementation in Python

This repository contains a Python implementation of a **Bloom Filter**, a probabilistic data structure that is used to test whether an element is a member of a set. It is space-efficient and allows for false positives but no false negatives.

## Features

- **Hashing Algorithm**: Uses FNV-1 (Fowler–Noll–Vo) hash function for efficient and reliable hashing.
- **Probabilistic Membership Testing**: Quickly checks for membership with minimal memory usage.
- **Customizable Parameters**: Configure the size of the bit array, the number of hash functions, and salt.

## How It Works

A Bloom Filter works by hashing input elements using multiple hash functions and setting the corresponding bits in a bit array. To check membership, the same hash functions are applied, and the corresponding bits are checked. If all bits are set, the element is likely in the set; otherwise, it is definitely not.