# Katelyn Curtiss
# 3-17-25

import pygame 
import sys 
import config

def draw_text(screen,text, x,y,font_size, color, font_name=None, bold=False, italic=False):
    if font_name:
        font = pygame.font.Font(font_name, font_size)
    else:
        font = pygame.font.Font(None, font_size)
    font.set_bold(bold)
    font.set_italic(italic)
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x,y)) 

    def init_game():
        pygame.init()
        pygame.font.init()
        screen = pygame.display.set_mode((config.WINDOW_WIDTH, config.WINDOW_HEIGHT))
        pygame.display.set_caption(config.TITLE)

        return screen 
    
    def handle_events():
        for event in pygame.event.get():
            if event.type == pygame.Quit:
                return False 
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return False
                return True
            
def handle_events(x1, y1):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return x1, y1, False
        
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        y1 -= 10
        if keys[pygame.K_DOWN]:
            y1 += 10
        if keys[pygame.K_LEFT]:
            x1 -= 10
        if keys[pygame.K_RIGHT]:
            x1 += 10
        
        return x1, y1, True
    
    def main():
        screen = init_game()
        clock = pygame.time.Clock()


        text1 = "Hello!" 
        font_size1 = 48
        color1 = config.BLACK
        x1, y1 = (200, 250)

        running = True
        while running:
            x1, y1, running = handle_events(x1, y1)
            screen.fill(config.PURPLE)

            draw_text(screen, text1, x1, y1, font_size1, color1)

            pygame.display.flip()
            clock.tick(config.FPS)

        pygame.quit()
        sys.exit()

    if __name__ == "__main__":
        main()