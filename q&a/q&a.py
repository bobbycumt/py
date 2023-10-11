# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import messagebox, font
import time
import pygame

# 定义问题和答案
questions = [
    {
        "question": "红色教育的目的是什么？\n",
        "options": ["提高人民的生活水平", "提高人民的政治觉悟", "提高人民的文化素养"],
        "answer": 1
    },
    {
        "question": "红色教育的内容包括哪些？\n",
        "options": ["革命历史", "科学技术", "文学艺术"],
        "answer": 0
    },
    {
        "question": "红色教育对社会发展有什么作用？\n",
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
        # 设置窗口尺寸
        self.master.geometry('800x600')

        # 设置字体
        self.font = font.Font(family='FangSong',size=28, weight='bold')
        self.color = 'red'
        self.create_widgets()
    # def show_startup_screen(self):
    #     pygame.init()

    #     # 设置启动页面的尺寸
    #     screen = pygame.display.set_mode((800, 600))
    #     pygame.display.set_caption("启动页面")

    #     # 添加文本信息
    #     # font = pygame.font.Font(None, 36)
    #     chinese_font = pygame.font.Font("simsun.ttc", size=36)
    #     creator_text = chinese_font.render("制作者：张朝翔", True, (255, 255, 255))
    #     school_text = chinese_font.render("学校：唐山第十二中学", True, (255, 255, 255))

    #     # 添加图片
    #     image = pygame.image.load(r"C:\Users\Administrator\Pictures\1.jpg")  # 替换成你的图片路径
    #     image = pygame.transform.scale(image, (300, 200))  # 调整图片大小

    #     # 主循环，用于显示启动页面
    #     running = True
    #     while running:
    #         for event in pygame.event.get():
    #             if event.type == pygame.QUIT:
    #                 running = False

    #         screen.fill((0, 0, 0))
    #         screen.blit(image, (250, 50))  # 调整图片位置
    #         screen.blit(creator_text, (100, 300))  # 调整文本位置
    #         screen.blit(school_text, (100, 350))  # 调整文本位置

    #         pygame.display.flip()

    #     pygame.quit()

    def create_widgets(self):
        # self.show_startup_screen()
        # 创建问题标签
        self.question_label = tk.Label(self, font=self.font,fg=self.color, justify='center', anchor='center')
        self.question_label.pack()

        # 创建选项按钮
        self.option_buttons = []
        for i in range(3):
            button = tk.Button(self, font=self.font,fg=self.color, justify='center', anchor='center')
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

# 创建启动页面
class StartupPage(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        # 显示图片
        image = tk.PhotoImage(file=r"C:\Users\Administrator\Pictures\1.png")  # 替换成你的图片路径
        image_label = tk.Label(self, image=image)
        image_label.image = image
        image_label.pack()

        # 显示制作者和学校信息
        creator_label = tk.Label(self, text="制作者：张朝翔", font=("宋体", 18))
        creator_label.pack()
        school_label = tk.Label(self, text="学校：唐山第十二中学", font=("宋体", 18))
        school_label.pack()

        # 添加开始按钮
        start_button = tk.Button(self, text="开始闯关", font=("宋体", 18), command=self.start_game)
        start_button.pack()

    def start_game(self):
        self.master.destroy()  # 销毁启动页面
        game_window = tk.Tk()
        game_app = Game(master=game_window)
        game_app.mainloop()

# 创建启动页面窗口
startup_window = tk.Tk()
startup_window.geometry('800x600')

# 创建启动页面实例
startup_page = StartupPage(master=startup_window)

# 启动主循环
startup_window.mainloop()





# 创建游戏窗口并运行游戏
# root = tk.Tk()
# app = Game(master=root)
# app.mainloop()
