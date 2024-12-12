extends Node2D

#misc
var rng = RandomNumberGenerator.new()
@onready var tile_map = $TileMap



#display for gen
var width : int = 100
var height : int =  100
var tile_size = 64



#TERRAIN GENERATION
@export var land_noise_texture : NoiseTexture2D
@export var tree_noise_texture : NoiseTexture2D

var land_noise : Noise
var tree_noise : Noise

var all_land = []
var all_trees = []



#atlas for textures
var land_atlas = Vector2i(0, 0)
var edge_land_atlas = Vector2i(0, 1)
var water_atlas = Vector2i(2, 0)
var tree_atlas = Vector2i(1, 0)



#castle
var castle_coordinates
var castle_atlas = Vector2i(0, 1)



#trees
var tree_prefab = preload("res://scenes/tree.tscn")







func _ready():
	
	#preparing for generation
	land_noise = land_noise_texture.noise
	tree_noise = tree_noise_texture.noise
	
	land_noise.seed = randi()
	
	generate_world()
	
	#setting castle location
	castle_coordinates = all_land.pick_random()
	
	



func generate_world():
	var land_noise_val
	var tree_noise_val
	
	#every pixel in the specified width and height
	for x in range(width):
		for y in range(height):
			
			land_noise_val = land_noise.get_noise_2d(x, y)
			tree_noise_val = tree_noise.get_noise_2d(x, y)
			
			
			#setting all to water
			tile_map.set_cell(0, Vector2i(x, y), 0, water_atlas, 0)


			#setting specific noise values to land
			if land_noise_val > 0.1:
			
				#specifying trees with tree noise
				if tree_noise_val > 0.1:
					tile_map.set_cell(0, Vector2i(x, y), 0, tree_atlas, 0)
					all_trees.append(Vector2i(x*tile_size, y*tile_size))
					
					create(tree_prefab, Vector2i(x*tile_size, y*tile_size))
				else:
					tile_map.set_cell(0, Vector2i(x, y), 0, land_atlas, 0)
					all_land.append(Vector2i(x*tile_size, y*tile_size))		
					
					

				
			






func create(prefab, pos):
	var instance = prefab.instantiate()
	instance.global_position = pos
	
	add_child(instance)
