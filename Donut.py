import pygame
import math

pygame.init()

# ----------Initial Setting----------
COLOR = "#D1D1D1"
BACK_GROUND = "#050505"

root_x = 0
root_y = 0

WIDTH = 700
HEIGHT = 700

x_separator = 10
y_separator = 20

ROW_NUMBER = HEIGHT // y_separator
COLUMN_NUMBER = WIDTH // x_separator
screen_size = ROW_NUMBER * COLUMN_NUMBER

x_offset = COLUMN_NUMBER / 2
y_offset = ROW_NUMBER / 2

# Initial Rotation Speed
A = 0
B = 0

theta_spacing = 10
phi_spacing = 1

chars = ".,-~:;=!*#$@"  # luminance index

window = pygame.display.set_mode((WIDTH, HEIGHT))
screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Donut")
font = pygame.font.SysFont("Arial", 12, bold=True)


# ----------Generate Letter----------
def text_display(letter, x_start, y_start):
    text = font.render(str(letter), True, COLOR)
    screen.blit(text, (x_start, y_start))


# ----------Main Program----------
run = True
while run:
    window.fill(BACK_GROUND)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False

    background = [0] * screen_size
    string = [' '] * screen_size

    for i in range(0, 628, theta_spacing):
        for j in range(0, 628, phi_spacing):
            si = math.sin(i)
            ci = math.cos(i)
            sj = math.sin(j)
            cj = math.cos(j)
            sA = math.sin(A)
            cA = math.cos(A)
            sB = math.sin(B)
            cB = math.cos(B)
            h = ci + 2
            D = 1 / (sj * h * sA + si * cA + 5)
            t = sj * h * cA - si * sA
            x = int(x_offset + 40 * D * (cj * h * cB - t * sB))
            y = int(y_offset + 20 * D * (cj * h * sB + t * cB))
            z = int(x + COLUMN_NUMBER * y)
            L = int(8 * ((si * sA - sj * ci * cA) * cB - sj * ci * sA - si * cA - cj * ci * sB))
            if ROW_NUMBER > y > 0 and COLUMN_NUMBER > x > 0 and D > background[z]:
                background[z] = D
                string[z] = chars[L if L > 0 else 0]

    if root_y == ROW_NUMBER * y_separator - y_separator:
        root_y = 0

    for j in range(len(string)):
        A += 0.00003
        B += 0.00002
        if j == 0 or j % COLUMN_NUMBER:
            text_display(string[j], root_x, root_y)
            root_x += x_separator
        else:
            root_y += y_separator
            root_x = 0
            text_display(string[j], root_x, root_y)

    pygame.display.update()
