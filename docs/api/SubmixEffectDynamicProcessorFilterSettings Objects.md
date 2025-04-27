## SubmixEffectDynamicProcessorFilterSettings Objects

```python
class SubmixEffectDynamicProcessorFilterSettings(StructBase)
```

Submix Effect Dynamic Processor Filter Settings

**C++ Source:**

- **Module**: AudioMixer
- **File**: AudioMixerSubmixEffectDynamicsProcessor.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``cutoff`` (float):  [Read-Write] The cutoff frequency of the HPF applied to key signal
- ``enabled`` (bool):  [Read-Write] Whether or not filter is enabled
- ``gain_db`` (float):  [Read-Write] The gain of the filter shelf applied to the key signal

<a id="unreal.SubmixEffectDynamicProcessorFilterSettings.__init__"></a>

#### __init__

```python
def __init__(enabled: bool = False,
             cutoff: float = 0.000000,
             gain_db: float = 0.000000) -> None
```

<a id="unreal.SubmixEffectDynamicProcessorFilterSettings.enabled"></a>

#### enabled

```python
@property
def enabled() -> bool
```

(bool):  [Read-Write] Whether or not filter is enabled

<a id="unreal.SubmixEffectDynamicProcessorFilterSettings.enabled"></a>

#### enabled

```python
@enabled.setter
def enabled(value: bool) -> None
```

<a id="unreal.SubmixEffectDynamicProcessorFilterSettings.cutoff"></a>

#### cutoff

```python
@property
def cutoff() -> float
```

(float):  [Read-Write] The cutoff frequency of the HPF applied to key signal

<a id="unreal.SubmixEffectDynamicProcessorFilterSettings.cutoff"></a>

#### cutoff

```python
@cutoff.setter
def cutoff(value: float) -> None
```

<a id="unreal.SubmixEffectDynamicProcessorFilterSettings.gain_db"></a>

#### gain_db

```python
@property
def gain_db() -> float
```

(float):  [Read-Write] The gain of the filter shelf applied to the key signal

<a id="unreal.SubmixEffectDynamicProcessorFilterSettings.gain_db"></a>

#### gain_db

```python
@gain_db.setter
def gain_db(value: float) -> None
```

<a id="unreal.SubmixEffectDynamicsProcessorSettings"></a>