import tkinter as tk
import webbrowser as webb
from data import namelist
import main
var = None


def init():
    global var
    root = tk.Tk()
    root.title('新型冠状病毒肺炎数据查询')
    
    root.geometry('330x800')
    menubar = tk.Menu(root)
    filemenu = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label='帮助', menu=filemenu)
    def h():
        webb.open('file:///'+__file__[:-6]+'help.html')
    filemenu.add_command(label='查看使用说明', command=h)
    root.config(menu=menubar)
    var = tk.StringVar()
    l = tk.Label(root, width=20, text='请选择城市')
    l.pack()

    def q():
        l.config(text='你选择了' + var.get())

    for i in range(1, 25):
        exec(
            f'r{i}= tk.Radiobutton(root, text=namelist[{i}], variable=var, value=namelist[{i}], command=q)'
        )
    for i in range(1, 25):
        exec(f'r{i}.pack()')

    def h_c():
        global var
        main.main()
        webb.open('file:///D:/temp.html')

    b = tk.Button(root, text='提交', command=h_c)
    b.pack()

    root.mainloop()


if __name__ == "__main__":
    init()