import tkinter as tk
from my_frame import MyFrame  # フレームクラスをインポートするのじゃ

class Main(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("500x600")
        self.title("フレーム統合じゃ")

        window_width = 586  
        window_height = 329
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x_coordinate = (screen_width // 2) - (window_width // 2)   # モニター中央-ウィンドウ半分
        y_coordinate = (screen_height // 2) - (window_height // 2) # モニター中央-ウィンドウ半分
        self.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")

        frame = MyFrame(master=self)
        frame.pack(expand=True, fill="both")


# 別ファイルのフレームを呼び出して配置
if __name__ == "__main__":
    app = Main()
    app.mainloop()