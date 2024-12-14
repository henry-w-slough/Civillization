extends Node2D

#for objects that are selected by mouse
var selected_tile = "none"

var removable_trees = []

@onready var tile_map = get_parent().get_node("TileMap")





# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(_delta):
	
	if Input.is_action_just_pressed("Select"):               
		selected_tile = tile_map.local_to_map(get_global_mouse_position())
		
		
		
		
		
	

	
	
	





	
