## CurveEditorBakeFilter Objects

```python
class CurveEditorBakeFilter(CurveEditorFilterBase)
```

Curve Editor Bake Filter

**C++ Source:**

- **Module**: CurveEditor
- **File**: CurveEditorBakeFilter.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``bake_interval`` (FrameNumber):  [Read-Write] The interval between baked keys.
- ``bake_interval_in_seconds`` (float):  [Read-Write] The interval between baked keys when there is no valid Display Rate and Tick Resolution.
- ``custom_range`` (CurveEditorBakeFilterRange):  [Read-Write] Specifies a custom range to use for baking
- ``custom_range_max_in_seconds`` (float):  [Read-Write] Specifies a custom range to use for baking when there is no valid Display Rate and Tick Resolution.
- ``custom_range_min_in_seconds`` (float):  [Read-Write] Specifies a custom range to use for baking when there is no valid Display Rate and Tick Resolution.
- ``custom_range_override`` (bool):  [Read-Write] When enabled, CustomRange will be used for the bake region. Otherwise the selected keys will be used.

<a id="unreal.CurveEditorBakeFilter.bake_interval_in_seconds"></a>

#### bake_interval_in_seconds

```python
@property
def bake_interval_in_seconds() -> float
```

(float):  [Read-Write] The interval between baked keys when there is no valid Display Rate and Tick Resolution.

<a id="unreal.CurveEditorBakeFilter.bake_interval_in_seconds"></a>

#### bake_interval_in_seconds

```python
@bake_interval_in_seconds.setter
def bake_interval_in_seconds(value: float) -> None
```

<a id="unreal.CurveEditorBakeFilter.bake_interval"></a>

#### bake_interval

```python
@property
def bake_interval() -> FrameNumber
```

(FrameNumber):  [Read-Write] The interval between baked keys.

<a id="unreal.CurveEditorBakeFilter.bake_interval"></a>

#### bake_interval

```python
@bake_interval.setter
def bake_interval(value: FrameNumber) -> None
```

<a id="unreal.CurveEditorBakeFilter.custom_range_override"></a>

#### custom_range_override

```python
@property
def custom_range_override() -> bool
```

(bool):  [Read-Write] When enabled, CustomRange will be used for the bake region. Otherwise the selected keys will be used.

<a id="unreal.CurveEditorBakeFilter.custom_range_override"></a>

#### custom_range_override

```python
@custom_range_override.setter
def custom_range_override(value: bool) -> None
```

<a id="unreal.CurveEditorBakeFilter.custom_range_min_in_seconds"></a>

#### custom_range_min_in_seconds

```python
@property
def custom_range_min_in_seconds() -> float
```

(float):  [Read-Write] Specifies a custom range to use for baking when there is no valid Display Rate and Tick Resolution.

<a id="unreal.CurveEditorBakeFilter.custom_range_min_in_seconds"></a>

#### custom_range_min_in_seconds

```python
@custom_range_min_in_seconds.setter
def custom_range_min_in_seconds(value: float) -> None
```

<a id="unreal.CurveEditorBakeFilter.custom_range_max_in_seconds"></a>

#### custom_range_max_in_seconds

```python
@property
def custom_range_max_in_seconds() -> float
```

(float):  [Read-Write] Specifies a custom range to use for baking when there is no valid Display Rate and Tick Resolution.

<a id="unreal.CurveEditorBakeFilter.custom_range_max_in_seconds"></a>

#### custom_range_max_in_seconds

```python
@custom_range_max_in_seconds.setter
def custom_range_max_in_seconds(value: float) -> None
```

<a id="unreal.CurveEditorBakeFilter.custom_range"></a>

#### custom_range

```python
@property
def custom_range() -> CurveEditorBakeFilterRange
```

(CurveEditorBakeFilterRange):  [Read-Write] Specifies a custom range to use for baking

<a id="unreal.CurveEditorBakeFilter.custom_range"></a>

#### custom_range

```python
@custom_range.setter
def custom_range(value: CurveEditorBakeFilterRange) -> None
```

<a id="unreal.CurveEditorEulerFilter"></a>