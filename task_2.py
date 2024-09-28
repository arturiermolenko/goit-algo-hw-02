from collections import deque

def check_palindrome(string: str) -> None:
    filtered_string = ''.join(c.lower() for c in string if c.isalpha())
    
    dq = deque(filtered_string)
    
    while len(dq) > 1:
        if dq.popleft() != dq.pop():
            print(f"The phrase {string} is not a palindrome!")
            return

    print(f"The phrase '{string}' is palindrome")

if __name__ == "__main__":
    pali_string = "Sore was I ere I saw Eros."
    not_pali_string = "Just some text"
    check_palindrome(pali_string)
    check_palindrome(not_pali_string)

