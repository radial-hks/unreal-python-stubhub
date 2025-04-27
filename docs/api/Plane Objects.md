## Plane Objects

```python
class Plane(Vector)
```

A plane definition in 3D space.
note: The full C++ class is located here: Engine\Source\Runtime\Core\Public\Math\Plane.h

**C++ Source:**

- **Module**: CoreUObject
- **File**: NoExportTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``w`` (double):  [Read-Write]
- ``x`` (double):  [Read-Write]
- ``y`` (double):  [Read-Write]
- ``z`` (double):  [Read-Write]

<a id="unreal.Plane.__init__"></a>

#### __init__

```python
def __init__(x: float = 0.000000,
             y: float = 0.000000,
             z: float = 0.000000,
             w: float = 0.000000) -> None
```

<a id="unreal.Plane.w"></a>

#### w

```python
@property
def w() -> float
```

(double):  [Read-Write]

<a id="unreal.Plane.w"></a>

#### w

```python
@w.setter
def w(value: float) -> None
```

<a id="unreal.Matrix44f"></a>