ip_add = input("Enter the IP address :")

first_octet = ip_add[0:3]

first_octet=int(first_octet)

if first_octet >=0 and first_octet<=127:
    ip_class="Class A"
elif first_octet >=128 and first_octet<=191:
    ip_class="Class B"
elif first_octet >=192 and first_octet<=223:
    ip_class="Class C"
elif first_octet >=224 and first_octet<=239:
    ip_class="Class D"
elif first_octet >=240 and first_octet<=255:
    ip_class="Class E"
else:
    ip_class="Invalid"
    
print(ip_class+" IP Address.")