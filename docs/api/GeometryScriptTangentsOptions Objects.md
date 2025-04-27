## GeometryScriptTangentsOptions Objects

```python
class GeometryScriptTangentsOptions(StructBase)
```

Geometry Script Tangents Options

**C++ Source:**

- **Plugin**: GeometryScripting
- **Module**: GeometryScriptingCore
- **File**: MeshNormalsFunctions.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``type`` (GeometryScriptTangentTypes):  [Read-Write]
- ``uv_layer`` (int32):  [Read-Write]

<a id="unreal.GeometryScriptTangentsOptions.__init__"></a>

#### __init__

```python
def __init__(type: GeometryScriptTangentTypes = GeometryScriptTangentTypes.
             FAST_MIKK_T,
             uv_layer: int = 0) -> None
```

<a id="unreal.GeometryScriptTangentsOptions.type"></a>

#### type

```python
@property
def type() -> GeometryScriptTangentTypes
```

(GeometryScriptTangentTypes):  [Read-Write]

<a id="unreal.GeometryScriptTangentsOptions.type"></a>

#### type

```python
@type.setter
def type(value: GeometryScriptTangentTypes) -> None
```

<a id="unreal.GeometryScriptTangentsOptions.uv_layer"></a>

#### uv_layer

```python
@property
def uv_layer() -> int
```

(int32):  [Read-Write]

<a id="unreal.GeometryScriptTangentsOptions.uv_layer"></a>

#### uv_layer

```python
@uv_layer.setter
def uv_layer(value: int) -> None
```

<a id="unreal.GeometryScriptPrimitiveOptions"></a>