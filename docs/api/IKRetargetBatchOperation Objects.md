## IKRetargetBatchOperation Objects

```python
class IKRetargetBatchOperation(Object)
```

Encapsulate ability to batch duplicate and retarget a set of animation assets

**C++ Source:**

- **Plugin**: IKRig
- **Module**: IKRigEditor
- **File**: IKRetargetBatchOperation.h

<a id="unreal.IKRetargetBatchOperation.duplicate_and_retarget"></a>

#### duplicate_and_retarget

```python
@classmethod
def duplicate_and_retarget(
        cls,
        assets_to_retarget: Array[AssetData],
        source_mesh: SkeletalMesh,
        target_mesh: SkeletalMesh,
        ik_retarget_asset: IKRetargeter,
        search: str = "",
        replace: str = "",
        prefix: str = "",
        suffix: str = "",
        include_referenced_assets: bool = True) -> Array[AssetData]
```

X.duplicate_and_retarget(assets_to_retarget, source_mesh, target_mesh, ik_retarget_asset, search="", replace="", prefix="", suffix="", include_referenced_assets=True) -> Array[AssetData]
Convenience function to run a batch animation retarget from Blueprint / Python. This function will duplicate a list of
       * assets and use the supplied IK Retargeter to retarget the animation from the source to the target using the
       * settings in the provided IK Retargeter asset.
       *
       *

Args:
    assets_to_retarget (Array[AssetData]): A list of animation assets to retarget (sequences, blendspaces or montages) *
    source_mesh (SkeletalMesh): The skeletal mesh with desired proportions to playback the assets to retarget *
    target_mesh (SkeletalMesh): The skeletal mesh to retarget the animation onto. *
    ik_retarget_asset (IKRetargeter): The IK Retargeter asset with IK Rigs appropriate for the source and target skeletal mesh *
    search (str): A string to search for in the file name (replaced with "Replace" string) *
    replace (str): A string to replace with in the file name *
    prefix (str): A string to add to the start of the new file name *
    suffix (str): A string to add at the end of the new file name *
    include_referenced_assets (bool): 

Returns:
    Array[AssetData]:

<a id="unreal.BatchExportOptions"></a>