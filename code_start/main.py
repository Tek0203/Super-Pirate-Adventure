from settings import * 
from level import Level
from pytmx.util_pygame import load_pygame
from os.path import join
from support import *
from data import Data
from debug import debug
from ui import UI

class Game:
	def __init__(self):
		pygame.init()
		self.display_surface = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
		pygame.display.set_caption('Super Pirate Adventure')
		self.clock = pygame.time.Clock()
		self.import_assets()

		self.ui = UI(self.font, self.ui_frames)
		self.data = Data(self.ui)
		self.tmx_maps = {0: load_pygame(join('data/levels/omni.tmx'))}
		self.current_stage = Level(self.tmx_maps[0], self.level_frames, self.data)

	def import_assets(self):
		self.level_frames = {
			'flag': import_folder('graphics/level/flag'),
			'saw': import_folder('graphics/enemies/saw/animation'),
			'floor_spike': import_folder('graphics/enemies/floor_spikes'),
			'player': import_sub_folders('graphics/player'),
			'saw': import_folder('graphics/enemies/saw/animation'),
			'saw chain': import_image('graphics/enemies/saw/saw_chain'),
			'helicopter': import_folder('graphics/level/helicopter'),
			'boat': import_folder('graphics/objects/boat'),
			'spike': import_image('graphics/enemies/spike_ball/Spiked Ball'),
			'spike_chain': import_image('graphics/enemies/spike_ball/spiked_chain'),
			'tooth': import_folder('graphics/enemies/tooth/run'),
			'shell': import_sub_folders('graphics/enemies/shell'),
			'pearl': import_image('graphics/enemies/bullets/pearl'),
			'items': import_sub_folders('graphics/items'),
			'particle': import_folder('graphics/effects/particle'),
			'water_top': import_folder('graphics/level/water/top'),
			'water_body': import_image('graphics/level/water/body'),
			'bg_tiles': import_folder_dict('graphics/level/bg/tiles'),
			'cloud_small': import_folder('graphics/level/clouds/small'),
			'cloud_large': import_image('graphics/level/clouds/large_cloud')
		}

		self.font = pygame.font.Font(join('graphics/ui/runescape_uf.ttf'), 40)
		self.ui_frames = {
			'heart': import_folder('graphics/ui/heart'),
			'coin': import_folder('graphics/ui/coin')
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
			self.ui.update(dt)
			pygame.display.update()

if __name__ == '__main__':
	game = Game()
	game.run()