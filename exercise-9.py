
def isPalindrome(num):

    numbers = num

    reversed_num = 0

    while num != 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num //= 10

    if numbers == reversed_num:
        return True
    else:
        return False

print(isPalindrome(num = int(input("Lütfen bir sayı giriniz:"))))

