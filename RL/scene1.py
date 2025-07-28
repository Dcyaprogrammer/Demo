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
        earth.move_to([5, 1.5, 0])
        environment = Text("Environment", font_size=46, color=WHITE)
        environment.move_to([5, 0, 0])

        # policy
        person = SVGMobject("person.svg")
        person.scale(1)
        person.set_color(WHITE)
        person.move_to([-5, 1.5, 0])
        policy = Text("Policy", font_size=46, color=WHITE)
        policy.move_to([-5, 0, 0])
        
        policy_group = VGroup(person, policy)
        
        # 动画展示
        self.play(Create(earth), run_time=1)
        self.play(Create(person), run_time=1)
        self.play(Write(policy), run_time=1)
        self.play(Write(environment), run_time=1)
        self.wait(1)
