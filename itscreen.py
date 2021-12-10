import pygame

pygame.init()
pygame.font.init()

sw = 1920
sh = 1080

screen = pygame.display.set_mode((sw, sh), pygame.FULLSCREEN)
clock = pygame.time.Clock()

bg = pygame.image.load("assets/bg.png")
font1 = pygame.font.SysFont("None", 300)
font2 = pygame.font.SysFont("None", 100)

text_ledig = font1.render("LEDIG", False, (255,255,255))
text_rect1 = text_ledig.get_rect(center=(sw/2, sh/2.1))
text_ledig2 = font1.render("KOM INN!", False, (255,255,255))
text_rect12 = text_ledig2.get_rect(center=(sw/2, sh/1.5))

text_mote = font1.render("SITTER I MØTE", False, (255,0,0))
text_rect2 = text_mote.get_rect(center=(sw/2, sh/2.1))
text_mote2 = font2.render("KOM TILBAKE SENERE", False, (255,0,0))
text_rect22 = text_mote2.get_rect(center=(sw/2, sh/1.6))

text_annet = font1.render("INGEN TILSTEDE", False, (255,255,255))
text_rect3 = text_annet.get_rect(center=(sw/2, sh/2.1))
text_annet2 = font2.render("KOM TILBAKE SENERE", False, (255,255,255))
text_rect32 = text_annet2.get_rect(center=(sw/2, sh/1.6))
text_annet3 = font2.render("ELLER RING/SEND MELDING PÅ TEAMS", False, (255,255,255))
text_rect33 = text_annet3.get_rect(center=(sw/2, sh/1.4))

def ledig():
    screen.blit(bg, (0,0))
    screen.blit(text_ledig, text_rect1)
    screen.blit(text_ledig2, text_rect12)
    color = (0,255,0)
    pygame.draw.rect(screen, color, pygame.Rect(0,0,sw,sh), 100)
    pygame.display.update()
                    

def mote():
    screen.blit(bg, (0,0))
    screen.blit(text_mote, text_rect2)
    screen.blit(text_mote2, text_rect22)
    color = (255,0,0)
    pygame.draw.rect(screen, color, pygame.Rect(0,0,sw,sh), 100)
    pygame.display.update()

def annet_oppdrag():
    screen.blit(bg, (0,0))
    screen.blit(text_annet, text_rect3)
    screen.blit(text_annet2, text_rect32)
    screen.blit(text_annet3, text_rect33)
    color = (255,255,0)
    pygame.draw.rect(screen, color, pygame.Rect(0,0,sw,sh), 100)
    pygame.display.update()
