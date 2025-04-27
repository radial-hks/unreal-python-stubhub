## SubmixEffectEQBand Objects

```python
class SubmixEffectEQBand(StructBase)
```

A multiband EQ submix effect.

**C++ Source:**

- **Module**: AudioMixer
- **File**: AudioMixerSubmixEffectEQ.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``bandwidth`` (float):  [Read-Write]
- ``enabled`` (bool):  [Read-Write]
- ``frequency`` (float):  [Read-Write]
- ``gain_db`` (float):  [Read-Write]

<a id="unreal.SubmixEffectEQBand.__init__"></a>

#### __init__

```python
def __init__(frequency: float = 0.000000,
             bandwidth: float = 0.000000,
             gain_db: float = 0.000000,
             enabled: bool = False) -> None
```

<a id="unreal.SubmixEffectEQBand.frequency"></a>

#### frequency

```python
@property
def frequency() -> float
```

(float):  [Read-Write]

<a id="unreal.SubmixEffectEQBand.frequency"></a>

#### frequency

```python
@frequency.setter
def frequency(value: float) -> None
```

<a id="unreal.SubmixEffectEQBand.bandwidth"></a>

#### bandwidth

```python
@property
def bandwidth() -> float
```

(float):  [Read-Write]

<a id="unreal.SubmixEffectEQBand.bandwidth"></a>

#### bandwidth

```python
@bandwidth.setter
def bandwidth(value: float) -> None
```

<a id="unreal.SubmixEffectEQBand.gain_db"></a>

#### gain_db

```python
@property
def gain_db() -> float
```

(float):  [Read-Write]

<a id="unreal.SubmixEffectEQBand.gain_db"></a>

#### gain_db

```python
@gain_db.setter
def gain_db(value: float) -> None
```

<a id="unreal.SubmixEffectEQBand.enabled"></a>

#### enabled

```python
@property
def enabled() -> bool
```

(bool):  [Read-Write]

<a id="unreal.SubmixEffectEQBand.enabled"></a>

#### enabled

```python
@enabled.setter
def enabled(value: bool) -> None
```

<a id="unreal.SubmixEffectSubmixEQSettings"></a>