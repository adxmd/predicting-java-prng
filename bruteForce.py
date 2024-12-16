import hashlib
import time

def next(seed, bits=32):
    seed1 = (seed * MULTIPLIER + ADDEND) & MASK
    # print(f"seed: {seed1}")

    ret = int(seed1 >> (48 - bits))
    # print(f"value: {ret}")

    return ret

def next1(seed, bits=32):
    seed1 = (seed * MULTIPLIER + ADDEND) & MASK
    # print(f"seed: {seed1}")

    ret = int(seed1 >> (48 - bits))
    # print(f"value: {ret}")

    return ret, seed1

# # hashlib.sha3_224(next_value.strip().encode()).hexdigest()
# # 42790b1d58cfa9c7d10613cb4006f36d358909c3694063d3b775a1fc - hash to find

# n3 = xxxxxxxxxx? #We need to find this
# hashlib.sha3_224(n3.strip().encode()).hexdigest

#Constants in Java's Random class
MULTIPLIER = 0x5DEECE66D
ADDEND = 0xB
MASK = (1 << 48) - 1

n1 = -745632980
n2 = 2066963502

hashToFind = "42790b1d58cfa9c7d10613cb4006f36d358909c3694063d3b775a1fc"

def hashFunction(inputString):
    return hashlib.sha3_224(inputString.strip().encode()).hexdigest()

#Given 2^16 possibilities (48 - 32)
for i in range(65536):
    seed = n1 * 65536 + i
    if(next(seed) == n2):
        print(f"seed found: {seed}")
        break

print(f"Seed after brute-forcing: {seed}")
inputSeed = (seed ^ MULTIPLIER) & MASK
print(f"Seed inputted as seed to new Random(seed), (bruteSeed xor MUL) & MASK")
print(inputSeed)