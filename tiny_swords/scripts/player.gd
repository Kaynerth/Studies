class_name Player
extends CharacterBody2D

@onready var animation_player: AnimationPlayer = $AnimationPlayer
@onready var sprite: Sprite2D = $PlayerCharacter
@onready var sword_area: Area2D = $SwordArea
@onready var hitbox_area: Area2D = $HitboxArea
@onready var health_progress_bar: ProgressBar = $HealthProgressBar

@export var speed: float = 3
@export var sword_damage: int = 2
@export var power_damage: int = 1
@export var power_interval: float = 30
@export var power_scene: PackedScene
@export var max_health: int = 100
@export var health: int = max_health
@export var death_prefab: PackedScene

var is_running: bool = false
var is_attacking: bool = false
var was_running: bool = false
var deadzone: float = 0.15
var attack_cooldown: float = 0.0
var input_vector: Vector2 = Vector2(0, 0)
var target_velocity
var hitbox_cooldown: float = 0.0
var power_cooldown: float = 0.0


func _process(delta: float) -> void:
	GameManager.player_position = position
	
	read_input()
	
	update_attack_cooldown(delta)
	if Input.is_action_just_pressed("ui_attack"):
		attack()
	
	play_run_idle_animation()
	
	if not is_attacking:
		rotate_sprite()
	
	update_hitbox_detection(delta)
	
	update_power(delta)
	
	health_progress_bar.max_value = max_health
	health_progress_bar.value = health

func _physics_process(_delta: float) -> void:
	target_velocity = input_vector * speed * 100.0
	if is_attacking:
		target_velocity *= 0.25
	
	velocity = lerp(velocity, target_velocity, 0.1)
	
	move_and_slide()


func read_input() -> void:
	input_vector = Input.get_vector("ui_left", "ui_right", "ui_up", "ui_down")
	
	if abs(input_vector.x) < deadzone:
		input_vector.x = 0.0
	if abs(input_vector.y) < deadzone:
		input_vector.y = 0.0
		
	was_running = is_running
	is_running = not input_vector.is_zero_approx()

func play_run_idle_animation() -> void:
	if not is_attacking:
		if was_running != is_running:
			if is_running:
				animation_player.play("run")
			else:
				animation_player.play("idle")

func rotate_sprite() -> void:
	if input_vector.x > 0:
		sprite.flip_h = false
	elif input_vector.x < 0:
		sprite.flip_h = true

func update_attack_cooldown(delta: float) -> void:
	if is_attacking:
		attack_cooldown -= delta
		
		if attack_cooldown <= 0.0:
			is_attacking = false
			is_running = false
			animation_player.play("idle")

func attack() -> void:
	if is_attacking:
		return
	
	animation_player.play("attack_side_1")
	attack_cooldown = 0.6
	is_attacking = true
	
func deal_damage_to_enemies() -> void:
	var bodies = sword_area.get_overlapping_bodies()
	for body in bodies:
		if body.is_in_group("enemies"):
			var enemy: Enemy = body
			var direction_to_enemy = (enemy.position - position).normalized()
			var attack_direction: Vector2
			
			if sprite.flip_h:
				attack_direction = Vector2.LEFT
			else:
				attack_direction = Vector2.RIGHT
			
			var dot_product = direction_to_enemy.dot(attack_direction)
			print(dot_product)
			
			if dot_product >= 0.3:
				enemy.damage(sword_damage)

func damage(amout: int) -> void:
	if health <= 0: return
	
	health -= amout
	
	var tween = create_tween()
	modulate = Color.RED
	tween.set_ease(Tween.EASE_IN)
	tween.set_trans(Tween.TRANS_QUINT)
	tween.tween_property(self, "modulate", Color.WHITE, 0.3)
	
	if health <= 0:
		die()


func die() -> void:
	if death_prefab:
		var death_object = death_prefab.instantiate()
		death_object.position = position
		get_parent().add_child(death_object)
		
	queue_free()
	get_tree().reload_current_scene()

func update_hitbox_detection(delta: float) -> void:
	hitbox_cooldown -= delta
	if hitbox_cooldown > 0: return
	
	hitbox_cooldown = 0.5
	
	var bodies = hitbox_area.get_overlapping_bodies()
	
	for body in bodies:
		if body.is_in_group("enemies"):
			var _enemy: Enemy = body
			var damage_amount = 1
			damage(damage_amount)
			
	

func heal(amount: int) -> int:
	health += amount
	if health > max_health:
		health = max_health
	return health

func update_power(delta: float) -> void:
	power_cooldown -= delta
	if power_cooldown > 0: return
	
	power_cooldown = power_interval
	
	var power = power_scene.instantiate()
	power.damage_amount = power_damage
	add_child(power)
