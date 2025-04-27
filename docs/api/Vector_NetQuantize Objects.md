## Vector_NetQuantize Objects

```python
class Vector_NetQuantize(Vector)
```

FVector_NetQuantize

0 decimal place of precision.
Up to 20 bits per component.
Valid range: 2^20 = +/- 1,048,576

Note: this is the historical UE format for vector net serialization

**C++ Source:**

- **Module**: Engine
- **File**: NetSerialization.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``x`` (double):  [Read-Write]
- ``y`` (double):  [Read-Write]
- ``z`` (double):  [Read-Write]

<a id="unreal.Vector_NetQuantize.__init__"></a>

#### __init__

```python
def __init__(x: float = 0.000000,
             y: float = 0.000000,
             z: float = 0.000000) -> None
```

<a id="unreal.Vector_NetQuantizeNormal"></a>