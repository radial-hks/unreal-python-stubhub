## GeometryScriptIterativeMeshSmoothingOptions Objects

```python
class GeometryScriptIterativeMeshSmoothingOptions(StructBase)
```

Geometry Script Iterative Mesh Smoothing Options

**C++ Source:**

- **Plugin**: GeometryScripting
- **Module**: GeometryScriptingCore
- **File**: MeshDeformFunctions.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``alpha`` (float):  [Read-Write]
- ``empty_behavior`` (GeometryScriptEmptySelectionBehavior):  [Read-Write] EmptyBehavior Defines how an empty input selection should be interpreted
- ``num_iterations`` (int32):  [Read-Write]

<a id="unreal.GeometryScriptIterativeMeshSmoothingOptions.__init__"></a>

#### __init__

```python
def __init__(
    num_iterations: int = 0,
    alpha: float = 0.000000,
    empty_behavior:
    GeometryScriptEmptySelectionBehavior = GeometryScriptEmptySelectionBehavior
    .FULL_MESH_SELECTION
) -> None
```

<a id="unreal.GeometryScriptIterativeMeshSmoothingOptions.num_iterations"></a>

#### num_iterations

```python
@property
def num_iterations() -> int
```

(int32):  [Read-Write]

<a id="unreal.GeometryScriptIterativeMeshSmoothingOptions.num_iterations"></a>

#### num_iterations

```python
@num_iterations.setter
def num_iterations(value: int) -> None
```

<a id="unreal.GeometryScriptIterativeMeshSmoothingOptions.alpha"></a>

#### alpha

```python
@property
def alpha() -> float
```

(float):  [Read-Write]

<a id="unreal.GeometryScriptIterativeMeshSmoothingOptions.alpha"></a>

#### alpha

```python
@alpha.setter
def alpha(value: float) -> None
```

<a id="unreal.GeometryScriptIterativeMeshSmoothingOptions.empty_behavior"></a>

#### empty_behavior

```python
@property
def empty_behavior() -> GeometryScriptEmptySelectionBehavior
```

(GeometryScriptEmptySelectionBehavior):  [Read-Write] EmptyBehavior Defines how an empty input selection should be interpreted

<a id="unreal.GeometryScriptIterativeMeshSmoothingOptions.empty_behavior"></a>

#### empty_behavior

```python
@empty_behavior.setter
def empty_behavior(value: GeometryScriptEmptySelectionBehavior) -> None
```

<a id="unreal.GeometryScriptDisplaceFromTextureOptions"></a>