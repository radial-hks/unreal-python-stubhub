## GeometryScriptMeshSelfUnionOptions Objects

```python
class GeometryScriptMeshSelfUnionOptions(StructBase)
```

Geometry Script Mesh Self Union Options

**C++ Source:**

- **Plugin**: GeometryScripting
- **Module**: GeometryScriptingCore
- **File**: MeshBooleanFunctions.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``fill_holes`` (bool):  [Read-Write]
- ``simplify_output`` (bool):  [Read-Write]
- ``simplify_planar_tolerance`` (float):  [Read-Write]
- ``trim_flaps`` (bool):  [Read-Write]
- ``winding_threshold`` (float):  [Read-Write]

<a id="unreal.GeometryScriptMeshSelfUnionOptions.__init__"></a>

#### __init__

```python
def __init__(fill_holes: bool = False,
             trim_flaps: bool = False,
             simplify_output: bool = False,
             simplify_planar_tolerance: float = 0.000000,
             winding_threshold: float = 0.000000) -> None
```

<a id="unreal.GeometryScriptMeshSelfUnionOptions.fill_holes"></a>

#### fill_holes

```python
@property
def fill_holes() -> bool
```

(bool):  [Read-Write]

<a id="unreal.GeometryScriptMeshSelfUnionOptions.fill_holes"></a>

#### fill_holes

```python
@fill_holes.setter
def fill_holes(value: bool) -> None
```

<a id="unreal.GeometryScriptMeshSelfUnionOptions.trim_flaps"></a>

#### trim_flaps

```python
@property
def trim_flaps() -> bool
```

(bool):  [Read-Write]

<a id="unreal.GeometryScriptMeshSelfUnionOptions.trim_flaps"></a>

#### trim_flaps

```python
@trim_flaps.setter
def trim_flaps(value: bool) -> None
```

<a id="unreal.GeometryScriptMeshSelfUnionOptions.simplify_output"></a>

#### simplify_output

```python
@property
def simplify_output() -> bool
```

(bool):  [Read-Write]

<a id="unreal.GeometryScriptMeshSelfUnionOptions.simplify_output"></a>

#### simplify_output

```python
@simplify_output.setter
def simplify_output(value: bool) -> None
```

<a id="unreal.GeometryScriptMeshSelfUnionOptions.simplify_planar_tolerance"></a>

#### simplify_planar_tolerance

```python
@property
def simplify_planar_tolerance() -> float
```

(float):  [Read-Write]

<a id="unreal.GeometryScriptMeshSelfUnionOptions.simplify_planar_tolerance"></a>

#### simplify_planar_tolerance

```python
@simplify_planar_tolerance.setter
def simplify_planar_tolerance(value: float) -> None
```

<a id="unreal.GeometryScriptMeshSelfUnionOptions.winding_threshold"></a>

#### winding_threshold

```python
@property
def winding_threshold() -> float
```

(float):  [Read-Write]

<a id="unreal.GeometryScriptMeshSelfUnionOptions.winding_threshold"></a>

#### winding_threshold

```python
@winding_threshold.setter
def winding_threshold(value: float) -> None
```

<a id="unreal.GeometryScriptMeshPlaneCutOptions"></a>