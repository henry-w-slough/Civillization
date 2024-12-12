extends Area2D

#for objects that are selected by mouse
var selected_tile

var removable_trees = []

@onready var tile_map = get_parent().get_node("TileMap")





# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(_delta):
	global_position = get_global_mouse_position()
	
	
	
	if Input.is_action_just_pressed("Select"):               
		selected_tile = get_atlas(tile_map.local_to_map(global_position))
		
		
		
		
		
		
		
		
func get_atlas(tile_coords):
	return tile_map.get_cell_atlas_coords( 0, tile_coords )

	
	
	





	
