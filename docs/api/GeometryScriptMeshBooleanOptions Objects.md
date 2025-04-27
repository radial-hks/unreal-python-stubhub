## GeometryScriptMeshBooleanOptions Objects

```python
class GeometryScriptMeshBooleanOptions(StructBase)
```

Geometry Script Mesh Boolean Options

**C++ Source:**

- **Plugin**: GeometryScripting
- **Module**: GeometryScriptingCore
- **File**: MeshBooleanFunctions.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``allow_empty_result`` (bool):  [Read-Write] Whether to allow the Mesh Boolean operation to generate an empty mesh as its result
- ``fill_holes`` (bool):  [Read-Write]
- ``simplify_output`` (bool):  [Read-Write]
- ``simplify_planar_tolerance`` (float):  [Read-Write]

<a id="unreal.GeometryScriptMeshBooleanOptions.__init__"></a>

#### __init__

```python
def __init__(fill_holes: bool = False,
             simplify_output: bool = False,
             simplify_planar_tolerance: float = 0.000000,
             allow_empty_result: bool = False) -> None
```

<a id="unreal.GeometryScriptMeshBooleanOptions.fill_holes"></a>

#### fill_holes

```python
@property
def fill_holes() -> bool
```

(bool):  [Read-Write]

<a id="unreal.GeometryScriptMeshBooleanOptions.fill_holes"></a>

#### fill_holes

```python
@fill_holes.setter
def fill_holes(value: bool) -> None
```

<a id="unreal.GeometryScriptMeshBooleanOptions.simplify_output"></a>

#### simplify_output

```python
@property
def simplify_output() -> bool
```

(bool):  [Read-Write]

<a id="unreal.GeometryScriptMeshBooleanOptions.simplify_output"></a>

#### simplify_output

```python
@simplify_output.setter
def simplify_output(value: bool) -> None
```

<a id="unreal.GeometryScriptMeshBooleanOptions.simplify_planar_tolerance"></a>

#### simplify_planar_tolerance

```python
@property
def simplify_planar_tolerance() -> float
```

(float):  [Read-Write]

<a id="unreal.GeometryScriptMeshBooleanOptions.simplify_planar_tolerance"></a>

#### simplify_planar_tolerance

```python
@simplify_planar_tolerance.setter
def simplify_planar_tolerance(value: float) -> None
```

<a id="unreal.GeometryScriptMeshBooleanOptions.allow_empty_result"></a>

#### allow_empty_result

```python
@property
def allow_empty_result() -> bool
```

(bool):  [Read-Write] Whether to allow the Mesh Boolean operation to generate an empty mesh as its result

<a id="unreal.GeometryScriptMeshBooleanOptions.allow_empty_result"></a>

#### allow_empty_result

```python
@allow_empty_result.setter
def allow_empty_result(value: bool) -> None
```

<a id="unreal.GeometryScriptMeshSelfUnionOptions"></a>