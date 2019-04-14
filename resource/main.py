import pygame
from pygame.locals import *
from sys import  exit
#设置游戏屏幕大小
#主窗体实现
SCREEN_WIDTH=480
SCREEN_HEIGHT=800

#子弹类
class Bullt(pygame.sprite.Sprite):
    def __init__(self,bullet_img,init_pos):   #子弹图片及位置
        pygame.sprite.Sprite.__init__(self)#实现父类初始化方法
        self.image=bullet_img
        self.rect=self.image.get_rect()

        self.rect.midootom=init_pos #子弹发射位置
        self.speed=10
        def move(self):
            self.rect.top -=self.speed  #每次调用方法就减速，相当于子弹向上移动

#玩家飞机类
class Player(pygame.sprite.Sprite):
    def __init__(self,plane_img,player_rect,init_pos):
        pygame.sprite.Sprite.__init__(self)
        self.imge=[]  #小飞机图片和飞机爆炸效果图，用列表存
        for i in range(len(player_rect)):
         self.imge.append(plane_img.subsurface(player_rect[i].convert_alpha())
         self.rect = player_rect[0]
        self.rect.topleft=init_pos    #左上角坐标
        self.speed=8
        self.bullets=pygame.spirte.Group()   #定义飞机发射子弹的集合
        self.imge_index=0
        self.is_hit=False  #默认飞机没有被击中

         #发射子弹
        def shoot(self,buttet_img):
            buttet=Bullt(buttet_img,self.rect.midootom) #传递子弹图片及发射位置
            self.bullet.add(buttet)  #发射的子弹添加到创建的速度里

            # 飞机的向上移动
             def moveUp(self):
                if self.rect.top<=0:  #小于0超出边界
                    self.rect.top=0
                else:
                    self.rect.top -=self.speed
            #向下
            def moveDown (self):
                if self.rect.top>=SCREEN_HEIGHT-self.rect.height:
                    self.top=SCREEN_HEIGHT-self.rect.height        #如果顶部大于主界面高减图片的高，证明飞机已经在最底部
                else:
                    self.rect.top +=self.speed
            #向左
            def moveLeft(self):
                if self.rect.left<=0:
                    self.rect.left=0
                else:
                    self.rect.left -=self.speed

             #向右
            def moveRight(self):
                if self.rect.left>=SCREEN_WIDTH-self.rect.width:
                    self.rect.left=SCREEN_WIDTH-self.rect.width
                else:
                    self.rect.left +=self.speed

#敌机
class Enemy(pygame.sprite.Sprite):
    def __init__(self,enemy_img,enemy_down_img,init_pos):  #敌机初始化方法，敌机图片及击落时候图片和位置
    pygame.sprite.Sprite.__init__(self)   #调用父类初始化方法
    self.image=enemy_img   #设置图片
    self.rect=self.image.get_rect()  #设置位置
    self.rect.topleft=init_pos
    self.down_imgs=enemy_down_imgs
    self.speed=2
    self.down_imgs_index=0
    def move(self):
        self.rect.top +=self.speed
        def move(self):
            self.rect.top +=speed

#游戏界面设置
#初始化pygame
pygame.init()
screen=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))  #pygame内置方法实现界面大小
pygame.display.set_caption('飞机大战')   #设置名称
ic_launcher=pygame.image.load('resources/image/ic_launcher.png').convert_alpha()#插入图片，并使它透明
pygame.display.set_icon(ic_launcher)  #设置icon,修改显示窗口图标
background=pygame.image.load("resources/image/background.png")    #加载背景图
game_over=pygame.image.load('resources/image/gameover.png')    #游戏结束画面
plane_img=pygame.image.load('resources/image/shoot.png')

def startGame():
    player_rect=[]

    player_rect.append(pygame.Rect(0, 99, 100, 120))  # 获取图片所在位置
    player_rect.append(pygame.Rect(0, 99, 100, 120))  # 获取图片所在位置
    player_rect.append(pygame.Rect(0, 99, 100, 120))  # 获取图片所在位置
    player_rect.append(pygame.Rect(0, 99, 100, 120))  # 获取图片所在位置

    player_pos[200,600]
    player=Player(plane_img,player_rect,player_pos)
#游戏主循环
running=TURE
while running:
    screen.fill(0)
    screen.blit(background,(0,0))
    if not player.is_hit:
        screen.bit(player.imge[player.imge_index],player.rect)
    pygame.display.update()   #循环一次后更新一下屏幕
    for event in pygame.event.get():
        if event.type=pygame.QUIT:  #判断退出游戏
            pygame.quit()
            exit()
    key_pressed=pygame.key.get_pressed()    #获取键盘点击事件
    if key_pressed[K_w] or key_pressed[K_UP] :  #判断点击向上
        player.moveUp()

     if key_pressed[K_s] or key_pressed[K_DOWN]:  # 判断点击向下
            player.moveDown()

    if key_pressed[K_a] or key_pressed[K_LEFT]:  # 判断点击向左
                player.moveLeft()

    if key_pressed[K_d] or key_pressed[K_RIGHT]:  # 判断点击向右
                    player.moveRight()
startGame()







