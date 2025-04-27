## SourceEffectEQSettings Objects

```python
class SourceEffectEQSettings(StructBase)
```

EQ source effect settings

**C++ Source:**

- **Plugin**: Synthesis
- **Module**: Synthesis
- **File**: SourceEffectEQ.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``eq_bands`` (Array[SourceEffectEQBand]):  [Read-Write] The EQ bands to use

<a id="unreal.SourceEffectEQSettings.__init__"></a>

#### __init__

```python
def __init__(eq_bands: Array[SourceEffectEQBand] = []) -> None
```

<a id="unreal.SourceEffectEQSettings.eq_bands"></a>

#### eq_bands

```python
@property
def eq_bands() -> Array[SourceEffectEQBand]
```

(Array[SourceEffectEQBand]):  [Read-Write] The EQ bands to use

<a id="unreal.SourceEffectEQSettings.eq_bands"></a>

#### eq_bands

```python
@eq_bands.setter
def eq_bands(value: Array[SourceEffectEQBand]) -> None
```

<a id="unreal.SourceEffectFilterAudioBusModulationSettings"></a>