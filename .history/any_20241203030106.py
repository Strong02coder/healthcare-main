def encrypt(plaintext, key): v0, v1 = plaintext[0], plaintext[1] k0, k1, k2, k3 = key[0], key[1], key[2], key[3] delta = 0x9e3779b9 sum = 0 for _ in range(32): sum += delta v0 += ((v1 << 4) + k0) ^ (v1 + sum) ^ ((v1 >> 5) + k1) v1 += ((v0 << 4) + k2) ^ (v0 + sum) ^ ((v0 >> 5) + k3) return v0, v1