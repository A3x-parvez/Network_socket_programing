def xor(a, b):
    result = []
    for i in range(1,len(b)):
        if a[i] == b[i]:
            result.append('0')
        else:
            result.append('1')
    return ''.join(result)

def mod2div(divident, divisor):
    pick = len(divisor)
    temp = divident[0:pick]
    
    while pick < len(divident):
        if temp[0] == '1':
            temp = xor(divisor, temp) + divident[pick]
        else:
            temp = xor('0' * pick, temp) + divident[pick]
        pick += 1
    
    if temp[0] == '1':
        temp = xor(divisor, temp)
    else:
        temp = xor('0' * pick, temp)
        
    return temp

def encode(data, divisor):
    l_key = len(divisor) - 1
    append_data = data + "0" * l_key
    reminder = mod2div(append_data, divisor)
    final_data = data + reminder
    return final_data, reminder

data = input("Enter the data: ")
divisor = input("Enter the divisor: ")
final_data, reminder = encode(data, divisor)
print("Main Data: ", data)
print("Divisor: ", divisor)
print("Encoded Data: ", final_data)
print("Reminder: ", reminder)
