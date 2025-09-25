from palindrome_checker import IsPalindrome

def main():
    text_to_check = "Лев осовел"
    print(f"'{text_to_check}' — палиндром?", IsPalindrome(text_to_check))

    text_to_check = "Набор бкув"
    print(f"'{text_to_check}' — палиндром?", IsPalindrome(text_to_check))

if __name__ == "__main__":
    main()