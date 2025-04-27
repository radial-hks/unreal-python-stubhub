## SourceEffectChorusBaseSettings Objects

```python
class SourceEffectChorusBaseSettings(StructBase)
```

Source Effect Chorus Base Settings

**C++ Source:**

- **Plugin**: Synthesis
- **Module**: Synthesis
- **File**: SourceEffectChorus.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``depth`` (float):  [Read-Write] The depth of the chorus effect
- ``dry_level`` (float):  [Read-Write] The dry level of the chorus effect
- ``feedback`` (float):  [Read-Write] The feedback of the chorus effect
- ``frequency`` (float):  [Read-Write] The frequency of the chorus effect
- ``spread`` (float):  [Read-Write] The spread of the effect (larger means greater difference between left and right delay lines)
- ``wet_level`` (float):  [Read-Write] The wet level of the chorus effect

<a id="unreal.SourceEffectChorusBaseSettings.__init__"></a>

#### __init__

```python
def __init__(depth: float = 0.000000,
             frequency: float = 0.000000,
             feedback: float = 0.000000,
             wet_level: float = 0.000000,
             dry_level: float = 0.000000,
             spread: float = 0.000000) -> None
```

<a id="unreal.SourceEffectChorusBaseSettings.depth"></a>

#### depth

```python
@property
def depth() -> float
```

(float):  [Read-Write] The depth of the chorus effect

<a id="unreal.SourceEffectChorusBaseSettings.depth"></a>

#### depth

```python
@depth.setter
def depth(value: float) -> None
```

<a id="unreal.SourceEffectChorusBaseSettings.frequency"></a>

#### frequency

```python
@property
def frequency() -> float
```

(float):  [Read-Write] The frequency of the chorus effect

<a id="unreal.SourceEffectChorusBaseSettings.frequency"></a>

#### frequency

```python
@frequency.setter
def frequency(value: float) -> None
```

<a id="unreal.SourceEffectChorusBaseSettings.feedback"></a>

#### feedback

```python
@property
def feedback() -> float
```

(float):  [Read-Write] The feedback of the chorus effect

<a id="unreal.SourceEffectChorusBaseSettings.feedback"></a>

#### feedback

```python
@feedback.setter
def feedback(value: float) -> None
```

<a id="unreal.SourceEffectChorusBaseSettings.wet_level"></a>

#### wet_level

```python
@property
def wet_level() -> float
```

(float):  [Read-Write] The wet level of the chorus effect

<a id="unreal.SourceEffectChorusBaseSettings.wet_level"></a>

#### wet_level

```python
@wet_level.setter
def wet_level(value: float) -> None
```

<a id="unreal.SourceEffectChorusBaseSettings.dry_level"></a>

#### dry_level

```python
@property
def dry_level() -> float
```

(float):  [Read-Write] The dry level of the chorus effect

<a id="unreal.SourceEffectChorusBaseSettings.dry_level"></a>

#### dry_level

```python
@dry_level.setter
def dry_level(value: float) -> None
```

<a id="unreal.SourceEffectChorusBaseSettings.spread"></a>

#### spread

```python
@property
def spread() -> float
```

(float):  [Read-Write] The spread of the effect (larger means greater difference between left and right delay lines)

<a id="unreal.SourceEffectChorusBaseSettings.spread"></a>

#### spread

```python
@spread.setter
def spread(value: float) -> None
```

<a id="unreal.SourceEffectChorusSettings"></a>