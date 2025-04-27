## GeometryScriptDetermineMeshOcclusionOptions Objects

```python
class GeometryScriptDetermineMeshOcclusionOptions(StructBase)
```

Geometry Script Determine Mesh Occlusion Options

**C++ Source:**

- **Plugin**: GeometryScripting
- **Module**: GeometryScriptingCore
- **File**: SceneUtilityFunctions.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``double_sided`` (bool):  [Read-Write] Whether to treat faces as double-sided when determining visibility
- ``num_search_directions`` (int32):  [Read-Write] Number of directions to test for visibility
- ``sampling_density`` (double):  [Read-Write] Approximate spacing between samples on triangle faces used for determining visibility

<a id="unreal.GeometryScriptDetermineMeshOcclusionOptions.__init__"></a>

#### __init__

```python
def __init__(sampling_density: float = 0.000000,
             double_sided: bool = False,
             num_search_directions: int = 0) -> None
```

<a id="unreal.GeometryScriptDetermineMeshOcclusionOptions.sampling_density"></a>

#### sampling_density

```python
@property
def sampling_density() -> float
```

(double):  [Read-Write] Approximate spacing between samples on triangle faces used for determining visibility

<a id="unreal.GeometryScriptDetermineMeshOcclusionOptions.sampling_density"></a>

#### sampling_density

```python
@sampling_density.setter
def sampling_density(value: float) -> None
```

<a id="unreal.GeometryScriptDetermineMeshOcclusionOptions.double_sided"></a>

#### double_sided

```python
@property
def double_sided() -> bool
```

(bool):  [Read-Write] Whether to treat faces as double-sided when determining visibility

<a id="unreal.GeometryScriptDetermineMeshOcclusionOptions.double_sided"></a>

#### double_sided

```python
@double_sided.setter
def double_sided(value: bool) -> None
```

<a id="unreal.GeometryScriptDetermineMeshOcclusionOptions.num_search_directions"></a>

#### num_search_directions

```python
@property
def num_search_directions() -> int
```

(int32):  [Read-Write] Number of directions to test for visibility

<a id="unreal.GeometryScriptDetermineMeshOcclusionOptions.num_search_directions"></a>

#### num_search_directions

```python
@num_search_directions.setter
def num_search_directions(value: int) -> None
```

<a id="unreal.GeometryScriptSampleTextureOptions"></a>