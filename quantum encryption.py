# This code simulates the key distribution process of quantum encryption

import random

# Function to simulate quantum key distribution
def quantum_key_distribution(bits):
    alice_bits = [random.choice([0, 1]) for _ in range(bits)]
    alice_bases = [random.choice(['X', '+']) for _ in range(bits)]
    
    bob_bases = [random.choice(['X', '+']) for _ in range(bits)]
    
    bob_results = []
    for i in range(bits):
        if alice_bases[i] == bob_bases[i]:
            bob_results.append(alice_bits[i])
        else:
            bob_results.append(random.choice([0, 1]))
    
    return alice_bits, alice_bases, bob_bases, bob_results

# Function to filter matching bits and create a secure key
def filter_matching_bits(alice_bases, bob_bases, bob_results):
    matching_indices = [i for i in range(len(alice_bases)) if alice_bases[i] == bob_bases[i]]
    filtered_key = [bob_results[i] for i in matching_indices]
    return filtered_key

def main():
    bits = 10  # Number of qubits (bits) to simulate
    
    # Simulate quantum key distribution
    alice_bits, alice_bases, bob_bases, bob_results = quantum_key_distribution(bits)
    
    # Filter matching bits to create a secure key
    secure_key = filter_matching_bits(alice_bases, bob_bases, bob_results)
    
    print("Alice's bits:", alice_bits)
    print("Alice's bases:", alice_bases)
    print("Bob's bases:", bob_bases)
    print("Bob's results:", bob_results)
    print("Secure key:", secure_key)

if __name__ == "__main__":
    main()
