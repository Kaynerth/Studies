extends Node

@export var speed: float = 1

var sprite
var enemy: Enemy
var player_position
var difference
var input_vector

func _ready() -> void:
	enemy = get_parent()
	sprite = enemy.get_node("GoblinCharacter")

func _physics_process(_delta: float) -> void:
	player_position = GameManager.player_position
	difference = player_position - enemy.position
	input_vector = difference.normalized()
	enemy.velocity = input_vector * speed * 100.0
	enemy.move_and_slide()
	
	if input_vector.x > 0:
		sprite.flip_h = false
	elif input_vector.x < 0:
		sprite.flip_h = true
