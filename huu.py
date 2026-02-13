import pgzrun
import random

# 画面サイズ
WIDTH = 600
HEIGHT = 800

# 変数初期化
balloons = []
score = 0
timer = 30 # 30秒制限
game_over = False

def create_balloon():
    # 風船をランダムな位置に作成
    balloon = Actor("balloon") # balloon.pngが必要
    balloon.x = random.randint(50, 550)
    balloon.y = HEIGHT + 50
    balloons.append(balloon)

def update():
    global game_over, timer
    if game_over: return

    # 時間管理
    timer -= 1/60
    if timer <= 0:
        game_over = True

    # 風船を浮かせる
    for b in balloons:
        b.y -= 2 
    
    # たまに新しい風船を追加
    if random.randint(1, 30) == 1:
        create_balloon()

def on_mouse_down(pos):
    global score
    if game_over: return

    # サイコロを振る (1〜6)
    dice = random.randint(1, 6)
    print(f"サイコロの目: {dice}")

    # 出た目の数だけ、画面内にいる風船を消す
    count = 0
    for b in balloons[:]:
        if count < dice:
            balloons.remove(b)
            count += 1
            score += 1

def draw():
    screen.clear()
    screen.fill((135, 206, 235)) # 空色
    
    for b in balloons:
        b.draw()
    
    screen.draw.text(f"Score: {score}", (10, 10), fontsize=40, color="white")
    screen.draw.text(f"Time: {int(timer)}", (10, 50), fontsize=40, color="red")

    if game_over:
        screen.draw.text("GAME OVER", center=(WIDTH/2, HEIGHT/2), fontsize=70)

pgzrun.go()
