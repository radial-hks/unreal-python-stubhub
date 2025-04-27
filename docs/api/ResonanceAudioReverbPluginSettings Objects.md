## ResonanceAudioReverbPluginSettings Objects

```python
class ResonanceAudioReverbPluginSettings(StructBase)
```

Resonance Audio Reverb Plugin Settings

**C++ Source:**

- **Plugin**: ResonanceAudio
- **Module**: ResonanceAudio
- **File**: ResonanceAudioReverb.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``back_wall_material`` (RaMaterialName):  [Read-Write] Back wall acoustic material
- ``ceiling_material`` (RaMaterialName):  [Read-Write] Ceiling acoustic material
- ``enable_room_effects`` (bool):  [Read-Write] Whether Resonance Audio room effects are enabled
- ``floor_material`` (RaMaterialName):  [Read-Write] Floor acoustic material
- ``front_wall_material`` (RaMaterialName):  [Read-Write] Front wall acoustic material
- ``get_transform_from_audio_volume`` (bool):  [Read-Write] Whether the room transform should be taken from the Audio Volume this preset is attached to.
  If not used with the Audio Volume, last saved values will be used.
- ``left_wall_material`` (RaMaterialName):  [Read-Write] Left wall acoustic material
- ``reflection_scalar`` (float):  [Read-Write] Early reflections gain multiplier. Default: 1.0
- ``reverb_brightness`` (float):  [Read-Write] Reverb brightness modifier. Default: 0.0
- ``reverb_gain`` (float):  [Read-Write] Reverb gain multiplier. Default: 1.0
- ``reverb_time_modifier`` (float):  [Read-Write] Reverb time modifier. Default: 1.0
- ``right_wall_material`` (RaMaterialName):  [Read-Write] Right wall acoustic material
- ``room_dimensions`` (Vector):  [Read-Write] Room dimensions in 3D space
- ``room_position`` (Vector):  [Read-Write] Room position in 3D space
- ``room_rotation`` (Quat):  [Read-Write] Room rotation in 3D space

<a id="unreal.ResonanceAudioReverbPluginSettings.__init__"></a>

#### __init__

```python
def __init__(enable_room_effects: bool = False,
             room_position: Vector = [0.000000, 0.000000, 0.000000],
             room_rotation: Quat = [0.000000, 0.000000, 0.000000, 1.000000],
             room_dimensions: Vector = [0.000000, 0.000000, 0.000000],
             left_wall_material: RaMaterialName = RaMaterialName.TRANSPARENT,
             right_wall_material: RaMaterialName = RaMaterialName.TRANSPARENT,
             floor_material: RaMaterialName = RaMaterialName.TRANSPARENT,
             ceiling_material: RaMaterialName = RaMaterialName.TRANSPARENT,
             front_wall_material: RaMaterialName = RaMaterialName.TRANSPARENT,
             back_wall_material: RaMaterialName = RaMaterialName.TRANSPARENT,
             reflection_scalar: float = 0.000000,
             reverb_gain: float = 0.000000,
             reverb_time_modifier: float = 0.000000,
             reverb_brightness: float = 0.000000) -> None
```

<a id="unreal.ResonanceAudioReverbPluginSettings.enable_room_effects"></a>

#### enable_room_effects

```python
@property
def enable_room_effects() -> bool
```

(bool):  [Read-Write] Whether Resonance Audio room effects are enabled

<a id="unreal.ResonanceAudioReverbPluginSettings.enable_room_effects"></a>

#### enable_room_effects

```python
@enable_room_effects.setter
def enable_room_effects(value: bool) -> None
```

<a id="unreal.ResonanceAudioReverbPluginSettings.room_position"></a>

#### room_position

```python
@property
def room_position() -> Vector
```

(Vector):  [Read-Write] Room position in 3D space

<a id="unreal.ResonanceAudioReverbPluginSettings.room_position"></a>

#### room_position

```python
@room_position.setter
def room_position(value: Vector) -> None
```

<a id="unreal.ResonanceAudioReverbPluginSettings.room_rotation"></a>

#### room_rotation

```python
@property
def room_rotation() -> Quat
```

(Quat):  [Read-Write] Room rotation in 3D space

<a id="unreal.ResonanceAudioReverbPluginSettings.room_rotation"></a>

#### room_rotation

```python
@room_rotation.setter
def room_rotation(value: Quat) -> None
```

<a id="unreal.ResonanceAudioReverbPluginSettings.room_dimensions"></a>

#### room_dimensions

```python
@property
def room_dimensions() -> Vector
```

(Vector):  [Read-Write] Room dimensions in 3D space

<a id="unreal.ResonanceAudioReverbPluginSettings.room_dimensions"></a>

#### room_dimensions

