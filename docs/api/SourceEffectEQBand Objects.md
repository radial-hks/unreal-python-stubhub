## SourceEffectEQBand Objects

```python
class SourceEffectEQBand(StructBase)
```

Source Effect EQBand

**C++ Source:**

- **Plugin**: Synthesis
- **Module**: Synthesis
- **File**: SourceEffectEQ.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``bandwidth`` (float):  [Read-Write] The bandwidth (in octaves) of the band
- ``enabled`` (bool):  [Read-Write] Whether or not the band is enabled. Allows changing bands on the fly.
- ``frequency`` (float):  [Read-Write] The cutoff frequency of the band
- ``gain_db`` (float):  [Read-Write] The gain in decibels to apply to the eq band

<a id="unreal.SourceEffectEQBand.__init__"></a>

#### __init__

```python
def __init__(frequency: float = 0.000000,
             bandwidth: float = 0.000000,
             gain_db: float = 0.000000,
             enabled: bool = False) -> None
```

<a id="unreal.SourceEffectEQBand.frequency"></a>

#### frequency

```python
@property
def frequency() -> float
```

(float):  [Read-Write] The cutoff frequency of the band

<a id="unreal.SourceEffectEQBand.frequency"></a>

#### frequency

```python
@frequency.setter
def frequency(value: float) -> None
```

<a id="unreal.SourceEffectEQBand.bandwidth"></a>

#### bandwidth

```python
@property
def bandwidth() -> float
```

(float):  [Read-Write] The bandwidth (in octaves) of the band

<a id="unreal.SourceEffectEQBand.bandwidth"></a>

#### bandwidth

```python
@bandwidth.setter
def bandwidth(value: float) -> None
```

<a id="unreal.SourceEffectEQBand.gain_db"></a>

#### gain_db

```python
@property
def gain_db() -> float
```

(float):  [Read-Write] The gain in decibels to apply to the eq band

<a id="unreal.SourceEffectEQBand.gain_db"></a>

#### gain_db

```python
@gain_db.setter
def gain_db(value: float) -> None
```

<a id="unreal.SourceEffectEQBand.enabled"></a>

#### enabled

```python
@property
def enabled() -> bool
```

(bool):  [Read-Write] Whether or not the band is enabled. Allows changing bands on the fly.

<a id="unreal.SourceEffectEQBand.enabled"></a>

#### enabled

```python
@enabled.setter
def enabled(value: bool) -> None
```

<a id="unreal.SourceEffectEQSettings"></a>