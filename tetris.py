#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import pygame

from pygame.locals import *

def terminate(error=0):
	pygame.quit()
	sys.exit(error)

def main():
	pygame.init()
	pygame.display.set_mode((400,500))
	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				terminate()

if __name__ == '__main__':
	main()
