
s = input("Enter a string: ")
print("Uppercase:", s.upper())
print("Lowercase:", s.lower())
print("Reversed:", s[::-1])
vowels = "aeiouAEIOU"
count = 0

for ch in s:
    if ch in vowels:
        count += 1

print("Number of vowels:", count)