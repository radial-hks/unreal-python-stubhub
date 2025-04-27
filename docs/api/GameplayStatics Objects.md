## GameplayStatics Objects

```python
class GameplayStatics(BlueprintFunctionLibrary)
```

Static class with useful gameplay utility functions that can be called from both Blueprint and C++

**C++ Source:**

- **Module**: Engine
- **File**: GameplayStatics.h

<a id="unreal.GameplayStatics.un_retain_all_sounds_in_sound_class"></a>

#### un_retain_all_sounds_in_sound_class

```python
@classmethod
def un_retain_all_sounds_in_sound_class(cls, sound_class: SoundClass) -> None
```

X.un_retain_all_sounds_in_sound_class(sound_class) -> None
Iterate through all sound waves and releases handles to retained chunks. (If the chunk is not being played it will be up for eviction)

Args:
    sound_class (SoundClass):

<a id="unreal.GameplayStatics.unload_stream_level_by_soft_object_ptr"></a>

#### unload_stream_level_by_soft_object_ptr

```python
@classmethod
def unload_stream_level_by_soft_object_ptr(
        cls, world_context_object: Object, level: World,
        latent_info: LatentActionInfo, should_block_on_unload: bool) -> None
```

X.unload_stream_level_by_soft_object_ptr(world_context_object, level, latent_info, should_block_on_unload) -> None
Unload a streamed in level (by Object Reference)

Args:
    world_context_object (Object): 
    level (World): 
    latent_info (LatentActionInfo): 
    should_block_on_unload (bool):

<a id="unreal.GameplayStatics.unload_stream_level"></a>

#### unload_stream_level

```python
@classmethod
def unload_stream_level(cls, world_context_object: Object, level_name: Name,
                        latent_info: LatentActionInfo,
                        should_block_on_unload: bool) -> None
```

X.unload_stream_level(world_context_object, level_name, latent_info, should_block_on_unload) -> None
Unload a streamed in level (by Name)

Args:
    world_context_object (Object): 
    level_name (Name): 
    latent_info (LatentActionInfo): 
    should_block_on_unload (bool):

<a id="unreal.GameplayStatics.transform_world_to_first_person"></a>

#### transform_world_to_first_person

```python
@classmethod
def transform_world_to_first_person(cls, view_info: MinimalViewInfo,
                                    world_position: Vector,
                                    ignore_first_person_scale: bool) -> Vector
```

X.transform_world_to_first_person(view_info, world_position, ignore_first_person_scale) -> Vector
Transforms a world space location into "first person space". This function mirrors the morphing that is applied to first person primitives
when they are rendered on the GPU, so it can be used for spawning objects (e.g. projectiles or ejected shell casings) relative to the morphed
first person geometry on screen.

Args:
    view_info (MinimalViewInfo): FMinimalViewInfo struct holding the first person camera parameters.
    world_position (Vector): World space position to transform.
    ignore_first_person_scale (bool): Ignores the scaling that is applied to first person primitives which can be useful when spawning full size world space projectiles relative to a first person weapon.

Returns:
    Vector:

<a id="unreal.GameplayStatics.suggest_projectile_velocity_moving_target"></a>

#### suggest_projectile_velocity_moving_target

```python
@classmethod
def suggest_projectile_velocity_moving_target(
    cls,
    world_context_object: Object,
    projectile_start_location: Vector,
    target_actor: Actor,
    target_location_offset: Vector = [0.000000, 0.000000, 0.000000],
    gravity_z_override: float = 0.000000,
    time_to_target: float = 1.000000,
    draw_debug_type: DrawDebugTrace = DrawDebugTrace.NONE,
    draw_debug_time: float = 3.000000,
    draw_debug_color: LinearColor = [1.000000, 0.000000, 0.000000, 1.000000]
) -> Optional[Vector]
```

X.suggest_projectile_velocity_moving_target(world_context_object, projectile_start_location, target_actor, target_location_offset=[0.000000, 0.000000, 0.000000], gravity_z_override=0.000000, time_to_target=1.000000, draw_debug_type=DrawDebugTrace.NONE, draw_debug_time=3.000000, draw_debug_color=[1.000000, 0.000000, 0.000000, 1.000000]) -> Vector or None
Returns a launch velocity need for a projectile to hit the TargetActor in TimeToTarget seconds based on the TargetActor's current velocity.
This assumes the projectile is only accelerated by gravity (i.e. no outside forces), and that the TargetActor is moving at a constant velocity.

Args:
    world_context_object (Object): 
    projectile_start_location (Vector): Location the projectile is launched from
    target_actor (Actor): Actor that the projectile should hit in TimeToTarget seconds
    target_location_offset (Vector): Offset to apply to the location the projectile is aiming for
    gravity_z_override (double): Optional override of WorldGravityZ
    time_to_target (double): Time (in seconds) between the projectile being launched and the projectile hitting the TargetActor - clamped to be at least 0.1
    draw_debug_type (DrawDebugTrace): 
    draw_debug_time (float): 
    draw_debug_color (LinearColor): 

Returns:
    Vector or None: 

    out_launch_velocity (Vector): The launch velocity returned from this calculation

<a id="unreal.GameplayStatics.suggest_projectile_velocity_custom_arc"></a>

#### suggest_projectile_velocity_custom_arc

```python
@classmethod
def suggest_projectile_velocity_custom_arc(
        cls,
        world_context_object: Object,
        start_pos: Vector,
        end_pos: Vector,
        override_gravity_z: float = 0.000000,
        arc_param: float = 0.500000) -> Optional[Vector]
```

X.suggest_projectile_velocity_custom_arc(world_context_object, start_pos, end_pos, override_gravity_z=0.000000, arc_param=0.500000) -> Vector or None
Returns the launch velocity needed for a projectile at rest at StartPos to land on EndPos.
Assumes a medium arc (e.g. 45 deg on level ground). Projectile velocity is variable and unconstrained.
Does no tracing.

Args:
    world_context_object (Object): 
    start_pos (Vector): Start position of the simulation
    end_pos (Vector): Desired end location for the simulation
    override_gravity_z (float): Optional override of WorldGravityZ
    arc_param (float): Change height of arc between 0.0-1.0 where 0.5 is the default medium arc, 0 is up, and 1 is directly toward EndPos.

Returns:
    Vector or None: 

    out_launch_velocity (Vector): Returns the launch velocity required to reach the EndPos

<a id="unreal.GameplayStatics.spawn_sound_attached"></a>

#### spawn_sound_attached

```python
@classmethod
def spawn_sound_attached(
        cls,
        sound: SoundBase,
        attach_to_component: SceneComponent,
        attach_point_name: Name = "None",
        location: Vector = [0.000000, 0.000000, 0.000000],
        rotation: Rotator = [0.000000, 0.000000, 0.000000],
        location_type: AttachLocation = AttachLocation.KEEP_RELATIVE_OFFSET,
        stop_when_attached_to_destroyed: bool = False,
        volume_multiplier: float = 1.000000,
        pitch_multiplier: float = 1.000000,
        start_time: float = 0.000000,
        attenuation_settings: SoundAttenuation = None,
        concurrency_settings: SoundConcurrency = None,
        auto_destroy: bool = True) -> AudioComponent
```

X.spawn_sound_attached(sound, attach_to_component, attach_point_name="None", location=[0.000000, 0.000000, 0.000000], rotation=[0.000000, 0.000000, 0.000000], location_type=AttachLocation.KEEP_RELATIVE_OFFSET, stop_when_attached_to_destroyed=False, volume_multiplier=1.000000, pitch_multiplier=1.000000, start_time=0.000000, attenuation_settings=None, concurrency_settings=None, auto_destroy=True) -> AudioComponent
This function allows users to create and play Audio Components attached to a specific Scene Component.
Useful for spatialized and/or distance-attenuated sounds that need to follow another object in space.

Args:
    sound (SoundBase): sound to play
    attach_to_component (SceneComponent): 
    attach_point_name (Name): Optional named point within the AttachComponent to play the sound at
    location (Vector): Depending on the value of Location Type this is either a relative offset from the attach component/point or an absolute world position that will be translated to a relative offset
    rotation (Rotator): Depending on the value of Location Type this is either a relative offset from the attach component/point or an absolute world rotation that will be translated to a relative offset
    location_type (AttachLocation): Specifies whether Location is a relative offset or an absolute world position
    stop_when_attached_to_destroyed (bool): Specifies whether the sound should stop playing when the owner of the attach to component is destroyed.
    volume_multiplier (float): A linear scalar multiplied with the volume, in order to make the sound louder or softer.
    pitch_multiplier (float): A linear scalar multiplied with the pitch.
    start_time (float): How far in to the sound to begin playback at
    attenuation_settings (SoundAttenuation): Override attenuation settings package to play sound with
    concurrency_settings (SoundConcurrency): Override concurrency settings package to play sound with
    auto_destroy (bool): Whether the returned audio component will be automatically cleaned up when the sound finishes (by completing or stopping) or whether it can be reactivated

Returns:
    AudioComponent: An audio component to manipulate the spawned sound

<a id="unreal.GameplayStatics.play_sound_attached"></a>

#### play_sound_attached

```python
@classmethod
def play_sound_attached(
        cls,
        sound: SoundBase,
        attach_to_component: SceneComponent,
        attach_point_name: Name = "None",
        location: Vector = [0.000000, 0.000000, 0.000000],
        rotation: Rotator = [0.000000, 0.000000, 0.000000],
        location_type: AttachLocation = AttachLocation.KEEP_RELATIVE_OFFSET,
        stop_when_attached_to_destroyed: bool = False,
        volume_multiplier: float = 1.000000,
        pitch_multiplier: float = 1.000000,
        start_time: float = 0.000000,
        attenuation_settings: SoundAttenuation = None,
        concurrency_settings: SoundConcurrency = None,
        auto_destroy: bool = True) -> AudioComponent
```

deprecated: 'play_sound_attached' was renamed to 'spawn_sound_attached'.

<a id="unreal.GameplayStatics.spawn_sound_at_location"></a>

#### spawn_sound_at_location

```python
@classmethod
def spawn_sound_at_location(cls,
                            world_context_object: Object,
                            sound: SoundBase,
                            location: Vector,
                            rotation: Rotator = [0.000000, 0.000000, 0.000000],
                            volume_multiplier: float = 1.000000,
                            pitch_multiplier: float = 1.000000,
                            start_time: float = 0.000000,
                            attenuation_settings: SoundAttenuation = None,
                            concurrency_settings: SoundConcurrency = None,
                            auto_destroy: bool = True) -> AudioComponent
```

X.spawn_sound_at_location(world_context_object, sound, location, rotation=[0.000000, 0.000000, 0.000000], volume_multiplier=1.000000, pitch_multiplier=1.000000, start_time=0.000000, attenuation_settings=None, concurrency_settings=None, auto_destroy=True) -> AudioComponent
Spawns a sound at the given location. This does not travel with any actor. Replication is also not handled at this point.

Args:
    world_context_object (Object): 
    sound (SoundBase): sound to play
    location (Vector): World position to play sound at
    rotation (Rotator): World rotation to play sound at
    volume_multiplier (float): A linear scalar multiplied with the volume, in order to make the sound louder or softer.
    pitch_multiplier (float): A linear scalar multiplied with the pitch.
    start_time (float): How far in to the sound to begin playback at
    attenuation_settings (SoundAttenuation): Override attenuation settings package to play sound with
    concurrency_settings (SoundConcurrency): Override concurrency settings package to play sound with
    auto_destroy (bool): Whether the returned audio component will be automatically cleaned up when the sound finishes (by completing or stopping) or whether it can be reactivated

Returns:
    AudioComponent: An audio component to manipulate the spawned sound

<a id="unreal.GameplayStatics.spawn_sound2d"></a>

#### spawn_sound2d

```python
@classmethod
def spawn_sound2d(cls,
                  world_context_object: Object,
                  sound: SoundBase,
                  volume_multiplier: float = 1.000000,
                  pitch_multiplier: float = 1.000000,
                  start_time: float = 0.000000,
                  concurrency_settings: SoundConcurrency = None,
                  persist_across_level_transition: bool = False,
                  auto_destroy: bool = True) -> AudioComponent
```

X.spawn_sound2d(world_context_object, sound, volume_multiplier=1.000000, pitch_multiplier=1.000000, start_time=0.000000, concurrency_settings=None, persist_across_level_transition=False, auto_destroy=True) -> AudioComponent
This function allows users to create Audio Components with settings specifically for non-spatialized,
non-distance-attenuated sounds. Audio Components created using this function by default will not have
Spatialization applied. Sound instances will begin playing upon spawning this Audio Component.

* Not Replicated.

Args:
    world_context_object (Object): 
    sound (SoundBase): Sound to play.
    volume_multiplier (float): A linear scalar multiplied with the volume, in order to make the sound louder or softer.
    pitch_multiplier (float): A linear scalar multiplied with the pitch.
    start_time (float): How far in to the sound to begin playback at
    concurrency_settings (SoundConcurrency): Override concurrency settings package to play sound with
    persist_across_level_transition (bool): 
    auto_destroy (bool): Whether the returned audio component will be automatically cleaned up when the sound finishes (by completing or stopping) or whether it can be reactivated

Returns:
    AudioComponent: An audio component to manipulate the spawned sound

<a id="unreal.GameplayStatics.spawn_force_feedback_attached"></a>

#### spawn_force_feedback_attached

```python
@classmethod
def spawn_force_feedback_attached(
        cls,
        force_feedback_effect: ForceFeedbackEffect,
        attach_to_component: SceneComponent,
        attach_point_name: Name = "None",
        location: Vector = [0.000000, 0.000000, 0.000000],
        rotation: Rotator = [0.000000, 0.000000, 0.000000],
        location_type: AttachLocation = AttachLocation.KEEP_RELATIVE_OFFSET,
        stop_when_attached_to_destroyed: bool = False,
        looping: bool = False,
        intensity_multiplier: float = 1.000000,
        start_time: float = 0.000000,
        attenuation_settings: ForceFeedbackAttenuation = None,
        auto_destroy: bool = True) -> ForceFeedbackComponent
```

