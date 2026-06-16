from settings import * 
from level import Level
from pytmx.util_pygame import load_pygame
from os.path import join

from support import *

class Game:
	def __init__(self):
		pygame.init()
		self.display_surface = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
		pygame.display.set_caption('Super Pirate Adventure')
		self.clock = pygame.time.Clock()
		self.import_assets()

		self.tmx_maps = {0: load_pygame(join('data/levels/omni.tmx'))}
		self.current_stage = Level(self.tmx_maps[0], self.level_frames)

	def import_assets(self):
		self.level_frames = {
			'flag': import_folder('graphics/level/flag'),
			'saw': import_folder('graphics/enemies/saw/animation'),
			'floor_spike': import_folder('graphics/enemies/floor_spikes'),
			'player': import_sub_folders('graphics/player')
		}

	def run(self):
		# Main Game Loop
		while True:
			dt = self.clock.tick(30) / 1000
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()

			self.current_stage.run(dt)
			pygame.display.update()

if __name__ == '__main__':
	game = Game()
	game.run()