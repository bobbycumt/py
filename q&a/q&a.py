import tkinter as tk
from tkinter import messagebox
import time

#这是没用的注释
# 定义问题和答案
questions = [
    {
        "question": "红色教育的目的是什么？",
        "options": ["提高人民的生活水平", "提高人民的政治觉悟", "提高人民的文化素养"],
        "answer": 1
    },
    {
        "question": "红色教育的内容包括哪些？",
        "options": ["革命历史", "科学技术", "文学艺术"],
        "answer": 0
    },
    {
        "question": "红色教育对社会发展有什么作用？",
        "options": ["促进经济发展", "促进社会和谐", "促进人民健康"],
        "answer": 1
    }
]

# 定义游戏类
class Game(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.current_question = 0 # 当前问题索引
        self.score = 0 # 玩家得分
        self.total_time = 0 # 玩家答题总时间
        self.start_time = time.time() # 当前问题开始时间
        self.create_widgets()

    def create_widgets(self):
        # 创建问题标签
        self.question_label = tk.Label(self)
        self.question_label.pack()

        # 创建选项按钮
        self.option_buttons = []
        for i in range(3):
            button = tk.Button(self)
            button.pack()
            self.option_buttons.append(button)

        # 更新问题和选项
        self.update_question()

    def check_answer(self, answer):
        # 计算答题时间
        time_taken = round(time.time() - self.start_time, 2)
        self.total_time += time_taken

        # 检查答案是否正确
        if answer == questions[self.current_question]["answer"]:
            self.score += 1
            messagebox.showinfo("回答正确！", f"你用时{time_taken}秒，你的得分是：{self.score}")
        else:
            messagebox.showerror("回答错误！", f"你用时{time_taken}秒，你的得分是：{self.score}")

        # 更新当前问题索引
        self.current_question += 1

        # 判断游戏是否结束
        if self.current_question < len(questions):
            # 更新问题和选项
            self.update_question()
            # 更新当前问题开始时间
            self.start_time = time.time()
        else:
            # 游戏结束，显示总得分和总时间
            messagebox.showinfo("游戏结束！", f"你的最终得分是：{self.score}，总时间是：{self.total_time}秒")
            self.master.destroy()

    def update_question(self):
        # 更新问题标签文本
        self.question_label["text"] = questions[self.current_question]["question"]

        # 更新选项按钮文本和命令
        for i, option in enumerate(questions[self.current_question]["options"]):
            self.option_buttons[i]["text"] = option
            self.option_buttons[i]["command"] = lambda i=i: self.check_answer(i)

# 创建游戏窗口并运行游戏
root = tk.Tk()
app = Game(master=root)
app.mainloop()
