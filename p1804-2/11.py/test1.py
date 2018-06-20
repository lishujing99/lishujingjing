import pygame
#import time
'''
# 1.x 2.y 3.width 4.height
feiji=pygame.Rect(100,500,50,50)
print('x= %d' % feiji.x)
print('y= %d' % feiji.y)
print('width宽度是 %d' % feiji.width)
print('height高度是 %d' % feiji.height)
'''

def main():
    # 创建游戏窗口：
    screen=pygame.display.set_mode((400,500),0,32)
    # 把本地文件夹的图片获取到代码中
    background=pygame.image.load('./images/bg.png')
    feiji1=pygame.image.load('./images/hero1.png')
    feiji2=pygame.image.load('./images/enemy1.png')
    # 设置飞机 : 横坐标，竖坐标，照片大小
    rect=pygame.Rect((400-100)/2,350,100,125)
    rect2=pygame.Rect(150,250,100,124)
    # 获得游戏时钟，控制器。
    clock=pygame.time.Clock()
    move_step=10 # 移动的步长值
    while True:
        # 把图片转移到游戏窗口中
        screen.blit(background,(0,0))
        # 设置飞机
        screen.blit(feiji1,rect)
        screen.blit(feiji2,rect2)
        # 移动
        #rect.x+=1
        #if rect.x>400:
         #   rect.x=0
        # 刷新显示
        pygame.display.update()
        clock.tick(60)# 表示60/1秒运行一次。
        #游戏事件的监听 控制
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                print('game over!!!')
                pygame.quit()
                exit() # 退出程序
            elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_UP:
                    rect.y-=move_step
                elif event.key==pygame.K_DOWN:
                    rect.y+=move_step
                elif event.key==pygame.K_LEFT:
                    rect.x-=move_step
                elif event.key==pygame.K_RIGHT:
                    rect.x+=move_step
            elif event.type==pygame.KEYUP:
                pass


if __name__=='__main__':
    main()















