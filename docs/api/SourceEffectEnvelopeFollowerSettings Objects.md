## SourceEffectEnvelopeFollowerSettings Objects

```python
class SourceEffectEnvelopeFollowerSettings(StructBase)
```

Source Effect Envelope Follower Settings

**C++ Source:**

- **Plugin**: Synthesis
- **Module**: Synthesis
- **File**: SourceEffectEnvelopeFollower.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``attack_time`` (float):  [Read-Write] The attack time of the envelope follower in milliseconds
- ``is_analog_mode`` (bool):  [Read-Write] Whether or not the envelope follower is in analog mode
- ``peak_mode`` (EnvelopeFollowerPeakMode):  [Read-Write] The peak mode of the envelope follower
- ``release_time`` (float):  [Read-Write] The release time of the envelope follower in milliseconds

<a id="unreal.SourceEffectEnvelopeFollowerSettings.__init__"></a>

#### \_\_init\_\_

```python
def __init__(attack_time: float = 0.000000,
             release_time: float = 0.000000,
             peak_mode: EnvelopeFollowerPeakMode = EnvelopeFollowerPeakMode.
             MEAN_SQUARED,
             is_analog_mode: bool = False) -> None
```

<a id="unreal.SourceEffectEnvelopeFollowerSettings.attack_time"></a>

#### attack\_time

```python
@property
def attack_time() -> float
```

(float):  [Read-Write] The attack time of the envelope follower in milliseconds

<a id="unreal.SourceEffectEnvelopeFollowerSettings.attack_time"></a>

#### attack\_time

```python
@attack_time.setter
def attack_time(value: float) -> None
```

<a id="unreal.SourceEffectEnvelopeFollowerSettings.release_time"></a>

#### release\_time

```python
@property
def release_time() -> float
```

(float):  [Read-Write] The release time of the envelope follower in milliseconds

<a id="unreal.SourceEffectEnvelopeFollowerSettings.release_time"></a>

#### release\_time

```python
@release_time.setter
def release_time(value: float) -> None
```

<a id="unreal.SourceEffectEnvelopeFollowerSettings.peak_mode"></a>

#### peak\_mode

```python
@property
def peak_mode() -> EnvelopeFollowerPeakMode
```

(EnvelopeFollowerPeakMode):  [Read-Write] The peak mode of the envelope follower

<a id="unreal.SourceEffectEnvelopeFollowerSettings.peak_mode"></a>

#### peak\_mode

```python
@peak_mode.setter
def peak_mode(value: EnvelopeFollowerPeakMode) -> None
```

<a id="unreal.SourceEffectEnvelopeFollowerSettings.is_analog_mode"></a>

#### is\_analog\_mode

```python
@property
def is_analog_mode() -> bool
```

(bool):  [Read-Write] Whether or not the envelope follower is in analog mode

<a id="unreal.SourceEffectEnvelopeFollowerSettings.is_analog_mode"></a>

#### is\_analog\_mode

```python
@is_analog_mode.setter
def is_analog_mode(value: bool) -> None
```

<a id="unreal.SourceEffectEQBand"></a>