## SubmixEffectFilterPreset Objects

```python
class SubmixEffectFilterPreset(SoundEffectSubmixPreset)
```

USubmixEffectFilterPreset
Class which processes audio streams and uses parameters defined in the preset class.

**C++ Source:**

- **Plugin**: Synthesis
- **Module**: Synthesis
- **File**: SubmixEffectFilter.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``settings`` (SubmixEffectFilterSettings):  [Read-Write]

<a id="unreal.SubmixEffectFilterPreset.settings"></a>

#### settings

```python
@property
def settings() -> SubmixEffectFilterSettings
```

(SubmixEffectFilterSettings):  [Read-Write]

<a id="unreal.SubmixEffectFilterPreset.settings"></a>

#### settings

```python
@settings.setter
def settings(value: SubmixEffectFilterSettings) -> None
```

<a id="unreal.SubmixEffectFilterPreset.set_settings"></a>

#### set_settings

```python
def set_settings(settings: SubmixEffectFilterSettings) -> None
```

x.set_settings(settings) -> None
Set all filter effect settings

Args:
    settings (SubmixEffectFilterSettings):

<a id="unreal.SubmixEffectFilterPreset.set_filter_type"></a>

#### set_filter_type

```python
def set_filter_type(type: SubmixFilterType) -> None
```

x.set_filter_type(type) -> None
Sets the filter type

Args:
    type (SubmixFilterType):

<a id="unreal.SubmixEffectFilterPreset.set_filter_q_mod"></a>

#### set_filter_q_mod

```python
def set_filter_q_mod(q: float) -> None
```

x.set_filter_q_mod(q) -> None
Sets the filter Q

Args:
    q (float):

<a id="unreal.SubmixEffectFilterPreset.set_filter_q"></a>

#### set_filter_q

```python
def set_filter_q(q: float) -> None
```

x.set_filter_q(q) -> None
Sets the filter Q

Args:
    q (float):

<a id="unreal.SubmixEffectFilterPreset.set_filter_cutoff_frequency_mod"></a>

#### set_filter_cutoff_frequency_mod

```python
def set_filter_cutoff_frequency_mod(frequency: float) -> None
```

x.set_filter_cutoff_frequency_mod(frequency) -> None
Sets the mod filter cutoff frequency

Args:
    frequency (float):

<a id="unreal.SubmixEffectFilterPreset.set_filter_cutoff_frequency"></a>

#### set_filter_cutoff_frequency

```python
def set_filter_cutoff_frequency(frequency: float) -> None
```

x.set_filter_cutoff_frequency(frequency) -> None
Sets the base filter cutoff frequency

Args:
    frequency (float):

<a id="unreal.SubmixEffectFilterPreset.set_filter_algorithm"></a>

#### set_filter_algorithm

```python
def set_filter_algorithm(algorithm: SubmixFilterAlgorithm) -> None
```

x.set_filter_algorithm(algorithm) -> None
Sets the filter algorithm

Args:
    algorithm (SubmixFilterAlgorithm):

<a id="unreal.SubmixEffectFlexiverbPreset"></a>