## SubmixEffectFilterSettings Objects

```python
class SubmixEffectFilterSettings(StructBase)
```

FSubmixEffectFilterSettings
UStruct used to define user-exposed params for use with your effect.

**C++ Source:**

- **Plugin**: Synthesis
- **Module**: Synthesis
- **File**: SubmixEffectFilter.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``filter_algorithm`` (SubmixFilterAlgorithm):  [Read-Write] What type of filter algorithm to use for the submix filter effect
- ``filter_frequency`` (float):  [Read-Write] The output filter cutoff frequency (hz) [0.0, 20000.0]
- ``filter_q`` (float):  [Read-Write] The output filter resonance (Q) [0.5, 10]
- ``filter_type`` (SubmixFilterType):  [Read-Write] What type of filter to use for the submix filter effect

<a id="unreal.SubmixEffectFilterSettings.__init__"></a>

#### __init__

```python
def __init__(filter_type: SubmixFilterType = SubmixFilterType.LOW_PASS,
             filter_algorithm: SubmixFilterAlgorithm = SubmixFilterAlgorithm.
             ONE_POLE,
             filter_frequency: float = 0.000000,
             filter_q: float = 0.000000) -> None
```

<a id="unreal.SubmixEffectFilterSettings.filter_type"></a>

#### filter_type

```python
@property
def filter_type() -> SubmixFilterType
```

(SubmixFilterType):  [Read-Write] What type of filter to use for the submix filter effect

<a id="unreal.SubmixEffectFilterSettings.filter_type"></a>

#### filter_type

```python
@filter_type.setter
def filter_type(value: SubmixFilterType) -> None
```

<a id="unreal.SubmixEffectFilterSettings.filter_algorithm"></a>

#### filter_algorithm

```python
@property
def filter_algorithm() -> SubmixFilterAlgorithm
```

(SubmixFilterAlgorithm):  [Read-Write] What type of filter algorithm to use for the submix filter effect

<a id="unreal.SubmixEffectFilterSettings.filter_algorithm"></a>

#### filter_algorithm

```python
@filter_algorithm.setter
def filter_algorithm(value: SubmixFilterAlgorithm) -> None
```

<a id="unreal.SubmixEffectFilterSettings.filter_frequency"></a>

#### filter_frequency

```python
@property
def filter_frequency() -> float
```

(float):  [Read-Write] The output filter cutoff frequency (hz) [0.0, 20000.0]

<a id="unreal.SubmixEffectFilterSettings.filter_frequency"></a>

#### filter_frequency

```python
@filter_frequency.setter
def filter_frequency(value: float) -> None
```

<a id="unreal.SubmixEffectFilterSettings.filter_q"></a>

#### filter_q

```python
@property
def filter_q() -> float
```

(float):  [Read-Write] The output filter resonance (Q) [0.5, 10]

<a id="unreal.SubmixEffectFilterSettings.filter_q"></a>

#### filter_q

```python
@filter_q.setter
def filter_q(value: float) -> None
```

<a id="unreal.SubmixEffectFlexiverbSettings"></a>