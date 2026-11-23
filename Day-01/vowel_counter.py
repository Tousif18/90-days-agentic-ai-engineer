text = input("Enter a string: ").lower()
vowels = "aeiou"
count = sum(1 for character in text if character in vowels)

print(f"Number of vowels: {count}")
