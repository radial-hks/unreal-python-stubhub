## SourceEffectChainEntry Objects

```python
class SourceEffectChainEntry(StructBase)
```

Source Effect Chain Entry

**C++ Source:**

- **Module**: Engine
- **File**: SoundEffectSource.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``bypass`` (bool):  [Read-Write]
- ``preset`` (SoundEffectSourcePreset):  [Read-Write]

<a id="unreal.SourceEffectChainEntry.__init__"></a>

#### __init__

```python
def __init__(preset: SoundEffectSourcePreset = None,
             bypass: bool = False) -> None
```

<a id="unreal.SourceEffectChainEntry.preset"></a>

#### preset

```python
@property
def preset() -> SoundEffectSourcePreset
```

(SoundEffectSourcePreset):  [Read-Write]

<a id="unreal.SourceEffectChainEntry.preset"></a>

#### preset

```python
@preset.setter
def preset(value: SoundEffectSourcePreset) -> None
```

<a id="unreal.SourceEffectChainEntry.bypass"></a>

#### bypass

```python
@property
def bypass() -> bool
```

(bool):  [Read-Write]

<a id="unreal.SourceEffectChainEntry.bypass"></a>

#### bypass

```python
@bypass.setter
def bypass(value: bool) -> None
```

<a id="unreal.ModulatorContinuousParams"></a>