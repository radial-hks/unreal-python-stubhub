## AudioMaterialEnvelopeSettings Objects

```python
class AudioMaterialEnvelopeSettings(StructBase)
```

Audio Material Envelope Settings

**C++ Source:**

- **Plugin**: AudioWidgets
- **Module**: AudioWidgets
- **File**: AudioMaterialEnvelopeSettings.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``attack_curve`` (float):  [Read-Write] Curve of the envelopes attack stage.
  Attack is the time taken for the rise of the level from zero to a given value.
- ``attack_time`` (float):  [Read-Write] Time the Value reaches the Attack stage.
  Attack is the time taken for the rise of the level from zero to a given value.
- ``attack_value`` (float):  [Read-Write] Value of the envelopes attack stage.
  Attack is the time taken for the rise of the level from zero to a given value.
- ``decay_curve`` (float):  [Read-Write] Curve of the envelopes Decay stage.
  Decay is the time taken for the level to reduce from the attack level to the sustain level.
- ``decay_time`` (float):  [Read-Write] Time that takes to reach the level of the Sustain stage.
  Decay is the time taken for the level to reduce from the attack level to the sustain level.
- ``envelope_type`` (AudioMaterialEnvelopeType):  [Read-Write] The Type of the envelope curve.
- ``release_curve`` (float):  [Read-Write] Curve of the envelopes Release stage.
  Release is the time taken for the level to decay from sustain to zero.
- ``release_time`` (float):  [Read-Write] Time that takes to reach zero level
  Release is the time taken for the level to decay from sustain to zero.
- ``sustain_value`` (float):  [Read-Write] Value of the envelopes Sustain stage.
  Sustain is the level maintained until release stage.

<a id="unreal.AudioMaterialEnvelopeSettings.__init__"></a>

#### __init__

```python
def __init__(attack_curve: float = 0.000000,
             attack_value: float = 0.000000,
             attack_time: float = 0.000000,
             decay_curve: float = 0.000000,
             decay_time: float = 0.000000,
             sustain_value: float = 0.000000,
             release_curve: float = 0.000000,
             release_time: float = 0.000000) -> None
```

<a id="unreal.AudioMaterialEnvelopeSettings.attack_curve"></a>

#### attack_curve

```python
@property
def attack_curve() -> float
```

(float):  [Read-Write] Curve of the envelopes attack stage.
Attack is the time taken for the rise of the level from zero to a given value.

<a id="unreal.AudioMaterialEnvelopeSettings.attack_curve"></a>

#### attack_curve

```python
@attack_curve.setter
def attack_curve(value: float) -> None
```

<a id="unreal.AudioMaterialEnvelopeSettings.attack_value"></a>

#### attack_value

```python
@property
def attack_value() -> float
```

(float):  [Read-Write] Value of the envelopes attack stage.
Attack is the time taken for the rise of the level from zero to a given value.

<a id="unreal.AudioMaterialEnvelopeSettings.attack_value"></a>

#### attack_value

```python
@attack_value.setter
def attack_value(value: float) -> None
```

<a id="unreal.AudioMaterialEnvelopeSettings.attack_time"></a>

#### attack_time

```python
@property
def attack_time() -> float
```

(float):  [Read-Write] Time the Value reaches the Attack stage.
Attack is the time taken for the rise of the level from zero to a given value.

<a id="unreal.AudioMaterialEnvelopeSettings.attack_time"></a>

#### attack_time

```python
@attack_time.setter
def attack_time(value: float) -> None
```

<a id="unreal.AudioMaterialEnvelopeSettings.decay_curve"></a>

#### decay_curve

```python
@property
def decay_curve() -> float
```

(float):  [Read-Write] Curve of the envelopes Decay stage.
Decay is the time taken for the level to reduce from the attack level to the sustain level.

<a id="unreal.AudioMaterialEnvelopeSettings.decay_curve"></a>

#### decay_curve

```python
@decay_curve.setter
def decay_curve(value: float) -> None
```

<a id="unreal.AudioMaterialEnvelopeSettings.decay_time"></a>

#### decay_time

```python
@property
def decay_time() -> float
```

(float):  [Read-Write] Time that takes to reach the level of the Sustain stage.
Decay is the time taken for the level to reduce from the attack level to the sustain level.

<a id="unreal.AudioMaterialEnvelopeSettings.decay_time"></a>

#### decay_time

```python
@decay_time.setter
def decay_time(value: float) -> None
```

<a id="unreal.AudioMaterialEnvelopeSettings.sustain_value"></a>

#### sustain_value

```python
@property
def sustain_value() -> float
```

(float):  [Read-Write] Value of the envelopes Sustain stage.
Sustain is the level maintained until release stage.

<a id="unreal.AudioMaterialEnvelopeSettings.sustain_value"></a>

#### sustain_value

```python
@sustain_value.setter
def sustain_value(value: float) -> None
```

<a id="unreal.AudioMaterialEnvelopeSettings.release_curve"></a>

#### release_curve

```python
@property
def release_curve() -> float
```

(float):  [Read-Write] Curve of the envelopes Release stage.
Release is the time taken for the level to decay from sustain to zero.

<a id="unreal.AudioMaterialEnvelopeSettings.release_curve"></a>

#### release_curve

```python
@release_curve.setter
def release_curve(value: float) -> None
```

<a id="unreal.AudioMaterialEnvelopeSettings.release_time"></a>

#### release_time

```python
@property
def release_time() -> float
```

(float):  [Read-Write] Time that takes to reach zero level
Release is the time taken for the level to decay from sustain to zero.

<a id="unreal.AudioMaterialEnvelopeSettings.release_time"></a>

#### release_time

```python
@release_time.setter
def release_time(value: float) -> None
```

<a id="unreal.AudioMaterialButtonStyle"></a>