extends CharacterBody2D


#navigation variables
@onready var nav = $NavigationAgent2D
var speed = 300
var accel = 20
var direction

var current_task = "idle"

var array = [9, 2, 5, 1]





func _ready():
	#verifying navigation layer is created before the villager tries to move
	set_physics_process(false)
	call_deferred("wait_init")
	
	
	
	
	
	
func _physics_process(delta):
	move_to_nav_pos(delta)
		
		
		
	move_and_slide()
	
	
	
	
	
func wait_init():
	await get_tree().process_frame
	set_physics_process(true)
	
	global_position = get_parent().castle_coordinates
	
	
	
	

func move_to_nav_pos(delta):
	direction = Vector3()
	
	direction = nav.get_next_path_position() - global_position
	direction = direction.normalized()
	
	velocity = velocity.lerp(direction * speed, accel * delta)
	
	if nav.is_target_reached():
		velocity = Vector2(0, 0)
		
		
			
	

	
	
	
	
	
	
	

		
		
		
	
		 
