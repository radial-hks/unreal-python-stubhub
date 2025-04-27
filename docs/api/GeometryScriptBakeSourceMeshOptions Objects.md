## GeometryScriptBakeSourceMeshOptions Objects

```python
class GeometryScriptBakeSourceMeshOptions(StructBase)
```

Geometry Script Bake Source Mesh Options

**C++ Source:**

- **Plugin**: GeometryScripting
- **Module**: GeometryScriptingCore
- **File**: MeshBakeFunctions.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``source_normal_map`` (Texture2D):  [Read-Write]
- ``source_normal_space`` (GeometryScriptBakeNormalSpace):  [Read-Write]
- ``source_normal_uv_layer`` (int32):  [Read-Write]

<a id="unreal.GeometryScriptBakeSourceMeshOptions.__init__"></a>

#### __init__

```python
def __init__(
    source_normal_map: Texture2D = None,
    source_normal_uv_layer: int = 0,
    source_normal_space:
    GeometryScriptBakeNormalSpace = GeometryScriptBakeNormalSpace.TANGENT
) -> None
```

<a id="unreal.GeometryScriptBakeSourceMeshOptions.source_normal_map"></a>

#### source_normal_map

```python
@property
def source_normal_map() -> Texture2D
```

(Texture2D):  [Read-Write]

<a id="unreal.GeometryScriptBakeSourceMeshOptions.source_normal_map"></a>

#### source_normal_map

```python
@source_normal_map.setter
def source_normal_map(value: Texture2D) -> None
```

<a id="unreal.GeometryScriptBakeSourceMeshOptions.source_normal_uv_layer"></a>

#### source_normal_uv_layer

```python
@property
def source_normal_uv_layer() -> int
```

(int32):  [Read-Write]

<a id="unreal.GeometryScriptBakeSourceMeshOptions.source_normal_uv_layer"></a>

#### source_normal_uv_layer

```python
@source_normal_uv_layer.setter
def source_normal_uv_layer(value: int) -> None
```

<a id="unreal.GeometryScriptBakeSourceMeshOptions.source_normal_space"></a>

#### source_normal_space

```python
@property
def source_normal_space() -> GeometryScriptBakeNormalSpace
```

(GeometryScriptBakeNormalSpace):  [Read-Write]

<a id="unreal.GeometryScriptBakeSourceMeshOptions.source_normal_space"></a>

#### source_normal_space

```python
@source_normal_space.setter
def source_normal_space(value: GeometryScriptBakeNormalSpace) -> None
```

<a id="unreal.GeometryScriptBakeRenderCaptureOptions"></a>