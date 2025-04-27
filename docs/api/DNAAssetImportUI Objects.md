## DNAAssetImportUI Objects

```python
class DNAAssetImportUI(Object)
```

DNAAsset Import UI

**C++ Source:**

- **Plugin**: RigLogic
- **Module**: RigLogicEditor
- **File**: DNAAssetImportUI.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``file_name`` (str):  [Read-Only] The DNA file name
- ``skeletal_mesh`` (SkeletalMesh):  [Read-Write] Skeletal mesh to use for imported DNA asset. When importing DNA, leaving this as "None" will generate new skeletal mesh.

<a id="unreal.DNAAssetImportUI.skeletal_mesh"></a>

#### skeletal_mesh

```python
@property
def skeletal_mesh() -> SkeletalMesh
```

(SkeletalMesh):  [Read-Write] Skeletal mesh to use for imported DNA asset. When importing DNA, leaving this as "None" will generate new skeletal mesh.

<a id="unreal.DNAAssetImportUI.skeletal_mesh"></a>

#### skeletal_mesh

```python
@skeletal_mesh.setter
def skeletal_mesh(value: SkeletalMesh) -> None
```

<a id="unreal.DNAAssetImportUI.reset_to_default"></a>

#### reset_to_default

```python
def reset_to_default() -> None
```

x.reset_to_default() -> None
Reset to Default

<a id="unreal.DNAAssetImportFactory"></a>