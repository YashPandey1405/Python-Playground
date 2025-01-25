with open("test_bin.bin", "wb") as f: 
    f.write(b"\x48\x61\x6C\x6c\x6F\x2c\x20\x57\x6F\x72\x6c\x64\x21")

with open("test_bin.bin", "rb") as f: 
    print(f.read())  
