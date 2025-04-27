## CurveSourceInterface Objects

```python
class CurveSourceInterface(Interface)
```

Curve Source Interface

**C++ Source:**

- **Module**: Engine
- **File**: CurveSourceInterface.h

<a id="unreal.CurveSourceInterface.get_curve_value"></a>

#### get_curve_value

```python
def get_curve_value(curve_name: Name) -> float
```

x.get_curve_value(curve_name) -> float
Get the value for a specified curve

Args:
    curve_name (Name): 

Returns:
    float:

<a id="unreal.CurveSourceInterface.get_curves"></a>

#### get_curves

```python
def get_curves() -> Array[NamedCurveValue]
```

x.get_curves() -> Array[NamedCurveValue]
Evaluate all curves that this source provides

Returns:
    Array[NamedCurveValue]: 

    out_values (Array[NamedCurveValue]):

<a id="unreal.CurveSourceInterface.get_binding_name"></a>

#### get_binding_name

```python
def get_binding_name() -> Name
```

x.get_binding_name() -> Name
Get the name that this curve source can be bound to by.
Clients of this curve source will use this name to identify this source.

Returns:
    Name:

<a id="unreal.DataTable"></a>