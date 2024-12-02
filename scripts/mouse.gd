extends Area2D

#for objects that are selected by mouse
var selected_object

var removable_trees = []





# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	global_position = get_global_mouse_position()
	
	if Input.is_action_just_pressed("Select"):
		print(selected_object.name)
		

	
	
	




func _on_area_exited(area):
	selected_object = ""


func _on_area_entered(area):
	selected_object = area
	
	print(selected_object.name)
