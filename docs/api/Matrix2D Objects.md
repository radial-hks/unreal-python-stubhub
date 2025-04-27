## Matrix2D Objects

```python
class Matrix2D(StructBase)
```

Corresponds to pxr::GfMatrix2d. We don't expose any methods though, this is just to facilitate reading/writing
these types from USD.

**C++ Source:**

- **Plugin**: USDCore
- **Module**: UnrealUSDWrapper
- **File**: UnrealUSDWrapper.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``row0`` (Vector2D):  [Read-Write]
- ``row1`` (Vector2D):  [Read-Write]

<a id="unreal.Matrix2D.__init__"></a>

#### __init__

```python
def __init__(row0: Vector2D = [0.000000, 0.000000],
             row1: Vector2D = [0.000000, 0.000000]) -> None
```

<a id="unreal.Matrix2D.row0"></a>

#### row0

```python
@property
def row0() -> Vector2D
```

(Vector2D):  [Read-Write]

<a id="unreal.Matrix2D.row0"></a>

#### row0

```python
@row0.setter
def row0(value: Vector2D) -> None
```

<a id="unreal.Matrix2D.row1"></a>

#### row1

```python
@property
def row1() -> Vector2D
```

(Vector2D):  [Read-Write]

<a id="unreal.Matrix2D.row1"></a>

#### row1

```python
@row1.setter
def row1(value: Vector2D) -> None
```

<a id="unreal.Matrix3D"></a>