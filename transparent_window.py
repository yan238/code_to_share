import pygame
import win32api
import win32con
import win32gui
from win32api import GetSystemMetrics

#     pygame.init()
#
#     screen_size = (GetSystemMetrics(0),GetSystemMetrics(1))
#
#     pygame.init()
#     screen = pygame.display.set_mode(screen_size, pygame.NOFRAME) # For borderless, use pygame.NOFRAME
#     # done = False
#     fuchsia = (255, 0, 128)  # Transparency color
#
#     # Create layered window
#     hwnd = pygame.display.get_wm_info()["window"]
#     win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE,win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE) | win32con.WS_EX_LAYERED)
#
#     # Set window transparency color
#     win32gui.SetLayeredWindowAttributes(hwnd, win32api.RGB(*fuchsia), 0, win32con.LWA_COLORKEY)
#
#     win32gui.SetWindowPos(pygame.display.get_wm_info()['window'], win32con.HWND_TOPMOST, 0, 0, 0, 0, win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)

# counter = 1000

transparency_colour = (255, 0, 128)

class TransparentWindow:

    screen_size = (GetSystemMetrics(0), GetSystemMetrics(1))
    screen = pygame.display.set_mode(screen_size, pygame.NOFRAME) # For borderless, use pygame.NOFRAME
    hwnd = pygame.display.get_wm_info()["window"]
    win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE, win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE) | win32con.WS_EX_LAYERED)
    win32gui.SetLayeredWindowAttributes(hwnd, win32api.RGB(*transparency_colour), 0, win32con.LWA_COLORKEY)
    win32gui.SetWindowPos(pygame.display.get_wm_info()['window'], win32con.HWND_TOPMOST, 0, 0, 0, 0,win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)

#
# pygame.init()
#
# screen = TransparentWindow.screen
#
# run = True
#
# # if counter == 0:
# #     run = False
# # else:
# #     counter -= 1
#
# while run:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_ESCAPE]:
#             done = True
#
#     screen.fill(transparency_colour)  # Transparent background
#     pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(0, 0, 100, 100))
#     pygame.display.update()
