## GeometryScriptRemoveHiddenTrianglesOptions Objects

```python
class GeometryScriptRemoveHiddenTrianglesOptions(StructBase)
```

Geometry Script Remove Hidden Triangles Options

**C++ Source:**

- **Plugin**: GeometryScripting
- **Module**: GeometryScriptingCore
- **File**: MeshRepairFunctions.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``compact_result`` (bool):  [Read-Write]
- ``method`` (GeometryScriptRemoveHiddenTrianglesMethod):  [Read-Write]
- ``normal_offset`` (float):  [Read-Write] Nudge sample points out by this amount to try to counteract numerical issues
- ``rays_per_sample`` (int32):  [Read-Write] random rays to add beyond +/- major axes, for raycast sampling
- ``samples_per_triangle`` (int32):  [Read-Write] add triangle samples per triangle (in addition to TriangleSamplingMethod)
- ``shrink_selection`` (int32):  [Read-Write] once triangles to remove are identified, do iterations of boundary erosion, ie contract selection by boundary vertex one-rings
- ``winding_iso_value`` (float):  [Read-Write] use this as winding isovalue for WindingNumber mode

<a id="unreal.GeometryScriptRemoveHiddenTrianglesOptions.__init__"></a>

#### __init__

```python
def __init__(
        method:
    GeometryScriptRemoveHiddenTrianglesMethod = GeometryScriptRemoveHiddenTrianglesMethod
    .FAST_WINDING_NUMBER,
        samples_per_triangle: int = 0,
        shrink_selection: int = 0,
        winding_iso_value: float = 0.000000,
        rays_per_sample: int = 0,
        normal_offset: float = 0.000000,
        compact_result: bool = False) -> None
```

<a id="unreal.GeometryScriptRemoveHiddenTrianglesOptions.method"></a>

#### method

```python
@property
def method() -> GeometryScriptRemoveHiddenTrianglesMethod
```

(GeometryScriptRemoveHiddenTrianglesMethod):  [Read-Write]

<a id="unreal.GeometryScriptRemoveHiddenTrianglesOptions.method"></a>

#### method

```python
@method.setter
def method(value: GeometryScriptRemoveHiddenTrianglesMethod) -> None
```

<a id="unreal.GeometryScriptRemoveHiddenTrianglesOptions.samples_per_triangle"></a>

#### samples_per_triangle

```python
@property
def samples_per_triangle() -> int
```

(int32):  [Read-Write] add triangle samples per triangle (in addition to TriangleSamplingMethod)

<a id="unreal.GeometryScriptRemoveHiddenTrianglesOptions.samples_per_triangle"></a>

#### samples_per_triangle

```python
@samples_per_triangle.setter
def samples_per_triangle(value: int) -> None
```

<a id="unreal.GeometryScriptRemoveHiddenTrianglesOptions.shrink_selection"></a>

#### shrink_selection

```python
@property
def shrink_selection() -> int
```

(int32):  [Read-Write] once triangles to remove are identified, do iterations of boundary erosion, ie contract selection by boundary vertex one-rings

<a id="unreal.GeometryScriptRemoveHiddenTrianglesOptions.shrink_selection"></a>

#### shrink_selection

```python
@shrink_selection.setter
def shrink_selection(value: int) -> None
```

<a id="unreal.GeometryScriptRemoveHiddenTrianglesOptions.winding_iso_value"></a>

#### winding_iso_value

```python
@property
def winding_iso_value() -> float
```

(float):  [Read-Write] use this as winding isovalue for WindingNumber mode

<a id="unreal.GeometryScriptRemoveHiddenTrianglesOptions.winding_iso_value"></a>

#### winding_iso_value

```python
@winding_iso_value.setter
def winding_iso_value(value: float) -> None
```

<a id="unreal.GeometryScriptRemoveHiddenTrianglesOptions.rays_per_sample"></a>

#### rays_per_sample

```python
@property
def rays_per_sample() -> int
```

(int32):  [Read-Write] random rays to add beyond +/- major axes, for raycast sampling

<a id="unreal.GeometryScriptRemoveHiddenTrianglesOptions.rays_per_sample"></a>

#### rays_per_sample

```python
@rays_per_sample.setter
def rays_per_sample(value: int) -> None
```

<a id="unreal.GeometryScriptRemoveHiddenTrianglesOptions.normal_offset"></a>

#### normal_offset

```python
@property
def normal_offset() -> float
```

(float):  [Read-Write] Nudge sample points out by this amount to try to counteract numerical issues

<a id="unreal.GeometryScriptRemoveHiddenTrianglesOptions.normal_offset"></a>

#### normal_offset

```python
@normal_offset.setter
def normal_offset(value: float) -> None
```

<a id="unreal.GeometryScriptRemoveHiddenTrianglesOptions.compact_result"></a>

#### compact_result

```python
@property
def compact_result() -> bool
```

(bool):  [Read-Write]

<a id="unreal.GeometryScriptRemoveHiddenTrianglesOptions.compact_result"></a>

#### compact_result

```python
@compact_result.setter
def compact_result(value: bool) -> None
```

<a id="unreal.GeometryScriptDegenerateTriangleOptions"></a>