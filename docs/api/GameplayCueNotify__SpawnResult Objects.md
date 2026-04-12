## GameplayCueNotify\_SpawnResult Objects

```python
class GameplayCueNotify_SpawnResult(StructBase)
```

FGameplayCueNotify_SpawnResult

    Temporary structure used to track results of spawning components.

**C++ Source:**

- **Plugin**: GameplayAbilities
- **Module**: GameplayAbilities
- **File**: GameplayCueNotifyTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``audio_components`` (Array[AudioComponent]):  [Read-Write] List of audio components spawned.  There may be null pointers here as it matches the defined order.
- ``camera_lens_effects`` (Array[CameraLensEffectInterface]):  [Read-Write] List of camera len effects spawned.  There will be one camera lens effect per local player controller if the effect is played in world.
- ``camera_shakes`` (Array[CameraShakeBase]):  [Read-Write] List of camera shakes played.  There will be one camera shake per local player controller if shake is played in world.
- ``decal_component`` (DecalComponent):  [Read-Write] Spawned decal component.  This may be null.
- ``force_feedback_component`` (ForceFeedbackComponent):  [Read-Write] Force feedback component that was spawned.  This is only valid when force feedback is set to play in world.
- ``fx_system_components`` (Array[FXSystemComponent]):  [Read-Write] List of FX components spawned.  There may be null pointers here as it matches the defined order.

<a id="unreal.GameplayCueNotify_SpawnResult.__init__"></a>

#### \_\_init\_\_

```python
def __init__(fx_system_components: Array[FXSystemComponent] = [],
             audio_components: Array[AudioComponent] = [],
             camera_shakes: Array[CameraShakeBase] = [],
             camera_lens_effects: Array[CameraLensEffectInterface] = [],
             force_feedback_component: ForceFeedbackComponent = None,
             decal_component: DecalComponent = None) -> None
```

<a id="unreal.GameplayCueNotify_SpawnResult.fx_system_components"></a>

#### fx\_system\_components

```python
@property
def fx_system_components() -> Array[FXSystemComponent]
```

(Array[FXSystemComponent]):  [Read-Only] List of FX components spawned.  There may be null pointers here as it matches the defined order.

<a id="unreal.GameplayCueNotify_SpawnResult.audio_components"></a>

#### audio\_components

```python
@property
def audio_components() -> Array[AudioComponent]
```

(Array[AudioComponent]):  [Read-Only] List of audio components spawned.  There may be null pointers here as it matches the defined order.

<a id="unreal.GameplayCueNotify_SpawnResult.camera_shakes"></a>

#### camera\_shakes

```python
@property
def camera_shakes() -> Array[CameraShakeBase]
```

(Array[CameraShakeBase]):  [Read-Only] List of camera shakes played.  There will be one camera shake per local player controller if shake is played in world.

<a id="unreal.GameplayCueNotify_SpawnResult.camera_lens_effects"></a>

#### camera\_lens\_effects

```python
@property
def camera_lens_effects() -> Array[CameraLensEffectInterface]
```

(Array[CameraLensEffectInterface]):  [Read-Only] List of camera len effects spawned.  There will be one camera lens effect per local player controller if the effect is played in world.

<a id="unreal.GameplayCueNotify_SpawnResult.force_feedback_component"></a>

#### force\_feedback\_component

```python
@property
def force_feedback_component() -> ForceFeedbackComponent
```

(ForceFeedbackComponent):  [Read-Only] Force feedback component that was spawned.  This is only valid when force feedback is set to play in world.

<a id="unreal.GameplayCueNotify_SpawnResult.decal_component"></a>

#### decal\_component

```python
@property
def decal_component() -> DecalComponent
```

(DecalComponent):  [Read-Only] Spawned decal component.  This may be null.

<a id="unreal.GameplayCueNotify_ParticleInfo"></a>