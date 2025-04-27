## SourceEffectSimpleDelaySettings Objects

```python
class SourceEffectSimpleDelaySettings(StructBase)
```

Source Effect Simple Delay Settings

**C++ Source:**

- **Plugin**: Synthesis
- **Module**: Synthesis
- **File**: SourceEffectSimpleDelay.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``delay_amount`` (float):  [Read-Write] Delay amount in seconds
- ``delay_based_on_distance`` (bool):  [Read-Write] Whether or not to delay the audio based on the distance to the listener or use manual delay
- ``dry_amount`` (float):  [Read-Write] Gain stage on dry (non-delayed signal)
- ``feedback`` (float):  [Read-Write] Amount to feedback into the delay line (because why not)
- ``speed_of_sound`` (float):  [Read-Write] Speed of sound in meters per second when using distance-based delay
- ``use_distance_override`` (bool):  [Read-Write] Whether or not to allow the attenuation distance override value vs the distance to listener to be used for distance-based delay.
- ``wet_amount`` (float):  [Read-Write] Gain stage on wet (delayed) signal

<a id="unreal.SourceEffectSimpleDelaySettings.__init__"></a>

#### __init__

```python
def __init__(speed_of_sound: float = 0.000000,
             delay_amount: float = 0.000000,
             dry_amount: float = 0.000000,
             wet_amount: float = 0.000000,
             feedback: float = 0.000000,
             delay_based_on_distance: bool = False,
             use_distance_override: bool = False) -> None
```

<a id="unreal.SourceEffectSimpleDelaySettings.speed_of_sound"></a>

#### speed_of_sound

```python
@property
def speed_of_sound() -> float
```

(float):  [Read-Write] Speed of sound in meters per second when using distance-based delay

<a id="unreal.SourceEffectSimpleDelaySettings.speed_of_sound"></a>

#### speed_of_sound

```python
@speed_of_sound.setter
def speed_of_sound(value: float) -> None
```

<a id="unreal.SourceEffectSimpleDelaySettings.delay_amount"></a>

#### delay_amount

```python
@property
def delay_amount() -> float
```

(float):  [Read-Write] Delay amount in seconds

<a id="unreal.SourceEffectSimpleDelaySettings.delay_amount"></a>

#### delay_amount

```python
@delay_amount.setter
def delay_amount(value: float) -> None
```

<a id="unreal.SourceEffectSimpleDelaySettings.dry_amount"></a>

#### dry_amount

```python
@property
def dry_amount() -> float
```

(float):  [Read-Write] Gain stage on dry (non-delayed signal)

<a id="unreal.SourceEffectSimpleDelaySettings.dry_amount"></a>

#### dry_amount

```python
@dry_amount.setter
def dry_amount(value: float) -> None
```

<a id="unreal.SourceEffectSimpleDelaySettings.wet_amount"></a>

#### wet_amount

```python
@property
def wet_amount() -> float
```

(float):  [Read-Write] Gain stage on wet (delayed) signal

<a id="unreal.SourceEffectSimpleDelaySettings.wet_amount"></a>

#### wet_amount

```python
@wet_amount.setter
def wet_amount(value: float) -> None
```

<a id="unreal.SourceEffectSimpleDelaySettings.feedback"></a>

#### feedback

```python
@property
def feedback() -> float
```

(float):  [Read-Write] Amount to feedback into the delay line (because why not)

<a id="unreal.SourceEffectSimpleDelaySettings.feedback"></a>

#### feedback

```python
@feedback.setter
def feedback(value: float) -> None
```

<a id="unreal.SourceEffectSimpleDelaySettings.delay_based_on_distance"></a>

#### delay_based_on_distance

```python
@property
def delay_based_on_distance() -> bool
```

(bool):  [Read-Write] Whether or not to delay the audio based on the distance to the listener or use manual delay

<a id="unreal.SourceEffectSimpleDelaySettings.delay_based_on_distance"></a>

#### delay_based_on_distance

```python
@delay_based_on_distance.setter
def delay_based_on_distance(value: bool) -> None
```

<a id="unreal.SourceEffectSimpleDelaySettings.use_distance_override"></a>

#### use_distance_override

```python
@property
def use_distance_override() -> bool
```

(bool):  [Read-Write] Whether or not to allow the attenuation distance override value vs the distance to listener to be used for distance-based delay.

<a id="unreal.SourceEffectSimpleDelaySettings.use_distance_override"></a>

#### use_distance_override

```python
@use_distance_override.setter
def use_distance_override(value: bool) -> None
```

<a id="unreal.SourceEffectStereoDelaySettings"></a>