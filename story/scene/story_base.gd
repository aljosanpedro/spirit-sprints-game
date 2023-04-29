extends Control


const TIMELINE_PATH = "res://story/timelines/chapter0/Chapter0Trans.dtl"


func _ready():
	Dialogic.start_timeline(TIMELINE_PATH)
