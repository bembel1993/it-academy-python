palindrome = 12345654321
reverse = 0
palindrome_main = palindrome

while (palindrome > 0):
    remainder = palindrome % 10
    reverse = (reverse * 10) + remainder
    palindrome = palindrome//10

if palindrome_main == reverse:
    print("Число является палиндромом")
else:
    print("Число не является палиндромом")
    

