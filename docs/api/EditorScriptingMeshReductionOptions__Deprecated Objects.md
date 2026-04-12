## EditorScriptingMeshReductionOptions\_Deprecated Objects

```python
class EditorScriptingMeshReductionOptions_Deprecated(StructBase)
```

Deprecated as of 5.0, use the struct FStaticMeshReductionOptions in Static Mesh Editor Library Instead

**C++ Source:**

- **Plugin**: EditorScriptingUtilities
- **Module**: EditorScriptingUtilities
- **File**: EditorStaticMeshLibrary.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``auto_compute_lod_screen_size`` (bool):  [Read-Write] If true, the screen sizes at which LODs swap are computed automatically
  note: that this is displayed as 'Auto Compute LOD Distances' in the UI
- ``reduction_settings`` (Array[EditorScriptingMeshReductionSettings_Deprecated]):  [Read-Write] Array of reduction settings to apply to each new LOD mesh.

<a id="unreal.EditorScriptingMeshReductionOptions_Deprecated.__init__"></a>

#### \_\_init\_\_

```python
def __init__(
    auto_compute_lod_screen_size: bool = False,
    reduction_settings: Array[
        EditorScriptingMeshReductionSettings_Deprecated] = []
) -> None
```

<a id="unreal.EditorScriptingMeshReductionOptions_Deprecated.auto_compute_lod_screen_size"></a>

#### auto\_compute\_lod\_screen\_size

```python
@property
def auto_compute_lod_screen_size() -> bool
```

(bool):  [Read-Write] If true, the screen sizes at which LODs swap are computed automatically
note: that this is displayed as 'Auto Compute LOD Distances' in the UI

<a id="unreal.EditorScriptingMeshReductionOptions_Deprecated.auto_compute_lod_screen_size"></a>

#### auto\_compute\_lod\_screen\_size

```python
@auto_compute_lod_screen_size.setter
def auto_compute_lod_screen_size(value: bool) -> None
```

<a id="unreal.EditorScriptingMeshReductionOptions_Deprecated.reduction_settings"></a>

#### reduction\_settings

```python
@property
def reduction_settings(
) -> Array[EditorScriptingMeshReductionSettings_Deprecated]
```

(Array[EditorScriptingMeshReductionSettings_Deprecated]):  [Read-Write] Array of reduction settings to apply to each new LOD mesh.

<a id="unreal.EditorScriptingMeshReductionOptions_Deprecated.reduction_settings"></a>

#### reduction\_settings

```python
@reduction_settings.setter
def reduction_settings(
        value: Array[EditorScriptingMeshReductionSettings_Deprecated]) -> None
```

<a id="unreal.AbcCompressionSettings"></a>