## SoundSubmixSendInfoBase Objects

```python
class SoundSubmixSendInfoBase(StructBase)
```

Common set of settings that are uses as submix sends.

**C++ Source:**

- **Module**: Engine
- **File**: SoundSubmixSend.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``custom_send_level_curve`` (RuntimeFloatCurve):  [Read-Write] The custom reverb send curve to use for distance-based send level.
- ``disable_manual_send_clamp`` (bool):  [Read-Write] Whether to disable the 0-1 clamp for manual SendLevel control
- ``max_send_distance`` (float):  [Read-Write] The max distance to send to the master
- ``max_send_level`` (float):  [Read-Write] The amount to send to master when sound is located at a distance equal to value specified in the max send distance.
- ``min_send_distance`` (float):  [Read-Write] The min distance to send to the master
- ``min_send_level`` (float):  [Read-Write] The amount to send to master when sound is located at a distance equal to value specified in the min send distance.
- ``send_level`` (float):  [Read-Write] The amount of audio to send
- ``send_level_control_method`` (SendLevelControlMethod):  [Read-Write] Manual: Use Send Level only
  Linear: Interpolate between Min and Max Send Levels based on listener distance (between Distance Min and Distance Max)
  Custom Curve: Use the float curve to map Send Level to distance (0.0-1.0 on curve maps to Distance Min - Distance Max)
- ``sound_submix`` (SoundSubmixBase):  [Read-Write] The submix to send the audio to

<a id="unreal.SoundSubmixSendInfoBase.__init__"></a>

#### __init__

```python
def __init__(send_level_control_method:
             SendLevelControlMethod = SendLevelControlMethod.LINEAR,
             sound_submix: SoundSubmixBase = None,
             send_level: float = 0.000000,
             disable_manual_send_clamp: bool = False,
             min_send_level: float = 0.000000,
             max_send_level: float = 0.000000,
             min_send_distance: float = 0.000000,
             max_send_distance: float = 0.000000,
             custom_send_level_curve: RuntimeFloatCurve = []) -> None
```

<a id="unreal.SoundSubmixSendInfoBase.send_level_control_method"></a>

#### send_level_control_method

```python
@property
def send_level_control_method() -> SendLevelControlMethod
```

(SendLevelControlMethod):  [Read-Write] Manual: Use Send Level only
Linear: Interpolate between Min and Max Send Levels based on listener distance (between Distance Min and Distance Max)
Custom Curve: Use the float curve to map Send Level to distance (0.0-1.0 on curve maps to Distance Min - Distance Max)

<a id="unreal.SoundSubmixSendInfoBase.send_level_control_method"></a>

#### send_level_control_method

```python
@send_level_control_method.setter
def send_level_control_method(value: SendLevelControlMethod) -> None
```

<a id="unreal.SoundSubmixSendInfoBase.sound_submix"></a>

#### sound_submix

```python
@property
def sound_submix() -> SoundSubmixBase
```

(SoundSubmixBase):  [Read-Write] The submix to send the audio to

<a id="unreal.SoundSubmixSendInfoBase.sound_submix"></a>

#### sound_submix

```python
@sound_submix.setter
def sound_submix(value: SoundSubmixBase) -> None
```

<a id="unreal.SoundSubmixSendInfoBase.send_level"></a>

#### send_level

```python
@property
def send_level() -> float
```

(float):  [Read-Write] The amount of audio to send

<a id="unreal.SoundSubmixSendInfoBase.send_level"></a>

#### send_level

```python
@send_level.setter
def send_level(value: float) -> None
```

<a id="unreal.SoundSubmixSendInfoBase.disable_manual_send_clamp"></a>

#### disable_manual_send_clamp

```python
@property
def disable_manual_send_clamp() -> bool
```

(bool):  [Read-Write] Whether to disable the 0-1 clamp for manual SendLevel control

<a id="unreal.SoundSubmixSendInfoBase.disable_manual_send_clamp"></a>

#### disable_manual_send_clamp

```python
@disable_manual_send_clamp.setter
def disable_manual_send_clamp(value: bool) -> None
```

<a id="unreal.SoundSubmixSendInfoBase.min_send_level"></a>

#### min_send_level

```python
@property
def min_send_level() -> float
```

(float):  [Read-Write] The amount to send to master when sound is located at a distance equal to value specified in the min send distance.

<a id="unreal.SoundSubmixSendInfoBase.min_send_level"></a>

#### min_send_level

```python
@min_send_level.setter
def min_send_level(value: float) -> None
```

<a id="unreal.SoundSubmixSendInfoBase.max_send_level"></a>

#### max_send_level

```python
@property
def max_send_level() -> float
```

(float):  [Read-Write] The amount to send to master when sound is located at a distance equal to value specified in the max send distance.

<a id="unreal.SoundSubmixSendInfoBase.max_send_level"></a>

#### max_send_level

```python
@max_send_level.setter
def max_send_level(value: float) -> None
```

<a id="unreal.SoundSubmixSendInfoBase.min_send_distance"></a>

#### min_send_distance

```python
@property
def min_send_distance() -> float
```

(float):  [Read-Write] The min distance to send to the master

<a id="unreal.SoundSubmixSendInfoBase.min_send_distance"></a>

#### min_send_distance

```python
@min_send_distance.setter
def min_send_distance(value: float) -> None
```

<a id="unreal.SoundSubmixSendInfoBase.max_send_distance"></a>

#### max_send_distance

```python
@property
def max_send_distance() -> float
```

(float):  [Read-Write] The max distance to send to the master

<a id="unreal.SoundSubmixSendInfoBase.max_send_distance"></a>

#### max_send_distance

```python
@max_send_distance.setter
def max_send_distance(value: float) -> None
```

<a id="unreal.SoundSubmixSendInfoBase.custom_send_level_curve"></a>

#### custom_send_level_curve

```python
@property
def custom_send_level_curve() -> RuntimeFloatCurve
```

(RuntimeFloatCurve):  [Read-Write] The custom reverb send curve to use for distance-based send level.

<a id="unreal.SoundSubmixSendInfoBase.custom_send_level_curve"></a>

#### custom_send_level_curve

```python
@custom_send_level_curve.setter
def custom_send_level_curve(value: RuntimeFloatCurve) -> None
```

<a id="unreal.AttenuationSubmixSendSettings"></a>