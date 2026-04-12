## SubmixEffectStereoToQuadSettings Objects

```python
class SubmixEffectStereoToQuadSettings(StructBase)
```

Submix Effect Stereo to Quad Settings

**C++ Source:**

- **Plugin**: Synthesis
- **Module**: Synthesis
- **File**: SubmixEffectStereoToQuad.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``flip_channels`` (bool):  [Read-Write] Whether or not to flip the left and right input channels when sending to the rear channel.
  This can be useful to have a stereo field when hearing audio to the left and right in surround output configuration.
- ``rear_channel_gain`` (float):  [Read-Write] The gain (in decibels) of the rear channels

<a id="unreal.SubmixEffectStereoToQuadSettings.__init__"></a>

#### \_\_init\_\_

```python
def __init__(flip_channels: bool = False,
             rear_channel_gain: float = 0.000000) -> None
```

<a id="unreal.SubmixEffectStereoToQuadSettings.flip_channels"></a>

#### flip\_channels

```python
@property
def flip_channels() -> bool
```

(bool):  [Read-Write] Whether or not to flip the left and right input channels when sending to the rear channel.
This can be useful to have a stereo field when hearing audio to the left and right in surround output configuration.

<a id="unreal.SubmixEffectStereoToQuadSettings.flip_channels"></a>

#### flip\_channels

```python
@flip_channels.setter
def flip_channels(value: bool) -> None
```

<a id="unreal.SubmixEffectStereoToQuadSettings.rear_channel_gain"></a>

#### rear\_channel\_gain

```python
@property
def rear_channel_gain() -> float
```

(float):  [Read-Write] The gain (in decibels) of the rear channels

<a id="unreal.SubmixEffectStereoToQuadSettings.rear_channel_gain"></a>

#### rear\_channel\_gain

```python
@rear_channel_gain.setter
def rear_channel_gain(value: float) -> None
```

<a id="unreal.TapDelayInfo"></a>