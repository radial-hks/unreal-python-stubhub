## ProcMeshVertex Objects

```python
class ProcMeshVertex(StructBase)
```

One vertex for the procedural mesh, used for storing data internally

**C++ Source:**

- **Plugin**: ProceduralMeshComponent
- **Module**: ProceduralMeshComponent
- **File**: ProceduralMeshComponent.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``color`` (Color):  [Read-Write] Vertex color
- ``normal`` (Vector):  [Read-Write] Vertex normal
- ``position`` (Vector):  [Read-Write] Vertex position
- ``tangent`` (ProcMeshTangent):  [Read-Write] Vertex tangent
- ``uv0`` (Vector2D):  [Read-Write] Vertex texture co-ordinate
- ``uv1`` (Vector2D):  [Read-Write] Vertex texture co-ordinate
- ``uv2`` (Vector2D):  [Read-Write] Vertex texture co-ordinate
- ``uv3`` (Vector2D):  [Read-Write] Vertex texture co-ordinate

<a id="unreal.ProcMeshVertex.__init__"></a>

#### __init__

```python
def __init__(position: Vector = [0.000000, 0.000000, 0.000000],
             normal: Vector = [0.000000, 0.000000, 0.000000],
             tangent: ProcMeshTangent = [[1.000000, 0.000000, 0.000000],
                                         False],
             color: Color = [0, 0, 0, 0],
             uv0: Vector2D = [0.000000, 0.000000],
             uv1: Vector2D = [0.000000, 0.000000],
             uv2: Vector2D = [0.000000, 0.000000],
             uv3: Vector2D = [0.000000, 0.000000]) -> None
```

<a id="unreal.ProcMeshVertex.position"></a>

#### position

```python
@property
def position() -> Vector
```

(Vector):  [Read-Write] Vertex position

<a id="unreal.ProcMeshVertex.position"></a>

#### position

```python
@position.setter
def position(value: Vector) -> None
```

<a id="unreal.ProcMeshVertex.normal"></a>

#### normal

```python
@property
def normal() -> Vector
```

(Vector):  [Read-Write] Vertex normal

<a id="unreal.ProcMeshVertex.normal"></a>

#### normal

```python
@normal.setter
def normal(value: Vector) -> None
```

<a id="unreal.ProcMeshVertex.tangent"></a>

#### tangent

```python
@property
def tangent() -> ProcMeshTangent
```

(ProcMeshTangent):  [Read-Write] Vertex tangent

<a id="unreal.ProcMeshVertex.tangent"></a>

#### tangent

```python
@tangent.setter
def tangent(value: ProcMeshTangent) -> None
```

<a id="unreal.ProcMeshVertex.color"></a>

#### color

```python
@property
def color() -> Color
```

(Color):  [Read-Write] Vertex color

<a id="unreal.ProcMeshVertex.color"></a>

#### color

```python
@color.setter
def color(value: Color) -> None
```

<a id="unreal.ProcMeshVertex.uv0"></a>

#### uv0

```python
@property
def uv0() -> Vector2D
```

(Vector2D):  [Read-Write] Vertex texture co-ordinate

<a id="unreal.ProcMeshVertex.uv0"></a>

#### uv0

```python
@uv0.setter
def uv0(value: Vector2D) -> None
```

<a id="unreal.ProcMeshVertex.uv1"></a>

#### uv1

```python
@property
def uv1() -> Vector2D
```

(Vector2D):  [Read-Write] Vertex texture co-ordinate

<a id="unreal.ProcMeshVertex.uv1"></a>

#### uv1

```python
@uv1.setter
def uv1(value: Vector2D) -> None
```

<a id="unreal.ProcMeshVertex.uv2"></a>

#### uv2

```python
@property
def uv2() -> Vector2D
```

(Vector2D):  [Read-Write] Vertex texture co-ordinate

<a id="unreal.ProcMeshVertex.uv2"></a>

#### uv2

```python
@uv2.setter
def uv2(value: Vector2D) -> None
```

<a id="unreal.ProcMeshVertex.uv3"></a>

#### uv3

```python
@property
def uv3() -> Vector2D
```

(Vector2D):  [Read-Write] Vertex texture co-ordinate

<a id="unreal.ProcMeshVertex.uv3"></a>

#### uv3

```python
@uv3.setter
def uv3(value: Vector2D) -> None
```

<a id="unreal.ActorLayer"></a>