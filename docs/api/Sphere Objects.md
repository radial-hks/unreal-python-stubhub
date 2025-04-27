## Sphere Objects

```python
class Sphere(StructBase)
```

3D Sphere represented by Center and Radius.
note: The full C++ class is located here: Engine\Source\Runtime\Core\Public\Math\Sphere.h

**C++ Source:**

- **Module**: CoreUObject
- **File**: NoExportTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``center`` (Vector):  [Read-Write]
- ``w`` (double):  [Read-Write]

<a id="unreal.Sphere.__init__"></a>

#### __init__

```python
def __init__(center: Vector = [0.000000, 0.000000, 0.000000],
             w: float = 0.000000) -> None
```

<a id="unreal.Sphere.center"></a>

#### center

```python
@property
def center() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.Sphere.center"></a>

#### center

```python
@center.setter
def center(value: Vector) -> None
```

<a id="unreal.Sphere.w"></a>

#### w

```python
@property
def w() -> float
```

(double):  [Read-Write]

<a id="unreal.Sphere.w"></a>

#### w

```python
@w.setter
def w(value: float) -> None
```

<a id="unreal.TemplateString"></a>