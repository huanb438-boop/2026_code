class Settings():
    """储存 所有设置的类"""

    def __init__(self):
        """初始化游戏的静态设置"""
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 700
        # self.bg_color = (135,206,235)
        self.bg_color = (230, 230, 230)

        #飞船的设置
        self.ship_speed_factor = 0.6
        self.ship_limit = 3

        # 子弹设置
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullet_allowed = 3

        #外星人设置
        self.alien_speed_factor = 0.1
        self.fleet_drop_speed = 3
#         设置fleet_drop_speed指定了有外星人撞到屏幕边缘时，外星人群向下移动的速度。

#                以什么样的速度加快游戏节奏
        self.speedup_scale = 3
        # 外星人点数的提高速度
        self.score_scale = 1

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """初始化随游戏进行而变化的设置"""
        # self.ship_speed_factor *=  self.score_scale
        # self.bullet_speed_factor *=  self.score_scale
        self.alien_speed_factor *=  self.score_scale
        # # fleet_direction为1 表示向右移动  -1表示向左移动
        self.fleet_direction = 1
        # 记分
        self.alien_points = 50


    def increase_speed(self):
        """提高速度设置和外星人点数"""
        # self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points *  self.score_scale)

        print(self.alien_points)