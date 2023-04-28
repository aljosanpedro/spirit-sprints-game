extends Control


const BUTTON_CLICKED_ANIMATION = "clicked"
const BUTTON_RESET_ANIMATION = "unclicked"


func _on_continue_pressed():
	$Icon/Sprites.animation = BUTTON_CLICKED_ANIMATION
	
	$Timer/ClickedAnimation.start()
	$Button/Continue.disabled = true


func _on_clicked_animation_timeout():
	$Icon/Sprites.animation = BUTTON_RESET_ANIMATION
	$Button/Continue.disabled = false
	
	queue_free()
