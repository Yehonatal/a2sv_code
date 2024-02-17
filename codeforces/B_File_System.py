n = int(input())

file_sys = {}
for _ in range(n):
    file_name = input()
    if file_name in file_sys:
        print(f"{file_name}{file_sys[file_name]}")
        file_sys[file_name] = file_sys.get(file_name, 0) + 1
    else:
        file_sys[file_name] = file_sys.get(file_name, 0) + 1
        print("OK")
