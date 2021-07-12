from dataclasses import dataclass

@dataclass
class User:
    name: str
    age: int
    married: bool = False


user1 = User("홍길동", 33, True)
user2 = User("홍길동", 33, True)

print(user1)
print(user1 == user2)
