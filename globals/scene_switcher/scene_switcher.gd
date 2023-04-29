extends Node2D


const START_PATH = "res://ui/buttons/buttons_hub/buttons_hub.tscn"
#const START_PATH = "res://prog/scenes/ui/pause_button.tscn"


# keys are for visual guidance only
	# the values (paths) are what's needed

const SCENE_NAMES_TO_PATHS := {
	"TitleScreen" : "res://ui/screens/title/title_screen.tscn",
	
	"IntroStory"  : "res://prog/scenes/story/intro_story.tscn",
	
	"GMStory"     : "res://prog/scenes/story/gm_story.tscn",
	"GMBattle"    : "res://prog/scenes/battle/gm_battle.tscn",
	
	"PunoStory"   : "res://prog/scenes/story/puno_story.tscn",
	"PunoBattle"  : "res://prog/scenes/battle/puno_battle.tscn",
	
	"IlogStory"   : "res://prog/scenes/story/ilog_story.tscn",
	"IlogBattle"  : "res://prog/scenes/battle/ilog_battle.tscn",
	
	"OutroStory"  : "res://prog/scenes/story/outro_story.tscn",
}


var scene_names := SCENE_NAMES_TO_PATHS.keys()
var scene_paths := SCENE_NAMES_TO_PATHS.values()

var scene_index := 0
var scene_path := ""


func _ready():
	get_tree().change_scene_to_file(START_PATH)


func next_scene():
	scene_index += 1
	
	if scene_index > len(SCENE_NAMES_TO_PATHS) - 1:
		scene_index = 0
	
	scene_path = scene_paths[scene_index]
	get_tree().change_scene_to_file(scene_path)
