from manim import *

class RLFrameworkFlow(Scene):
    def construct(self):
        # 设置黑色背景
        self.camera.background_color = BLACK

        def create_mini_framework():
            # env - 缩小版本
            earth = SVGMobject("env.svg")
            earth.scale(0.4)  # 缩小到原来的40%
            earth.set_color(WHITE)
            earth.move_to([-5, 2.5, 0])  # 移到左上角
            environment = Text("Environment", font_size=20, color=WHITE)  # 缩小字体
            environment.move_to([-5, 2, 0])

            # policy - 缩小版本
            person = SVGMobject("person.svg")
            person.scale(0.4)  # 缩小到原来的40%
            person.set_color(WHITE)
            person.move_to([-6.5, 2.5, 0])  # 移到左上角
            policy = Text("Policy", font_size=20, color=WHITE)  # 缩小字体
            policy.move_to([-6.5, 2, 0])

            # action arrow - 缩小版本
            action_ar = Arrow(
                start=person.get_right() + UP * 0.2,  # 调整位置
                end=earth.get_left() + UP * 0.2,
                color=WHITE,
                buff=0.1,  # 缩小间距
                stroke_width=2  # 缩小线条粗细
            )     
            action_label = Text("Action", font_size=14, color=WHITE)  # 缩小字体
            action_label.move_to([-5.75, 3.2, 0]) 
            
            # return arrow - 缩小版本
            return_ar = Arrow(
                start=earth.get_left() + DOWN * 0.2,
                end=person.get_right() + DOWN * 0.2,
                stroke_width=2  # 缩小线条粗细
            )

            state_label = Text("Next State & Reward", font_size=12, color=WHITE)  # 缩小字体
            state_label.move_to([-5.75, 1.3, 0])

            # 创建组
            mini_framework = VGroup(
                earth, environment, person, policy, 
                action_ar, action_label, return_ar, state_label
            )
            
            return mini_framework, earth, person, action_ar, return_ar

        # 创建缩小的框架
        mini_framework, earth, person, action_ar, return_ar = create_mini_framework()

        # 演示动画 - 先展示完整版本，然后缩小到左上角
        # 创建完整版本用于初始展示
        earth_full = SVGMobject("env.svg")
        earth_full.scale(1)
        earth_full.set_color(WHITE)
        earth_full.move_to([4, 1.5, 0])
        environment_full = Text("Environment", font_size=46, color=WHITE)
        environment_full.move_to([4, 0, 0])

        person_full = SVGMobject("person.svg")
        person_full.scale(1)
        person_full.set_color(WHITE)
        person_full.move_to([-4, 1.5, 0])
        policy_full = Text("Policy", font_size=46, color=WHITE)
        policy_full.move_to([-4, 0, 0])

        action_ar_full = Arrow(
            start=person_full.get_right() + UP * 0.5,
            end=earth_full.get_left() + UP * 0.5,
            color=WHITE,
            buff=0.3
        )     
        action_label_full = Text("Action", font_size=32, color=WHITE)
        action_label_full.move_to([0, 2.5, 0]) 
        
        return_ar_full = Arrow(
            start=earth_full.get_left() + DOWN * 0.5,
            end=person_full.get_right() + DOWN * 0.5
        )

        state_label_full = Text("Next State & Reward", font_size=32, color=WHITE)
        state_label_full.move_to([0, 0.5, 0])

        # 初始展示完整版本
        self.play(Create(earth_full), run_time=0.5)
        self.play(Create(person_full), run_time=0.5)
        self.play(Write(policy_full), run_time=0.5)
        self.play(Write(environment_full), run_time=0.5)
        self.wait(1)

        self.play(Create(action_ar_full), run_time=0.5)
        self.play(Write(action_label_full), run_time=0.5)
        self.wait(1)

        self.play(Create(return_ar_full), run_time=0.5)
        self.play(Write(state_label_full), run_time=0.5)
        self.wait(1)

        # 展示流动动画
        def create_flow_animation_full():
            particle1 = Dot(radius=0.2, color=RED)
            particle1.move_to(person_full.get_right() + UP * 0.5)
            
            self.play(
                Create(particle1),
                particle1.animate.move_to(earth_full.get_left() + UP * 0.5),
                run_time=1.2,
                rate_func=linear
            )
            self.play(FadeOut(particle1), run_time=0.3)
            
            particle2 = Dot(radius=0.2, color=BLUE)
            particle2.move_to(earth_full.get_left() + DOWN * 0.5)
            
            self.play(
                Create(particle2),
                particle2.animate.move_to(person_full.get_right() + DOWN * 0.5),
                run_time=1.2,
                rate_func=linear
            )
            self.play(FadeOut(particle2), run_time=0.3)

        # 循环展示流动过程
        for i in range(2):  # 减少到2次
            create_flow_animation_full()
            self.wait(0.5)

        # 将完整版本缩小并移动到左上角
        full_framework = VGroup(
            earth_full, environment_full, person_full, policy_full,
            action_ar_full, action_label_full, return_ar_full, state_label_full
        )
        
        self.play(
            Transform(full_framework, mini_framework),
            run_time=1.5
        )
        
        # 现在中央空间可以用来展示新内容
        # 例如：添加一个标题
        main_title = Text("Reinforcement Learning Framework", font_size=36, color=WHITE)
        main_title.move_to([0, 3, 0])
        
        # 添加中央的主要内容区域
        content_area = Rectangle(
            width=8, height=4, 
            color=WHITE, 
            stroke_width=2,
            fill_opacity=0.1
        )
        content_area.move_to([0, 0, 0])
        
        content_label = Text("Main Content Area", font_size=24, color=WHITE)
        content_label.move_to([0, 0, 0])
        
        self.play(Write(main_title), run_time=0.8)
        self.play(Create(content_area), run_time=0.8)
        self.play(Write(content_label), run_time=0.8)