X.spawn_force_feedback_attached(force_feedback_effect, attach_to_component, attach_point_name="None", location=[0.000000, 0.000000, 0.000000], rotation=[0.000000, 0.000000, 0.000000], location_type=AttachLocation.KEEP_RELATIVE_OFFSET, stop_when_attached_to_destroyed=False, looping=False, intensity_multiplier=1.000000, start_time=0.000000, attenuation_settings=None, auto_destroy=True) -> ForceFeedbackComponent
Plays a force feedback effect attached to and following the specified component. This is a fire and forget effect. Replication is also not handled at this point.

Args:
    force_feedback_effect (ForceFeedbackEffect): effect to play
    attach_to_component (SceneComponent): 
    attach_point_name (Name): Optional named point within the AttachComponent to attach to
    location (Vector): Depending on the value of Location Type this is either a relative offset from the attach component/point or an absolute world position that will be translated to a relative offset
    rotation (Rotator): Depending on the value of Location Type this is either a relative offset from the attach component/point or an absolute world rotation that will be translated to a relative offset
    location_type (AttachLocation): Specifies whether Location is a relative offset or an absolute world position
    stop_when_attached_to_destroyed (bool): Specifies whether the feedback effect should stop playing when the owner of the attach to component is destroyed.
    looping (bool): 
    intensity_multiplier (float): Intensity multiplier
    start_time (float): How far in to the feedback effect to begin playback at
    attenuation_settings (ForceFeedbackAttenuation): Override attenuation settings package to play effect with
    auto_destroy (bool): Whether the returned force feedback component will be automatically cleaned up when the feedback patern finishes (by completing or stopping) or whether it can be reactivated

Returns:
    ForceFeedbackComponent: Force Feedback Component to manipulate the playing feedback effect with

<a id="unreal.GameplayStatics.spawn_force_feedback_at_location"></a>

#### spawn_force_feedback_at_location

```python
@classmethod
def spawn_force_feedback_at_location(
        cls,
        world_context_object: Object,
        force_feedback_effect: ForceFeedbackEffect,
        location: Vector,
        rotation: Rotator = [0.000000, 0.000000, 0.000000],
        looping: bool = False,
        intensity_multiplier: float = 1.000000,
        start_time: float = 0.000000,
        attenuation_settings: ForceFeedbackAttenuation = None,
        auto_destroy: bool = True) -> ForceFeedbackComponent
```

X.spawn_force_feedback_at_location(world_context_object, force_feedback_effect, location, rotation=[0.000000, 0.000000, 0.000000], looping=False, intensity_multiplier=1.000000, start_time=0.000000, attenuation_settings=None, auto_destroy=True) -> ForceFeedbackComponent
Plays a force feedback effect at the given location. This is a fire and forget effect and does not travel with any actor. Replication is also not handled at this point.

Args:
    world_context_object (Object): 
    force_feedback_effect (ForceFeedbackEffect): effect to play
    location (Vector): World position to center the effect at
    rotation (Rotator): World rotation to center the effect at
    looping (bool): 
    intensity_multiplier (float): Intensity multiplier
    start_time (float): How far in to the feedback effect to begin playback at
    attenuation_settings (ForceFeedbackAttenuation): Override attenuation settings package to play effect with
    auto_destroy (bool): Whether the returned force feedback component will be automatically cleaned up when the feedback pattern finishes (by completing or stopping) or whether it can be reactivated

Returns:
    ForceFeedbackComponent: Force Feedback Component to manipulate the playing feedback effect with

<a id="unreal.GameplayStatics.spawn_emitter_attached"></a>

#### spawn_emitter_attached

```python
@classmethod
def spawn_emitter_attached(
        cls,
        emitter_template: ParticleSystem,
        attach_to_component: SceneComponent,
        attach_point_name: Name = "None",
        location: Vector = [0.000000, 0.000000, 0.000000],
        rotation: Rotator = [0.000000, 0.000000, 0.000000],
        scale: Vector = [1.000000, 1.000000, 1.000000],
        location_type: AttachLocation = AttachLocation.KEEP_RELATIVE_OFFSET,
        auto_destroy: bool = True,
        pooling_method: PSCPoolMethod = PSCPoolMethod.NONE,
        auto_activate: bool = True) -> ParticleSystemComponent
```

X.spawn_emitter_attached(emitter_template, attach_to_component, attach_point_name="None", location=[0.000000, 0.000000, 0.000000], rotation=[0.000000, 0.000000, 0.000000], scale=[1.000000, 1.000000, 1.000000], location_type=AttachLocation.KEEP_RELATIVE_OFFSET, auto_destroy=True, pooling_method=PSCPoolMethod.NONE, auto_activate=True) -> ParticleSystemComponent
Plays the specified effect attached to and following the specified component. The system will go away when the effect is complete. Does not replicate.

Args:
    emitter_template (ParticleSystem): particle system to create
    attach_to_component (SceneComponent): 
    attach_point_name (Name): Optional named point within the AttachComponent to spawn the emitter at
    location (Vector): Depending on the value of LocationType this is either a relative offset from the attach component/point or an absolute world location that will be translated to a relative offset (if LocationType is KeepWorldPosition).
    rotation (Rotator): Depending on the value of LocationType this is either a relative offset from the attach component/point or an absolute world rotation that will be translated to a relative offset (if LocationType is KeepWorldPosition).
    scale (Vector): Depending on the value of LocationType this is either a relative scale from the attach component or an absolute world scale that will be translated to a relative scale (if LocationType is KeepWorldPosition).
    location_type (AttachLocation): Specifies whether Location is a relative offset or an absolute world position
    auto_destroy (bool): Whether the component will automatically be destroyed when the particle system completes playing or whether it can be reactivated
    pooling_method (PSCPoolMethod): Method used for pooling this component. Defaults to none.
    auto_activate (bool): Whether the component will be automatically activated on creation.

Returns:
    ParticleSystemComponent:

<a id="unreal.GameplayStatics.spawn_emitter_at_location"></a>

#### spawn_emitter_at_location

```python
@classmethod
def spawn_emitter_at_location(
        cls,
        world_context_object: Object,
        emitter_template: ParticleSystem,
        location: Vector,
        rotation: Rotator = [0.000000, 0.000000, 0.000000],
        scale: Vector = [1.000000, 1.000000, 1.000000],
        auto_destroy: bool = True,
        pooling_method: PSCPoolMethod = PSCPoolMethod.NONE,
        auto_activate_system: bool = True) -> ParticleSystemComponent
```

X.spawn_emitter_at_location(world_context_object, emitter_template, location, rotation=[0.000000, 0.000000, 0.000000], scale=[1.000000, 1.000000, 1.000000], auto_destroy=True, pooling_method=PSCPoolMethod.NONE, auto_activate_system=True) -> ParticleSystemComponent
Plays the specified effect at the given location and rotation, fire and forget. The system will go away when the effect is complete. Does not replicate.

Args:
    world_context_object (Object): Object that we can obtain a world context from
    emitter_template (ParticleSystem): particle system to create
    location (Vector): location to place the effect in world space
    rotation (Rotator): rotation to place the effect in world space
    scale (Vector): scale to create the effect at
    auto_destroy (bool): Whether the component will automatically be destroyed when the particle system completes playing or whether it can be reactivated
    pooling_method (PSCPoolMethod): Method used for pooling this component. Defaults to none.
    auto_activate_system (bool): 

Returns:
    ParticleSystemComponent:

<a id="unreal.GameplayStatics.spawn_dialogue_attached"></a>

#### spawn_dialogue_attached

```python
@classmethod
def spawn_dialogue_attached(
        cls,
        dialogue: DialogueWave,
        context: DialogueContext,
        attach_to_component: SceneComponent,
        attach_point_name: Name = "None",
        location: Vector = [0.000000, 0.000000, 0.000000],
        rotation: Rotator = [0.000000, 0.000000, 0.000000],
        location_type: AttachLocation = AttachLocation.KEEP_RELATIVE_OFFSET,
        stop_when_attached_to_destroyed: bool = False,
        volume_multiplier: float = 1.000000,
        pitch_multiplier: float = 1.000000,
        start_time: float = 0.000000,
        attenuation_settings: SoundAttenuation = None,
        auto_destroy: bool = True) -> AudioComponent
```

X.spawn_dialogue_attached(dialogue, context, attach_to_component, attach_point_name="None", location=[0.000000, 0.000000, 0.000000], rotation=[0.000000, 0.000000, 0.000000], location_type=AttachLocation.KEEP_RELATIVE_OFFSET, stop_when_attached_to_destroyed=False, volume_multiplier=1.000000, pitch_multiplier=1.000000, start_time=0.000000, attenuation_settings=None, auto_destroy=True) -> AudioComponent
Spawns a DialogueWave, a special type of Asset that requires Context data in order to resolve a specific SoundBase,
    which is then passed on to the new Audio Component. This function allows users to create and play Audio Components
    attached to a specific Scene Component. Useful for spatialized and/or distance-attenuated dialogue that needs to
    follow another object in space.

Args:
    dialogue (DialogueWave): dialogue to play
    context (DialogueContext): context the dialogue is to play in
    attach_to_component (SceneComponent): 
    attach_point_name (Name): Optional named point within the AttachComponent to play the sound at
    location (Vector): Depending on the value of Location Type this is either a relative offset from the attach component/point or an absolute world position that will be translated to a relative offset
    rotation (Rotator): Depending on the value of Location Type this is either a relative offset from the attach component/point or an absolute world rotation that will be translated to a relative offset
    location_type (AttachLocation): Specifies whether Location is a relative offset or an absolute world position
    stop_when_attached_to_destroyed (bool): Specifies whether the sound should stop playing when the owner its attached to is destroyed.
    volume_multiplier (float): A linear scalar multiplied with the volume, in order to make the sound louder or softer.
    pitch_multiplier (float): A linear scalar multiplied with the pitch.
    start_time (float): How far in to the dialogue to begin playback at
    attenuation_settings (SoundAttenuation): Override attenuation settings package to play sound with
    auto_destroy (bool): Whether the returned audio component will be automatically cleaned up when the sound finishes (by completing or stopping) or whether it can be reactivated

Returns:
    AudioComponent: Audio Component to manipulate the playing dialogue with

<a id="unreal.GameplayStatics.play_dialogue_attached"></a>

#### play_dialogue_attached

```python
@classmethod
def play_dialogue_attached(
        cls,
        dialogue: DialogueWave,
        context: DialogueContext,
        attach_to_component: SceneComponent,
        attach_point_name: Name = "None",
        location: Vector = [0.000000, 0.000000, 0.000000],
        rotation: Rotator = [0.000000, 0.000000, 0.000000],
        location_type: AttachLocation = AttachLocation.KEEP_RELATIVE_OFFSET,
        stop_when_attached_to_destroyed: bool = False,
        volume_multiplier: float = 1.000000,
        pitch_multiplier: float = 1.000000,
        start_time: float = 0.000000,
        attenuation_settings: SoundAttenuation = None,
        auto_destroy: bool = True) -> AudioComponent
```

deprecated: 'play_dialogue_attached' was renamed to 'spawn_dialogue_attached'.

<a id="unreal.GameplayStatics.spawn_dialogue_at_location"></a>

#### spawn_dialogue_at_location

```python
@classmethod
def spawn_dialogue_at_location(cls,
                               world_context_object: Object,
                               dialogue: DialogueWave,
                               context: DialogueContext,
                               location: Vector,
                               rotation: Rotator = [
                                   0.000000, 0.000000, 0.000000
                               ],
                               volume_multiplier: float = 1.000000,
                               pitch_multiplier: float = 1.000000,
                               start_time: float = 0.000000,
                               attenuation_settings: SoundAttenuation = None,
                               auto_destroy: bool = True) -> AudioComponent
```

X.spawn_dialogue_at_location(world_context_object, dialogue, context, location, rotation=[0.000000, 0.000000, 0.000000], volume_multiplier=1.000000, pitch_multiplier=1.000000, start_time=0.000000, attenuation_settings=None, auto_destroy=True) -> AudioComponent
Spawns a DialogueWave, a special type of Asset that requires Context data in order to resolve a specific SoundBase,
which is then passed on to the new Audio Component. This function allows users to create and play Audio Components at a
specific World Location and Rotation. Useful for spatialized and/or distance-attenuated dialogue.

Args:
    world_context_object (Object): 
    dialogue (DialogueWave): Dialogue to play
    context (DialogueContext): Context the dialogue is to play in
    location (Vector): World position to play dialogue at
    rotation (Rotator): World rotation to play dialogue at
    volume_multiplier (float): A linear scalar multiplied with the volume, in order to make the sound louder or softer.
    pitch_multiplier (float): A linear scalar multiplied with the pitch.
    start_time (float): How far into the dialogue to begin playback at
    attenuation_settings (SoundAttenuation): Override attenuation settings package to play sound with
    auto_destroy (bool): Whether the returned audio component will be automatically cleaned up when the sound finishes (by completing or stopping) or whether it can be reactivated

Returns:
    AudioComponent: Audio Component to manipulate the playing dialogue with

<a id="unreal.GameplayStatics.spawn_dialogue2d"></a>

#### spawn_dialogue2d

```python
@classmethod
def spawn_dialogue2d(cls,
                     world_context_object: Object,
                     dialogue: DialogueWave,
                     context: DialogueContext,
                     volume_multiplier: float = 1.000000,
                     pitch_multiplier: float = 1.000000,
                     start_time: float = 0.000000,
                     auto_destroy: bool = True) -> AudioComponent
```

X.spawn_dialogue2d(world_context_object, dialogue, context, volume_multiplier=1.000000, pitch_multiplier=1.000000, start_time=0.000000, auto_destroy=True) -> AudioComponent
Spawns a DialogueWave, a special type of Asset that requires Context data in order to resolve a specific SoundBase,
which is then passed on to the new Audio Component. Audio Components created using this function by default will not
have Spatialization applied. Sound instances will begin playing upon spawning this Audio Component.

* Not Replicated.

