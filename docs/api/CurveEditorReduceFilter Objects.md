## CurveEditorReduceFilter Objects

```python
class CurveEditorReduceFilter(CurveEditorFilterBase)
```

Curve Editor Reduce Filter

**C++ Source:**

- **Module**: CurveEditor
- **File**: CurveEditorReduceFilter.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``sample_rate`` (FrameRate):  [Read-Write] Rate at which the curve should be sampled to compare against value tolerance.
- ``tolerance`` (float):  [Read-Write] Minimum change in values required for a key to be considered distinct enough to keep.
- ``try_remove_user_set_tangent_keys`` (bool):  [Read-Write] Flag whether or not to use SampleRate for sampling between evaluated keys, which allows for removing user-tangent keys.

<a id="unreal.CurveEditorReduceFilter.tolerance"></a>

#### tolerance

```python
@property
def tolerance() -> float
```

(float):  [Read-Write] Minimum change in values required for a key to be considered distinct enough to keep.

<a id="unreal.CurveEditorReduceFilter.tolerance"></a>

#### tolerance

```python
@tolerance.setter
def tolerance(value: float) -> None
```

<a id="unreal.CurveEditorReduceFilter.try_remove_user_set_tangent_keys"></a>

#### try_remove_user_set_tangent_keys

```python
@property
def try_remove_user_set_tangent_keys() -> bool
```

(bool):  [Read-Write] Flag whether or not to use SampleRate for sampling between evaluated keys, which allows for removing user-tangent keys.

<a id="unreal.CurveEditorReduceFilter.try_remove_user_set_tangent_keys"></a>

#### try_remove_user_set_tangent_keys

```python
@try_remove_user_set_tangent_keys.setter
def try_remove_user_set_tangent_keys(value: bool) -> None
```

<a id="unreal.CurveEditorReduceFilter.sample_rate"></a>

#### sample_rate

```python
@property
def sample_rate() -> FrameRate
```

(FrameRate):  [Read-Write] Rate at which the curve should be sampled to compare against value tolerance.

<a id="unreal.CurveEditorReduceFilter.sample_rate"></a>

#### sample_rate

```python
@sample_rate.setter
def sample_rate(value: FrameRate) -> None
```

<a id="unreal.CurveEditorSmartReduceFilter"></a>