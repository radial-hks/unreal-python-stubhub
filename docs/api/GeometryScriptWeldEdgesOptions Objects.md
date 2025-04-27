## GeometryScriptWeldEdgesOptions Objects

```python
class GeometryScriptWeldEdgesOptions(StructBase)
```

Geometry Script Weld Edges Options

**C++ Source:**

- **Plugin**: GeometryScripting
- **Module**: GeometryScriptingCore
- **File**: MeshRepairFunctions.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``only_unique_pairs`` (bool):  [Read-Write] Only merge unambiguous pairs that have unique duplicate-edge matches
- ``tolerance`` (float):  [Read-Write] Edges are coincident if both pairs of endpoint vertices, and their midpoint, are closer than this distance

<a id="unreal.GeometryScriptWeldEdgesOptions.__init__"></a>

#### __init__

```python
def __init__(tolerance: float = 0.000000,
             only_unique_pairs: bool = False) -> None
```

<a id="unreal.GeometryScriptWeldEdgesOptions.tolerance"></a>

#### tolerance

```python
@property
def tolerance() -> float
```

(float):  [Read-Write] Edges are coincident if both pairs of endpoint vertices, and their midpoint, are closer than this distance

<a id="unreal.GeometryScriptWeldEdgesOptions.tolerance"></a>

#### tolerance

```python
@tolerance.setter
def tolerance(value: float) -> None
```

<a id="unreal.GeometryScriptWeldEdgesOptions.only_unique_pairs"></a>

#### only_unique_pairs

```python
@property
def only_unique_pairs() -> bool
```

(bool):  [Read-Write] Only merge unambiguous pairs that have unique duplicate-edge matches

<a id="unreal.GeometryScriptWeldEdgesOptions.only_unique_pairs"></a>

#### only_unique_pairs

```python
@only_unique_pairs.setter
def only_unique_pairs(value: bool) -> None
```

<a id="unreal.GeometryScriptResolveTJunctionOptions"></a>