## SubmixEffectTapDelaySettings Objects

```python
class SubmixEffectTapDelaySettings(StructBase)
```

FTapDelaySubmixPresetSettings
UStruct used to define user-exposed params for use with your effect.

**C++ Source:**

- **Plugin**: Synthesis
- **Module**: Synthesis
- **File**: SubmixEffectTapDelay.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``interpolation_time`` (float):  [Read-Write] Number of milliseconds over which a tap will reach it's set length and gain. Smaller values are more responsive, while larger values will make pitching less dramatic.
- ``maximum_delay_length`` (float):  [Read-Write] Maximum possible length for a delay, in milliseconds. Changing this at runtime will reset the effect.
- ``taps`` (Array[TapDelayInfo]):  [Read-Write] Each tap's metadata

<a id="unreal.SubmixEffectTapDelaySettings.__init__"></a>

#### __init__

```python
def __init__(maximum_delay_length: float = 0.000000,
             interpolation_time: float = 0.000000,
             taps: Array[TapDelayInfo] = []) -> None
```

<a id="unreal.SubmixEffectTapDelaySettings.maximum_delay_length"></a>

#### maximum_delay_length

```python
@property
def maximum_delay_length() -> float
```

(float):  [Read-Write] Maximum possible length for a delay, in milliseconds. Changing this at runtime will reset the effect.

<a id="unreal.SubmixEffectTapDelaySettings.maximum_delay_length"></a>

#### maximum_delay_length

```python
@maximum_delay_length.setter
def maximum_delay_length(value: float) -> None
```

<a id="unreal.SubmixEffectTapDelaySettings.interpolation_time"></a>

#### interpolation_time

```python
@property
def interpolation_time() -> float
```

(float):  [Read-Write] Number of milliseconds over which a tap will reach it's set length and gain. Smaller values are more responsive, while larger values will make pitching less dramatic.

<a id="unreal.SubmixEffectTapDelaySettings.interpolation_time"></a>

#### interpolation_time

```python
@interpolation_time.setter
def interpolation_time(value: float) -> None
```

<a id="unreal.SubmixEffectTapDelaySettings.taps"></a>

#### taps

```python
@property
def taps() -> Array[TapDelayInfo]
```

(Array[TapDelayInfo]):  [Read-Write] Each tap's metadata

<a id="unreal.SubmixEffectTapDelaySettings.taps"></a>

#### taps

```python
@taps.setter
def taps(value: Array[TapDelayInfo]) -> None
```

<a id="unreal.Synth2DSliderStyle"></a>