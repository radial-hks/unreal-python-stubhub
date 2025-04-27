## GaussianParams Objects

```python
class GaussianParams(StructBase)
```

Gaussian Params

**C++ Source:**

- **Module**: CurveEditor
- **File**: CurveEditorGaussianFilter.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``kernel_width`` (int32):  [Read-Write] Sigma that determines how 'fat' the filter is, higher value means fatter width

<a id="unreal.GaussianParams.__init__"></a>

#### __init__

```python
def __init__(kernel_width: int = 0) -> None
```

<a id="unreal.GaussianParams.kernel_width"></a>

#### kernel_width

```python
@property
def kernel_width() -> int
```

(int32):  [Read-Write] Sigma that determines how 'fat' the filter is, higher value means fatter width

<a id="unreal.GaussianParams.kernel_width"></a>

#### kernel_width

```python
@kernel_width.setter
def kernel_width(value: int) -> None
```

<a id="unreal.SmartReduceParams"></a>