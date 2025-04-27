## ProcMeshTangent Objects

```python
class ProcMeshTangent(StructBase)
```

Struct used to specify a tangent vector for a vertex
The Y tangent is computed from the cross product of the vertex normal (Tangent Z) and the TangentX member.

**C++ Source:**

- **Plugin**: ProceduralMeshComponent
- **Module**: ProceduralMeshComponent
- **File**: ProceduralMeshComponent.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``flip_tangent_y`` (bool):  [Read-Write] Bool that indicates whether we should flip the Y tangent when we compute it using cross product
- ``tangent_x`` (Vector):  [Read-Write] Direction of X tangent for this vertex

<a id="unreal.ProcMeshTangent.__init__"></a>

#### __init__

```python
def __init__(tangent_x: Vector = [0.000000, 0.000000, 0.000000],
             flip_tangent_y: bool = False) -> None
```

<a id="unreal.ProcMeshTangent.tangent_x"></a>

#### tangent_x

```python
@property
def tangent_x() -> Vector
```

(Vector):  [Read-Write] Direction of X tangent for this vertex

<a id="unreal.ProcMeshTangent.tangent_x"></a>

#### tangent_x

```python
@tangent_x.setter
def tangent_x(value: Vector) -> None
```

<a id="unreal.ProcMeshTangent.flip_tangent_y"></a>

#### flip_tangent_y

```python
@property
def flip_tangent_y() -> bool
```

(bool):  [Read-Write] Bool that indicates whether we should flip the Y tangent when we compute it using cross product

<a id="unreal.ProcMeshTangent.flip_tangent_y"></a>

#### flip_tangent_y

```python
@flip_tangent_y.setter
def flip_tangent_y(value: bool) -> None
```

<a id="unreal.ProcMeshVertex"></a>