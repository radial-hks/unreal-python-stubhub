## GeometryScriptRemoveSmallComponentOptions Objects

```python
class GeometryScriptRemoveSmallComponentOptions(StructBase)
```

Geometry Script Remove Small Component Options

**C++ Source:**

- **Plugin**: GeometryScripting
- **Module**: GeometryScriptingCore
- **File**: MeshRepairFunctions.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``min_area`` (float):  [Read-Write]
- ``min_triangle_count`` (int32):  [Read-Write]
- ``min_volume`` (float):  [Read-Write]

<a id="unreal.GeometryScriptRemoveSmallComponentOptions.__init__"></a>

#### __init__

```python
def __init__(min_volume: float = 0.000000,
             min_area: float = 0.000000,
             min_triangle_count: int = 0) -> None
```

<a id="unreal.GeometryScriptRemoveSmallComponentOptions.min_volume"></a>

#### min_volume

```python
@property
def min_volume() -> float
```

(float):  [Read-Write]

<a id="unreal.GeometryScriptRemoveSmallComponentOptions.min_volume"></a>

#### min_volume

```python
@min_volume.setter
def min_volume(value: float) -> None
```

<a id="unreal.GeometryScriptRemoveSmallComponentOptions.min_area"></a>

#### min_area

```python
@property
def min_area() -> float
```

(float):  [Read-Write]

<a id="unreal.GeometryScriptRemoveSmallComponentOptions.min_area"></a>

#### min_area

```python
@min_area.setter
def min_area(value: float) -> None
```

<a id="unreal.GeometryScriptRemoveSmallComponentOptions.min_triangle_count"></a>

#### min_triangle_count

```python
@property
def min_triangle_count() -> int
```

(int32):  [Read-Write]

<a id="unreal.GeometryScriptRemoveSmallComponentOptions.min_triangle_count"></a>

#### min_triangle_count

```python
@min_triangle_count.setter
def min_triangle_count(value: int) -> None
```

<a id="unreal.GeometryScriptRemoveHiddenTrianglesOptions"></a>