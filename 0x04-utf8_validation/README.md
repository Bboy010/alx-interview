# UTF-8 Validation interview

---
**UTF-8 Validation**
---
[UTF-8](./0-validate_utf8.py)
Follow these step to execute the program:

### Write a method that determines if a given data set represents a valid UTF-8 encoding.

0️⃣ Prototype: def validUTF8(data)
1️⃣ Return: True if data is a valid UTF-8 encoding, else return False
2️⃣ A character in UTF-8 can be 1 to 4 bytes long
3️⃣ The data set can contain multiple characters
4️⃣ The data will be represented by a list of integers
5️⃣ Each integer represents 1 byte of data, therefore you only need to handle the 8 least significant bits of each integer

```sh
$ cat main_0.py
#!/usr/bin/python3
"""
Main file for testing
"""

validUTF8 = __import__('0-validate_utf8').validUTF8

data = [65]
print(validUTF8(data))

data = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
print(validUTF8(data))

data = [229, 65, 127, 256]
print(validUTF8(data))
```
---
🥳0️⃣1️⃣2️⃣3️⃣4️⃣5️⃣6️⃣7️⃣8️⃣9️⃣🔟

