from manim import *

class RLFrameworkTitle(Scene):
    def construct(self):
        # 设置黑色背景
        self.camera.background_color = BLACK
        
        # 主标题
        title = Text(
            "A minimum framework",
            font_size=60,
            color=WHITE,
            font="Arial"
        )
        
        # 动画：标题从上方滑入
        self.play(
            Write(title),
            run_time=1
        )
        
        # 停留时间
        self.wait(1.5)
        
        # 缩小并向上移动
        self.play(
            title.animate.scale(0.6).move_to([0, 5, 0]),
            run_time=1.5
        )

class RLFrameworkFlow(Scene):
    def construct(self):
        # 设置黑色背景
        self.camera.background_color = BLACK
        
        # env
        earth = SVGMobject("env.svg")
        earth.scale(1)
        earth.set_color(WHITE)
        earth.move_to([4, 1.5, 0])
        environment = Text("Environment", font_size=46, color=WHITE)
        environment.move_to([4, 0, 0])

        # policy
        person = SVGMobject("person.svg")
        person.scale(1)
        person.set_color(WHITE)
        person.move_to([-4, 1.5, 0])
        policy = Text("Policy", font_size=46, color=WHITE)
        policy.move_to([-4, 0, 0])

        # action arrow
        action_ar = Arrow(
            start=person.get_right() + UP * 0.5,
            end=earth.get_left() + UP * 0.5,
            color=WHITE,
            buff=0.3
        )     
        action_label = Text("Action", font_size=32, color=WHITE)
        action_label.move_to([0, 2.5, 0]) 
        
        # return arrow
        return_ar = Arrow(
            start=earth.get_left() + DOWN * 0.5,
            end=person.get_right() + DOWN * 0.5
        )

        state_label = Text("Next State & Reward", font_size=32, color=WHITE)
        state_label.move_to([0, 0.5, 0])

        # demo
        self.play(Create(earth), run_time=0.5)
        self.play(Create(person), run_time=0.5)
        self.play(Write(policy), run_time=0.5)
        self.play(Write(environment), run_time=0.5)
        self.wait(1)

        self.play(Create(action_ar), run_time=0.5)
        self.play(Write(action_label), run_time=0.5)
        self.wait(1)

        self.play(Create(return_ar), run_time=0.5)
        self.play(Write(state_label), run_time=0.5)
        self.wait(1)

        def create_flow_animation():
            # Action流动 - 移动粒子
            particle1 = Dot(radius=0.2, color=RED)
            particle1.move_to(person.get_right() + UP * 0.5)
            
            self.play(
                Create(particle1),
                particle1.animate.move_to(earth.get_left() + UP * 0.5),
                run_time=1.2,
                rate_func=linear
            )
            self.play(FadeOut(particle1), run_time=0.3)
            
            # Return流动 - 移动粒子
            particle2 = Dot(radius=0.2, color=BLUE)
            particle2.move_to(earth.get_left() + DOWN * 0.5)
            
            self.play(
                Create(particle2),
                particle2.animate.move_to(person.get_right() + DOWN * 0.5),
                run_time=1.2,
                rate_func=linear
            )
            self.play(FadeOut(particle2), run_time=0.3)

        # 循环展示流动过程
        for i in range(3):  # 循环3次
            create_flow_animation()
            self.wait(0.5)

        self.wait(2)