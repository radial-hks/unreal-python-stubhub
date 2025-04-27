## GeometryScriptDisplaceFromTextureOptions Objects

```python
class GeometryScriptDisplaceFromTextureOptions(StructBase)
```

Geometry Script Displace from Texture Options

**C++ Source:**

- **Plugin**: GeometryScripting
- **Module**: GeometryScriptingCore
- **File**: MeshDeformFunctions.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``center`` (float):  [Read-Write]
- ``empty_behavior`` (GeometryScriptEmptySelectionBehavior):  [Read-Write] EmptyBehavior Defines how an empty input selection should be interpreted
- ``image_channel`` (int32):  [Read-Write]
- ``magnitude`` (float):  [Read-Write]
- ``uv_offset`` (Vector2D):  [Read-Write]
- ``uv_scale`` (Vector2D):  [Read-Write]

<a id="unreal.GeometryScriptDisplaceFromTextureOptions.__init__"></a>

#### __init__

```python
def __init__(
    magnitude: float = 0.000000,
    uv_scale: Vector2D = [0.000000, 0.000000],
    uv_offset: Vector2D = [0.000000, 0.000000],
    center: float = 0.000000,
    image_channel: int = 0,
    empty_behavior:
    GeometryScriptEmptySelectionBehavior = GeometryScriptEmptySelectionBehavior
    .FULL_MESH_SELECTION
) -> None
```

<a id="unreal.GeometryScriptDisplaceFromTextureOptions.magnitude"></a>

#### magnitude

```python
@property
def magnitude() -> float
```

(float):  [Read-Write]

<a id="unreal.GeometryScriptDisplaceFromTextureOptions.magnitude"></a>

#### magnitude

```python
@magnitude.setter
def magnitude(value: float) -> None
```

<a id="unreal.GeometryScriptDisplaceFromTextureOptions.uv_scale"></a>

#### uv_scale

```python
@property
def uv_scale() -> Vector2D
```

(Vector2D):  [Read-Write]

<a id="unreal.GeometryScriptDisplaceFromTextureOptions.uv_scale"></a>

#### uv_scale

```python
@uv_scale.setter
def uv_scale(value: Vector2D) -> None
```

<a id="unreal.GeometryScriptDisplaceFromTextureOptions.uv_offset"></a>

#### uv_offset

```python
@property
def uv_offset() -> Vector2D
```

(Vector2D):  [Read-Write]

<a id="unreal.GeometryScriptDisplaceFromTextureOptions.uv_offset"></a>

#### uv_offset

```python
@uv_offset.setter
def uv_offset(value: Vector2D) -> None
```

<a id="unreal.GeometryScriptDisplaceFromTextureOptions.center"></a>

#### center

```python
@property
def center() -> float
```

(float):  [Read-Write]

<a id="unreal.GeometryScriptDisplaceFromTextureOptions.center"></a>

#### center

```python
@center.setter
def center(value: float) -> None
```

<a id="unreal.GeometryScriptDisplaceFromTextureOptions.image_channel"></a>

#### image_channel

```python
@property
def image_channel() -> int
```

(int32):  [Read-Write]

<a id="unreal.GeometryScriptDisplaceFromTextureOptions.image_channel"></a>

#### image_channel

```python
@image_channel.setter
def image_channel(value: int) -> None
```

<a id="unreal.GeometryScriptDisplaceFromTextureOptions.empty_behavior"></a>

#### empty_behavior

```python
@property
def empty_behavior() -> GeometryScriptEmptySelectionBehavior
```

(GeometryScriptEmptySelectionBehavior):  [Read-Write] EmptyBehavior Defines how an empty input selection should be interpreted

<a id="unreal.GeometryScriptDisplaceFromTextureOptions.empty_behavior"></a>

#### empty_behavior

```python
@empty_behavior.setter
def empty_behavior(value: GeometryScriptEmptySelectionBehavior) -> None
```

<a id="unreal.GeometryScriptMeshEditPolygroupOptions"></a>