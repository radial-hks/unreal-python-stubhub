## GeometryScriptSelectiveTessellateOptions Objects

```python
class GeometryScriptSelectiveTessellateOptions(StructBase)
```

Geometry Script Selective Tessellate Options

**C++ Source:**

- **Plugin**: GeometryScripting
- **Module**: GeometryScriptingCore
- **File**: MeshSubdivideFunctions.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``empty_behavior`` (GeometryScriptEmptySelectionBehavior):  [Read-Write] EmptyBehavior Defines how an empty input selection should be interpreted
- ``enable_multithreading`` (bool):  [Read-Write]

<a id="unreal.GeometryScriptSelectiveTessellateOptions.__init__"></a>

#### __init__

```python
def __init__(
    enable_multithreading: bool = False,
    empty_behavior:
    GeometryScriptEmptySelectionBehavior = GeometryScriptEmptySelectionBehavior
    .FULL_MESH_SELECTION
) -> None
```

<a id="unreal.GeometryScriptSelectiveTessellateOptions.enable_multithreading"></a>

#### enable_multithreading

```python
@property
def enable_multithreading() -> bool
```

(bool):  [Read-Write]

<a id="unreal.GeometryScriptSelectiveTessellateOptions.enable_multithreading"></a>

#### enable_multithreading

```python
@enable_multithreading.setter
def enable_multithreading(value: bool) -> None
```

<a id="unreal.GeometryScriptSelectiveTessellateOptions.empty_behavior"></a>

#### empty_behavior

```python
@property
def empty_behavior() -> GeometryScriptEmptySelectionBehavior
```

(GeometryScriptEmptySelectionBehavior):  [Read-Write] EmptyBehavior Defines how an empty input selection should be interpreted

<a id="unreal.GeometryScriptSelectiveTessellateOptions.empty_behavior"></a>

#### empty_behavior

```python
@empty_behavior.setter
def empty_behavior(value: GeometryScriptEmptySelectionBehavior) -> None
```

<a id="unreal.GeometryScriptRepackUVsOptions"></a>