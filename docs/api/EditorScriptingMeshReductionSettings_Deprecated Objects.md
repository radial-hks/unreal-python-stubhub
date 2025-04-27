## EditorScriptingMeshReductionSettings_Deprecated Objects

```python
class EditorScriptingMeshReductionSettings_Deprecated(StructBase)
```

Deprecated as of 5.0, use the struct FStaticMeshReductionSettings in Static Mesh Editor Library Instead

**C++ Source:**

- **Plugin**: EditorScriptingUtilities
- **Module**: EditorScriptingUtilities
- **File**: EditorStaticMeshLibrary.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``percent_triangles`` (float):  [Read-Write] Percentage of triangles to keep. Ranges from 0.0 to 1.0: 1.0 = no reduction, 0.0 = no triangles.
- ``screen_size`` (float):  [Read-Write] ScreenSize to display this LOD. Ranges from 0.0 to 1.0.

<a id="unreal.EditorScriptingMeshReductionSettings_Deprecated.__init__"></a>

#### __init__

```python
def __init__(percent_triangles: float = 0.000000,
             screen_size: float = 0.000000) -> None
```

<a id="unreal.EditorScriptingMeshReductionSettings_Deprecated.percent_triangles"></a>

#### percent_triangles

```python
@property
def percent_triangles() -> float
```

(float):  [Read-Write] Percentage of triangles to keep. Ranges from 0.0 to 1.0: 1.0 = no reduction, 0.0 = no triangles.

<a id="unreal.EditorScriptingMeshReductionSettings_Deprecated.percent_triangles"></a>

#### percent_triangles

```python
@percent_triangles.setter
def percent_triangles(value: float) -> None
```

<a id="unreal.EditorScriptingMeshReductionSettings_Deprecated.screen_size"></a>

#### screen_size

```python
@property
def screen_size() -> float
```

(float):  [Read-Write] ScreenSize to display this LOD. Ranges from 0.0 to 1.0.

<a id="unreal.EditorScriptingMeshReductionSettings_Deprecated.screen_size"></a>

#### screen_size

```python
@screen_size.setter
def screen_size(value: float) -> None
```

<a id="unreal.EditorScriptingMeshReductionOptions_Deprecated"></a>