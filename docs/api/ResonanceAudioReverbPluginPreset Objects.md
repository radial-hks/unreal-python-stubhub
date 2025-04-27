## ResonanceAudioReverbPluginPreset Objects

```python
class ResonanceAudioReverbPluginPreset(SoundEffectSubmixPreset)
```

Resonance Audio Reverb Plugin Preset

**C++ Source:**

- **Plugin**: ResonanceAudio
- **Module**: ResonanceAudio
- **File**: ResonanceAudioReverb.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``settings`` (ResonanceAudioReverbPluginSettings):  [Read-Write]

<a id="unreal.ResonanceAudioReverbPluginPreset.set_room_rotation"></a>

#### set_room_rotation

```python
def set_room_rotation(rotation: Quat) -> None
```

x.set_room_rotation(rotation) -> None
Sets room rotation in 3D space

Args:
    rotation (Quat):

<a id="unreal.ResonanceAudioReverbPluginPreset.set_room_position"></a>

#### set_room_position

```python
def set_room_position(position: Vector) -> None
```

x.set_room_position(position) -> None
Sets room position in 3D space

Args:
    position (Vector):

<a id="unreal.ResonanceAudioReverbPluginPreset.set_room_materials"></a>

#### set_room_materials

```python
def set_room_materials(materials: Array[RaMaterialName]) -> None
```

x.set_room_materials(materials) -> None
Sets Resonance Audio room's acoustic materials

Args:
    materials (Array[RaMaterialName]):

<a id="unreal.ResonanceAudioReverbPluginPreset.set_room_dimensions"></a>

#### set_room_dimensions

```python
def set_room_dimensions(dimensions: Vector) -> None
```

x.set_room_dimensions(dimensions) -> None
Sets room dimensions in 3D space

Args:
    dimensions (Vector):

<a id="unreal.ResonanceAudioReverbPluginPreset.set_reverb_time_modifier"></a>

#### set_reverb_time_modifier

```python
def set_reverb_time_modifier(reverb_time_modifier: float) -> None
```

x.set_reverb_time_modifier(reverb_time_modifier) -> None
Adjusts the reverberation time across all frequency bands by multiplying the computed values by this factor.
Has no effect when set to 1.0

Args:
    reverb_time_modifier (float):

<a id="unreal.ResonanceAudioReverbPluginPreset.set_reverb_gain"></a>

#### set_reverb_gain

```python
def set_reverb_gain(reverb_gain: float) -> None
```

x.set_reverb_gain(reverb_gain) -> None
Sets reverb gain multiplier

Args:
    reverb_gain (float):

<a id="unreal.ResonanceAudioReverbPluginPreset.set_reverb_brightness"></a>

#### set_reverb_brightness

```python
def set_reverb_brightness(reverb_brightness: float) -> None
```

x.set_reverb_brightness(reverb_brightness) -> None
Increases high frequency reverberation times when positive, decreases when negative.
Has no effect when set to 0.0

Args:
    reverb_brightness (float):

<a id="unreal.ResonanceAudioReverbPluginPreset.set_reflection_scalar"></a>

#### set_reflection_scalar

```python
def set_reflection_scalar(reflection_scalar: float) -> None
```

x.set_reflection_scalar(reflection_scalar) -> None
Sets early reflections gain multiplier

Args:
    reflection_scalar (float):

<a id="unreal.ResonanceAudioReverbPluginPreset.set_enable_room_effects"></a>

#### set_enable_room_effects

```python
def set_enable_room_effects(enable_room_effects: bool) -> None
```

x.set_enable_room_effects(enable_room_effects) -> None
Enables/disables Resonance Audio room effects

Args:
    enable_room_effects (bool):

<a id="unreal.ResonanceAudioSpatializationSourceSettings"></a>