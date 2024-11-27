extends Node2D

@onready var tile_map = $TileMap

@export var land_noise_texture : NoiseTexture2D
@export var tree_noise_texture : NoiseTexture2D

@export var max_trees = 100
var tree_prefab = preload("res://scenes/tree.tscn")

var rng = RandomNumberGenerator.new()


var width : int = 300
var height : int =  300


#TERRAIN GENERATION
var land_noise : Noise
var tree_noise : Noise

var all_land = []
var all_trees = []

var land_atlas = Vector2i(0, 0)
var water_atlas = Vector2i(2, 0)
var tree_atlas = Vector2i(1, 0)

var castle_atlas = Vector2i(0, 1)

var hover_land_atlas = Vector2i(0, 1)
var hover_water_atlas = Vector2i(2, 1)
var hover_tree_atlas = Vector2i(2, 1)




var castle_coordinates





func _ready():
	
	#preparing for generation
	land_noise = land_noise_texture.noise
	tree_noise = tree_noise_texture.noise
	
	land_noise.seed = randi()
	
	generate_world()
	
	#setting castle location
	castle_coordinates = all_land.pick_random()
	
	for tree in range(max_trees):
		create(tree_prefab, all_trees.pick_random())
		
		
		
		
	
	
	



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
				tile_map.set_cell(0, Vector2i(x, y), 0, land_atlas, 0)
				
				#specifying trees with tree noise
				if tree_noise_val > 0.1:
					tile_map.set_cell(0, Vector2i(x, y), 0, tree_atlas, 0)
					all_trees.append(Vector2i(x*64, y*64))
				else:
					all_land.append(Vector2i(x*64, y*64))
					
					
				
				
				
				
				
func create(prefab, pos):
	var instance = prefab.instantiate()
	instance.global_position = pos
	
	add_child(instance)
