## GeometryScriptMeshOffsetOptions Objects

```python
class GeometryScriptMeshOffsetOptions(StructBase)
```

Geometry Script Mesh Offset Options

**C++ Source:**

- **Plugin**: GeometryScripting
- **Module**: GeometryScriptingCore
- **File**: MeshModelingFunctions.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``boundary_alpha`` (float):  [Read-Write] should not be > 0.9
- ``fixed_boundary`` (bool):  [Read-Write]
- ``offset_distance`` (float):  [Read-Write]
- ``reproject_during_smoothing`` (bool):  [Read-Write]
- ``smooth_alpha`` (float):  [Read-Write]
- ``solve_steps`` (int32):  [Read-Write]

<a id="unreal.GeometryScriptMeshOffsetOptions.__init__"></a>

#### \_\_init\_\_

```python
def __init__(offset_distance: float = 0.000000,
             fixed_boundary: bool = False,
             solve_steps: int = 0,
             smooth_alpha: float = 0.000000,
             reproject_during_smoothing: bool = False,
             boundary_alpha: float = 0.000000) -> None
```

<a id="unreal.GeometryScriptMeshOffsetOptions.offset_distance"></a>

#### offset\_distance

```python
@property
def offset_distance() -> float
```

(float):  [Read-Write]

<a id="unreal.GeometryScriptMeshOffsetOptions.offset_distance"></a>

#### offset\_distance

```python
@offset_distance.setter
def offset_distance(value: float) -> None
```

<a id="unreal.GeometryScriptMeshOffsetOptions.fixed_boundary"></a>

#### fixed\_boundary

```python
@property
def fixed_boundary() -> bool
```

(bool):  [Read-Write]

<a id="unreal.GeometryScriptMeshOffsetOptions.fixed_boundary"></a>

#### fixed\_boundary

```python
@fixed_boundary.setter
def fixed_boundary(value: bool) -> None
```

<a id="unreal.GeometryScriptMeshOffsetOptions.solve_steps"></a>

#### solve\_steps

```python
@property
def solve_steps() -> int
```

(int32):  [Read-Write]

<a id="unreal.GeometryScriptMeshOffsetOptions.solve_steps"></a>

#### solve\_steps

```python
@solve_steps.setter
def solve_steps(value: int) -> None
```

<a id="unreal.GeometryScriptMeshOffsetOptions.smooth_alpha"></a>

#### smooth\_alpha

```python
@property
def smooth_alpha() -> float
```

(float):  [Read-Write]

<a id="unreal.GeometryScriptMeshOffsetOptions.smooth_alpha"></a>

#### smooth\_alpha

```python
@smooth_alpha.setter
def smooth_alpha(value: float) -> None
```

<a id="unreal.GeometryScriptMeshOffsetOptions.reproject_during_smoothing"></a>

#### reproject\_during\_smoothing

```python
@property
def reproject_during_smoothing() -> bool
```

(bool):  [Read-Write]

<a id="unreal.GeometryScriptMeshOffsetOptions.reproject_during_smoothing"></a>

#### reproject\_during\_smoothing

```python
@reproject_during_smoothing.setter
def reproject_during_smoothing(value: bool) -> None
```

<a id="unreal.GeometryScriptMeshOffsetOptions.boundary_alpha"></a>

#### boundary\_alpha

```python
@property
def boundary_alpha() -> float
```

(float):  [Read-Write] should not be > 0.9

<a id="unreal.GeometryScriptMeshOffsetOptions.boundary_alpha"></a>

#### boundary\_alpha

```python
@boundary_alpha.setter
def boundary_alpha(value: float) -> None
```

<a id="unreal.GeometryScriptMeshExtrudeOptions"></a>