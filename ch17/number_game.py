import cmd


class NumberGame(cmd.Cmd):
    intro = '숫자게임에 오신것을 환영합니다. 도움말은 help 또는 ? 을 입력하세요.\n'
    prompt = '(숫자게임) '

    def do_quit(self, *arg):
        """ 게임을 종료합니다 """
        return True

    def preloop(self):
        import random
        self.answer = random.randint(1, 9)
        self.count = 0

    def do_answer(self, arg):
        """ 1~9 사이의 숫자를 입력하세요 """
        n = int(arg)
        self.count += 1
        if n > self.answer:
            print('너무 높아요')
        elif n < self.answer:
            print('너무 낮아요')
        else:
            print(f'정답입니다!! 시도횟수:{self.count}')
            return True


if __name__ == '__main__':
    NumberGame().cmdloop()
