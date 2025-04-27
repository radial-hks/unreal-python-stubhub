## SourceEffectFoldbackDistortionSettings Objects

```python
class SourceEffectFoldbackDistortionSettings(StructBase)
```

Source Effect Foldback Distortion Settings

**C++ Source:**

- **Plugin**: Synthesis
- **Module**: Synthesis
- **File**: SourceEffectFoldbackDistortion.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``input_gain_db`` (float):  [Read-Write] The amount of gain to add to input to allow forcing the triggering of the threshold
- ``output_gain_db`` (float):  [Read-Write] The amount of gain to apply to the output
- ``threshold_db`` (float):  [Read-Write] If the audio amplitude is higher than this, it will fold back

<a id="unreal.SourceEffectFoldbackDistortionSettings.__init__"></a>

#### __init__

```python
def __init__(input_gain_db: float = 0.000000,
             threshold_db: float = 0.000000,
             output_gain_db: float = 0.000000) -> None
```

<a id="unreal.SourceEffectFoldbackDistortionSettings.input_gain_db"></a>

#### input_gain_db

```python
@property
def input_gain_db() -> float
```

(float):  [Read-Write] The amount of gain to add to input to allow forcing the triggering of the threshold

<a id="unreal.SourceEffectFoldbackDistortionSettings.input_gain_db"></a>

#### input_gain_db

```python
@input_gain_db.setter
def input_gain_db(value: float) -> None
```

<a id="unreal.SourceEffectFoldbackDistortionSettings.threshold_db"></a>

#### threshold_db

```python
@property
def threshold_db() -> float
```

(float):  [Read-Write] If the audio amplitude is higher than this, it will fold back

<a id="unreal.SourceEffectFoldbackDistortionSettings.threshold_db"></a>

#### threshold_db

```python
@threshold_db.setter
def threshold_db(value: float) -> None
```

<a id="unreal.SourceEffectFoldbackDistortionSettings.output_gain_db"></a>

#### output_gain_db

```python
@property
def output_gain_db() -> float
```

(float):  [Read-Write] The amount of gain to apply to the output

<a id="unreal.SourceEffectFoldbackDistortionSettings.output_gain_db"></a>

#### output_gain_db

```python
@output_gain_db.setter
def output_gain_db(value: float) -> None
```

<a id="unreal.SourceEffectMidSideSpreaderSettings"></a>