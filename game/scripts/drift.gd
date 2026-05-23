extends Sprite2D

@export var speed: float = 10.0
@export var wrap_min_x: float = -2000.0
@export var wrap_max_x: float = 4000.0

func _process(delta: float) -> void:
	position.x += speed * delta
	if speed > 0.0 and position.x > wrap_max_x:
		position.x = wrap_min_x
	elif speed < 0.0 and position.x < wrap_min_x:
		position.x = wrap_max_x
