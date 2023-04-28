extends Control

@export var setting_name := "Name"

@export var setting_value := 8


func _ready():
	$SettingLabel.text = setting_name.to_upper()
	
	set_setting_value_text()


func _on_decrease_button_pressed():
	if setting_value > 0: 
		setting_value -= 1
		
		set_setting_value_text()


func _on_increase_button_pressed():
	if setting_value < 10:
		setting_value += 1
		
		set_setting_value_text()


# Helper Functions
func set_setting_value_text():
	$ValuePanel/Text.text = str(setting_value)
