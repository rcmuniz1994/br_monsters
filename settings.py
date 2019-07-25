class Settings():
    """
    Armazena as configurações do jogo
    """

    def __init__(self):
        #Screen 
        self.screen_width = 1280
        self.screen_height = 680
        self.bg_color = (200, 200, 200)

        #Bullet
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)