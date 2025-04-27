## AudioBasedVibrationData Objects

```python
class AudioBasedVibrationData(StructBase)
```

Audio Based Vibration Data

**C++ Source:**

- **Module**: Engine
- **File**: InputDeviceProperties.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``sound`` (SoundBase):  [Read-Write] The sound to play on the gamepad. Make sure the set the sound's submix sends to the gamepad audio and vibration endpoints!

<a id="unreal.AudioBasedVibrationData.__init__"></a>

#### __init__

```python
def __init__(sound: SoundBase = None) -> None
```

<a id="unreal.AudioBasedVibrationData.sound"></a>

#### sound

```python
@property
def sound() -> SoundBase
```

(SoundBase):  [Read-Write] The sound to play on the gamepad. Make sure the set the sound's submix sends to the gamepad audio and vibration endpoints!

<a id="unreal.AudioBasedVibrationData.sound"></a>

#### sound

```python
@sound.setter
def sound(value: SoundBase) -> None
```

<a id="unreal.ActivateDevicePropertyParams"></a>