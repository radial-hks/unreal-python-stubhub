## GeometryScriptNaniteOptions Objects

```python
class GeometryScriptNaniteOptions(StructBase)
```

Configuration settings for Nanite Rendering on StaticMesh Assets

**C++ Source:**

- **Plugin**: GeometryScripting
- **Module**: GeometryScriptingCore
- **File**: MeshAssetFunctions.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``enabled`` (bool):  [Read-Write] Set Nanite to Enabled/Disabled
- ``fallback_percent_triangles`` (float):  [Read-Write] Percentage of triangles to maintain in Fallback Mesh used when Nanite is unavailable
- ``fallback_relative_error`` (float):  [Read-Write] Relative Error to maintain in Fallback Mesh used when Nanite is unavailable. Overrides FallbackPercentTriangles. Set to 0 to only use FallbackPercentTriangles (default).

<a id="unreal.GeometryScriptNaniteOptions.__init__"></a>

#### __init__

```python
def __init__(enabled: bool = False,
             fallback_percent_triangles: float = 0.000000,
             fallback_relative_error: float = 0.000000) -> None
```

<a id="unreal.GeometryScriptNaniteOptions.enabled"></a>

#### enabled

```python
@property
def enabled() -> bool
```

(bool):  [Read-Write] Set Nanite to Enabled/Disabled

<a id="unreal.GeometryScriptNaniteOptions.enabled"></a>

#### enabled

```python
@enabled.setter
def enabled(value: bool) -> None
```

<a id="unreal.GeometryScriptNaniteOptions.fallback_percent_triangles"></a>

#### fallback_percent_triangles

```python
@property
def fallback_percent_triangles() -> float
```

(float):  [Read-Write] Percentage of triangles to maintain in Fallback Mesh used when Nanite is unavailable

<a id="unreal.GeometryScriptNaniteOptions.fallback_percent_triangles"></a>

#### fallback_percent_triangles

```python
@fallback_percent_triangles.setter
def fallback_percent_triangles(value: float) -> None
```

<a id="unreal.GeometryScriptNaniteOptions.fallback_relative_error"></a>

#### fallback_relative_error

```python
@property
def fallback_relative_error() -> float
```

(float):  [Read-Write] Relative Error to maintain in Fallback Mesh used when Nanite is unavailable. Overrides FallbackPercentTriangles. Set to 0 to only use FallbackPercentTriangles (default).

<a id="unreal.GeometryScriptNaniteOptions.fallback_relative_error"></a>

#### fallback_relative_error

```python
@fallback_relative_error.setter
def fallback_relative_error(value: float) -> None
```

<a id="unreal.GeometryScriptCopyMeshToAssetOptions"></a>