Args:
    world_context_object (Object): 
    dialogue (DialogueWave): dialogue to play
    context (DialogueContext): context the dialogue is to play in
    volume_multiplier (float): A linear scalar multiplied with the volume, in order to make the sound louder or softer.
    pitch_multiplier (float): A linear scalar multiplied with the pitch.
    start_time (float): How far in to the dialogue to begin playback at
    auto_destroy (bool): Whether the returned audio component will be automatically cleaned up when the sound finishes (by completing or stopping) or whether it can be reactivated

Returns:
    AudioComponent: An audio component to manipulate the spawned sound

<a id="unreal.GameplayStatics.spawn_decal_attached"></a>

#### spawn_decal_attached

```python
@classmethod
def spawn_decal_attached(
        cls,
        decal_material: MaterialInterface,
        decal_size: Vector,
        attach_to_component: SceneComponent,
        attach_point_name: Name = "None",
        location: Vector = [0.000000, 0.000000, 0.000000],
        rotation: Rotator = [0.000000, 0.000000, 0.000000],
        location_type: AttachLocation = AttachLocation.KEEP_RELATIVE_OFFSET,
        life_span: float = 0.000000) -> DecalComponent
```

X.spawn_decal_attached(decal_material, decal_size, attach_to_component, attach_point_name="None", location=[0.000000, 0.000000, 0.000000], rotation=[0.000000, 0.000000, 0.000000], location_type=AttachLocation.KEEP_RELATIVE_OFFSET, life_span=0.000000) -> DecalComponent
Spawns a decal attached to and following the specified component. Does not replicate.

Args:
    decal_material (MaterialInterface): decal's material
    decal_size (Vector): size of decal
    attach_to_component (SceneComponent): 
    attach_point_name (Name): Optional named point within the AttachComponent to spawn the emitter at
    location (Vector): Depending on the value of Location Type this is either a relative offset from the attach component/point or an absolute world position that will be translated to a relative offset
    rotation (Rotator): Depending on the value of LocationType this is either a relative offset from the attach component/point or an absolute world rotation that will be translated to a realative offset
    location_type (AttachLocation): Specifies whether Location is a relative offset or an absolute world position
    life_span (float): destroy decal component after time runs out (0 = infinite)

Returns:
    DecalComponent:

<a id="unreal.GameplayStatics.spawn_decal_at_location"></a>

#### spawn_decal_at_location

```python
@classmethod
def spawn_decal_at_location(cls,
                            world_context_object: Object,
                            decal_material: MaterialInterface,
                            decal_size: Vector,
                            location: Vector,
                            rotation: Rotator = [
                                0.000000, -90.000000, 0.000000
                            ],
                            life_span: float = 0.000000) -> DecalComponent
```

X.spawn_decal_at_location(world_context_object, decal_material, decal_size, location, rotation=[0.000000, -90.000000, 0.000000], life_span=0.000000) -> DecalComponent
Spawns a decal at the given location and rotation, fire and forget. Does not replicate.

Args:
    world_context_object (Object): 
    decal_material (MaterialInterface): decal's material
    decal_size (Vector): size of decal
    location (Vector): location to place the decal in world space
    rotation (Rotator): rotation to place the decal in world space
    life_span (float): destroy decal component after time runs out (0 = infinite)

Returns:
    DecalComponent:

<a id="unreal.GameplayStatics.set_world_origin_location"></a>

#### set_world_origin_location

```python
@classmethod
def set_world_origin_location(cls, world_context_object: Object,
                              new_location: IntVector) -> None
```

X.set_world_origin_location(world_context_object, new_location) -> None
Requests a new location for a world origin.

Args:
    world_context_object (Object): 
    new_location (IntVector):

<a id="unreal.GameplayStatics.set_viewport_mouse_capture_mode"></a>

#### set_viewport_mouse_capture_mode

```python
@classmethod
def set_viewport_mouse_capture_mode(
        cls, world_context_object: Object,
        mouse_capture_mode: MouseCaptureMode) -> None
```

X.set_viewport_mouse_capture_mode(world_context_object, mouse_capture_mode) -> None
Sets the current viewport mouse capture mode

Args:
    world_context_object (Object): 
    mouse_capture_mode (MouseCaptureMode):

<a id="unreal.GameplayStatics.set_subtitles_enabled"></a>

#### set_subtitles_enabled

```python
@classmethod
def set_subtitles_enabled(cls, enabled: bool) -> None
```

X.set_subtitles_enabled(enabled) -> None
Will set subtitles to be enabled or disabled.

Args:
    enabled (bool): will enable subtitle drawing if true, disable if false.

<a id="unreal.GameplayStatics.set_sound_mix_class_override"></a>

#### set_sound_mix_class_override

```python
@classmethod
def set_sound_mix_class_override(cls,
                                 world_context_object: Object,
                                 sound_mix_modifier: SoundMix,
                                 sound_class: SoundClass,
                                 volume: float = 1.000000,
                                 pitch: float = 1.000000,
                                 fade_in_time: float = 1.000000,
                                 apply_to_children: bool = True) -> None
```

X.set_sound_mix_class_override(world_context_object, sound_mix_modifier, sound_class, volume=1.000000, pitch=1.000000, fade_in_time=1.000000, apply_to_children=True) -> None
Overrides the sound class adjuster in the given sound mix. If the sound class does not exist in the input sound mix,
    the sound class adjuster will be added to the list of active sound mix modifiers.

Args:
    world_context_object (Object): 
    sound_mix_modifier (SoundMix): The sound mix to modify.
    sound_class (SoundClass): The sound class to override (or add) in the sound mix.
    volume (float): The volume scale to set the sound class adjuster to.
    pitch (float): The pitch scale to set the sound class adjuster to.
    fade_in_time (float): The interpolation time to use to go from the current sound class adjuster values to the new values.
    apply_to_children (bool): Whether or not to apply this override to the sound class' children or to just the specified sound class.

<a id="unreal.GameplayStatics.set_sound_class_distance_scale"></a>

#### set_sound_class_distance_scale

```python
@classmethod
def set_sound_class_distance_scale(cls,
                                   world_context_object: Object,
                                   sound_class: SoundClass,
                                   distance_attenuation_scale: float,
                                   time_sec: float = 0.000000) -> None
```

X.set_sound_class_distance_scale(world_context_object, sound_class, distance_attenuation_scale, time_sec=0.000000) -> None
Linearly interpolates the attenuation distance scale value from it's current attenuation distance override value
(1.0f it not overridden) to its new attenuation distance override, over the given amount of time

* Fire and Forget.
* Not Replicated.

Args:
    world_context_object (Object): 
    sound_class (SoundClass): Sound class to to use to set the attenuation distance scale on.
    distance_attenuation_scale (float): A scalar for the attenuation distance used for computing distance attenuation.
    time_sec (float): A time value to linearly interpolate from the current distance attenuation scale value to the new value.

<a id="unreal.GameplayStatics.set_player_platform_user_id"></a>

#### set_player_platform_user_id

```python
@classmethod
def set_player_platform_user_id(cls, player_controller: PlayerController,
                                user_id: PlatformUserId) -> None
```

X.set_player_platform_user_id(player_controller, user_id) -> None
Sets what platform user id a player should be using. This only works for local player controllers.

Args:
    player_controller (PlayerController): 
    user_id (PlatformUserId):

<a id="unreal.GameplayStatics.set_player_controller_id"></a>

#### set_player_controller_id

```python
@classmethod
def set_player_controller_id(cls, player: PlayerController,
                             controller_id: int) -> None
```

X.set_player_controller_id(player, controller_id) -> None
Sets what physical controller ID a player should be using. This only works for local player controllers.

Args:
    player (PlayerController): The player controller of the player to change the controller ID of
    controller_id (int32): The controller ID to assign to this player

<a id="unreal.GameplayStatics.set_max_audio_channels_scaled"></a>

#### set_max_audio_channels_scaled

```python
@classmethod
def set_max_audio_channels_scaled(cls, world_context_object: Object,
                                  max_channel_count_scale: float) -> None
```

X.set_max_audio_channels_scaled(world_context_object, max_channel_count_scale) -> None
Sets the max number of voices (also known as "channels") dynamically by percentage. E.g. if you want to temporarily
reduce voice count by 50%, use 0.50. Later, you can return to the original max voice count by using 1.0.

Args:
    world_context_object (Object): 
    max_channel_count_scale (float): The percentage of the original voice count to set the max number of voices to

<a id="unreal.GameplayStatics.set_global_time_dilation"></a>

#### set_global_time_dilation

```python
@classmethod
def set_global_time_dilation(cls, world_context_object: Object,
                             time_dilation: float) -> None
```

X.set_global_time_dilation(world_context_object, time_dilation) -> None
Sets the global time dilation.

Args:
    world_context_object (Object): 
    time_dilation (float): value to set the global time dilation to

<a id="unreal.GameplayStatics.set_time_dilation"></a>

#### set_time_dilation

```python
@classmethod
def set_time_dilation(cls, world_context_object: Object,
                      time_dilation: float) -> None
```

deprecated: 'set_time_dilation' was renamed to 'set_global_time_dilation'.

<a id="unreal.GameplayStatics.set_global_pitch_modulation"></a>

#### set_global_pitch_modulation

```python
@classmethod
def set_global_pitch_modulation(cls, world_context_object: Object,
                                pitch_modulation: float,
                                time_sec: float) -> None
```

X.set_global_pitch_modulation(world_context_object, pitch_modulation, time_sec) -> None
Sets a global pitch modulation scalar that will apply to all non-UI sounds

* Fire and Forget.
* Not Replicated.

Args:
    world_context_object (Object): 
    pitch_modulation (float): A pitch modulation value to globally set.
    time_sec (float): A time value to linearly interpolate the global modulation pitch over from it's current value.

<a id="unreal.GameplayStatics.set_global_listener_focus_parameters"></a>

#### set_global_listener_focus_parameters

```python
@classmethod
def set_global_listener_focus_parameters(
        cls,
        world_context_object: Object,
        focus_azimuth_scale: float = 1.000000,
        non_focus_azimuth_scale: float = 1.000000,
        focus_distance_scale: float = 1.000000,
        non_focus_distance_scale: float = 1.000000,
        focus_volume_scale: float = 1.000000,
        non_focus_volume_scale: float = 1.000000,
        focus_priority_scale: float = 1.000000,
        non_focus_priority_scale: float = 1.000000) -> None
```

X.set_global_listener_focus_parameters(world_context_object, focus_azimuth_scale=1.000000, non_focus_azimuth_scale=1.000000, focus_distance_scale=1.000000, non_focus_distance_scale=1.000000, focus_volume_scale=1.000000, non_focus_volume_scale=1.000000, focus_priority_scale=1.000000, non_focus_priority_scale=1.000000) -> None
Sets the global listener focus parameters, which will scale focus behavior of sounds based on their focus azimuth
settings in their attenuation settings.

* Fire and Forget.
* Not Replicated.

Args:
    world_context_object (Object): 
    focus_azimuth_scale (float): An angle scale value used to scale the azimuth angle that defines where sounds are in-focus.
    non_focus_azimuth_scale (float): 
    focus_distance_scale (float): A distance scale value to use for sounds which are in-focus. Values < 1.0 will reduce perceived distance to sounds, values > 1.0 will increase perceived distance to in-focus sounds.
    non_focus_distance_scale (float): A distance scale value to use for sounds which are out-of-focus. Values < 1.0 will reduce perceived distance to sounds, values > 1.0 will increase perceived distance to in-focus sounds.
    focus_volume_scale (float): 
    non_focus_volume_scale (float): 
    focus_priority_scale (float): A priority scale value (> 0.0) to use for sounds which are in-focus. Values < 1.0 will reduce the priority of in-focus sounds, values > 1.0 will increase the priority of in-focus sounds.
    non_focus_priority_scale (float): A priority scale value (> 0.0) to use for sounds which are out-of-focus. Values < 1.0 will reduce the priority of sounds out-of-focus sounds, values > 1.0 will increase the priority of out-of-focus sounds.

<a id="unreal.GameplayStatics.set_game_paused"></a>

#### set_game_paused

```python
@classmethod
def set_game_paused(cls, world_context_object: Object, paused: bool) -> bool
```

X.set_game_paused(world_context_object, paused) -> bool
Sets the game's paused state

Args:
    world_context_object (Object): 
    paused (bool): Whether the game should be paused or not

Returns:
    bool: Whether the game was successfully paused/unpaused

<a id="unreal.GameplayStatics.set_force_disable_splitscreen"></a>

#### set_force_disable_splitscreen

```python
@classmethod
def set_force_disable_splitscreen(cls, world_context_object: Object,
                                  disable: bool) -> None
```

X.set_force_disable_splitscreen(world_context_object, disable) -> None
Enables split screen

Args:
    world_context_object (Object): 
    disable (bool): Whether the viewport should split screen between local players or not

<a id="unreal.GameplayStatics.set_enable_world_rendering"></a>

#### set_enable_world_rendering

```python
@classmethod
def set_enable_world_rendering(cls, world_context_object: Object,
                               enable: bool) -> None
```

X.set_enable_world_rendering(world_context_object, enable) -> None
Enabled rendering of the world

Args:
    world_context_object (Object): 
    enable (bool): Whether the world should be rendered or not

<a id="unreal.GameplayStatics.set_base_sound_mix"></a>

#### set_base_sound_mix

```python
@classmethod
def set_base_sound_mix(cls, world_context_object: Object,
                       sound_mix: SoundMix) -> None
```

X.set_base_sound_mix(world_context_object, sound_mix) -> None
Set the sound mix of the audio system for special EQing

Args:
    world_context_object (Object): 
    sound_mix (SoundMix):

<a id="unreal.GameplayStatics.k2_set_sound_mode"></a>

#### k2_set_sound_mode

```python
@classmethod
def k2_set_sound_mode(cls, world_context_object: Object,
                      sound_mix: SoundMix) -> None
```

deprecated: 'k2_set_sound_mode' was renamed to 'set_base_sound_mix'.

<a id="unreal.GameplayStatics.set_active_spatial_plugin_by_name"></a>

#### set_active_spatial_plugin_by_name

```python
@classmethod
def set_active_spatial_plugin_by_name(cls, world_context_object: Object,
                                      plugin_name: Name) -> bool
```

