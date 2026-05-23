extends Node2D

## Sparse bob/shuffle for crowd silhouettes.
## Picks ONE random figure per cycle and runs a gentle asymmetric down-then-up
## position tween (slower sink, slightly faster recovery — reads as weight
## settling). Random interval between picks; concurrent bobs from prior cycles
## are allowed (creates natural breathing across the crowd) but no two figures
## ever START in the same frame. Locked architecture: "subtle bob/shuffle
## motion on 1-2 figures every few seconds keeps it alive without competing
## with cloud and mist motion for attention."

@export var min_interval: float = 1.5
@export var max_interval: float = 5.0
@export var bob_amount: float = 5.0
@export var bob_down_duration: float = 1.2
@export var bob_up_duration: float = 1.0

var _figures: Array[Sprite2D] = []
var _original_y: Dictionary = {}
var _bobbing: Dictionary = {}


func _ready() -> void:
	for child in get_children():
		if child is Sprite2D:
			_figures.append(child)
			_original_y[child] = child.position.y
			_bobbing[child] = false
	_schedule_next_bob()


func _schedule_next_bob() -> void:
	var wait := randf_range(min_interval, max_interval)
	await get_tree().create_timer(wait).timeout
	_pick_and_bob()
	_schedule_next_bob()


func _pick_and_bob() -> void:
	var available: Array[Sprite2D] = []
	for s in _figures:
		if not _bobbing[s]:
			available.append(s)
	if available.is_empty():
		return
	var sprite: Sprite2D = available[randi() % available.size()]
	_bob(sprite)


func _bob(sprite: Sprite2D) -> void:
	_bobbing[sprite] = true
	var base_y: float = _original_y[sprite]
	var tween := create_tween()
	tween.tween_property(sprite, "position:y", base_y + bob_amount, bob_down_duration) \
		.set_trans(Tween.TRANS_SINE).set_ease(Tween.EASE_IN_OUT)
	tween.tween_property(sprite, "position:y", base_y, bob_up_duration) \
		.set_trans(Tween.TRANS_SINE).set_ease(Tween.EASE_IN_OUT)
	tween.tween_callback(func() -> void: _bobbing[sprite] = false)
