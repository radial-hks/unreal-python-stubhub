## InterchangeMeshUtilities Objects

```python
class InterchangeMeshUtilities(Object)
```

Interchange Mesh Utilities

**C++ Source:**

- **Module**: InterchangeEngine
- **File**: InterchangeMeshUtilities.h

<a id="unreal.InterchangeMeshUtilities.scripted_import_morph_target"></a>

#### scripted_import_morph_target

```python
def scripted_import_morph_target(skeletal_mesh: SkeletalMesh, lod_index: int,
                                 source_data: InterchangeSourceData,
                                 morph_target_name: str) -> bool
```

x.scripted_import_morph_target(skeletal_mesh, lod_index, source_data, morph_target_name) -> bool
This function import a morph target from the source data and add/replace the skeletal mesh morph target.

Args:
    skeletal_mesh (SkeletalMesh): The target skeletal mesh we want to add the morph targets
    lod_index (int32): The index of the LOD we want to replace or add the morph targets
    source_data (InterchangeSourceData): The source to import the morph targets
    morph_target_name (str): If not empty we will use this name to create the morph target, if there is already an existing morph target it will be re-import

Returns:
    bool: return true if it successfully add or replace the skeletal mesh morph target at LodIndex, flase otherwise.

<a id="unreal.AssetTools"></a>