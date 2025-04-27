## GeometryScriptSweptHullOptions Objects

```python
class GeometryScriptSweptHullOptions(StructBase)
```

Geometry Script Swept Hull Options

**C++ Source:**

- **Plugin**: GeometryScripting
- **Module**: GeometryScriptingCore
- **File**: ContainmentFunctions.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``min_edge_length`` (float):  [Read-Write]
- ``min_thickness`` (float):  [Read-Write]
- ``prefilter_grid_resolution`` (int32):  [Read-Write]
- ``prefilter_vertices`` (bool):  [Read-Write]
- ``simplify`` (bool):  [Read-Write]
- ``simplify_tolerance`` (float):  [Read-Write]

<a id="unreal.GeometryScriptSweptHullOptions.__init__"></a>

#### __init__

```python
def __init__(prefilter_vertices: bool = False,
             prefilter_grid_resolution: int = 0,
             min_thickness: float = 0.000000,
             simplify: bool = False,
             min_edge_length: float = 0.000000,
             simplify_tolerance: float = 0.000000) -> None
```

<a id="unreal.GeometryScriptSweptHullOptions.prefilter_vertices"></a>

#### prefilter_vertices

```python
@property
def prefilter_vertices() -> bool
```

(bool):  [Read-Write]

<a id="unreal.GeometryScriptSweptHullOptions.prefilter_vertices"></a>

#### prefilter_vertices

```python
@prefilter_vertices.setter
def prefilter_vertices(value: bool) -> None
```

<a id="unreal.GeometryScriptSweptHullOptions.prefilter_grid_resolution"></a>

#### prefilter_grid_resolution

```python
@property
def prefilter_grid_resolution() -> int
```

(int32):  [Read-Write]

<a id="unreal.GeometryScriptSweptHullOptions.prefilter_grid_resolution"></a>

#### prefilter_grid_resolution

```python
@prefilter_grid_resolution.setter
def prefilter_grid_resolution(value: int) -> None
```

<a id="unreal.GeometryScriptSweptHullOptions.min_thickness"></a>

#### min_thickness

```python
@property
def min_thickness() -> float
```

(float):  [Read-Write]

<a id="unreal.GeometryScriptSweptHullOptions.min_thickness"></a>

#### min_thickness

```python
@min_thickness.setter
def min_thickness(value: float) -> None
```

<a id="unreal.GeometryScriptSweptHullOptions.simplify"></a>

#### simplify

```python
@property
def simplify() -> bool
```

(bool):  [Read-Write]

<a id="unreal.GeometryScriptSweptHullOptions.simplify"></a>

#### simplify

```python
@simplify.setter
def simplify(value: bool) -> None
```

<a id="unreal.GeometryScriptSweptHullOptions.min_edge_length"></a>

#### min_edge_length

```python
@property
def min_edge_length() -> float
```

(float):  [Read-Write]

<a id="unreal.GeometryScriptSweptHullOptions.min_edge_length"></a>

#### min_edge_length

```python
@min_edge_length.setter
def min_edge_length(value: float) -> None
```

<a id="unreal.GeometryScriptSweptHullOptions.simplify_tolerance"></a>

#### simplify_tolerance

```python
@property
def simplify_tolerance() -> float
```

(float):  [Read-Write]

<a id="unreal.GeometryScriptSweptHullOptions.simplify_tolerance"></a>

#### simplify_tolerance

```python
@simplify_tolerance.setter
def simplify_tolerance(value: float) -> None
```

<a id="unreal.GeometryScriptConvexDecompositionOptions"></a>