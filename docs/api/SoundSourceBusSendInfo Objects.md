## SoundSourceBusSendInfo Objects

```python
class SoundSourceBusSendInfo(StructBase)
```

Sound Source Bus Send Info

**C++ Source:**

- **Module**: Engine
- **File**: SoundSourceBusSend.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``audio_bus`` (AudioBus):  [Read-Write] An audio bus to send the audio to. Audio buses can be used to route audio to DSP effects or other purposes. E.g. side-chaining, analysis, etc. Audio buses are not audible unless hooked up to a source bus.
- ``custom_send_level_curve`` (RuntimeFloatCurve):  [Read-Write] The custom curve to use for distance-based bus send level.
- ``max_send_distance`` (float):  [Read-Write] The distance at which the max send level is sent to the bus
- ``max_send_level`` (float):  [Read-Write] The amount to send to the bus when sound is located at a distance equal to value specified in the max send distance.
- ``min_send_distance`` (float):  [Read-Write] The distance at which the min send Level is sent to the bus
- ``min_send_level`` (float):  [Read-Write] The amount to send to the bus when sound is located at a distance equal to value specified in the min send distance.
- ``send_level`` (float):  [Read-Write] The amount of audio to send to the bus.
- ``sound_source_bus`` (SoundSourceBus):  [Read-Write] A source Bus to send the audio to. Source buses sonify (make audible) the audio sent to it and are themselves sounds which take up a voice slot in the audio engine.
- ``source_bus_send_level_control_method`` (SourceBusSendLevelControlMethod):  [Read-Write] Manual: Use Send Level only
  Linear: Interpolate between Min and Max Send Levels based on listener distance (between Distance Min and Distance Max)
  Custom Curve: Use the float curve to map Send Level to distance (0.0-1.0 on curve maps to Distance Min - Distance Max)

<a id="unreal.SoundSourceBusSendInfo.__init__"></a>

#### __init__

```python
def __init__(min_send_level: float = 0.000000,
             max_send_level: float = 0.000000,
             min_send_distance: float = 0.000000,
             max_send_distance: float = 0.000000,
             custom_send_level_curve: RuntimeFloatCurve = []) -> None
```

<a id="unreal.SoundSourceBusSendInfo.min_send_level"></a>

#### min_send_level

```python
@property
def min_send_level() -> float
```

(float):  [Read-Write] The amount to send to the bus when sound is located at a distance equal to value specified in the min send distance.

<a id="unreal.SoundSourceBusSendInfo.min_send_level"></a>

#### min_send_level

```python
@min_send_level.setter
def min_send_level(value: float) -> None
```

<a id="unreal.SoundSourceBusSendInfo.max_send_level"></a>

#### max_send_level

```python
@property
def max_send_level() -> float
```

(float):  [Read-Write] The amount to send to the bus when sound is located at a distance equal to value specified in the max send distance.

<a id="unreal.SoundSourceBusSendInfo.max_send_level"></a>

#### max_send_level

```python
@max_send_level.setter
def max_send_level(value: float) -> None
```

<a id="unreal.SoundSourceBusSendInfo.min_send_distance"></a>

#### min_send_distance

```python
@property
def min_send_distance() -> float
```

(float):  [Read-Write] The distance at which the min send Level is sent to the bus

<a id="unreal.SoundSourceBusSendInfo.min_send_distance"></a>

#### min_send_distance

```python
@min_send_distance.setter
def min_send_distance(value: float) -> None
```

<a id="unreal.SoundSourceBusSendInfo.max_send_distance"></a>

#### max_send_distance

```python
@property
def max_send_distance() -> float
```

(float):  [Read-Write] The distance at which the max send level is sent to the bus

<a id="unreal.SoundSourceBusSendInfo.max_send_distance"></a>

#### max_send_distance

```python
@max_send_distance.setter
def max_send_distance(value: float) -> None
```

<a id="unreal.SoundSourceBusSendInfo.custom_send_level_curve"></a>

#### custom_send_level_curve

```python
@property
def custom_send_level_curve() -> RuntimeFloatCurve
```

(RuntimeFloatCurve):  [Read-Write] The custom curve to use for distance-based bus send level.

<a id="unreal.SoundSourceBusSendInfo.custom_send_level_curve"></a>

#### custom_send_level_curve

```python
@custom_send_level_curve.setter
def custom_send_level_curve(value: RuntimeFloatCurve) -> None
```

<a id="unreal.SoundWaveSpectralData"></a>