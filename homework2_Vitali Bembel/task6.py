palindrome = 12345654321
reverse = 0
palindromeMain = palindrome

while (palindrome > 0):
    remainder = palindrome % 10
    reverse = (reverse * 10) + remainder
    palindrome = palindrome//10

print(palindromeMain)  
print(reverse)

if palindromeMain == reverse:
    print("Число является палиндромом")
else:
    print("Число не является палиндромом")
    

