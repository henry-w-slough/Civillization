extends Area2D


#getting the hovered over sprite
var area_sprite

#hover textures
var tree_hover_texture = preload("res://sprites/tree2.png")

# Called when the node enters the scene tree for the first time.
func _ready():
	pass # Replace with function body.


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	global_position = get_global_mouse_position()
	
	

	
	

func _on_area_entered(area):
	area_sprite = area.get_node("AnimatedSprite2D")
	
	area_sprite.play("hover")
	
	
	



func _on_area_exited(area):
	area_sprite = area.get_node("AnimatedSprite2D")
	
	area_sprite.play("not_hovered")
