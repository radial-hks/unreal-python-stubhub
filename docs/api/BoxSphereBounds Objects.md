## BoxSphereBounds Objects

```python
class BoxSphereBounds(StructBase)
```

A bounding box and bounding sphere with the same origin.
note: The full C++ class is located here : Engine\Source\Runtime\Core\Public\Math\BoxSphereBounds.h

**C++ Source:**

- **Module**: CoreUObject
- **File**: NoExportTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``box_extent`` (Vector):  [Read-Write] Holds the extent of the bounding box, which is half the size of the box in 3D space
- ``origin`` (Vector):  [Read-Write] Holds the origin of the bounding box and sphere.
- ``sphere_radius`` (double):  [Read-Write] Holds the radius of the bounding sphere.

<a id="unreal.BoxSphereBounds.__init__"></a>

#### __init__

```python
def __init__(origin: Vector = [0.000000, 0.000000, 0.000000],
             box_extent: Vector = [0.000000, 0.000000, 0.000000],
             sphere_radius: float = 0.000000) -> None
```

<a id="unreal.BoxSphereBounds.origin"></a>

#### origin

```python
@property
def origin() -> Vector
```

(Vector):  [Read-Write] Holds the origin of the bounding box and sphere.

<a id="unreal.BoxSphereBounds.origin"></a>

#### origin

```python
@origin.setter
def origin(value: Vector) -> None
```

<a id="unreal.BoxSphereBounds.box_extent"></a>

#### box_extent

```python
@property
def box_extent() -> Vector
```

(Vector):  [Read-Write] Holds the extent of the bounding box, which is half the size of the box in 3D space

<a id="unreal.BoxSphereBounds.box_extent"></a>

#### box_extent

```python
@box_extent.setter
def box_extent(value: Vector) -> None
```

<a id="unreal.BoxSphereBounds.sphere_radius"></a>

#### sphere_radius

```python
@property
def sphere_radius() -> float
```

(double):  [Read-Write] Holds the radius of the bounding sphere.

<a id="unreal.BoxSphereBounds.sphere_radius"></a>

#### sphere_radius

```python
@sphere_radius.setter
def sphere_radius(value: float) -> None
```

<a id="unreal.Color"></a>