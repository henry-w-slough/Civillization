extends Node2D

@onready var tile_map = get_parent().get_node("TileMap")

@onready var camera = get_node("Camera2D")

	
	

	
	
	
	
		


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(_delta):
	camera_movement(50)
	
	global_position = get_parent().castle_coordinates
	
	
	
	
	
	
	
	
func camera_movement(camera_speed):
	
	if Input.is_action_pressed("camera_up"):
		camera.global_position.y -= camera_speed
	if Input.is_action_pressed("camera_down"):
		camera.global_position.y += camera_speed
	if Input.is_action_pressed("camera_left"):
		camera.global_position.x -= camera_speed
	if Input.is_action_pressed("camera_right"):
		camera.global_position.x += camera_speed
	
	
	if camera.zoom < Vector2(4.9, 4.9):
		if Input.is_action_just_pressed("camera_zoom_in"):
			camera.zoom += Vector2(0.2, 0.2)
			
	if camera.zoom > Vector2(0.3, 0.3):
		if Input.is_action_just_pressed("camera_zoom_out"):
			camera.zoom -= Vector2(0.2, 0.2)
		
		
	
	