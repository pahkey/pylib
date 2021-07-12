import curses
import random

try:
    stdscr = curses.initscr()

    curses.start_color()
    curses.use_default_colors()
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)

    success = 0
    failure = 0

    for i in range(3):
        stdscr.clear()  # 문제가 변경되면 화면을 클리어한다.
        a = random.randint(1, 100)
        b = random.randint(1, 100)
        result = a + b

        stdscr.addstr(0, 0, str(a), curses.color_pair(1) | curses.A_BOLD)
        stdscr.addstr(" + ")
        stdscr.addstr(str(b), curses.color_pair(1) | curses.A_BOLD)
        stdscr.addstr(" = ?")

        answer = stdscr.getstr(1, 0, 3)

        if result == int(answer):
            success += 1
        else:
            failure += 1

    stdscr.addstr(3, 0, "맞은갯수:%d, 틀린갯수:%d" % (success, failure))
    stdscr.addstr(5, 0, "Press enter key...")
    stdscr.getkey()

finally:
    curses.endwin()
