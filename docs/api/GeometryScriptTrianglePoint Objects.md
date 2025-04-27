## GeometryScriptTrianglePoint Objects

```python
class GeometryScriptTrianglePoint(StructBase)
```

Geometry Script Triangle Point

**C++ Source:**

- **Plugin**: GeometryScripting
- **Module**: GeometryScriptingCore
- **File**: GeometryScriptTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``bary_coords`` (Vector):  [Read-Write]
- ``position`` (Vector):  [Read-Write]
- ``triangle_id`` (int32):  [Read-Write]
- ``valid`` (bool):  [Read-Write]

<a id="unreal.GeometryScriptTrianglePoint.__init__"></a>

#### __init__

```python
def __init__(valid: bool = False,
             triangle_id: int = 0,
             position: Vector = [0.000000, 0.000000, 0.000000],
             bary_coords: Vector = [0.000000, 0.000000, 0.000000]) -> None
```

<a id="unreal.GeometryScriptTrianglePoint.valid"></a>

#### valid

```python
@property
def valid() -> bool
```

(bool):  [Read-Write]

<a id="unreal.GeometryScriptTrianglePoint.valid"></a>

#### valid

```python
@valid.setter
def valid(value: bool) -> None
```

<a id="unreal.GeometryScriptTrianglePoint.triangle_id"></a>

#### triangle_id

```python
@property
def triangle_id() -> int
```

(int32):  [Read-Write]

<a id="unreal.GeometryScriptTrianglePoint.triangle_id"></a>

#### triangle_id

```python
@triangle_id.setter
def triangle_id(value: int) -> None
```

<a id="unreal.GeometryScriptTrianglePoint.position"></a>

#### position

```python
@property
def position() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.GeometryScriptTrianglePoint.position"></a>

#### position

```python
@position.setter
def position(value: Vector) -> None
```

<a id="unreal.GeometryScriptTrianglePoint.bary_coords"></a>

#### bary_coords

```python
@property
def bary_coords() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.GeometryScriptTrianglePoint.bary_coords"></a>

#### bary_coords

```python
@bary_coords.setter
def bary_coords(value: Vector) -> None
```

<a id="unreal.GeometryScriptUVTriangle"></a>