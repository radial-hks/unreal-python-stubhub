## Matrix3D Objects

```python
class Matrix3D(StructBase)
```

Corresponds to pxr::GfMatrix3d. We don't expose any methods though, this is just to facilitate reading/writing
these types from USD.

**C++ Source:**

- **Plugin**: USDCore
- **Module**: UnrealUSDWrapper
- **File**: UnrealUSDWrapper.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``row0`` (Vector):  [Read-Write]
- ``row1`` (Vector):  [Read-Write]
- ``row2`` (Vector):  [Read-Write]

<a id="unreal.Matrix3D.__init__"></a>

#### __init__

```python
def __init__(row0: Vector = [0.000000, 0.000000, 0.000000],
             row1: Vector = [0.000000, 0.000000, 0.000000],
             row2: Vector = [0.000000, 0.000000, 0.000000]) -> None
```

<a id="unreal.Matrix3D.row0"></a>

#### row0

```python
@property
def row0() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.Matrix3D.row0"></a>

#### row0

```python
@row0.setter
def row0(value: Vector) -> None
```

<a id="unreal.Matrix3D.row1"></a>

#### row1

```python
@property
def row1() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.Matrix3D.row1"></a>

#### row1

```python
@row1.setter
def row1(value: Vector) -> None
```

<a id="unreal.Matrix3D.row2"></a>

#### row2

```python
@property
def row2() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.Matrix3D.row2"></a>

#### row2

```python
@row2.setter
def row2(value: Vector) -> None
```

<a id="unreal.LiveLinkTransformControllerData"></a>