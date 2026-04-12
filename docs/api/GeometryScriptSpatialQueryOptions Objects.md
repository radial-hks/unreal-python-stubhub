## GeometryScriptSpatialQueryOptions Objects

```python
class GeometryScriptSpatialQueryOptions(StructBase)
```

Geometry Script Spatial Query Options

**C++ Source:**

- **Plugin**: GeometryScripting
- **Module**: GeometryScriptingCore
- **File**: MeshSpatialFunctions.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``allow_unsafe_modified_queries`` (bool):  [Read-Write] When true, allows the provided BHV to be used even if the mesh has been updated
- ``max_distance`` (float):  [Read-Write]
- ``winding_iso_threshold`` (float):  [Read-Write]

<a id="unreal.GeometryScriptSpatialQueryOptions.__init__"></a>

#### \_\_init\_\_

```python
def __init__(max_distance: float = 0.000000,
             allow_unsafe_modified_queries: bool = False,
             winding_iso_threshold: float = 0.000000) -> None
```

<a id="unreal.GeometryScriptSpatialQueryOptions.max_distance"></a>

#### max\_distance

```python
@property
def max_distance() -> float
```

(float):  [Read-Write]

<a id="unreal.GeometryScriptSpatialQueryOptions.max_distance"></a>

#### max\_distance

```python
@max_distance.setter
def max_distance(value: float) -> None
```

<a id="unreal.GeometryScriptSpatialQueryOptions.allow_unsafe_modified_queries"></a>

#### allow\_unsafe\_modified\_queries

```python
@property
def allow_unsafe_modified_queries() -> bool
```

(bool):  [Read-Write] When true, allows the provided BHV to be used even if the mesh has been updated

<a id="unreal.GeometryScriptSpatialQueryOptions.allow_unsafe_modified_queries"></a>

#### allow\_unsafe\_modified\_queries

```python
@allow_unsafe_modified_queries.setter
def allow_unsafe_modified_queries(value: bool) -> None
```

<a id="unreal.GeometryScriptSpatialQueryOptions.winding_iso_threshold"></a>

#### winding\_iso\_threshold

```python
@property
def winding_iso_threshold() -> float
```

(float):  [Read-Write]

<a id="unreal.GeometryScriptSpatialQueryOptions.winding_iso_threshold"></a>

#### winding\_iso\_threshold

```python
@winding_iso_threshold.setter
def winding_iso_threshold(value: float) -> None
```

<a id="unreal.GeometryScriptRayHitResult"></a>