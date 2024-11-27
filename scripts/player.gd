extends CharacterBody2D

var direction : Vector2 = Vector2.ZERO


func _physics_process(_delta):

	direction = Input.get_vector("ui_left", "ui_right","ui_up","ui_down").normalized()
	if direction:
		velocity = direction * 3000
	else:
		velocity = Vector2.ZERO

	move_and_slide()


	