X.set_active_spatial_plugin_by_name(world_context_object, plugin_name) -> bool
Get list of available Audio Spatialization Plugins

Args:
    world_context_object (Object): 
    plugin_name (Name): 

Returns:
    bool:

<a id="unreal.GameplayStatics.save_game_to_slot"></a>

#### save_game_to_slot

```python
@classmethod
def save_game_to_slot(cls, save_game_object: SaveGame, slot_name: str,
                      user_index: int) -> bool
```

X.save_game_to_slot(save_game_object, slot_name, user_index) -> bool
Save the contents of the SaveGameObject to a platform-specific save slot/file.
note: This will write out all non-transient properties, the SaveGame property flag is not checked

Args:
    save_game_object (SaveGame): Object that contains data about the save game that we want to write out
    slot_name (str): Name of save game slot to save to.
    user_index (int32): The platform user index that identifies the user doing the saving, ignored on some platforms.

Returns:
    bool: Whether we successfully saved this information

<a id="unreal.GameplayStatics.remove_player"></a>

#### remove_player

```python
@classmethod
def remove_player(cls, player: PlayerController, destroy_pawn: bool) -> None
```

X.remove_player(player, destroy_pawn) -> None
Removes a local player from this game.

Args:
    player (PlayerController): The player controller of the player to be removed
    destroy_pawn (bool): Whether the controlled pawn should be deleted as well

<a id="unreal.GameplayStatics.rebase_zero_origin_onto_local"></a>

#### rebase_zero_origin_onto_local

```python
@classmethod
def rebase_zero_origin_onto_local(cls, world_context_object: Object,
                                  world_location: Vector) -> Vector
```

X.rebase_zero_origin_onto_local(world_context_object, world_location) -> Vector
Returns local location for origin based position.

Args:
    world_context_object (Object): 
    world_location (Vector): 

Returns:
    Vector:

<a id="unreal.GameplayStatics.rebase_local_origin_onto_zero"></a>

#### rebase_local_origin_onto_zero

```python
@classmethod
def rebase_local_origin_onto_zero(cls, world_context_object: Object,
                                  world_location: Vector) -> Vector
```

X.rebase_local_origin_onto_zero(world_context_object, world_location) -> Vector
Returns origin based position for local world location.

Args:
    world_context_object (Object): 
    world_location (Vector): 

Returns:
    Vector:

<a id="unreal.GameplayStatics.push_sound_mix_modifier"></a>

#### push_sound_mix_modifier

```python
@classmethod
def push_sound_mix_modifier(cls, world_context_object: Object,
                            sound_mix_modifier: SoundMix) -> None
```

X.push_sound_mix_modifier(world_context_object, sound_mix_modifier) -> None
Push a sound mix modifier onto the audio system

Args:
    world_context_object (Object): 
    sound_mix_modifier (SoundMix): The Sound Mix Modifier to add to the system

<a id="unreal.GameplayStatics.push_sound_mode"></a>

#### push_sound_mode

```python
@classmethod
def push_sound_mode(cls, world_context_object: Object,
                    sound_mix_modifier: SoundMix) -> None
```

deprecated: 'push_sound_mode' was renamed to 'push_sound_mix_modifier'.

<a id="unreal.GameplayStatics.project_world_to_screen"></a>

#### project_world_to_screen

```python
@classmethod
def project_world_to_screen(
        cls,
        player: PlayerController,
        world_position: Vector,
        player_viewport_relative: bool = False) -> Optional[Vector2D]
```

X.project_world_to_screen(player, world_position, player_viewport_relative=False) -> Vector2D or None
Transforms the given 3D world-space point into a its 2D screen space coordinate.

Args:
    player (PlayerController): Project using this player's view.
    world_position (Vector): World position to project.
    player_viewport_relative (bool): Should this be relative to the player viewport subregion (useful when using player attached widgets in split screen)

Returns:
    Vector2D or None: 

    screen_position (Vector2D): (out) Corresponding 2D position in screen space

<a id="unreal.GameplayStatics.prime_sound"></a>

#### prime_sound

```python
@classmethod
def prime_sound(cls, sound: SoundBase) -> None
```

X.prime_sound(sound) -> None
Primes the sound, caching the first chunk of streamed audio.

Args:
    sound (SoundBase):

<a id="unreal.GameplayStatics.prime_all_sounds_in_sound_class"></a>

#### prime_all_sounds_in_sound_class

```python
@classmethod
def prime_all_sounds_in_sound_class(cls, sound_class: SoundClass) -> None
```

X.prime_all_sounds_in_sound_class(sound_class) -> None
Primes the sound waves in the given USoundClass, caching the first chunk of streamed audio.

Args:
    sound_class (SoundClass):

<a id="unreal.GameplayStatics.pop_sound_mix_modifier"></a>

#### pop_sound_mix_modifier

```python
@classmethod
def pop_sound_mix_modifier(cls, world_context_object: Object,
                           sound_mix_modifier: SoundMix) -> None
```

X.pop_sound_mix_modifier(world_context_object, sound_mix_modifier) -> None
Pop a sound mix modifier from the audio system

Args:
    world_context_object (Object): 
    sound_mix_modifier (SoundMix): The Sound Mix Modifier to remove from the system

<a id="unreal.GameplayStatics.pop_sound_mode"></a>

#### pop_sound_mode

```python
@classmethod
def pop_sound_mode(cls, world_context_object: Object,
                   sound_mix_modifier: SoundMix) -> None
```

deprecated: 'pop_sound_mode' was renamed to 'pop_sound_mix_modifier'.

<a id="unreal.GameplayStatics.play_world_camera_shake"></a>

#### play_world_camera_shake

```python
@classmethod
def play_world_camera_shake(
        cls,
        world_context_object: Object,
        shake: Class,
        epicenter: Vector,
        inner_radius: float,
        outer_radius: float,
        falloff: float = 1.000000,
        orient_shake_towards_epicenter: bool = False) -> None
```

X.play_world_camera_shake(world_context_object, shake, epicenter, inner_radius, outer_radius, falloff=1.000000, orient_shake_towards_epicenter=False) -> None
Plays an in-world camera shake that affects all nearby local players, with distance-based attenuation. Does not replicate.

Args:
    world_context_object (Object): Object that we can obtain a world context from
    shake (type(Class)): Camera shake asset to use
    epicenter (Vector): location to place the effect in world space
    inner_radius (float): Cameras inside this radius are ignored
    outer_radius (float): Cameras outside of InnerRadius and inside this are effected
    falloff (float): Affects falloff of effect as it nears OuterRadius
    orient_shake_towards_epicenter (bool): Changes the rotation of shake to point towards epicenter instead of forward

<a id="unreal.GameplayStatics.play_sound_at_location"></a>

#### play_sound_at_location

```python
@classmethod
def play_sound_at_location(
        cls,
        world_context_object: Object,
        sound: SoundBase,
        location: Vector,
        rotation: Rotator,
        volume_multiplier: float = 1.000000,
        pitch_multiplier: float = 1.000000,
        start_time: float = 0.000000,
        attenuation_settings: SoundAttenuation = None,
        concurrency_settings: SoundConcurrency = None,
        owning_actor: Actor = None,
        initial_params: InitialActiveSoundParams = None) -> None
```

X.play_sound_at_location(world_context_object, sound, location, rotation, volume_multiplier=1.000000, pitch_multiplier=1.000000, start_time=0.000000, attenuation_settings=None, concurrency_settings=None, owning_actor=None, initial_params=None) -> None
Plays a sound at the given location. This is a fire and forget sound and does not travel with any actor.
Replication is also not handled at this point.

Args:
    world_context_object (Object): 
    sound (SoundBase): sound to play
    location (Vector): World position to play sound at
    rotation (Rotator): World rotation to play sound at
    volume_multiplier (float): A linear scalar multiplied with the volume, in order to make the sound louder or softer.
    pitch_multiplier (float): A linear scalar multiplied with the pitch.
    start_time (float): How far in to the sound to begin playback at
    attenuation_settings (SoundAttenuation): Override attenuation settings package to play sound with
    concurrency_settings (SoundConcurrency): Override concurrency settings package to play sound with
    owning_actor (Actor): The actor to use as the "owner" for concurrency settings purposes. Allows PlaySound calls to do a concurrency limit per owner.
    initial_params (InitialActiveSoundParams):

<a id="unreal.GameplayStatics.play_sound2d"></a>

#### play_sound2d

```python
@classmethod
def play_sound2d(cls,
                 world_context_object: Object,
                 sound: SoundBase,
                 volume_multiplier: float = 1.000000,
                 pitch_multiplier: float = 1.000000,
                 start_time: float = 0.000000,
                 concurrency_settings: SoundConcurrency = None,
                 owning_actor: Actor = None,
                 is_ui_sound: bool = True) -> None
```

X.play_sound2d(world_context_object, sound, volume_multiplier=1.000000, pitch_multiplier=1.000000, start_time=0.000000, concurrency_settings=None, owning_actor=None, is_ui_sound=True) -> None
Plays a sound directly with no attenuation, perfect for UI sounds.

* Fire and Forget.
* Not Replicated.

Args:
    world_context_object (Object): 
    sound (SoundBase): Sound to play.
    volume_multiplier (float): A linear scalar multiplied with the volume, in order to make the sound louder or softer.
    pitch_multiplier (float): A linear scalar multiplied with the pitch.
    start_time (float): How far in to the sound to begin playback at
    concurrency_settings (SoundConcurrency): Override concurrency settings package to play sound with
    owning_actor (Actor): The actor to use as the "owner" for concurrency settings purposes. Allows PlaySound calls to do a concurrency limit per owner.
    is_ui_sound (bool): True if sound is UI related, else false

<a id="unreal.GameplayStatics.play_dialogue_at_location"></a>

#### play_dialogue_at_location

```python
@classmethod
def play_dialogue_at_location(
        cls,
        world_context_object: Object,
        dialogue: DialogueWave,
        context: DialogueContext,
        location: Vector,
        rotation: Rotator,
        volume_multiplier: float = 1.000000,
        pitch_multiplier: float = 1.000000,
        start_time: float = 0.000000,
        attenuation_settings: SoundAttenuation = None) -> None
```

X.play_dialogue_at_location(world_context_object, dialogue, context, location, rotation, volume_multiplier=1.000000, pitch_multiplier=1.000000, start_time=0.000000, attenuation_settings=None) -> None
Plays a dialogue at the given location. This is a fire and forget sound and does not travel with any actor.
    Replication is also not handled at this point.

Args:
    world_context_object (Object): 
    dialogue (DialogueWave): dialogue to play
    context (DialogueContext): context the dialogue is to play in
    location (Vector): World position to play dialogue at
    rotation (Rotator): World rotation to play dialogue at
    volume_multiplier (float): A linear scalar multiplied with the volume, in order to make the sound louder or softer.
    pitch_multiplier (float): A linear scalar multiplied with the pitch.
    start_time (float): How far in to the dialogue to begin playback at
    attenuation_settings (SoundAttenuation): Override attenuation settings package to play sound with

<a id="unreal.GameplayStatics.play_dialogue2d"></a>

#### play_dialogue2d

```python
@classmethod
def play_dialogue2d(cls,
                    world_context_object: Object,
                    dialogue: DialogueWave,
                    context: DialogueContext,
                    volume_multiplier: float = 1.000000,
                    pitch_multiplier: float = 1.000000,
                    start_time: float = 0.000000) -> None
```

X.play_dialogue2d(world_context_object, dialogue, context, volume_multiplier=1.000000, pitch_multiplier=1.000000, start_time=0.000000) -> None
Plays a dialogue directly with no attenuation, perfect for UI.

* Fire and Forget.
* Not Replicated.

Args:
    world_context_object (Object): 
    dialogue (DialogueWave): dialogue to play
    context (DialogueContext): context the dialogue is to play in
    volume_multiplier (float): A linear scalar multiplied with the volume, in order to make the sound louder or softer.
    pitch_multiplier (float): A linear scalar multiplied with the pitch.
    start_time (float): How far in to the dialogue to begin playback at

<a id="unreal.GameplayStatics.parse_option"></a>

#### parse_option

```python
@classmethod
def parse_option(cls, options: str, key: str) -> str
```

X.parse_option(options, key) -> str
Find an option in the options string and return it.

Args:
    options (str): The string containing the options.
    key (str): The key to find the value of in Options.

Returns:
    str: The value associated with Key if Key found in Options string.

<a id="unreal.GameplayStatics.open_level_by_soft_object_ptr"></a>

#### open_level_by_soft_object_ptr

```python
@classmethod
def open_level_by_soft_object_ptr(cls,
                                  world_context_object: Object,
                                  level: World,
                                  absolute: bool = True,
                                  options: str = "") -> None
```

X.open_level_by_soft_object_ptr(world_context_object, level, absolute=True, options="") -> None
Travel to another level

Args:
    world_context_object (Object): 
    level (World): the level to open
    absolute (bool): if true options are reset, if false options are carried over from current level
    options (str): a string of options to use for the travel URL

<a id="unreal.GameplayStatics.open_level"></a>

#### open_level

```python
@classmethod
def open_level(cls,
               world_context_object: Object,
               level_name: Name,
               absolute: bool = True,
               options: str = "") -> None
```

X.open_level(world_context_object, level_name, absolute=True, options="") -> None
Travel to another level

Args:
    world_context_object (Object): 
    level_name (Name): the level to open
    absolute (bool): if true options are reset, if false options are carried over from current level
    options (str): a string of options to use for the travel URL

<a id="unreal.GameplayStatics.object_is_a"></a>

#### object_is_a

```python
@classmethod
def object_is_a(cls, object: Object, object_class: Class) -> bool
```

X.object_is_a(object, object_class) -> bool
Returns whether or not the object passed in is of (or inherits from) the class type.

Args:
    object (Object): 
    object_class (type(Class)): 

Returns:
    bool: True if the object is of (or inherits from) the class type.

<a id="unreal.GameplayStatics.load_stream_level_by_soft_object_ptr"></a>

#### load_stream_level_by_soft_object_ptr

