

names = ["유튜버 1","유튜버 2","유튜버 3","유튜버 4"]

for name in names:
    file_name = f"{name}.txt"
    with open(file_name, "w",encoding="utf8") as email_file:
        email_file.write(f"안녕하세요.{name} 감사합니다")
    