```python
@room_dimensions.setter
def room_dimensions(value: Vector) -> None
```

<a id="unreal.ResonanceAudioReverbPluginSettings.left_wall_material"></a>

#### left_wall_material

```python
@property
def left_wall_material() -> RaMaterialName
```

(RaMaterialName):  [Read-Write] Left wall acoustic material

<a id="unreal.ResonanceAudioReverbPluginSettings.left_wall_material"></a>

#### left_wall_material

```python
@left_wall_material.setter
def left_wall_material(value: RaMaterialName) -> None
```

<a id="unreal.ResonanceAudioReverbPluginSettings.right_wall_material"></a>

#### right_wall_material

```python
@property
def right_wall_material() -> RaMaterialName
```

(RaMaterialName):  [Read-Write] Right wall acoustic material

<a id="unreal.ResonanceAudioReverbPluginSettings.right_wall_material"></a>

#### right_wall_material

```python
@right_wall_material.setter
def right_wall_material(value: RaMaterialName) -> None
```

<a id="unreal.ResonanceAudioReverbPluginSettings.floor_material"></a>

#### floor_material

```python
@property
def floor_material() -> RaMaterialName
```

(RaMaterialName):  [Read-Write] Floor acoustic material

<a id="unreal.ResonanceAudioReverbPluginSettings.floor_material"></a>

#### floor_material

```python
@floor_material.setter
def floor_material(value: RaMaterialName) -> None
```

<a id="unreal.ResonanceAudioReverbPluginSettings.ceiling_material"></a>

#### ceiling_material

```python
@property
def ceiling_material() -> RaMaterialName
```

(RaMaterialName):  [Read-Write] Ceiling acoustic material

<a id="unreal.ResonanceAudioReverbPluginSettings.ceiling_material"></a>

#### ceiling_material

```python
@ceiling_material.setter
def ceiling_material(value: RaMaterialName) -> None
```

<a id="unreal.ResonanceAudioReverbPluginSettings.front_wall_material"></a>

#### front_wall_material

```python
@property
def front_wall_material() -> RaMaterialName
```

(RaMaterialName):  [Read-Write] Front wall acoustic material

<a id="unreal.ResonanceAudioReverbPluginSettings.front_wall_material"></a>

#### front_wall_material

```python
@front_wall_material.setter
def front_wall_material(value: RaMaterialName) -> None
```

<a id="unreal.ResonanceAudioReverbPluginSettings.back_wall_material"></a>

#### back_wall_material

```python
@property
def back_wall_material() -> RaMaterialName
```

(RaMaterialName):  [Read-Write] Back wall acoustic material

<a id="unreal.ResonanceAudioReverbPluginSettings.back_wall_material"></a>

#### back_wall_material

```python
@back_wall_material.setter
def back_wall_material(value: RaMaterialName) -> None
```

<a id="unreal.ResonanceAudioReverbPluginSettings.reflection_scalar"></a>

#### reflection_scalar

```python
@property
def reflection_scalar() -> float
```

(float):  [Read-Write] Early reflections gain multiplier. Default: 1.0

<a id="unreal.ResonanceAudioReverbPluginSettings.reflection_scalar"></a>

#### reflection_scalar

```python
@reflection_scalar.setter
def reflection_scalar(value: float) -> None
```

<a id="unreal.ResonanceAudioReverbPluginSettings.reverb_gain"></a>

#### reverb_gain

```python
@property
def reverb_gain() -> float
```

(float):  [Read-Write] Reverb gain multiplier. Default: 1.0

<a id="unreal.ResonanceAudioReverbPluginSettings.reverb_gain"></a>

#### reverb_gain

```python
@reverb_gain.setter
def reverb_gain(value: float) -> None
```

<a id="unreal.ResonanceAudioReverbPluginSettings.reverb_time_modifier"></a>

#### reverb_time_modifier

```python
@property
def reverb_time_modifier() -> float
```

(float):  [Read-Write] Reverb time modifier. Default: 1.0

<a id="unreal.ResonanceAudioReverbPluginSettings.reverb_time_modifier"></a>

#### reverb_time_modifier

```python
@reverb_time_modifier.setter
def reverb_time_modifier(value: float) -> None
```

<a id="unreal.ResonanceAudioReverbPluginSettings.reverb_brightness"></a>

#### reverb_brightness

```python
@property
def reverb_brightness() -> float
```

(float):  [Read-Write] Reverb brightness modifier. Default: 0.0

<a id="unreal.ResonanceAudioReverbPluginSettings.reverb_brightness"></a>

#### reverb_brightness

```python
@reverb_brightness.setter
def reverb_brightness(value: float) -> None
```

<a id="unreal.Synth1PatchCable"></a>