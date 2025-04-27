## CurveBase Objects

```python
class CurveBase(Object)
```

Defines a curve of interpolated points to evaluate over a given range

**C++ Source:**

- **Module**: Engine
- **File**: CurveBase.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``asset_import_data`` (AssetImportData):  [Read-Only]

<a id="unreal.CurveBase.get_value_range"></a>

#### get_value_range

```python
def get_value_range() -> Tuple[float, float]
```

x.get_value_range() -> (min_value=float, max_value=float)
Get the value range across all curves

Returns:
    tuple: 

    min_value (float): 

    max_value (float):

<a id="unreal.CurveBase.get_time_range"></a>

#### get_time_range

```python
def get_time_range() -> Tuple[float, float]
```

x.get_time_range() -> (min_time=float, max_time=float)
Get the time range across all curves

Returns:
    tuple: 

    min_time (float): 

    max_time (float):

<a id="unreal.CurveFloat"></a>