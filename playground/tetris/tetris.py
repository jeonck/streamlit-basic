import pygame
import random

# 게임 화면 크기 설정
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 500
GRID_SIZE = 20

# 색상 설정
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

# 테트리스 블록 모양 설정
SHAPES = [
    [[1, 1, 1],
     [0, 1, 0]],

    [[0, 1, 1],
     [1, 1, 0]],

    [[1, 1, 0],
     [0, 1, 1]],

    [[1, 1, 1, 1]],

    [[1, 1],
     [1, 1]],

    [[1, 1, 1],
     [1, 0, 0]],

    [[1, 1, 1],
     [0, 0, 1]]
]

class Tetris:
    def __init__(self):
        self.grid = [[0 for _ in range(SCREEN_WIDTH // GRID_SIZE)] for _ in range(SCREEN_HEIGHT // GRID_SIZE)]
        self.current_piece = self.get_new_piece()
        self.next_piece = self.get_new_piece()
        self.score = 0
        self.game_over = False

    def get_new_piece(self):
        shape = random.choice(SHAPES)
        return {'shape': shape, 'x': SCREEN_WIDTH // GRID_SIZE // 2 - len(shape[0]) // 2, 'y': 0}

    def collide(self):
        shape = self.current_piece['shape']
        offset_x = self.current_piece['x']
        offset_y = self.current_piece['y']

        for y, row in enumerate(shape):
            for x, cell in enumerate(row):
                if cell:
                    if (x + offset_x < 0 or x + offset_x >= SCREEN_WIDTH // GRID_SIZE or
                        y + offset_y >= SCREEN_HEIGHT // GRID_SIZE or
                        self.grid[y + offset_y][x + offset_x]):
                        return True
        return False

    def merge_piece(self):
        shape = self.current_piece['shape']
        offset_x = self.current_piece['x']
        offset_y = self.current_piece['y']

        for y, row in enumerate(shape):
            for x, cell in enumerate(row):
                if cell:
                    self.grid[y + offset_y][x + offset_x] = cell

        self.clear_lines()
        self.current_piece = self.next_piece
        self.next_piece = self.get_new_piece()

        if self.collide():
            self.game_over = True

    def clear_lines(self):
        lines_to_clear = [i for i, row in enumerate(self.grid) if all(row)]
        for i in reversed(lines_to_clear):
            del self.grid[i]
            self.grid.insert(0, [0 for _ in range(SCREEN_WIDTH // GRID_SIZE)])
        self.score += len(lines_to_clear)

    def rotate_piece(self):
        self.current_piece['shape'] = [list(row) for row in zip(*self.current_piece['shape'][::-1])]
        if self.collide():
            self.current_piece['shape'] = [list(row) for row in zip(*self.current_piece['shape'])][::-1]

    def drop_piece(self):
        self.current_piece['y'] += 1
        if self.collide():
            self.current_piece['y'] -= 1
            self.merge_piece()

    def move_piece(self, dx):
        self.current_piece['x'] += dx
        if self.collide():
            self.current_piece['x'] -= dx

    def draw_grid(self, screen):
        for y, row in enumerate(self.grid):
            for x, cell in enumerate(row):
                if cell:
                    pygame.draw.rect(screen, BLUE if cell == 1 else GREEN, (x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE))

    def draw_piece(self, screen):
        shape = self.current_piece['shape']
        offset_x = self.current_piece['x']
        offset_y = self.current_piece['y']

        for y, row in enumerate(shape):
            for x, cell in enumerate(row):
                if cell:
                    pygame.draw.rect(screen, RED, ((x + offset_x) * GRID_SIZE, (y + offset_y) * GRID_SIZE, GRID_SIZE, GRID_SIZE))

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Tetris')
    clock = pygame.time.Clock()
    tetris = Tetris()

    while not tetris.game_over:
        screen.fill(BLACK)
        tetris.draw_grid(screen)
        tetris.draw_piece(screen)
        pygame.display.flip()
        clock.tick(10)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                tetris.game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    tetris.move_piece(-1)
                elif event.key == pygame.K_RIGHT:
                    tetris.move_piece(1)
                elif event.key == pygame.K_DOWN:
                    tetris.drop_piece()
                elif event.key == pygame.K_UP:
                    tetris.rotate_piece()

        tetris.drop_piece()

    pygame.quit()

if __name__ == '__main__':
    main()