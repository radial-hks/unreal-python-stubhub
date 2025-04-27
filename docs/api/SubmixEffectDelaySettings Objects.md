## SubmixEffectDelaySettings Objects

```python
class SubmixEffectDelaySettings(StructBase)
```

FSubmixEffectDelaySettings
UStruct used to define user-exposed params for use with your effect.

**C++ Source:**

- **Plugin**: Synthesis
- **Module**: Synthesis
- **File**: SubmixEffectDelay.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``delay_length`` (float):  [Read-Write] Number of milliseconds of delay.  Caps at max delay at runtime.
- ``interpolation_time`` (float):  [Read-Write] Number of milliseconds over which a tap will reach it's set length and gain. Smaller values are more responsive, while larger values will make pitching less dramatic.
- ``maximum_delay_length`` (float):  [Read-Write] Maximum possible length for a delay, in milliseconds. Changing this at runtime will reset the effect.

<a id="unreal.SubmixEffectDelaySettings.__init__"></a>

#### __init__

```python
def __init__(maximum_delay_length: float = 0.000000,
             interpolation_time: float = 0.000000,
             delay_length: float = 0.000000) -> None
```

<a id="unreal.SubmixEffectDelaySettings.maximum_delay_length"></a>

#### maximum_delay_length

```python
@property
def maximum_delay_length() -> float
```

(float):  [Read-Write] Maximum possible length for a delay, in milliseconds. Changing this at runtime will reset the effect.

<a id="unreal.SubmixEffectDelaySettings.maximum_delay_length"></a>

#### maximum_delay_length

```python
@maximum_delay_length.setter
def maximum_delay_length(value: float) -> None
```

<a id="unreal.SubmixEffectDelaySettings.interpolation_time"></a>

#### interpolation_time

```python
@property
def interpolation_time() -> float
```

(float):  [Read-Write] Number of milliseconds over which a tap will reach it's set length and gain. Smaller values are more responsive, while larger values will make pitching less dramatic.

<a id="unreal.SubmixEffectDelaySettings.interpolation_time"></a>

#### interpolation_time

```python
@interpolation_time.setter
def interpolation_time(value: float) -> None
```

<a id="unreal.SubmixEffectDelaySettings.delay_length"></a>

#### delay_length

```python
@property
def delay_length() -> float
```

(float):  [Read-Write] Number of milliseconds of delay.  Caps at max delay at runtime.

<a id="unreal.SubmixEffectDelaySettings.delay_length"></a>

#### delay_length

```python
@delay_length.setter
def delay_length(value: float) -> None
```

<a id="unreal.SubmixEffectFilterSettings"></a>