from display import *
from draw import *
from parser import *
from matrix import *
import math

screen = new_screen()
zbuffer = new_zbuffer()
color = [ 0, 255, 0 ]
edges = []
polygons = []
t = new_matrix()
ident(t)
csystems = [ t ]

#polygons = [[10, 10, 0], [100, 50, 0], [50, 100, 0]]
#scanline_convert(polygons, screen, zbuffer, color)

#save_extension(screen, "img.png")
parse_file( 'script', edges, polygons, csystems, screen, zbuffer, color )
