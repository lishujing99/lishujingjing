import pygame
class W(object):
    def __init__(self,lujing,screen):
        self.x=200
        self.y=120
        self.width=30
        self.height=30
        self.lujing=lujing
        self.screen=screen
        self.renwu=pygame.image.load(self.lujing)
        self.rect=pygame.Rect(self.x,self.y,self.width,self.height)
    def get1(self):
        self.screen.blit(self.renwu,self.rect)
def main():
    # screen 窗口;表示创建游戏窗口。
    screen=pygame.display.set_mode((560,310),0,32)
    background=pygame.image.load('./images/yinghua.png')
    hongmao=W('./images/bomb-1.gif',screen)
    clock=pygame.time.Clock() # 获得游戏时钟 控制器
    move_step=10
    while True:
        screen.blit(background,(0,0))
        hongmao.get1()
        hongmao.rect.x+=1
        if hongmao.rect.x>560:
            hongmao.rect.x=0
        for event in pygame.event.get():
            if event.type==pygame.QUIT:# 退出游戏
                print('game over!')
                exit()# 退出程序

            '''
            elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_UP:
                    hongmao.rect.y-=move_step
                elif event.key==pygame.K_DOWN:
                    hongmao.rect.y+=move_step
                elif event.key==pygame.K_LEFT:
                    hongmao.rect.x-=move_step
                elif event.key==pygame.K_RIGHT:
                    hongmao.rect.x+=move_step
            elif event.type==pygame.KEYUP:
                pass
 '''
        pygame.display.update()
        clock.tick(60)# 让游戏时钟，1/60秒运行一次。

if __name__=='__main__':
    main()

