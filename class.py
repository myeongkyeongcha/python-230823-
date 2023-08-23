class Member():
    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password

    def display(self):
        print(
            f'회원님의 이름은 {self.name}이고, 아이디는 {self.username}, 비밀번호는 {self.password} 입니다.')


mem1 = Member('홍길동', 'dong', 1234)
mem2 = Member('김유진', 'kim', 5678)
mem3 = Member('이유진', 'lee', 9910)

mem1.display()
mem2.display()
mem3.display()


class Post():
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author
