## GeometryScriptDegenerateTriangleOptions Objects

```python
class GeometryScriptDegenerateTriangleOptions(StructBase)
```

Geometry Script Degenerate Triangle Options

**C++ Source:**

- **Plugin**: GeometryScripting
- **Module**: GeometryScriptingCore
- **File**: MeshRepairFunctions.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``compact_on_completion`` (bool):  [Read-Write]
- ``min_edge_length`` (double):  [Read-Write]
- ``min_triangle_area`` (double):  [Read-Write]
- ``mode`` (GeometryScriptRepairMeshMode):  [Read-Write]

<a id="unreal.GeometryScriptDegenerateTriangleOptions.__init__"></a>

#### __init__

```python
def __init__(mode: GeometryScriptRepairMeshMode = GeometryScriptRepairMeshMode.
             DELETE_ONLY,
             min_triangle_area: float = 0.000000,
             min_edge_length: float = 0.000000,
             compact_on_completion: bool = False) -> None
```

<a id="unreal.GeometryScriptDegenerateTriangleOptions.mode"></a>

#### mode

```python
@property
def mode() -> GeometryScriptRepairMeshMode
```

(GeometryScriptRepairMeshMode):  [Read-Write]

<a id="unreal.GeometryScriptDegenerateTriangleOptions.mode"></a>

#### mode

```python
@mode.setter
def mode(value: GeometryScriptRepairMeshMode) -> None
```

<a id="unreal.GeometryScriptDegenerateTriangleOptions.min_triangle_area"></a>

#### min_triangle_area

```python
@property
def min_triangle_area() -> float
```

(double):  [Read-Write]

<a id="unreal.GeometryScriptDegenerateTriangleOptions.min_triangle_area"></a>

#### min_triangle_area

```python
@min_triangle_area.setter
def min_triangle_area(value: float) -> None
```

<a id="unreal.GeometryScriptDegenerateTriangleOptions.min_edge_length"></a>

#### min_edge_length

```python
@property
def min_edge_length() -> float
```

(double):  [Read-Write]

<a id="unreal.GeometryScriptDegenerateTriangleOptions.min_edge_length"></a>

#### min_edge_length

```python
@min_edge_length.setter
def min_edge_length(value: float) -> None
```

<a id="unreal.GeometryScriptDegenerateTriangleOptions.compact_on_completion"></a>

#### compact_on_completion

```python
@property
def compact_on_completion() -> bool
```

(bool):  [Read-Write]

<a id="unreal.GeometryScriptDegenerateTriangleOptions.compact_on_completion"></a>

#### compact_on_completion

```python
@compact_on_completion.setter
def compact_on_completion(value: bool) -> None
```

<a id="unreal.GeometryScriptMeshPointSamplingOptions"></a>