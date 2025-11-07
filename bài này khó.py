def load_users(filename="users.txt"):
    users = {}
    f = open(filename, "r")  # mở file thủ công, không dùng 'with'
    lines = f.readlines()    # đọc toàn bộ dòng vào danh sách
    f.close()                # nhớ đóng file

    i = 0
    while i < len(lines):    # dùng while thay vì for
        line = lines[i].strip()
        parts = line.split(":")
        if len(parts) == 2:
            username = parts[0]
            password = parts[1]
            users[username] = password
        i += 1
    return users

def login(username, password):
    users = load_users()
    if username in users and users[username] == password:
        return True
    return False

if __name__ == "__main__":
    input_username = input("Tên đăng nhập: ")
    input_password = input("Mật khẩu: ")

    if login(input_username, input_password):
        print("Đăng nhập thành công!")
    else:
        print("Tên đăng nhập hoặc mật khẩu không đúng.")
