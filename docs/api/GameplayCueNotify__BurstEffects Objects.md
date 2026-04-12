## GameplayCueNotify\_BurstEffects Objects

```python
class GameplayCueNotify_BurstEffects(StructBase)
```

FGameplayCueNotify_BurstEffects

    Set of effects to spawn for a single event, used by all gameplay cue notify types.

**C++ Source:**

- **Plugin**: GameplayAbilities
- **Module**: GameplayAbilities
- **File**: GameplayCueNotifyTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``burst_camera_lens_effect`` (GameplayCueNotify_CameraLensEffectInfo):  [Read-Write] Camera lens effect to be played on gameplay cue execution.  This should never use a looping effect!
- ``burst_camera_shake`` (GameplayCueNotify_CameraShakeInfo):  [Read-Write] Camera shake to be played on gameplay cue execution.  This should never use a looping effect!
- ``burst_decal`` (GameplayCueNotify_DecalInfo):  [Read-Write] Decal to be spawned on gameplay cue execution.  Actor should have fade out time or override should be set so it will clean up properly.
- ``burst_device_property_effect`` (GameplayCueNotify_InputDevicePropertyInfo):  [Read-Write] Input device properties to be applied on gameplay cue execution
- ``burst_force_feedback`` (GameplayCueNotify_ForceFeedbackInfo):  [Read-Write] Force feedback to be played on gameplay cue execution.  This should never use a looping effect!
- ``burst_particles`` (Array[GameplayCueNotify_ParticleInfo]):  [Read-Write] Particle systems to be spawned on gameplay cue execution.  These should never use looping effects!
- ``burst_sounds`` (Array[GameplayCueNotify_SoundInfo]):  [Read-Write] Sound to be played on gameplay cue execution.  These should never use looping effects!

<a id="unreal.GameplayCueNotify_BurstEffects.__init__"></a>

#### \_\_init\_\_

```python
def __init__(
    burst_particles: Array[GameplayCueNotify_ParticleInfo] = [],
    burst_sounds: Array[GameplayCueNotify_SoundInfo] = [],
    burst_camera_shake: GameplayCueNotify_CameraShakeInfo = [
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
    burst_camera_lens_effect: GameplayCueNotify_CameraLensEffectInfo = [
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
    burst_force_feedback: GameplayCueNotify_ForceFeedbackInfo = [
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
    burst_device_property_effect: GameplayCueNotify_InputDevicePropertyInfo = [
        []
    ],
    burst_decal: GameplayCueNotify_DecalInfo = [
        [
            GameplayCueNotify_LocallyControlledSource.INSTIGATOR_ACTOR,
            GameplayCueNotify_LocallyControlledPolicy.ALWAYS, 1.000000, [], []
        ],
        [
            "None", GameplayCueNotify_AttachPolicy.DO_NOT_ATTACH,
            AttachmentRule.KEEP_WORLD, False, True,
            [0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]
        ], None, [128.000000, 256.000000,
                  256.000000], False, False, False, 0.000000, 0.000000
    ]
) -> None
```

<a id="unreal.GameplayCueNotify_BurstEffects.burst_particles"></a>

#### burst\_particles

```python
@property
def burst_particles() -> Array[GameplayCueNotify_ParticleInfo]
```

(Array[GameplayCueNotify_ParticleInfo]):  [Read-Only] Particle systems to be spawned on gameplay cue execution.  These should never use looping effects!

<a id="unreal.GameplayCueNotify_BurstEffects.burst_sounds"></a>

#### burst\_sounds

```python
@property
def burst_sounds() -> Array[GameplayCueNotify_SoundInfo]
```

(Array[GameplayCueNotify_SoundInfo]):  [Read-Only] Sound to be played on gameplay cue execution.  These should never use looping effects!

<a id="unreal.GameplayCueNotify_BurstEffects.burst_camera_shake"></a>

#### burst\_camera\_shake

```python
@property
def burst_camera_shake() -> GameplayCueNotify_CameraShakeInfo
```

(GameplayCueNotify_CameraShakeInfo):  [Read-Only] Camera shake to be played on gameplay cue execution.  This should never use a looping effect!

<a id="unreal.GameplayCueNotify_BurstEffects.burst_camera_lens_effect"></a>

#### burst\_camera\_lens\_effect

```python
@property
def burst_camera_lens_effect() -> GameplayCueNotify_CameraLensEffectInfo
```

(GameplayCueNotify_CameraLensEffectInfo):  [Read-Only] Camera lens effect to be played on gameplay cue execution.  This should never use a looping effect!

<a id="unreal.GameplayCueNotify_BurstEffects.burst_force_feedback"></a>

#### burst\_force\_feedback

```python
@property
def burst_force_feedback() -> GameplayCueNotify_ForceFeedbackInfo
```

(GameplayCueNotify_ForceFeedbackInfo):  [Read-Only] Force feedback to be played on gameplay cue execution.  This should never use a looping effect!

<a id="unreal.GameplayCueNotify_BurstEffects.burst_device_property_effect"></a>

#### burst\_device\_property\_effect

```python
@property
def burst_device_property_effect(
) -> GameplayCueNotify_InputDevicePropertyInfo
```

(GameplayCueNotify_InputDevicePropertyInfo):  [Read-Only] Input device properties to be applied on gameplay cue execution

<a id="unreal.GameplayCueNotify_BurstEffects.burst_decal"></a>

#### burst\_decal

```python
@property
def burst_decal() -> GameplayCueNotify_DecalInfo
```

(GameplayCueNotify_DecalInfo):  [Read-Only] Decal to be spawned on gameplay cue execution.  Actor should have fade out time or override should be set so it will clean up properly.

<a id="unreal.GameplayCueNotify_LoopingEffects"></a>