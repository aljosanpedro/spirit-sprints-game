extends Button


func _ready():
	self.text = get_parent().name


func _on_pressed():
	SceneSwitcher.next_scene()
