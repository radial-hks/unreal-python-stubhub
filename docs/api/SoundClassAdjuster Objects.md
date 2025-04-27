## SoundClassAdjuster Objects

```python
class SoundClassAdjuster(StructBase)
```

Elements of data for sound group volume control

**C++ Source:**

- **Module**: Engine
- **File**: SoundMix.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``apply_to_children`` (bool):  [Read-Write] Set to true to apply this adjuster to all children of the sound class.
- ``low_pass_filter_frequency`` (float):  [Read-Write] Lowpass filter cutoff frequency to apply to sound sources.
- ``pitch_adjuster`` (float):  [Read-Write] A multiplier applied to the pitch.
- ``sound_class_object`` (SoundClass):  [Read-Write] The sound class this adjuster affects.
- ``voice_center_channel_volume_adjuster`` (float):  [Read-Write] A multiplier applied to VoiceCenterChannelVolume.
- ``volume_adjuster`` (float):  [Read-Write] A multiplier applied to the volume.

<a id="unreal.SoundClassAdjuster.__init__"></a>

#### __init__

```python
def __init__(sound_class_object: SoundClass = None,
             volume_adjuster: float = 0.000000,
             pitch_adjuster: float = 0.000000,
             low_pass_filter_frequency: float = 0.000000,
             apply_to_children: bool = False,
             voice_center_channel_volume_adjuster: float = 0.000000) -> None
```

<a id="unreal.SoundClassAdjuster.sound_class_object"></a>

#### sound_class_object

```python
@property
def sound_class_object() -> SoundClass
```

(SoundClass):  [Read-Only] The sound class this adjuster affects.

<a id="unreal.SoundClassAdjuster.volume_adjuster"></a>

#### volume_adjuster

```python
@property
def volume_adjuster() -> float
```

(float):  [Read-Only] A multiplier applied to the volume.

<a id="unreal.SoundClassAdjuster.pitch_adjuster"></a>

#### pitch_adjuster

```python
@property
def pitch_adjuster() -> float
```

(float):  [Read-Only] A multiplier applied to the pitch.

<a id="unreal.SoundClassAdjuster.low_pass_filter_frequency"></a>

#### low_pass_filter_frequency

```python
@property
def low_pass_filter_frequency() -> float
```

(float):  [Read-Only] Lowpass filter cutoff frequency to apply to sound sources.

<a id="unreal.SoundClassAdjuster.apply_to_children"></a>

#### apply_to_children

```python
@property
def apply_to_children() -> bool
```

(bool):  [Read-Only] Set to true to apply this adjuster to all children of the sound class.

<a id="unreal.SoundClassAdjuster.voice_center_channel_volume_adjuster"></a>

#### voice_center_channel_volume_adjuster

```python
@property
def voice_center_channel_volume_adjuster() -> float
```

(float):  [Read-Only] A multiplier applied to VoiceCenterChannelVolume.

<a id="unreal.SoundModulationDefaultRoutingSettings"></a>