```python
@classmethod
def load_stream_level_by_soft_object_ptr(
        cls, world_context_object: Object, level: World,
        make_visible_after_load: bool, should_block_on_load: bool,
        latent_info: LatentActionInfo) -> None
```

X.load_stream_level_by_soft_object_ptr(world_context_object, level, make_visible_after_load, should_block_on_load, latent_info) -> None
Stream the level (by Object Reference); Calling again before it finishes has no effect

Args:
    world_context_object (Object): 
    level (World): 
    make_visible_after_load (bool): 
    should_block_on_load (bool): 
    latent_info (LatentActionInfo):

<a id="unreal.GameplayStatics.load_stream_level"></a>

#### load_stream_level

```python
@classmethod
def load_stream_level(cls, world_context_object: Object, level_name: Name,
                      make_visible_after_load: bool,
                      should_block_on_load: bool,
                      latent_info: LatentActionInfo) -> None
```

X.load_stream_level(world_context_object, level_name, make_visible_after_load, should_block_on_load, latent_info) -> None
Stream the level (by Name); Calling again before it finishes has no effect

Args:
    world_context_object (Object): 
    level_name (Name): 
    make_visible_after_load (bool): 
    should_block_on_load (bool): 
    latent_info (LatentActionInfo):

<a id="unreal.GameplayStatics.load_game_from_slot"></a>

#### load_game_from_slot

```python
@classmethod
def load_game_from_slot(cls, slot_name: str, user_index: int) -> SaveGame
```

X.load_game_from_slot(slot_name, user_index) -> SaveGame
Load the contents from a given slot.

Args:
    slot_name (str): Name of the save game slot to load from.
    user_index (int32): The platform user index that identifies the user doing the saving, ignored on some platforms.

Returns:
    SaveGame: Object containing loaded game state (nullptr if load fails)

<a id="unreal.GameplayStatics.is_splitscreen_force_disabled"></a>

#### is_splitscreen_force_disabled

```python
@classmethod
def is_splitscreen_force_disabled(cls, world_context_object: Object) -> bool
```

X.is_splitscreen_force_disabled(world_context_object) -> bool
Returns the split screen state

Args:
    world_context_object (Object): 

Returns:
    bool: Whether the game viewport is split screen or not

<a id="unreal.GameplayStatics.is_game_paused"></a>

#### is_game_paused

```python
@classmethod
def is_game_paused(cls, world_context_object: Object) -> bool
```

X.is_game_paused(world_context_object) -> bool
Returns the game's paused state

Args:
    world_context_object (Object): 

Returns:
    bool: Whether the game is currently paused or not

<a id="unreal.GameplayStatics.is_any_local_player_camera_within_range"></a>

#### is_any_local_player_camera_within_range

```python
@classmethod
def is_any_local_player_camera_within_range(cls, world_context_object: Object,
                                            location: Vector,
                                            maximum_range: float) -> bool
```

X.is_any_local_player_camera_within_range(world_context_object, location, maximum_range) -> bool
Determines if any local player controller's camera is within range of the specified location.
note: This will always return false on dedicated servers.

Args:
    world_context_object (Object): 
    location (Vector): The location from which test range
    maximum_range (float): The distance away from Location to test range

Returns:
    bool:

<a id="unreal.GameplayStatics.has_option"></a>

#### has_option

```python
@classmethod
def has_option(cls, options: str, key: str) -> bool
```

X.has_option(options, key) -> bool
Returns whether a key exists in an options string.

Args:
    options (str): The string containing the options.
    key (str): 

Returns:
    bool: Whether Key was found in Options.

<a id="unreal.GameplayStatics.has_launch_option"></a>

#### has_launch_option

```python
@classmethod
def has_launch_option(cls, option_to_check: str) -> bool
```

X.has_launch_option(option_to_check) -> bool
Checks the commandline to see if the desired option was specified on the commandline (e.g. -demobuild)

Args:
    option_to_check (str): 

Returns:
    bool: True if the launch option was specified on the commandline, false otherwise

<a id="unreal.GameplayStatics.grass_overlapping_sphere_count"></a>

#### grass_overlapping_sphere_count

```python
@classmethod
def grass_overlapping_sphere_count(cls, world_context_object: Object,
                                   static_mesh: StaticMesh,
                                   center_position: Vector,
                                   radius: float) -> int
```

X.grass_overlapping_sphere_count(world_context_object, static_mesh, center_position, radius) -> int32
Counts how many grass foliage instances overlap a given sphere.

Args:
    world_context_object (Object): 
    static_mesh (StaticMesh): 
    center_position (Vector): The center position of the sphere.
    radius (float): The radius of the sphere.

Returns:
    int32: Number of foliage instances with their mesh set to Mesh that overlap the sphere.

<a id="unreal.GameplayStatics.get_world_origin_location"></a>

#### get_world_origin_location

```python
@classmethod
def get_world_origin_location(cls, world_context_object: Object) -> IntVector
```

X.get_world_origin_location(world_context_object) -> IntVector
Returns world origin current location.

Args:
    world_context_object (Object): 

Returns:
    IntVector:

<a id="unreal.GameplayStatics.get_world_delta_seconds"></a>

#### get_world_delta_seconds

```python
@classmethod
def get_world_delta_seconds(cls, world_context_object: Object) -> float
```

X.get_world_delta_seconds(world_context_object) -> double
Returns the frame delta time in seconds, adjusted by time dilation.

Args:
    world_context_object (Object): 

Returns:
    double:

<a id="unreal.GameplayStatics.get_view_projection_matrix"></a>

#### get_view_projection_matrix

```python
@classmethod
def get_view_projection_matrix(
        cls, desired_view: MinimalViewInfo) -> Tuple[Matrix, Matrix, Matrix]
```

X.get_view_projection_matrix(desired_view) -> (view_matrix=Matrix, projection_matrix=Matrix, view_projection_matrix=Matrix)
Returns the View Matrix, Projection Matrix and the View x Projection Matrix for a given view

Args:
    desired_view (MinimalViewInfo): FMinimalViewInfo struct for a camera.

Returns:
    tuple: 

    view_matrix (Matrix): (out) Corresponding View Matrix

    projection_matrix (Matrix): (out) Corresponding Projection Matrix

    view_projection_matrix (Matrix): (out) Corresponding View x Projection Matrix

<a id="unreal.GameplayStatics.get_viewport_mouse_capture_mode"></a>

#### get_viewport_mouse_capture_mode

```python
@classmethod
def get_viewport_mouse_capture_mode(
        cls, world_context_object: Object) -> MouseCaptureMode
```

X.get_viewport_mouse_capture_mode(world_context_object) -> MouseCaptureMode
Returns the current viewport mouse capture mode

Args:
    world_context_object (Object): 

Returns:
    MouseCaptureMode:

<a id="unreal.GameplayStatics.get_unpaused_time_seconds"></a>

#### get_unpaused_time_seconds

```python
@classmethod
def get_unpaused_time_seconds(cls, world_context_object: Object) -> float
```

X.get_unpaused_time_seconds(world_context_object) -> double
Returns time in seconds since world was brought up for play, adjusted by time dilation and IS NOT stopped when game pauses

Args:
    world_context_object (Object): 

Returns:
    double:

<a id="unreal.GameplayStatics.get_time_seconds"></a>

#### get_time_seconds

```python
@classmethod
def get_time_seconds(cls, world_context_object: Object) -> float
```

X.get_time_seconds(world_context_object) -> double
Returns time in seconds since world was brought up for play, adjusted by time dilation and IS stopped when game pauses

Args:
    world_context_object (Object): 

Returns:
    double:

<a id="unreal.GameplayStatics.get_surface_type"></a>

#### get_surface_type

```python
@classmethod
def get_surface_type(cls, hit: HitResult) -> PhysicalSurface
```

X.get_surface_type(hit) -> PhysicalSurface
Returns the EPhysicalSurface type of the given Hit.
To edit surface type for your project, use ProjectSettings/Physics/PhysicalSurface section

Args:
    hit (HitResult): 

Returns:
    PhysicalSurface:

<a id="unreal.GameplayStatics.get_streaming_level"></a>

#### get_streaming_level

```python
@classmethod
def get_streaming_level(cls, world_context_object: Object,
                        package_name: Name) -> LevelStreaming
```

X.get_streaming_level(world_context_object, package_name) -> LevelStreaming
Returns level streaming object with specified level package name

Args:
    world_context_object (Object): 
    package_name (Name): 

Returns:
    LevelStreaming:

<a id="unreal.GameplayStatics.get_real_time_seconds"></a>

#### get_real_time_seconds

```python
@classmethod
def get_real_time_seconds(cls, world_context_object: Object) -> float
```

X.get_real_time_seconds(world_context_object) -> double
Returns time in seconds since world was brought up for play, does NOT stop when game pauses, NOT dilated/clamped

Args:
    world_context_object (Object): 

Returns:
    double:

<a id="unreal.GameplayStatics.get_player_state_from_unique_net_id"></a>

#### get_player_state_from_unique_net_id

```python
@classmethod
def get_player_state_from_unique_net_id(
        cls, world_context_object: Object,
        unique_id: UniqueNetIdRepl) -> PlayerState
```

X.get_player_state_from_unique_net_id(world_context_object, unique_id) -> PlayerState
Returns the player state that matches the passed in online id, or null for an invalid one.
This will work on both the client and server for local and remote players.

Args:
    world_context_object (Object): 
    unique_id (UniqueNetIdRepl): The player's unique net/online id

Returns:
    PlayerState:

<a id="unreal.GameplayStatics.get_player_state"></a>

#### get_player_state

```python
@classmethod
def get_player_state(cls, world_context_object: Object,
                     player_state_index: int) -> PlayerState
```

X.get_player_state(world_context_object, player_state_index) -> PlayerState
Returns the player state at the given index in the game state's PlayerArray.
This will work on both the client and server and the index will be consistent.
After initial replication, all clients and the server will have access to PlayerStates for all connected players.

Args:
    world_context_object (Object): 
    player_state_index (int32): Index into the game state's PlayerArray

Returns:
    PlayerState:

<a id="unreal.GameplayStatics.get_player_pawn"></a>

#### get_player_pawn

```python
@classmethod
def get_player_pawn(cls, world_context_object: Object,
                    player_index: int) -> Pawn
```

X.get_player_pawn(world_context_object, player_index) -> Pawn
Returns the pawn for the player controller at the specified player index.
This will not include pawns of remote clients with no available player controller, you can use the player states list for that.

Args:
    world_context_object (Object): 
    player_index (int32): Index in the player controller list, starting first with local players and then available remote ones

Returns:
    Pawn:

<a id="unreal.GameplayStatics.get_player_controller_id"></a>

#### get_player_controller_id

```python
@classmethod
def get_player_controller_id(cls, player: PlayerController) -> int
```

X.get_player_controller_id(player) -> int32
Gets what physical controller ID a player is using. This only works for local player controllers.

Args:
    player (PlayerController): The player controller of the player to get the ID of

Returns:
    int32: The ID of the passed in player. -1 if there is no physical controller assigned to the passed in player

<a id="unreal.GameplayStatics.get_player_controller_from_platform_user"></a>

#### get_player_controller_from_platform_user

```python
@classmethod
def get_player_controller_from_platform_user(
        cls, world_context_object: Object,
        user_id: PlatformUserId) -> PlayerController
```

X.get_player_controller_from_platform_user(world_context_object, user_id) -> PlayerController
Returns the player controller with the specified physical controller ID. This only works for local players.

Args:
    world_context_object (Object): 
    user_id (PlatformUserId): 

Returns:
    PlayerController:

<a id="unreal.GameplayStatics.get_player_controller_from_id"></a>

#### get_player_controller_from_id

```python
@classmethod
def get_player_controller_from_id(cls, world_context_object: Object,
                                  controller_id: int) -> PlayerController
```

X.get_player_controller_from_id(world_context_object, controller_id) -> PlayerController
Returns the player controller with the specified physical controller ID. This only works for local players.

Args:
    world_context_object (Object): 
    controller_id (int32): Physical controller ID, the same value returned from Get Player Controller ID

Returns:
    PlayerController:

<a id="unreal.GameplayStatics.get_player_controller"></a>

#### get_player_controller

```python
@classmethod
def get_player_controller(cls, world_context_object: Object,
                          player_index: int) -> PlayerController
```

X.get_player_controller(world_context_object, player_index) -> PlayerController
Returns the player controller found while iterating through the local and available remote player controllers.
On a network client, this will only include local players as remote player controllers are not available.
The index will be consistent as long as no new players join or leave, but it will not be the same across different clients and servers.

Args:
    world_context_object (Object): 
    player_index (int32): Index in the player controller list, starting first with local players and then available remote ones

Returns:
    PlayerController:

<a id="unreal.GameplayStatics.get_player_character"></a>

#### get_player_character

```python
@classmethod
def get_player_character(cls, world_context_object: Object,
                         player_index: int) -> Character
```

X.get_player_character(world_context_object, player_index) -> Character
Returns the pawn for the player controller at the specified player index, will return null if the pawn is not a character.
This will not include characters of remote clients with no available player controller, you can iterate the PlayerStates list for that.

Args:
    world_context_object (Object): 
    player_index (int32): Index in the player controller list, starting first with local players and then available remote ones

Returns:
    Character:

<a id="unreal.GameplayStatics.get_player_camera_manager"></a>

#### get_player_camera_manager

```python
@classmethod
def get_player_camera_manager(cls, world_context_object: Object,
                              player_index: int) -> PlayerCameraManager
```

X.get_player_camera_manager(world_context_object, player_index) -> PlayerCameraManager
Returns the camera manager for the Player Controller at the specified player index.
This will not include remote clients with no player controller.

Args:
    world_context_object (Object): 
    player_index (int32): Index in the player controller list, starting first with local players and then available remote ones

Returns:
    PlayerCameraManager:

<a id="unreal.GameplayStatics.get_player_camera"></a>

#### get_player_camera

```python
@classmethod
def get_player_camera(cls, world_context_object: Object,
                      player_index: int) -> PlayerCameraManager
```

deprecated: 'get_player_camera' was renamed to 'get_player_camera_manager'.

<a id="unreal.GameplayStatics.get_platform_name"></a>

