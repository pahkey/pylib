from tkinter import *
from tkinter.messagebox import *
from .blog_sqlite_model import *

root = Tk()
root.title('나의 블로그')

# use components
listbox = Listbox(root, exportselection=False)
label = Label(root, text='제목')
entry = Entry(root)
text = Text(root)
b1 = Button(root, text='생성')
b2 = Button(root, text='수정')
b3 = Button(root, text='삭제')

# placements
listbox.grid(row=0, column=0, columnspan=3, sticky='ew')
label.grid(row=1, column=0)

entry.grid(row=1, column=1, columnspan=2, sticky='ew')
text.grid(row=2, column=0, columnspan=3)
b1.grid(row=3, column=0, sticky='ew')
b2.grid(row=3, column=1, sticky='ew')
b3.grid(row=3, column=2, sticky='ew')


ROW_IDS = []
def load_blog_list():
    listbox.delete(0, END)
    blog_list = get_blog_list()
    for i, blog in enumerate(blog_list):
        ROW_IDS.append(blog["id"])
        listbox.insert(i, '[%s/%s/%s] %s' % (
            blog["date"][:4], blog["date"][4:6], blog["date"][6:], blog["subject"]))


def get_blog(event):
    _id = ROW_IDS[listbox.curselection()[0]]
    blog = read_blog(_id)
    entry.delete(0, END)
    entry.insert(0, blog["subject"])
    text.delete(1.0, END)
    text.insert(1.0, blog["content"])

listbox.bind('<<ListboxSelect>>', get_blog)


def refresh():
    ROW_IDS.clear()
    entry.delete(0, END)   # clear subject
    text.delete(1.0, END)  # clear content
    load_blog_list()


def btn_add(event):
    subject = entry.get().strip()
    content = text.get(1.0, END).strip()
    if not subject or not content:
        showerror("오류", "제목 또는 내용을 입력해 주세요")
        return
    add_blog(subject, content)
    refresh()

b1.bind('<Button-1>', btn_add)


def btn_modify(event):
    sel = listbox.curselection()
    if not sel:
        showerror("오류", "리스트를 먼저 선택해 주세요")
    else:
        _id = ROW_IDS[sel[0]]
    subject = entry.get().strip()
    content = text.get(1.0, END).strip()
    if not subject or not content:
        showerror("오류", "제목 또는 내용을 입력해 주세요")
        return

    modify_blog(_id, subject, content)
    refresh()

b2.bind('<Button-1>', btn_modify)


def btn_remove(event):
    sel = listbox.curselection()
    if not sel:
        showerror("오류", "리스트를 먼저 선택해 주세요")
        return
    _id = ROW_IDS[sel[0]]
    if askyesno("확인", "정말로 삭제하시겠습니까?"):
        remove_blog(_id)
        refresh()


b3.bind('<Button-1>', btn_remove)

init_blog()  # blog 테이블이 없을경우 생성한다.
load_blog_list()
root.mainloop()
