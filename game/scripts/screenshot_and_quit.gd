extends Node

@export var output_path: String = "user://hub_test.png"
@export var wait_frames: int = 3

func _ready() -> void:
	for i in wait_frames:
		await RenderingServer.frame_post_draw
	var img := get_viewport().get_texture().get_image()
	var resolved := output_path
	if resolved.begins_with("repo://"):
		var project_dir := ProjectSettings.globalize_path("res://").trim_suffix("/")
		var repo_root := project_dir.get_base_dir()
		resolved = repo_root.path_join(resolved.substr("repo://".length()))
		DirAccess.make_dir_recursive_absolute(resolved.get_base_dir())
	img.save_png(resolved)
	print("Screenshot saved to: ", resolved)
	get_tree().quit()