#### get_platform_name

```python
@classmethod
def get_platform_name(cls) -> str
```

X.get_platform_name() -> str
Returns the string name of the current platform, to perform different behavior based on platform.
(Platform names include Windows, Mac, Linux, IOS, Android, consoles, etc.).

Returns:
    str:

<a id="unreal.GameplayStatics.get_object_class"></a>

#### get_object_class

```python
@classmethod
def get_object_class(cls, object: Object) -> Class
```

X.get_object_class(object) -> type(Class)
Returns the class of a passed in Object, will always be valid if Object is not NULL

Args:
    object (Object): 

Returns:
    type(Class):

<a id="unreal.GameplayStatics.get_num_player_states"></a>

#### get_num_player_states

```python
@classmethod
def get_num_player_states(cls, world_context_object: Object) -> int
```

X.get_num_player_states(world_context_object) -> int32
Returns the number of active player states, there is one player state for every connected player even if they are a remote client.
Indexes up to this can be use as PlayerStateIndex parameters for other functions.

Args:
    world_context_object (Object): 

Returns:
    int32:

<a id="unreal.GameplayStatics.get_num_player_controllers"></a>

#### get_num_player_controllers

```python
@classmethod
def get_num_player_controllers(cls, world_context_object: Object) -> int
```

X.get_num_player_controllers(world_context_object) -> int32
Returns the total number of available player controllers, including remote players when called on a server.
Indexes up to this can be used as PlayerIndex parameters for the following functions.

Args:
    world_context_object (Object): 

Returns:
    int32:

<a id="unreal.GameplayStatics.get_num_local_player_controllers"></a>

#### get_num_local_player_controllers

```python
@classmethod
def get_num_local_player_controllers(cls, world_context_object: Object) -> int
```

X.get_num_local_player_controllers(world_context_object) -> int32
Returns the number of fully initialized local players, this will be 0 on dedicated servers.
Indexes up to this can be used as PlayerIndex parameters for the following functions, and you are guaranteed to get a local player controller.

Args:
    world_context_object (Object): 

Returns:
    int32:

<a id="unreal.GameplayStatics.get_max_audio_channel_count"></a>

#### get_max_audio_channel_count

```python
@classmethod
def get_max_audio_channel_count(cls, world_context_object: Object) -> int
```

X.get_max_audio_channel_count(world_context_object) -> int32
Retrieves the max voice count currently used by the audio engine.

Args:
    world_context_object (Object): 

Returns:
    int32:

<a id="unreal.GameplayStatics.get_key_value"></a>

#### get_key_value

```python
@classmethod
def get_key_value(cls, pair: str) -> Tuple[str, str]
```

X.get_key_value(pair) -> (key=str, value=str)
Break up a key=value pair into its key and value.

Args:
    pair (str): The string containing a pair to split apart.

Returns:
    tuple: 

    key (str): (out) Key portion of Pair. If no = in string will be the same as Pair.

    value (str): (out) Value portion of Pair. If no = in string will be empty.

<a id="unreal.GameplayStatics.get_int_option"></a>

#### get_int_option

```python
@classmethod
def get_int_option(cls, options: str, key: str, default_value: int) -> int
```

X.get_int_option(options, key, default_value) -> int32
Find an option in the options string and return it as an integer.

Args:
    options (str): The string containing the options.
    key (str): The key to find the value of in Options.
    default_value (int32): 

Returns:
    int32: The value associated with Key as an integer if Key found in Options string, otherwise DefaultValue.

<a id="unreal.GameplayStatics.get_global_time_dilation"></a>

#### get_global_time_dilation

```python
@classmethod
def get_global_time_dilation(cls, world_context_object: Object) -> float
```

X.get_global_time_dilation(world_context_object) -> float
Gets the current global time dilation.

Args:
    world_context_object (Object): 

Returns:
    float: Current time dilation.

<a id="unreal.GameplayStatics.get_game_state"></a>

#### get_game_state

```python
@classmethod
def get_game_state(cls, world_context_object: Object) -> GameStateBase
```

X.get_game_state(world_context_object) -> GameStateBase
Returns the current GameStateBase or Null if it can't be retrieved

Args:
    world_context_object (Object): 

Returns:
    GameStateBase:

<a id="unreal.GameplayStatics.get_game_replication_info"></a>

#### get_game_replication_info

```python
@classmethod
def get_game_replication_info(cls,
                              world_context_object: Object) -> GameStateBase
```

deprecated: 'get_game_replication_info' was renamed to 'get_game_state'.

<a id="unreal.GameplayStatics.get_game_mode"></a>

#### get_game_mode

```python
@classmethod
def get_game_mode(cls, world_context_object: Object) -> GameModeBase
```

X.get_game_mode(world_context_object) -> GameModeBase
Returns the current GameModeBase or Null if it can't be retrieved, such as on the client

Args:
    world_context_object (Object): 

Returns:
    GameModeBase:

<a id="unreal.GameplayStatics.get_game_info"></a>

#### get_game_info

```python
@classmethod
def get_game_info(cls, world_context_object: Object) -> GameModeBase
```

deprecated: 'get_game_info' was renamed to 'get_game_mode'.

<a id="unreal.GameplayStatics.get_game_instance"></a>

#### get_game_instance

```python
@classmethod
def get_game_instance(cls, world_context_object: Object) -> GameInstance
```

X.get_game_instance(world_context_object) -> GameInstance
Returns the game instance object

Args:
    world_context_object (Object): 

Returns:
    GameInstance:

<a id="unreal.GameplayStatics.get_enable_world_rendering"></a>

#### get_enable_world_rendering

```python
@classmethod
def get_enable_world_rendering(cls, world_context_object: Object) -> bool
```

X.get_enable_world_rendering(world_context_object) -> bool
Returns the world rendering state

Args:
    world_context_object (Object): 

Returns:
    bool: Whether the world should be rendered or not

<a id="unreal.GameplayStatics.get_current_reverb_effect"></a>

#### get_current_reverb_effect

```python
@classmethod
def get_current_reverb_effect(cls,
                              world_context_object: Object) -> ReverbEffect
```

X.get_current_reverb_effect(world_context_object) -> ReverbEffect
Returns the highest priority reverb settings currently active from any source (Audio Volumes or manual settings).

Args:
    world_context_object (Object): 

Returns:
    ReverbEffect:

<a id="unreal.GameplayStatics.get_current_level_name"></a>

#### get_current_level_name

```python
@classmethod
def get_current_level_name(cls,
                           world_context_object: Object,
                           remove_prefix_string: bool = True) -> str
```

X.get_current_level_name(world_context_object, remove_prefix_string=True) -> str
Get the name of the currently-open level.

Args:
    world_context_object (Object): 
    remove_prefix_string (bool): remove any streaming- or editor- added prefixes from the level name.

Returns:
    str:

<a id="unreal.GameplayStatics.get_closest_listener_location"></a>

#### get_closest_listener_location

```python
@classmethod
def get_closest_listener_location(
        cls, world_context_object: Object, location: Vector,
        maximum_range: float,
        allow_attenuation_override: bool) -> Optional[Vector]
```

X.get_closest_listener_location(world_context_object, location, maximum_range, allow_attenuation_override) -> Vector or None
Finds and returns the position of the closest listener to the specified location
note: This will always return false if there is no audio device, or the audio device is disabled.

Args:
    world_context_object (Object): 
    location (Vector): The location from which we'd like to find the closest listener, in world space.
    maximum_range (float): The maximum distance away from Location that a listener can be.
    allow_attenuation_override (bool): True for the adjusted listener position (if attenuation override is set), false for the raw listener position (for panning)

Returns:
    Vector or None: true if we've successfully found a listener within MaximumRange of Location, otherwise false.

    listener_position (Vector): [Out] The position of the closest listener in world space, if found.

<a id="unreal.GameplayStatics.get_available_spatial_plugin_names"></a>

#### get_available_spatial_plugin_names

```python
@classmethod
def get_available_spatial_plugin_names(
        cls, world_context_object: Object) -> Array[Name]
```

X.get_available_spatial_plugin_names(world_context_object) -> Array[Name]
Get list of available Audio Spatialization Plugin names

Args:
    world_context_object (Object): 

Returns:
    Array[Name]:

<a id="unreal.GameplayStatics.get_audio_time_seconds"></a>

#### get_audio_time_seconds

```python
@classmethod
def get_audio_time_seconds(cls, world_context_object: Object) -> float
```

X.get_audio_time_seconds(world_context_object) -> double
Returns time in seconds since world was brought up for play, IS stopped when game pauses, NOT dilated/clamped.

Args:
    world_context_object (Object): 

Returns:
    double:

<a id="unreal.GameplayStatics.get_all_actors_with_tag"></a>

#### get_all_actors_with_tag

```python
@classmethod
def get_all_actors_with_tag(cls, world_context_object: Object,
                            tag: Name) -> Array[Actor]
```

X.get_all_actors_with_tag(world_context_object, tag) -> Array[Actor]
Find all Actors in the world with the specified tag.
This is a very slow operation, as it will search over every actor in the world.

Args:
    world_context_object (Object): 
    tag (Name): Tag to find. Must be specified or result array will be empty.

Returns:
    Array[Actor]: 

    out_actors (Array[Actor]): Output array of Actors of the specified tag.

<a id="unreal.GameplayStatics.get_all_actors_with_interface"></a>

#### get_all_actors_with_interface

```python
@classmethod
def get_all_actors_with_interface(cls, world_context_object: Object,
                                  interface: Class) -> Array[Actor]
```

X.get_all_actors_with_interface(world_context_object, interface) -> Array[Actor]
Find all Actors in the world with the specified interface.
This is a very slow operation, as it will search over every actor in the world.

Args:
    world_context_object (Object): 
    interface (type(Class)): Interface to find. Must be specified or result array will be empty.

Returns:
    Array[Actor]: 

    out_actors (Array[Actor]): Output array of Actors of the specified interface.

<a id="unreal.GameplayStatics.get_all_actors_of_class_with_tag"></a>

#### get_all_actors_of_class_with_tag

```python
@classmethod
def get_all_actors_of_class_with_tag(cls, world_context_object: Object,
                                     actor_class: Class,
                                     tag: Name) -> Array[Actor]
```

X.get_all_actors_of_class_with_tag(world_context_object, actor_class, tag) -> Array[Actor]
Find all Actors in the world of the specified class with the specified tag.
This will be slow if there are many actors of the specified class.

Args:
    world_context_object (Object): 
    actor_class (type(Class)): Class of Actor to find. Must be specified or result array will be empty.
    tag (Name): Tag to find. Must be specified or result array will be empty.

Returns:
    Array[Actor]: 

    out_actors (Array[Actor]): Output array of Actors of the specified tag.

<a id="unreal.GameplayStatics.get_all_actors_of_class"></a>

#### get_all_actors_of_class

```python
@classmethod
def get_all_actors_of_class(cls, world_context_object: Object,
                            actor_class: Class) -> Array[Actor]
```

X.get_all_actors_of_class(world_context_object, actor_class) -> Array[Actor]
Find all Actors in the world of the specified class.
This will be slow if there are many actors of the specified class.

Args:
    world_context_object (Object): 
    actor_class (type(Class)): Class of Actor to find. Must be specified or result array will be empty.

Returns:
    Array[Actor]: 

    out_actors (Array[Actor]): Output array of Actors of the specified class.

<a id="unreal.GameplayStatics.get_actor_of_class"></a>

#### get_actor_of_class

```python
@classmethod
def get_actor_of_class(cls, world_context_object: Object,
                       actor_class: Class) -> Actor
```

X.get_actor_of_class(world_context_object, actor_class) -> Actor
Find the first Actor in the world of the specified class.

Args:
    world_context_object (Object): 
    actor_class (type(Class)): Class of Actor to find. Must be specified or result will be empty.

Returns:
    Actor: Actor of the specified class.

<a id="unreal.GameplayStatics.get_actor_array_bounds"></a>

#### get_actor_array_bounds

```python
@classmethod
def get_actor_array_bounds(
        cls, actors: Array[Actor],
        only_colliding_components: bool) -> Tuple[Vector, Vector]
```

X.get_actor_array_bounds(actors, only_colliding_components) -> (center=Vector, box_extent=Vector)
Bind the bounds of an array of Actors

Args:
    actors (Array[Actor]): 
    only_colliding_components (bool): 

Returns:
    tuple: 

    center (Vector): 

    box_extent (Vector):

<a id="unreal.GameplayStatics.get_actor_array_average_location"></a>

#### get_actor_array_average_location

```python
@classmethod
def get_actor_array_average_location(cls, actors: Array[Actor]) -> Vector
```

X.get_actor_array_average_location(actors) -> Vector
Find the average location (centroid) of an array of Actors

Args:
    actors (Array[Actor]): 

Returns:
    Vector:

<a id="unreal.GameplayStatics.get_active_spatial_plugin_name"></a>

#### get_active_spatial_plugin_name

```python
@classmethod
def get_active_spatial_plugin_name(cls, world_context_object: Object) -> Name
```

X.get_active_spatial_plugin_name(world_context_object) -> Name
Get currently active Audio Spatialization Plugin name

Args:
    world_context_object (Object): 

Returns:
    Name:

<a id="unreal.GameplayStatics.get_accurate_real_time"></a>

#### get_accurate_real_time

```python
@classmethod
def get_accurate_real_time(cls) -> Tuple[int, float]
```

X.get_accurate_real_time() -> (seconds=int32, partial_seconds=double)
Returns time in seconds since the application was started. Unlike the other time functions this is accurate to the exact time this function is called instead of set once per frame.

Returns:
    tuple: 

    seconds (int32): 

    partial_seconds (double):

<a id="unreal.GameplayStatics.flush_level_streaming"></a>

#### flush_level_streaming

```python
@classmethod
def flush_level_streaming(cls, world_context_object: Object) -> None
```

X.flush_level_streaming(world_context_object) -> None
Flushes level streaming in blocking fashion and returns when all sub-levels are loaded / visible / hidden

Args:
    world_context_object (Object):

<a id="unreal.GameplayStatics.find_nearest_actor"></a>

#### find_nearest_actor

