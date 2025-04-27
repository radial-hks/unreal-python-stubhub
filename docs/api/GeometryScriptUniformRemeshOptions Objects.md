## GeometryScriptUniformRemeshOptions Objects

```python
class GeometryScriptUniformRemeshOptions(StructBase)
```

Uniform Remeshing Options

**C++ Source:**

- **Plugin**: GeometryScripting
- **Module**: GeometryScriptingCore
- **File**: MeshRemeshFunctions.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``target_edge_length`` (float):  [Read-Write] Explicit Target Edge Length that is desired in the output uniform mesh
- ``target_triangle_count`` (int32):  [Read-Write] Approximate Target Triangle Count, combined with mesh surface area to derive a TargetEdgeLength
- ``target_type`` (GeometryScriptUniformRemeshTargetType):  [Read-Write] Method used to define target/goal of Uniform Remeshing

<a id="unreal.GeometryScriptUniformRemeshOptions.__init__"></a>

#### __init__

```python
def __init__(
        target_type:
    GeometryScriptUniformRemeshTargetType = GeometryScriptUniformRemeshTargetType
    .TRIANGLE_COUNT,
        target_triangle_count: int = 0,
        target_edge_length: float = 0.000000) -> None
```

<a id="unreal.GeometryScriptUniformRemeshOptions.target_type"></a>

#### target_type

```python
@property
def target_type() -> GeometryScriptUniformRemeshTargetType
```

(GeometryScriptUniformRemeshTargetType):  [Read-Write] Method used to define target/goal of Uniform Remeshing

<a id="unreal.GeometryScriptUniformRemeshOptions.target_type"></a>

#### target_type

```python
@target_type.setter
def target_type(value: GeometryScriptUniformRemeshTargetType) -> None
```

<a id="unreal.GeometryScriptUniformRemeshOptions.target_triangle_count"></a>

#### target_triangle_count

```python
@property
def target_triangle_count() -> int
```

(int32):  [Read-Write] Approximate Target Triangle Count, combined with mesh surface area to derive a TargetEdgeLength

<a id="unreal.GeometryScriptUniformRemeshOptions.target_triangle_count"></a>

#### target_triangle_count

```python
@target_triangle_count.setter
def target_triangle_count(value: int) -> None
```

<a id="unreal.GeometryScriptUniformRemeshOptions.target_edge_length"></a>

#### target_edge_length

```python
@property
def target_edge_length() -> float
```

(float):  [Read-Write] Explicit Target Edge Length that is desired in the output uniform mesh

<a id="unreal.GeometryScriptUniformRemeshOptions.target_edge_length"></a>

#### target_edge_length

```python
@target_edge_length.setter
def target_edge_length(value: float) -> None
```

<a id="unreal.GeometryScriptWeldEdgesOptions"></a>