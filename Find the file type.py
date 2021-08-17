FileName = input("Name of the File: ")

if FileName.endswith(".py"):
    print("It is a Python File")
elif FileName.endswith(".js"):
    print("It is a JavaScript File")
elif FileName.endswith(".java"):
    print("It is a Java File")
elif FileName.endswith(".css"):
    print("It is a Cascading Style Sheets File")
elif FileName.endswith(".htm"):
    print("It is a HyperText Markup Language File")
elif FileName.endswith(".html"):
    print("It is a HyperText Markup Language File")
elif FileName.endswith(".png"):
    print("It is a Portable Network Graphics File")
elif FileName.endswith(".jpg"):
    print("It is a Joint Photographic Expert Group File")
elif FileName.endswith(".jpeg"):
    print("It is a Joint Photographic Expert Group File")
elif FileName.endswith(".csv"):
    print("It is a Comma-Separated Values File")
elif FileName.endswith(".exe"):
    print("It is an Executable")
elif FileName.endswith(".txt"):
    print("It is a Text File")
elif FileName.endswith(".pdf"):
    print("It is a Portable Doucument Format File")
else:
    print("File Extension not Recongnised")
