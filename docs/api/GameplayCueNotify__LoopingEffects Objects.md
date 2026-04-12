## GameplayCueNotify\_LoopingEffects Objects

```python
class GameplayCueNotify_LoopingEffects(StructBase)
```

FGameplayCueNotify_LoopingEffects

    Set of looping effects to spawn for looping gameplay cues.

**C++ Source:**

- **Plugin**: GameplayAbilities
- **Module**: GameplayAbilities
- **File**: GameplayCueNotifyTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``looping_camera_lens_effect`` (GameplayCueNotify_CameraLensEffectInfo):  [Read-Write] Camera lens effect to be played on gameplay cue loop start.
- ``looping_camera_shake`` (GameplayCueNotify_CameraShakeInfo):  [Read-Write] Camera shake to be played on gameplay cue loop start.
- ``looping_force_feedback`` (GameplayCueNotify_ForceFeedbackInfo):  [Read-Write] Force feedback to be played on gameplay cue loop start.
- ``looping_input_device_property_effect`` (GameplayCueNotify_InputDevicePropertyInfo):  [Read-Write] Input device properties to be applied on gameplay cue loop start.
- ``looping_particles`` (Array[GameplayCueNotify_ParticleInfo]):  [Read-Write] Particle systems to be spawned on gameplay cue loop start.
- ``looping_sounds`` (Array[GameplayCueNotify_SoundInfo]):  [Read-Write] Sound to be played on gameplay cue loop start.

<a id="unreal.GameplayCueNotify_LoopingEffects.__init__"></a>

#### \_\_init\_\_

```python
def __init__(
    looping_particles: Array[GameplayCueNotify_ParticleInfo] = [],
    looping_sounds: Array[GameplayCueNotify_SoundInfo] = [],
    looping_camera_shake: GameplayCueNotify_CameraShakeInfo = [
        [
            GameplayCueNotify_LocallyControlledSource.INSTIGATOR_ACTOR,
            GameplayCueNotify_LocallyControlledPolicy.ALWAYS, 1.000000, [], []
        ],
        [
            "None", GameplayCueNotify_AttachPolicy.DO_NOT_ATTACH,
            AttachmentRule.KEEP_WORLD, False, True,
            [0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]
        ], None, 1.000000, GameplayCueNotify_EffectPlaySpace.CAMERA_SPACE,
        False, False, False, 0.000000, 0.000000, 1.000000
    ],
    looping_camera_lens_effect: GameplayCueNotify_CameraLensEffectInfo = [
        [
            GameplayCueNotify_LocallyControlledSource.INSTIGATOR_ACTOR,
            GameplayCueNotify_LocallyControlledPolicy.ALWAYS, 1.000000, [], []
        ],
        [
            "None", GameplayCueNotify_AttachPolicy.DO_NOT_ATTACH,
            AttachmentRule.KEEP_WORLD, False, True,
            [0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]
        ], None, False, False, False, 0.000000, 0.000000
    ],
    looping_force_feedback: GameplayCueNotify_ForceFeedbackInfo = [
        [
            GameplayCueNotify_LocallyControlledSource.INSTIGATOR_ACTOR,
            GameplayCueNotify_LocallyControlledPolicy.ALWAYS, 1.000000, [], []
        ],
        [
            "None", GameplayCueNotify_AttachPolicy.DO_NOT_ATTACH,
            AttachmentRule.KEEP_WORLD, False, True,
            [0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]
        ], None, "None", False, False, False, False, 1.000000, None
    ],
    looping_input_device_property_effect:
    GameplayCueNotify_InputDevicePropertyInfo = [[]]
) -> None
```

<a id="unreal.GameplayCueNotify_LoopingEffects.looping_particles"></a>

#### looping\_particles

```python
@property
def looping_particles() -> Array[GameplayCueNotify_ParticleInfo]
```

(Array[GameplayCueNotify_ParticleInfo]):  [Read-Only] Particle systems to be spawned on gameplay cue loop start.

<a id="unreal.GameplayCueNotify_LoopingEffects.looping_sounds"></a>

#### looping\_sounds

```python
@property
def looping_sounds() -> Array[GameplayCueNotify_SoundInfo]
```

(Array[GameplayCueNotify_SoundInfo]):  [Read-Only] Sound to be played on gameplay cue loop start.

<a id="unreal.GameplayCueNotify_LoopingEffects.looping_camera_shake"></a>

#### looping\_camera\_shake

```python
@property
def looping_camera_shake() -> GameplayCueNotify_CameraShakeInfo
```

(GameplayCueNotify_CameraShakeInfo):  [Read-Only] Camera shake to be played on gameplay cue loop start.

<a id="unreal.GameplayCueNotify_LoopingEffects.looping_camera_lens_effect"></a>

#### looping\_camera\_lens\_effect

```python
@property
def looping_camera_lens_effect() -> GameplayCueNotify_CameraLensEffectInfo
```

(GameplayCueNotify_CameraLensEffectInfo):  [Read-Only] Camera lens effect to be played on gameplay cue loop start.

<a id="unreal.GameplayCueNotify_LoopingEffects.looping_force_feedback"></a>

#### looping\_force\_feedback

```python
@property
def looping_force_feedback() -> GameplayCueNotify_ForceFeedbackInfo
```

(GameplayCueNotify_ForceFeedbackInfo):  [Read-Only] Force feedback to be played on gameplay cue loop start.

<a id="unreal.GameplayCueNotify_LoopingEffects.looping_input_device_property_effect"></a>

#### looping\_input\_device\_property\_effect

```python
@property
def looping_input_device_property_effect(
) -> GameplayCueNotify_InputDevicePropertyInfo
```

(GameplayCueNotify_InputDevicePropertyInfo):  [Read-Only] Input device properties to be applied on gameplay cue loop start.

<a id="unreal.GameplayEffectExecutionScopedModifierInfo"></a>