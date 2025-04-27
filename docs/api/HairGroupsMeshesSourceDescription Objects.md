## HairGroupsMeshesSourceDescription Objects

```python
class HairGroupsMeshesSourceDescription(StructBase)
```

Hair Groups Meshes Source Description

**C++ Source:**

- **Plugin**: HairStrands
- **Module**: HairStrandsCore
- **File**: GroomAssetMeshes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``group_index`` (int32):  [Read-Write] Group index on which this mesh geometry will be used (#hair_todo: change this to be a dropdown selection menu in FHairLODSettings instead)
- ``imported_mesh`` (StaticMesh):  [Read-Write] Mesh settings
- ``lod_index`` (int32):  [Read-Write] LOD on which this mesh geometry will be used. -1 means not used  (#hair_todo: change this to be a dropdown selection menu in FHairLODSettings instead)
- ``textures`` (HairGroupCardsTextures):  [Read-Write]

<a id="unreal.HairGroupsMeshesSourceDescription.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.HairSolverSettings"></a>