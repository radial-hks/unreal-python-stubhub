## SourceEffectMotionFilterModulationSettings Objects

```python
class SourceEffectMotionFilterModulationSettings(StructBase)
```

Source Effect Motion Filter Modulation Settings

**C++ Source:**

- **Plugin**: Synthesis
- **Module**: Synthesis
- **File**: SourceEffectMotionFilter.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``modulation_input_range`` (Vector2D):  [Read-Write] The Modulation Clamped Input Range
- ``modulation_output_maximum_range`` (Vector2D):  [Read-Write] The Modulation Random Maximum Output Range
- ``modulation_output_minimum_range`` (Vector2D):  [Read-Write] The Modulation Random Minimum Output Range
- ``modulation_source`` (SourceEffectMotionFilterModSource):  [Read-Write] The Modulation Source
- ``update_ease_ms`` (float):  [Read-Write] Update Ease Speed in milliseconds

<a id="unreal.SourceEffectMotionFilterModulationSettings.__init__"></a>

#### __init__

```python
def __init__(
        modulation_source:
    SourceEffectMotionFilterModSource = SourceEffectMotionFilterModSource.
    DISTANCE_FROM_LISTENER,
        modulation_input_range: Vector2D = [0.000000, 0.000000],
        modulation_output_minimum_range: Vector2D = [0.000000, 0.000000],
        modulation_output_maximum_range: Vector2D = [0.000000, 0.000000],
        update_ease_ms: float = 0.000000) -> None
```

<a id="unreal.SourceEffectMotionFilterModulationSettings.modulation_source"></a>

#### modulation_source

```python
@property
def modulation_source() -> SourceEffectMotionFilterModSource
```

(SourceEffectMotionFilterModSource):  [Read-Write] The Modulation Source

<a id="unreal.SourceEffectMotionFilterModulationSettings.modulation_source"></a>

#### modulation_source

```python
@modulation_source.setter
def modulation_source(value: SourceEffectMotionFilterModSource) -> None
```

<a id="unreal.SourceEffectMotionFilterModulationSettings.modulation_input_range"></a>

#### modulation_input_range

```python
@property
def modulation_input_range() -> Vector2D
```

(Vector2D):  [Read-Write] The Modulation Clamped Input Range

<a id="unreal.SourceEffectMotionFilterModulationSettings.modulation_input_range"></a>

#### modulation_input_range

```python
@modulation_input_range.setter
def modulation_input_range(value: Vector2D) -> None
```

<a id="unreal.SourceEffectMotionFilterModulationSettings.modulation_output_minimum_range"></a>

#### modulation_output_minimum_range

```python
@property
def modulation_output_minimum_range() -> Vector2D
```

(Vector2D):  [Read-Write] The Modulation Random Minimum Output Range

<a id="unreal.SourceEffectMotionFilterModulationSettings.modulation_output_minimum_range"></a>

#### modulation_output_minimum_range

```python
@modulation_output_minimum_range.setter
def modulation_output_minimum_range(value: Vector2D) -> None
```

<a id="unreal.SourceEffectMotionFilterModulationSettings.modulation_output_maximum_range"></a>

#### modulation_output_maximum_range

```python
@property
def modulation_output_maximum_range() -> Vector2D
```

(Vector2D):  [Read-Write] The Modulation Random Maximum Output Range

<a id="unreal.SourceEffectMotionFilterModulationSettings.modulation_output_maximum_range"></a>

#### modulation_output_maximum_range

```python
@modulation_output_maximum_range.setter
def modulation_output_maximum_range(value: Vector2D) -> None
```

<a id="unreal.SourceEffectMotionFilterModulationSettings.update_ease_ms"></a>

#### update_ease_ms

```python
@property
def update_ease_ms() -> float
```

(float):  [Read-Write] Update Ease Speed in milliseconds

<a id="unreal.SourceEffectMotionFilterModulationSettings.update_ease_ms"></a>

#### update_ease_ms

```python
@update_ease_ms.setter
def update_ease_ms(value: float) -> None
```

<a id="unreal.SourceEffectMotionFilterSettings"></a>