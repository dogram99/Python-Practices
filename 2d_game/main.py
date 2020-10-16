# Здесь подключаются модули
import pygame

# Инициализировать все импортированные модули Pygame
pygame.init()

# Здесь определяются константы, классы и функции:

# Установить текущий заголовок окна
pygame.display.set_caption('2D Game')

# Кадровая частота
FPS = 30

# Путь до изображений
image_url = 'image/'

# Размеры окна игры
WIDTH_WINDOW = 500
HEIGHT_WINDOW = 500

# Выводим на экран главное графическое окно игры с помощью функции set_mode()
window = pygame.display.set_mode((WIDTH_WINDOW, HEIGHT_WINDOW))

# Подключаем бэкграунд
bg = pygame.image.load(image_url + 'bg.jpg')

# Подключаем спрайт для стандартного положения
playerStand = pygame.image.load(image_url + 'idle.png')

# Подключаем спрайты для движение направо
walkRight = [pygame.image.load(image_url + 'right_1.png'), pygame.image.load(image_url + 'right_2.png'),
             pygame.image.load(image_url + 'right_3.png'),
             pygame.image.load(image_url + 'right_4.png'), pygame.image.load(image_url + 'right_5.png'),
             pygame.image.load(image_url + 'right_6.png')]

# Подключаем спрайты для движение налево
walkLeft = [pygame.image.load(image_url + 'left_1.png'), pygame.image.load(image_url + 'left_2.png'),
            pygame.image.load(image_url + 'left_3.png'),
            pygame.image.load(image_url + 'left_4.png'), pygame.image.load(image_url + 'left_5.png'),
            pygame.image.load(image_url + 'left_6.png')]

# Создаем объект, чтобы помочь отслеживать время
clock = pygame.time.Clock()

# Настройка главного персонажа:

# Размеры персонажа
width = 60
height = 71

# Стартовая координаты персонажа
x = 50
y = HEIGHT_WINDOW - height

# Скорость персонажа
speed = 10

# Параметры по умолчанию:
anim_count = 0
jumpCount = 10
isJump = False
left = False
right = False
lastMove = 'right'
run = True
bullets = []


# Создаем класс для снарядов
class Shell():
    # Конструктор
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8 * facing

    def draw(self, win):
        pygame.draw.circle(window, self.color, (self.x, self.y),
                           self.radius)


# Окно рисования
def draw_window():
    # Глобальная область видимости
    global anim_count

    # Создаем холст
    window.blit(bg, (0, 0))

    # Настройка анимаций персонажа
    if anim_count + 1 >= FPS:
        anim_count = 0
    if left:
        window.blit(walkLeft[anim_count // 5], (round(x), round(y)))
        anim_count += 1
    elif right:
        window.blit(walkRight[anim_count // 5], (round(x), round(y)))
        anim_count += 1
    else:
        window.blit(playerStand, (round(x), round(y)))

    # Перебираем и выводим снаряды
    for bullet in bullets:
        bullet.draw(window)

    # Обновление частей экрана для программных дисплеев
    pygame.display.update()


# Главный цикл
while run:
    # Задержка
    clock.tick(FPS)

    # Циклы обработки событий:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for bullet in bullets:
        if bullet.x < WIDTH_WINDOW and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_f]:
        if lastMove == 'right':
            facing = 1
        else:
            facing = -1

        if len(bullets) < 5:
            bullets.append(Shell(round(x + width // 2), round(y + height // 2), 5, (255, 0, 0), facing))

    if keys[pygame.K_LEFT] and x > 5:
        x -= speed
        left = True
        right = False
        lastMove = 'left'
    elif keys[pygame.K_RIGHT] and x < WIDTH_WINDOW - width - 5:
        x += speed
        left = False
        right = True
        lastMove = 'right'
    else:
        left = False
        right = False
        anim_count = 0
    if not (isJump):
        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if jumpCount >= -10:
            if jumpCount < 0:
                y += (jumpCount ** 2) / 2
            else:
                y -= (jumpCount ** 2) / 2
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10

    draw_window()

# Деинициализировать все модули Pygame
pygame.quit()
