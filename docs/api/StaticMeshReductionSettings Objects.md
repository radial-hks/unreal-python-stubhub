## StaticMeshReductionSettings Objects

```python
class StaticMeshReductionSettings(StructBase)
```

Static Mesh Reduction Settings

**C++ Source:**

- **Module**: StaticMeshEditor
- **File**: StaticMeshEditorSubsystemHelpers.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``percent_triangles`` (float):  [Read-Write] Percentage of triangles to keep. Ranges from 0.0 to 1.0: 1.0 = no reduction, 0.0 = no triangles.
- ``screen_size`` (float):  [Read-Write] ScreenSize to display this LOD. Ranges from 0.0 to 1.0.

<a id="unreal.StaticMeshReductionSettings.__init__"></a>

#### __init__

```python
def __init__(percent_triangles: float = 0.000000,
             screen_size: float = 0.000000) -> None
```

<a id="unreal.StaticMeshReductionSettings.percent_triangles"></a>

#### percent_triangles

```python
@property
def percent_triangles() -> float
```

(float):  [Read-Write] Percentage of triangles to keep. Ranges from 0.0 to 1.0: 1.0 = no reduction, 0.0 = no triangles.

<a id="unreal.StaticMeshReductionSettings.percent_triangles"></a>

#### percent_triangles

```python
@percent_triangles.setter
def percent_triangles(value: float) -> None
```

<a id="unreal.StaticMeshReductionSettings.screen_size"></a>

#### screen_size

```python
@property
def screen_size() -> float
```

(float):  [Read-Write] ScreenSize to display this LOD. Ranges from 0.0 to 1.0.

<a id="unreal.StaticMeshReductionSettings.screen_size"></a>

#### screen_size

```python
@screen_size.setter
def screen_size(value: float) -> None
```

<a id="unreal.EditorScriptingMeshReductionSettings"></a>