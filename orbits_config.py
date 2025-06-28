import pygame, math, random

pygame.init()

SCREENWIDTH = 600
SCREENHEIGHT = 600

screen = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
main_surface = pygame.Surface((SCREENWIDTH, SCREENHEIGHT), pygame.SRCALPHA)
trailer = pygame.Surface((SCREENWIDTH, SCREENHEIGHT), pygame.SRCALPHA)
pygame.display.set_caption("very cool thing")

FPS = "max"
clock = pygame.time.Clock()

POINT_AMT = 4

lenghts = []
remain = 300
point_amt = POINT_AMT

while point_amt > 0:
    lenght = random.randint(1, (remain-(point_amt-1)))
    remain -= lenght
    lenghts.append(lenght)

    point_amt -= 1

random.shuffle(lenghts)
# print(lenghts[0]+lenghts[1]+lenghts[2]+lenghts[3])

class Point:
    def __init__(self, centre, length, angle, orbit_rate, colour, line_width=2):
        self.length = length
        self.angle = (angle / 180) * math.pi
        if orbit_rate == 0:
            self.orbit_rate = 0
        else:
            self.orbit_rate = math.pi / orbit_rate
        self.last_pos = (
        (centre[0] + (math.cos(self.angle) * self.length)), (centre[1] + (math.sin(self.angle) * self.length)))
        self.colour = colour
        self.line_width = line_width

    def move(self, centre):
        self.angle += self.orbit_rate
        new_pos = (
        (centre[0] + (math.cos(self.angle) * self.length)), (centre[1] + (math.sin(self.angle) * self.length)))
        if self.colour is not None:
            if visualisation_mode:
                pygame.draw.line(main_surface, (255, 255, 255), new_pos, centre, 2)
                pygame.draw.circle(main_surface, self.colour, new_pos, 10)
            else:
                pygame.draw.line(main_surface, self.colour, new_pos, self.last_pos, self.line_width)
        self.last_pos = new_pos

visualisation_mode = False

counter = 1
points = []

points.append(Point((300, 300), lenghts[0], 0, random.randint(20, 100) * random.choice([-1, 1]),(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))))
for x in range(POINT_AMT-1):
    # points.append(Point(points[counter-1].last_pos, lenghts[counter], 0, x, (255, 255, 255)))
    points.append(Point(points[counter-1].last_pos, lenghts[counter], 0, random.randint(20, 100)*random.choice([-1, 1]), (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))))
    # points.append(Point(points[counter-1].last_pos, lenghts[counter], 0, random.randint(20, 100)*random.choice([-1, 1]), (255, 255, 255)))
    counter += 1

trail_wait = random.randint(0, 100)
trail_counter = 0

run = True
while run:

    if pygame.key.get_pressed()[pygame.K_SPACE]:
        FPS = 10
    else:
        FPS = "max"

    if visualisation_mode:
        main_surface.fill((0, 0, 0))
    else:
        if trail_counter == 0:
            trailer.fill((0, 0, 0, 1))
            main_surface.blit(trailer, (0, 0))
            trail_counter = trail_wait
        else:
            trail_counter -= 1

    for point in points:
        if points[0] == point:
            point.move((300, 300))
        else:
            centre = points[points.index(point) - 1].last_pos
            point.move(centre)

    screen.blit(main_surface, (0, 0))

    #end
    for event in pygame.event.get():
        if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_ESCAPE]:
            run = False
    pygame.display.update()
    if type(FPS) == int or type(FPS) == float:
        clock.tick(FPS)

pygame.quit()
