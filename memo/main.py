import tkinter as tk
from window import ToDoApp  # フレームクラスをインポートするのじゃ

root = tk.Tk()
root.title("フレーム統合じゃ")

# 別ファイルのフレームを呼び出して配置
frame = ToDoApp(master=root)
frame.pack()

root.mainloop()