# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import messagebox, font
import time
import pygame.mixer

media_dir=r"C:\Users\Administrator\Documents\code\py\q&a" #图片背景音乐路径文件夹，最后不要有“\”

# 初始化混音器模块
pygame.mixer.init()

# 加载音乐文件
pygame.mixer.music.load(media_dir+r"\1.mp3")


# 定义问题和答案
questions = [
    {
        "question": "中国传播马克思主义的的第一人是(  ) 。\n",
        "options": ["A.陈独秀", "B.李大钊", "C.毛泽东"],
        "answer": 1
    },
    {
        "question": "中国共产党的根本宗旨是(  )。\n",
        "options": ["A.无私奉献 ", "B.执政为民", " C.全心全意为人民服务"],
        "answer": 2
    },
    {
        "question": "国徽内容不包括什么(   )\n",
        "options": ["A.国旗", "B.天安门 ", "C.太阳"],
        "answer": 2
    },
    {
        "question": "标志着我国进入改革开放新时期的重要会议是(   )\n",
        "options": ["A.党的八大", "B.党的的十一届三中全会", "C.党的十二大"],
        "answer": 1
    },
    {
        "question": "中国共产党是(   )诞生的\n",
        "options": ["A.1919年", "B.1920年", "C.1921年"],
        "answer": 2
    },
    {
        "question": "长征途中,中央红军主力于1935年5月下旬飞夺(  )， \n越过了被敌人视为不可逾越的天险大渡河。 \n",
        "options": ["A.泸定桥", "B.赵州桥", "C.卢沟桥"],
        "answer": 0
    },
    {
        "question": "1935年1月召开的(  )会议确立了毛泽东在红军和党中央的领导地位，\n挽救了党、挽救了红军、挽救了中国革命，成为党的历史上一个生死攸关的转折点。\n",
        "options": ["A.古田 ", "B.黎平", "C.遵义"],
        "answer": 2
    },
    {
        "question": "抗日战争是何时胜利的?(  )\n",
        "options": ["A.1945年8月15日 ", "B.1955年4月10日 ", "C.1950年8月15日"],
        "answer": 0
    },
    {
        "question": "红军两万五千里长征的起点是哪里(  )\n",
        "options": ["A.陕西吴起", "B.井冈山", "C.江西瑞金"],
        "answer": 2
    },
    
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
        self.image_label = None  # 增加image_label属性
        self.create_widgets()

    def create_widgets(self):
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
            if self.image_label:
                self.image_label.destroy() #开始下一关后销毁
            if (self.current_question + 1) % 3 == 0 and (self.current_question + 1) ==3:
                messagebox.showinfo("恭喜！", f"你已经通过了第1关")
                image = tk.PhotoImage(file=media_dir+r"\恭喜闯关成功1.png") 
                self.image_label = tk.Label(self, image=image) #调用对象属性
                self.image_label.image = image
                self.image_label.pack()
               
            elif (self.current_question + 1) % 3 == 0 and (self.current_question + 1) ==6:
                messagebox.showinfo("恭喜！", f"你已经通过了第2关")
                image = tk.PhotoImage(file=media_dir+r"\恭喜闯关成功2.png")  
                self.image_label = tk.Label(self, image=image)
                self.image_label.image = image
                self.image_label.pack()
                

            elif (self.current_question + 1) == len(questions):
                messagebox.showinfo("恭喜！", f"你已经通过了所有关卡！")
                image = tk.PhotoImage(file=media_dir+r"\2.png")  
                self.image_label = tk.Label(self, image=image)
                self.image_label.image = image
                self.image_label.pack()                
                return

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
                
            return

        
        messagebox.showerror("回答错误！", f"你用时{time_taken}秒，你的得分是：{self.score}")
        
        image = tk.PhotoImage(file=media_dir+r"\3.png") 
        self.image_label = tk.Label(self, image=image)
        self.image_label.image = image
        self.image_label.pack()
        return

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
        # 添加标题
        title_label = tk.Label(self, text="红色中国--党史知识闯关游戏", font=("仿宋", 44), fg="red")
        title_label.pack()
        # 显示图片
        image = tk.PhotoImage(file=media_dir+r"\98.png") 
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
        game_window.title("红色中国--党史知识闯关游戏（作者：唐山十二中张朝翔）")
        game_window.state('zoomed')  # 窗口最大化
        game_app = Game(master=game_window)
        game_app.mainloop()

# 创建启动页面窗口
startup_window = tk.Tk()
startup_window.title("红色中国--党史知识闯关游戏（作者：唐山十二中张朝翔）")
startup_window.geometry('800x600')
startup_window.state('zoomed')  # 窗口最大化

# 创建启动页面实例
startup_page = StartupPage(master=startup_window)


# 播放音乐
pygame.mixer.music.play(-1)  # -1表示循环播放
# 启动主循环
startup_window.mainloop()
