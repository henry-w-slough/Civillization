extends CharacterBody2D

@onready var tile_map = get_parent().get_node("TileMap")
#navigation variables
@onready var nav = $NavigationAgent2D
var speed = 300
var accel = 20
var direction

#tasks (including mouse vars)
@onready var mouse = get_parent().get_node("Mouse")

var current_task = "idle"





func _ready():
	#verifying navigation layer is created before the villager tries to move
	set_physics_process(false)
	call_deferred("wait_init")
	
	
	
	
	
	
func _physics_process(delta):
	nav.target_position = get_global_mouse_position()
	if get_atlas(mouse.selected_tile) == Vector2i(1, 0) and nav.is_target_reached():
		current_task = "wood"
		
		
	direction = Vector3()
	
	direction = nav.get_next_path_position() - global_position
	direction = direction.normalized()
	
	velocity = velocity.lerp(direction * speed, accel * delta)
		
	move_and_slide()
		
	
	
	
	
	
func wait_init():
	await get_tree().process_frame
	set_physics_process(true)
	

	
	
	
	

func move_to_nav_pos(delta):
	direction = Vector3()
	
	direction = nav.get_next_path_position() - global_position
	direction = direction.normalized()
	
	velocity = velocity.lerp(direction * speed, accel * delta)
	
	if nav.is_target_reached():
		velocity = Vector2(0, 0)
		
		
			
	

	
	
	
	
	
	
	
func get_atlas(tile_coords):
	if str(tile_coords) != "none":
		return tile_map.get_cell_atlas_coords( 0, tile_coords )
		
		
		
	
		 
