## GeometryScriptSnapBoundariesOptions Objects

```python
class GeometryScriptSnapBoundariesOptions(StructBase)
```

Geometry Script Snap Boundaries Options

**C++ Source:**

- **Plugin**: GeometryScripting
- **Module**: GeometryScriptingCore
- **File**: MeshRepairFunctions.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``max_iterations`` (int32):  [Read-Write] Maximum number of iterations of boundary snapping to apply. Will stop earlier if an iteration applies no snapping.
- ``snap_to_edges`` (bool):  [Read-Write] Whether to snap vertices to open edges. If false, will only snap together vertices
- ``tolerance`` (float):  [Read-Write] Snapping tolerance

<a id="unreal.GeometryScriptSnapBoundariesOptions.__init__"></a>

#### __init__

```python
def __init__(tolerance: float = 0.000000,
             snap_to_edges: bool = False,
             max_iterations: int = 0) -> None
```

<a id="unreal.GeometryScriptSnapBoundariesOptions.tolerance"></a>

#### tolerance

```python
@property
def tolerance() -> float
```

(float):  [Read-Write] Snapping tolerance

<a id="unreal.GeometryScriptSnapBoundariesOptions.tolerance"></a>

#### tolerance

```python
@tolerance.setter
def tolerance(value: float) -> None
```

<a id="unreal.GeometryScriptSnapBoundariesOptions.snap_to_edges"></a>

#### snap_to_edges

```python
@property
def snap_to_edges() -> bool
```

(bool):  [Read-Write] Whether to snap vertices to open edges. If false, will only snap together vertices

<a id="unreal.GeometryScriptSnapBoundariesOptions.snap_to_edges"></a>

#### snap_to_edges

```python
@snap_to_edges.setter
def snap_to_edges(value: bool) -> None
```

<a id="unreal.GeometryScriptSnapBoundariesOptions.max_iterations"></a>

#### max_iterations

```python
@property
def max_iterations() -> int
```

(int32):  [Read-Write] Maximum number of iterations of boundary snapping to apply. Will stop earlier if an iteration applies no snapping.

<a id="unreal.GeometryScriptSnapBoundariesOptions.max_iterations"></a>

#### max_iterations

```python
@max_iterations.setter
def max_iterations(value: int) -> None
```

<a id="unreal.GeometryScriptFillHolesOptions"></a>