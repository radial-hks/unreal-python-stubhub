## GenerateStaticMeshLODProcess_PreprocessSettings Objects

```python
class GenerateStaticMeshLODProcess_PreprocessSettings(StructBase)
```

Generate Static Mesh LODProcess Preprocess Settings

**C++ Source:**

- **Plugin**: MeshLODToolset
- **Module**: MeshLODToolset
- **File**: GenerateStaticMeshLODProcess.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``filter_group_layer`` (Name):  [Read-Write] Group layer to use for filtering out detail before processing
- ``thicken_amount`` (float):  [Read-Write] Amount to thicken the mesh prior to Solidifying. The thicken weight map values are multiplied by this value.
  Thickening is primarily intended to repair shape erosion that can occur when using the Solidify Mesh Generators.
- ``thicken_weight_map_name`` (Name):  [Read-Write] Weight map used during mesh thickening

<a id="unreal.GenerateStaticMeshLODProcess_PreprocessSettings.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.GenerateStaticMeshLODProcessSettings"></a>