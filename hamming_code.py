def calculate_parity_bits(data):
    # Validate input data
    if not all(bit in '01' for bit in data):
        raise ValueError("Input data must be a binary string (only '0' and '1').")

    # Number of data bits
    m = len(data)
    # Calculate the number of parity bits needed
    r = 0
    while (2 ** r < m + r + 1):
        r += 1

    # Create a list to hold the encoded data
    encoded_data = ['0'] * (m + r)

    # Place data bits in the encoded data
    j = 0
    for i in range(1, m + r + 1):
        if (i & (i - 1)) != 0:  # If i is not a power of 2
            encoded_data[i - 1] = data[j]
            j += 1

    # Calculate parity bits
    for i in range(r):
        parity_pos = 2 ** i
        parity_value = 0
        for j in range(1, m + r + 1):
            if j & parity_pos:  # If the bit position includes this parity bit
                parity_value ^= int(encoded_data[j - 1])
        encoded_data[parity_pos - 1] = str(parity_value)

    return ''.join(encoded_data)

def hamming_decode(encoded_data):
    # Calculate the number of parity bits
    n = len(encoded_data)
    r = 0
    while (2 ** r < n + 1):
        r += 1

    # Find the error position
    error_pos = 0
    for i in range(r):
        parity_pos = 2 ** i
        parity_value = 0
        for j in range(1, n + 1):
            if j & parity_pos:  # If the bit position includes this parity bit
                parity_value ^= int(encoded_data[j - 1])
        if parity_value != 0:
            error_pos += parity_pos

    # Correct the error if there is one
    if error_pos != 0:
        print(f"Error detected at position: {error_pos}")
        encoded_data = list(encoded_data)
        # Flip the erroneous bit
        encoded_data[error_pos - 1] = '1' if encoded_data[error_pos - 1] == '0' else '0'
        encoded_data = ''.join(encoded_data)

    # Extract the original data (discard parity bits)
    original_data = []
    for i in range(1, n + 1):
        if (i & (i - 1)) != 0:  # If i is not a power of 2
            original_data.append(encoded_data[i - 1])

    return ''.join(original_data)

# Example usage
data = "1011"  # 4 bits of data
encoded = calculate_parity_bits(data)
print("Encoded Hamming Code:", encoded)

# Simulating an error for testing
encoded_with_error = encoded[:2] + '1' + encoded[3:]  # Introduce an error
print("Encoded with error:", encoded_with_error)

decoded = hamming_decode(encoded_with_error)
print("Decoded Data:", decoded)