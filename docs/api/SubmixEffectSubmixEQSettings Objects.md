## SubmixEffectSubmixEQSettings Objects

```python
class SubmixEffectSubmixEQSettings(StructBase)
```

EQ submix effect

**C++ Source:**

- **Module**: AudioMixer
- **File**: AudioMixerSubmixEffectEQ.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``eq_bands`` (Array[SubmixEffectEQBand]):  [Read-Write] The EQ bands to use.

<a id="unreal.SubmixEffectSubmixEQSettings.__init__"></a>

#### __init__

```python
def __init__(eq_bands: Array[SubmixEffectEQBand] = []) -> None
```

<a id="unreal.SubmixEffectSubmixEQSettings.eq_bands"></a>

#### eq_bands

```python
@property
def eq_bands() -> Array[SubmixEffectEQBand]
```

(Array[SubmixEffectEQBand]):  [Read-Write] The EQ bands to use.

<a id="unreal.SubmixEffectSubmixEQSettings.eq_bands"></a>

#### eq_bands

```python
@eq_bands.setter
def eq_bands(value: Array[SubmixEffectEQBand]) -> None
```

<a id="unreal.SubmixEffectReverbSettings"></a>