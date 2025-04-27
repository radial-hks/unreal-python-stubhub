## GeometryScriptCopyBonesFromMeshOptions Objects

```python
class GeometryScriptCopyBonesFromMeshOptions(StructBase)
```

Geometry Script Copy Bones from Mesh Options

**C++ Source:**

- **Plugin**: GeometryScripting
- **Module**: GeometryScriptingCore
- **File**: MeshBoneWeightFunctions.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``bones_to_copy_from_source`` (BonesToCopyFromSource):  [Read-Write] Specify which bones are copied from the source mesh to the target.
- ``reindex_weights`` (bool):  [Read-Write] If the target Dynamic mesh has bone weights and a skeleton, re-index (re-bind) target weight indices from the
  target skeleton to the source skeleton.

<a id="unreal.GeometryScriptCopyBonesFromMeshOptions.__init__"></a>

#### __init__

```python
def __init__(
    reindex_weights: bool = False,
    bones_to_copy_from_source: BonesToCopyFromSource = BonesToCopyFromSource.
    ALL_BONES
) -> None
```

<a id="unreal.GeometryScriptCopyBonesFromMeshOptions.reindex_weights"></a>

#### reindex_weights

```python
@property
def reindex_weights() -> bool
```

(bool):  [Read-Write] If the target Dynamic mesh has bone weights and a skeleton, re-index (re-bind) target weight indices from the
target skeleton to the source skeleton.

<a id="unreal.GeometryScriptCopyBonesFromMeshOptions.reindex_weights"></a>

#### reindex_weights

```python
@reindex_weights.setter
def reindex_weights(value: bool) -> None
```

<a id="unreal.GeometryScriptCopyBonesFromMeshOptions.bones_to_copy_from_source"></a>

#### bones_to_copy_from_source

```python
@property
def bones_to_copy_from_source() -> BonesToCopyFromSource
```

(BonesToCopyFromSource):  [Read-Write] Specify which bones are copied from the source mesh to the target.

<a id="unreal.GeometryScriptCopyBonesFromMeshOptions.bones_to_copy_from_source"></a>

#### bones_to_copy_from_source

```python
@bones_to_copy_from_source.setter
def bones_to_copy_from_source(value: BonesToCopyFromSource) -> None
```

<a id="unreal.GeometryScriptMeshBooleanOptions"></a>