```python
@classmethod
def find_nearest_actor(cls, origin: Vector,
                       actors_to_check: Array[Actor]) -> Tuple[Actor, float]
```

X.find_nearest_actor(origin, actors_to_check) -> (Actor, distance=float)
Returns an Actor nearest to Origin from ActorsToCheck array.

Args:
    origin (Vector): World Location from which the distance is measured.
    actors_to_check (Array[Actor]): Array of Actors to examine and return Actor nearest to Origin.

Returns:
    float: Nearest Actor.

    distance (float): Distance from Origin to the returned Actor.

<a id="unreal.GameplayStatics.find_collision_uv"></a>

#### find_collision_uv

```python
@classmethod
def find_collision_uv(cls, hit: HitResult,
                      uv_channel: int) -> Optional[Vector2D]
```

X.find_collision_uv(hit, uv_channel) -> Vector2D or None
Try and find the UV for a collision impact. Note this ONLY works if 'Support UV From Hit Results' is enabled in Physics Settings.

Args:
    hit (HitResult): 
    uv_channel (int32): 

Returns:
    Vector2D or None: 

    uv (Vector2D):

<a id="unreal.GameplayStatics.enable_live_streaming"></a>

#### enable_live_streaming

```python
@classmethod
def enable_live_streaming(cls, enable: bool = True) -> None
```

X.enable_live_streaming(enable=True) -> None
Toggle live DVR streaming.

Args:
    enable (bool): If true enable streaming, otherwise disable.

<a id="unreal.GameplayStatics.does_save_game_exist"></a>

#### does_save_game_exist

```python
@classmethod
def does_save_game_exist(cls, slot_name: str, user_index: int) -> bool
```

X.does_save_game_exist(slot_name, user_index) -> bool
See if a save game exists with the specified name.

Args:
    slot_name (str): Name of save game slot.
    user_index (int32): The platform user index that identifies the user doing the saving, ignored on some platforms.

Returns:
    bool:

<a id="unreal.GameplayStatics.deproject_screen_to_world"></a>

#### deproject_screen_to_world

```python
@classmethod
def deproject_screen_to_world(
        cls, player: PlayerController,
        screen_position: Vector2D) -> Optional[Tuple[Vector, Vector]]
```

X.deproject_screen_to_world(player, screen_position) -> (world_position=Vector, world_direction=Vector) or None
Transforms the given 2D screen space coordinate into a 3D world-space point and direction.

Args:
    player (PlayerController): Deproject using this player's view.
    screen_position (Vector2D): 2D screen space to deproject.

Returns:
    tuple or None: 

    world_position (Vector): (out) Corresponding 3D position in world space.

    world_direction (Vector): (out) World space direction vector away from the camera at the given 2d point.

<a id="unreal.GameplayStatics.deproject_scene_capture_to_world"></a>

#### deproject_scene_capture_to_world

```python
@classmethod
def deproject_scene_capture_to_world(
        cls, scene_capture2d: SceneCapture2D,
        target_uv: Vector2D) -> Optional[Tuple[Vector, Vector]]
```

X.deproject_scene_capture_to_world(scene_capture2d, target_uv) -> (world_position=Vector, world_direction=Vector) or None
Transforms the given 2D UV coordinate into a 3D world-space point and direction.

Args:
    scene_capture2d (SceneCapture2D): Deproject using this scene capture's view.
    target_uv (Vector2D): 

Returns:
    tuple or None: 

    world_position (Vector): (out) Corresponding 3D position on camera near plane, in world space.

    world_direction (Vector): (out) World space direction vector away from the camera at the given 2d point.

<a id="unreal.GameplayStatics.deproject_scene_capture_component_to_world"></a>

#### deproject_scene_capture_component_to_world

```python
@classmethod
def deproject_scene_capture_component_to_world(
        cls, scene_capture_component2d: SceneCaptureComponent2D,
        target_uv: Vector2D) -> Optional[Tuple[Vector, Vector]]
```

X.deproject_scene_capture_component_to_world(scene_capture_component2d, target_uv) -> (world_position=Vector, world_direction=Vector) or None
Transforms the given 2D UV coordinate into a 3D world-space point and direction.

Args:
    scene_capture_component2d (SceneCaptureComponent2D): Deproject using this scene capture component's view.
    target_uv (Vector2D): 

Returns:
    tuple or None: 

    world_position (Vector): (out) Corresponding 3D position on camera near plane, in world space.

    world_direction (Vector): (out) World space direction vector away from the camera at the given 2d point.

<a id="unreal.GameplayStatics.delete_game_in_slot"></a>

#### delete_game_in_slot

```python
@classmethod
def delete_game_in_slot(cls, slot_name: str, user_index: int) -> bool
```

X.delete_game_in_slot(slot_name, user_index) -> bool
Delete a save game in a particular slot.

Args:
    slot_name (str): Name of save game slot to delete.
    user_index (int32): The platform user index that identifies the user doing the saving, ignored on some platforms.

Returns:
    bool: True if a file was actually able to be deleted. use DoesSaveGameExist to distinguish between delete failures and failure due to file not existing.

<a id="unreal.GameplayStatics.deactivate_reverb_effect"></a>

#### deactivate_reverb_effect

```python
@classmethod
def deactivate_reverb_effect(cls, world_context_object: Object,
                             tag_name: Name) -> None
```

X.deactivate_reverb_effect(world_context_object, tag_name) -> None
Deactivates a Reverb Effect that was applied outside of an Audio Volume

Args:
    world_context_object (Object): 
    tag_name (Name): Tag associated with Reverb Effect to remove

<a id="unreal.GameplayStatics.create_sound2d"></a>

#### create_sound2d

```python
@classmethod
def create_sound2d(cls,
                   world_context_object: Object,
                   sound: SoundBase,
                   volume_multiplier: float = 1.000000,
                   pitch_multiplier: float = 1.000000,
                   start_time: float = 0.000000,
                   concurrency_settings: SoundConcurrency = None,
                   persist_across_level_transition: bool = False,
                   auto_destroy: bool = True) -> AudioComponent
```

X.create_sound2d(world_context_object, sound, volume_multiplier=1.000000, pitch_multiplier=1.000000, start_time=0.000000, concurrency_settings=None, persist_across_level_transition=False, auto_destroy=True) -> AudioComponent
This function allows users to create Audio Components in advance of playback with settings specifically for non-spatialized,
non-distance-attenuated sounds. Audio Components created using this function by default will not have Spatialization applied.

Args:
    world_context_object (Object): 
    sound (SoundBase): Sound to create.
    volume_multiplier (float): A linear scalar multiplied with the volume, in order to make the sound louder or softer.
    pitch_multiplier (float): A linear scalar multiplied with the pitch.
    start_time (float): How far into the sound to begin playback at
    concurrency_settings (SoundConcurrency): Override concurrency settings package to play sound with
    persist_across_level_transition (bool): 
    auto_destroy (bool): Whether the returned audio component will be automatically cleaned up when the sound finishes (by completing or stopping), or whether it can be reactivated

Returns:
    AudioComponent: An audio component to manipulate the created sound

<a id="unreal.GameplayStatics.create_save_game_object"></a>

#### create_save_game_object

```python
@classmethod
def create_save_game_object(cls, save_game_class: Class) -> SaveGame
```

X.create_save_game_object(save_game_class) -> SaveGame
Create a new, empty SaveGame object to set data on and then pass to SaveGameToSlot.

Args:
    save_game_class (type(Class)): Class of SaveGame to create

Returns:
    SaveGame: New SaveGame object to write data to

<a id="unreal.GameplayStatics.create_player_from_platform_user"></a>

#### create_player_from_platform_user

```python
@classmethod
def create_player_from_platform_user(
        cls,
        world_context_object: Object,
        user_id: PlatformUserId,
        spawn_player_controller: bool = True) -> PlayerController
```

X.create_player_from_platform_user(world_context_object, user_id, spawn_player_controller=True) -> PlayerController
Create a new local player for this game, for cases like local multiplayer.

Args:
    world_context_object (Object): 
    user_id (PlatformUserId): The platform user id that should control the newly created player. A valude of PLATFRMUSERID_NONE specifies to use the next available ID
    spawn_player_controller (bool): Whether a player controller should be spawned immediately for this player. If false a player controller will not be created automatically until transition to the next map.

Returns:
    PlayerController: The created player controller if one is created.

<a id="unreal.GameplayStatics.create_player"></a>

#### create_player

```python
@classmethod
def create_player(cls,
                  world_context_object: Object,
                  controller_id: int = -1,
                  spawn_player_controller: bool = True) -> PlayerController
```

X.create_player(world_context_object, controller_id=-1, spawn_player_controller=True) -> PlayerController
Create a new local player for this game, for cases like local multiplayer.

Args:
    world_context_object (Object): 
    controller_id (int32): The ID of the physical controller that the should control the newly created player. A value of -1 specifies to use the next available ID
    spawn_player_controller (bool): Whether a player controller should be spawned immediately for this player. If false a player controller will not be created automatically until transition to the next map.

Returns:
    PlayerController: The created player controller if one is created.

<a id="unreal.GameplayStatics.clear_sound_mix_modifiers"></a>

#### clear_sound_mix_modifiers

```python
@classmethod
def clear_sound_mix_modifiers(cls, world_context_object: Object) -> None
```

X.clear_sound_mix_modifiers(world_context_object) -> None
Clear all sound mix modifiers from the audio system

Args:
    world_context_object (Object):

<a id="unreal.GameplayStatics.clear_sound_mode"></a>

#### clear_sound_mode

```python
@classmethod
def clear_sound_mode(cls, world_context_object: Object) -> None
```

deprecated: 'clear_sound_mode' was renamed to 'clear_sound_mix_modifiers'.

<a id="unreal.GameplayStatics.clear_sound_mix_class_override"></a>

#### clear_sound_mix_class_override

```python
@classmethod
def clear_sound_mix_class_override(cls,
                                   world_context_object: Object,
                                   sound_mix_modifier: SoundMix,
                                   sound_class: SoundClass,
                                   fade_out_time: float = 1.000000) -> None
```

X.clear_sound_mix_class_override(world_context_object, sound_mix_modifier, sound_class, fade_out_time=1.000000) -> None
Clears any existing override of the Sound Class Adjuster in the given Sound Mix

Args:
    world_context_object (Object): 
    sound_mix_modifier (SoundMix): The sound mix to modify.
    sound_class (SoundClass): The sound class in the sound mix to clear overrides from.
    fade_out_time (float): The interpolation time to use to go from the current sound class adjuster override values to the non-override values.

<a id="unreal.GameplayStatics.cancel_async_loading"></a>

#### cancel_async_loading

```python
@classmethod
def cancel_async_loading(cls) -> None
```

X.cancel_async_loading() -> None
Cancels all currently queued streaming packages

<a id="unreal.GameplayStatics.blueprint_suggest_projectile_velocity"></a>

#### blueprint_suggest_projectile_velocity

```python
@classmethod
def blueprint_suggest_projectile_velocity(
        cls,
        world_context_object: Object,
        start_location: Vector,
        end_location: Vector,
        launch_speed: float,
        override_gravity_z: float,
        trace_option: SuggestProjVelocityTraceOption,
        collision_radius: float,
        favor_high_arc: bool,
        draw_debug: bool,
        accept_closest_on_no_solutions: bool = False) -> Optional[Vector]
```

X.blueprint_suggest_projectile_velocity(world_context_object, start_location, end_location, launch_speed, override_gravity_z, trace_option, collision_radius, favor_high_arc, draw_debug, accept_closest_on_no_solutions=False) -> Vector or None
Calculates an launch velocity for a projectile to hit a specified point.

Args:
    world_context_object (Object): 
    start_location (Vector): Intended launch location
    end_location (Vector): Desired landing location
    launch_speed (float): Desired launch speed
    override_gravity_z (float): Optional gravity override.  0 means "do not override".
    trace_option (SuggestProjVelocityTraceOption): Controls whether or not to validate a clear path by tracing along the calculated arc
    collision_radius (float): Radius of the projectile (assumed spherical), used when tracing
    favor_high_arc (bool): If true and there are 2 valid solutions, will return the higher arc.  If false, will favor the lower arc.
    draw_debug (bool): When true, a debug arc is drawn (red for an invalid arc, green for a valid arc)
    accept_closest_on_no_solutions (bool): If target is unreachable and no solutions are possible, provide a velocity that gets as close to the target as possible given this launch speed

Returns:
    Vector or None: Returns false if there is no valid solution or the valid solutions are blocked.  Returns true otherwise.

    toss_velocity (Vector): (output) Result launch velocity.

<a id="unreal.GameplayStatics.blueprint_predict_projectile_path_by_trace_channel"></a>

#### blueprint_predict_projectile_path_by_trace_channel

```python
@classmethod
def blueprint_predict_projectile_path_by_trace_channel(
    cls,
    world_context_object: Object,
    start_pos: Vector,
    launch_velocity: Vector,
    trace_path: bool = True,
    projectile_radius: float = ...,
    trace_channel: CollisionChannel = CollisionChannel.ECC_WORLD_DYNAMIC,
    trace_complex: bool = ...,
    actors_to_ignore: Array[Actor] = ...,
    draw_debug_type: DrawDebugTrace = ...,
    draw_debug_time: float = ...,
    sim_frequency: float = 15.000000,
    max_sim_time: float = 2.000000,
    override_gravity_z: float = 0.000000
) -> Optional[Tuple[HitResult, Array[Vector], Vector]]
```

X.blueprint_predict_projectile_path_by_trace_channel(world_context_object, start_pos, launch_velocity, trace_path=True, projectile_radius, trace_channel=CollisionChannel.ECC_WORLD_DYNAMIC, trace_complex, actors_to_ignore, draw_debug_type, draw_debug_time, sim_frequency=15.000000, max_sim_time=2.000000, override_gravity_z=0.000000) -> (out_hit=HitResult, out_path_positions=Array[Vector], out_last_trace_destination=Vector) or None
Predict the arc of a virtual projectile affected by gravity with collision checks along the arc. Returns a list of positions of the simulated arc and the destination reached by the simulation.
Returns true if it hit something (if tracing with collision).

