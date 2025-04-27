## GeometryScriptPerlinNoiseOptions Objects

```python
class GeometryScriptPerlinNoiseOptions(StructBase)
```

Geometry Script Perlin Noise Options

**C++ Source:**

- **Plugin**: GeometryScripting
- **Module**: GeometryScriptingCore
- **File**: MeshDeformFunctions.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``apply_along_normal`` (bool):  [Read-Write]
- ``base_layer`` (GeometryScriptPerlinNoiseLayerOptions):  [Read-Write]
- ``empty_behavior`` (GeometryScriptEmptySelectionBehavior):  [Read-Write] EmptyBehavior Defines how an empty input selection should be interpreted

<a id="unreal.GeometryScriptPerlinNoiseOptions.__init__"></a>

#### __init__

```python
def __init__(
    base_layer: GeometryScriptPerlinNoiseLayerOptions = [
        5.000000, 0.250000, [0.000000, 0.000000, 0.000000], 0
    ],
    apply_along_normal: bool = False,
    empty_behavior:
    GeometryScriptEmptySelectionBehavior = GeometryScriptEmptySelectionBehavior
    .FULL_MESH_SELECTION
) -> None
```

<a id="unreal.GeometryScriptPerlinNoiseOptions.base_layer"></a>

#### base_layer

```python
@property
def base_layer() -> GeometryScriptPerlinNoiseLayerOptions
```

(GeometryScriptPerlinNoiseLayerOptions):  [Read-Write]

<a id="unreal.GeometryScriptPerlinNoiseOptions.base_layer"></a>

#### base_layer

```python
@base_layer.setter
def base_layer(value: GeometryScriptPerlinNoiseLayerOptions) -> None
```

<a id="unreal.GeometryScriptPerlinNoiseOptions.apply_along_normal"></a>

#### apply_along_normal

```python
@property
def apply_along_normal() -> bool
```

(bool):  [Read-Write]

<a id="unreal.GeometryScriptPerlinNoiseOptions.apply_along_normal"></a>

#### apply_along_normal

```python
@apply_along_normal.setter
def apply_along_normal(value: bool) -> None
```

<a id="unreal.GeometryScriptPerlinNoiseOptions.empty_behavior"></a>

#### empty_behavior

```python
@property
def empty_behavior() -> GeometryScriptEmptySelectionBehavior
```

(GeometryScriptEmptySelectionBehavior):  [Read-Write] EmptyBehavior Defines how an empty input selection should be interpreted

<a id="unreal.GeometryScriptPerlinNoiseOptions.empty_behavior"></a>

#### empty_behavior

```python
@empty_behavior.setter
def empty_behavior(value: GeometryScriptEmptySelectionBehavior) -> None
```

<a id="unreal.GeometryScriptIterativeMeshSmoothingOptions"></a>