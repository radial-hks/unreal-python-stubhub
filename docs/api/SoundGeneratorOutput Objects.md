## SoundGeneratorOutput Objects

```python
class SoundGeneratorOutput(StructBase)
```

Base class for generators that have outputs that can be exposed to other game code.

NOTE: This is not widely supported and should be considered experimental.

**C++ Source:**

- **Module**: AudioExtensions
- **File**: SoundGeneratorOutput.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``name`` (Name):  [Read-Write] The output's name

<a id="unreal.SoundGeneratorOutput.__init__"></a>

#### __init__

```python
def __init__(name: Name = "None") -> None
```

<a id="unreal.SoundGeneratorOutput.name"></a>

#### name

```python
@property
def name() -> Name
```

(Name):  [Read-Only] The output's name

<a id="unreal.AudioParameter"></a>