Args:
    world_context_object (Object): 
    start_pos (Vector): First start trace location
    launch_velocity (Vector): Velocity the "virtual projectile" is launched at
    trace_path (bool): Trace along the entire path to look for blocking hits
    projectile_radius (float): Radius of the virtual projectile to sweep against the environment
    trace_channel (CollisionChannel): TraceChannel to trace against, if bTracePath is true.
    trace_complex (bool): Use TraceComplex (trace against triangles not primitives)
    actors_to_ignore (Array[Actor]): Actors to exclude from the traces
    draw_debug_type (DrawDebugTrace): Debug type (one-frame, duration, persistent)
    draw_debug_time (float): Duration of debug lines (only relevant for DrawDebugType::Duration)
    sim_frequency (float): Determines size of each sub-step in the simulation (chopping up MaxSimTime)
    max_sim_time (float): Maximum simulation time for the virtual projectile.
    override_gravity_z (float): Optional override of Gravity (if 0, uses WorldGravityZ)

Returns:
    tuple or None: True if hit something along the path (if tracing with collision).

    out_hit (HitResult): Predicted hit result, if the projectile will hit something

    out_path_positions (Array[Vector]): Predicted projectile path. Ordered series of positions from StartPos to the end. Includes location at point of impact if it hit something.

    out_last_trace_destination (Vector): Goal position of the final trace it did. Will not be in the path if there is a hit.

<a id="unreal.GameplayStatics.blueprint_predict_projectile_path_by_object_type"></a>

#### blueprint_predict_projectile_path_by_object_type

```python
@classmethod
def blueprint_predict_projectile_path_by_object_type(
    cls,
    world_context_object: Object,
    start_pos: Vector,
    launch_velocity: Vector,
    trace_path: bool = True,
    projectile_radius: float = ...,
    object_types: Array[ObjectTypeQuery] = ...,
    trace_complex: bool = ...,
    actors_to_ignore: Array[Actor] = ...,
    draw_debug_type: DrawDebugTrace = ...,
    draw_debug_time: float = ...,
    sim_frequency: float = 15.000000,
    max_sim_time: float = 2.000000,
    override_gravity_z: float = 0.000000
) -> Optional[Tuple[HitResult, Array[Vector], Vector]]
```

X.blueprint_predict_projectile_path_by_object_type(world_context_object, start_pos, launch_velocity, trace_path=True, projectile_radius, object_types, trace_complex, actors_to_ignore, draw_debug_type, draw_debug_time, sim_frequency=15.000000, max_sim_time=2.000000, override_gravity_z=0.000000) -> (out_hit=HitResult, out_path_positions=Array[Vector], out_last_trace_destination=Vector) or None
Predict the arc of a virtual projectile affected by gravity with collision checks along the arc. Returns a list of positions of the simulated arc and the destination reached by the simulation.
Returns true if it hit something.

Args:
    world_context_object (Object): 
    start_pos (Vector): First start trace location
    launch_velocity (Vector): Velocity the "virtual projectile" is launched at
    trace_path (bool): Trace along the entire path to look for blocking hits
    projectile_radius (float): Radius of the virtual projectile to sweep against the environment
    object_types (Array[ObjectTypeQuery]): ObjectTypes to trace against, if bTracePath is true.
    trace_complex (bool): Use TraceComplex (trace against triangles not primitives)
    actors_to_ignore (Array[Actor]): Actors to exclude from the traces
    draw_debug_type (DrawDebugTrace): Debug type (one-frame, duration, persistent)
    draw_debug_time (float): Duration of debug lines (only relevant for DrawDebugType::Duration)
    sim_frequency (float): Determines size of each sub-step in the simulation (chopping up MaxSimTime)
    max_sim_time (float): Maximum simulation time for the virtual projectile.
    override_gravity_z (float): Optional override of Gravity (if 0, uses WorldGravityZ)

Returns:
    tuple or None: True if hit something along the path if tracing for collision.

    out_hit (HitResult): Predicted hit result, if the projectile will hit something

    out_path_positions (Array[Vector]): Predicted projectile path. Ordered series of positions from StartPos to the end. Includes location at point of impact if it hit something.

    out_last_trace_destination (Vector): Goal position of the final trace it did. Will not be in the path if there is a hit.

<a id="unreal.GameplayStatics.predict_projectile_path"></a>

#### predict_projectile_path

```python
@classmethod
def predict_projectile_path(
    cls,
    world_context_object: Object,
    start_pos: Vector,
    launch_velocity: Vector,
    trace_path: bool = True,
    projectile_radius: float = ...,
    object_types: Array[ObjectTypeQuery] = ...,
    trace_complex: bool = ...,
    actors_to_ignore: Array[Actor] = ...,
    draw_debug_type: DrawDebugTrace = ...,
    draw_debug_time: float = ...,
    sim_frequency: float = 15.000000,
    max_sim_time: float = 2.000000,
    override_gravity_z: float = 0.000000
) -> Optional[Tuple[HitResult, Array[Vector], Vector]]
```

deprecated: 'predict_projectile_path' was renamed to 'blueprint_predict_projectile_path_by_object_type'.

<a id="unreal.GameplayStatics.blueprint_predict_projectile_path_advanced"></a>

#### blueprint_predict_projectile_path_advanced

```python
@classmethod
def blueprint_predict_projectile_path_advanced(
    cls, world_context_object: Object,
    predict_params: PredictProjectilePathParams
) -> Optional[PredictProjectilePathResult]
```

X.blueprint_predict_projectile_path_advanced(world_context_object, predict_params) -> PredictProjectilePathResult or None
Predict the arc of a virtual projectile affected by gravity with collision checks along the arc.
Returns true if it hit something.

Args:
    world_context_object (Object): 
    predict_params (PredictProjectilePathParams): Input params to the trace (start location, velocity, time to simulate, etc).

Returns:
    PredictProjectilePathResult or None: True if hit something along the path (if tracing with collision).

    predict_result (PredictProjectilePathResult): Output result of the trace (Hit result, array of location/velocity/times for each trace step, etc).

<a id="unreal.GameplayStatics.are_subtitles_enabled"></a>

#### are_subtitles_enabled

```python
@classmethod
def are_subtitles_enabled(cls) -> bool
```

X.are_subtitles_enabled() -> bool
Returns whether or not subtitles are currently enabled.

Returns:
    bool: true if subtitles are enabled.

<a id="unreal.GameplayStatics.are_any_listeners_within_range"></a>

#### are_any_listeners_within_range

```python
@classmethod
def are_any_listeners_within_range(cls, world_context_object: Object,
                                   location: Vector,
                                   maximum_range: float) -> bool
```

X.are_any_listeners_within_range(world_context_object, location, maximum_range) -> bool
Determines if any audio listeners are within range of the specified location
note: This will always return false if there is no audio device, or the audio device is disabled.

Args:
    world_context_object (Object): 
    location (Vector): The location from which test if a listener is in range
    maximum_range (float): The distance away from Location to test if any listener is within

Returns:
    bool:

<a id="unreal.GameplayStatics.apply_radial_damage_with_falloff"></a>

#### apply_radial_damage_with_falloff

```python
@classmethod
def apply_radial_damage_with_falloff(
    cls,
    world_context_object: Object,
    base_damage: float,
    minimum_damage: float,
    origin: Vector,
    damage_inner_radius: float,
    damage_outer_radius: float,
    damage_falloff: float,
    damage_type_class: Class,
    ignore_actors: Array[Actor],
    damage_causer: Actor = None,
    instigated_by_controller: Controller = None,
    damage_prevention_channel: CollisionChannel = CollisionChannel.
    ECC_VISIBILITY
) -> bool
```

X.apply_radial_damage_with_falloff(world_context_object, base_damage, minimum_damage, origin, damage_inner_radius, damage_outer_radius, damage_falloff, damage_type_class, ignore_actors, damage_causer=None, instigated_by_controller=None, damage_prevention_channel=CollisionChannel.ECC_VISIBILITY) -> bool
Hurt locally authoritative actors within the radius. Will only hit components that block the Visibility channel.

Args:
    world_context_object (Object): 
    base_damage (float): The base damage to apply, i.e. the damage at the origin.
    minimum_damage (float): 
    origin (Vector): Epicenter of the damage area.
    damage_inner_radius (float): Radius of the full damage area, from Origin
    damage_outer_radius (float): Radius of the minimum damage area, from Origin
    damage_falloff (float): Falloff exponent of damage from DamageInnerRadius to DamageOuterRadius
    damage_type_class (type(Class)): Class that describes the damage that was done.
    ignore_actors (Array[Actor]): List of Actors to ignore
    damage_causer (Actor): Actor that actually caused the damage (e.g. the grenade that exploded)
    instigated_by_controller (Controller): Controller that was responsible for causing this damage (e.g. player who threw the grenade)
    damage_prevention_channel (CollisionChannel): Damage will not be applied to victim if there is something between the origin and the victim which blocks traces on this channel

Returns:
    bool: true if damage was applied to at least one actor.

<a id="unreal.GameplayStatics.apply_radial_damage"></a>

#### apply_radial_damage

```python
@classmethod
def apply_radial_damage(
    cls,
    world_context_object: Object,
    base_damage: float,
    origin: Vector,
    damage_radius: float,
    damage_type_class: Class,
    ignore_actors: Array[Actor],
    damage_causer: Actor = None,
    instigated_by_controller: Controller = None,
    do_full_damage: bool = False,
    damage_prevention_channel: CollisionChannel = CollisionChannel.
    ECC_VISIBILITY
) -> bool
```

X.apply_radial_damage(world_context_object, base_damage, origin, damage_radius, damage_type_class, ignore_actors, damage_causer=None, instigated_by_controller=None, do_full_damage=False, damage_prevention_channel=CollisionChannel.ECC_VISIBILITY) -> bool
Hurt locally authoritative actors within the radius. Will only hit components that block the Visibility channel.

Args:
    world_context_object (Object): 
    base_damage (float): The base damage to apply, i.e. the damage at the origin.
    origin (Vector): Epicenter of the damage area.
    damage_radius (float): Radius of the damage area, from Origin
    damage_type_class (type(Class)): Class that describes the damage that was done.
    ignore_actors (Array[Actor]): List of Actors to ignore
    damage_causer (Actor): Actor that actually caused the damage (e.g. the grenade that exploded).  This actor will not be damaged and it will not block damage.
    instigated_by_controller (Controller): Controller that was responsible for causing this damage (e.g. player who threw the grenade)
    do_full_damage (bool): 
    damage_prevention_channel (CollisionChannel): Damage will not be applied to victim if there is something between the origin and the victim which blocks traces on this channel

Returns:
    bool: true if damage was applied to at least one actor.

<a id="unreal.GameplayStatics.apply_point_damage"></a>

#### apply_point_damage

```python
@classmethod
def apply_point_damage(cls, damaged_actor: Actor, base_damage: float,
                       hit_from_direction: Vector, hit_info: HitResult,
                       event_instigator: Controller, damage_causer: Actor,
                       damage_type_class: Class) -> float
```

X.apply_point_damage(damaged_actor, base_damage, hit_from_direction, hit_info, event_instigator, damage_causer, damage_type_class) -> float
Hurts the specified actor with the specified impact.

Args:
    damaged_actor (Actor): Actor that will be damaged.
    base_damage (float): The base damage to apply.
    hit_from_direction (Vector): Direction the hit came FROM
    hit_info (HitResult): Collision or trace result that describes the hit
    event_instigator (Controller): Controller that was responsible for causing this damage (e.g. player who shot the weapon)
    damage_causer (Actor): Actor that actually caused the damage (e.g. the grenade that exploded)
    damage_type_class (type(Class)): Class that describes the damage that was done.

Returns:
    float: Actual damage the ended up being applied to the actor.

<a id="unreal.GameplayStatics.apply_damage"></a>

#### apply_damage

```python
@classmethod
def apply_damage(cls, damaged_actor: Actor, base_damage: float,
                 event_instigator: Controller, damage_causer: Actor,
                 damage_type_class: Class) -> float
```

X.apply_damage(damaged_actor, base_damage, event_instigator, damage_causer, damage_type_class) -> float
Hurts the specified actor with generic damage.

Args:
    damaged_actor (Actor): Actor that will be damaged.
    base_damage (float): The base damage to apply.
    event_instigator (Controller): Controller that was responsible for causing this damage (e.g. player who shot the weapon)
    damage_causer (Actor): Actor that actually caused the damage (e.g. the grenade that exploded)
    damage_type_class (type(Class)): Class that describes the damage that was done.

Returns:
    float: Actual damage the ended up being applied to the actor.

<a id="unreal.GameplayStatics.announce_accessible_string"></a>

#### announce_accessible_string

```python
@classmethod
def announce_accessible_string(cls, announcement_string: str) -> None
```

X.announce_accessible_string(announcement_string) -> None
If accessibility is enabled, have the platform announce a string to the player.
These announcements can be interrupted by system accessibiliity announcements or other accessibility announcement requests.
This should be used judiciously as flooding a player with announcements can be overrwhelming and confusing.
Try to make announcements concise and clear.
NOTE: Currently only supported on Win10, Mac, iOS

Args:
    announcement_string (str):

<a id="unreal.GameplayStatics.activate_reverb_effect"></a>

#### activate_reverb_effect

```python
@classmethod
def activate_reverb_effect(cls,
                           world_context_object: Object,
                           reverb_effect: ReverbEffect,
                           tag_name: Name,
                           priority: float = 0.000000,
                           volume: float = 0.500000,
                           fade_time: float = 2.000000) -> None
```

X.activate_reverb_effect(world_context_object, reverb_effect, tag_name, priority=0.000000, volume=0.500000, fade_time=2.000000) -> None
Activates a Reverb Effect without the need for an Audio Volume

Args:
    world_context_object (Object): 
    reverb_effect (ReverbEffect): Reverb Effect to use
    tag_name (Name): Tag to associate with Reverb Effect
    priority (float): Priority of the Reverb Effect
    volume (float): Volume level of Reverb Effect
    fade_time (float): Time before Reverb Effect is fully active

<a id="unreal.GameSession"></a>