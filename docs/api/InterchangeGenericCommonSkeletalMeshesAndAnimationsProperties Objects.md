## InterchangeGenericCommonSkeletalMeshesAndAnimationsProperties Objects

```python
class InterchangeGenericCommonSkeletalMeshesAndAnimationsProperties(
        InterchangePipelineBase)
```

Interchange Generic Common Skeletal Meshes and Animations Properties

**C++ Source:**

- **Plugin**: Interchange
- **Module**: InterchangePipelines
- **File**: InterchangeGenericAssetsPipelineSharedSettings.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``convert_statics_with_morph_targets_to_skeletals`` (bool):  [Read-Write] If enabled, all static meshes that have morph targets will be imported as skeletal meshes instead.
- ``import_meshes_in_bone_hierarchy`` (bool):  [Read-Write] If enabled, meshes nested in bone hierarchies will be imported as meshes instead of being converted to bones. If the meshes are not skinned, they are
  added to the skeletal mesh and removed from the list of static meshes.
- ``import_only_animations`` (bool):  [Read-Write] If enabled, only animations are imported from the source. You must also set a valid skeleton.
- ``skeleton`` (Skeleton):  [Read-Write] Skeleton to use for imported asset. When importing a skeletal mesh, leaving this as "None" will create a new skeleton. When importing an animation, this must be specified.
- ``use_t0_as_ref_pose`` (bool):  [Read-Write] If enabled, frame 0 is used as the reference pose for skeletal meshes.

<a id="unreal.InterchangeGenericCommonSkeletalMeshesAndAnimationsProperties.import_only_animations"></a>

#### import_only_animations

```python
@property
def import_only_animations() -> bool
```

(bool):  [Read-Write] If enabled, only animations are imported from the source. You must also set a valid skeleton.

<a id="unreal.InterchangeGenericCommonSkeletalMeshesAndAnimationsProperties.import_only_animations"></a>

#### import_only_animations

```python
@import_only_animations.setter
def import_only_animations(value: bool) -> None
```

<a id="unreal.InterchangeGenericCommonSkeletalMeshesAndAnimationsProperties.skeleton"></a>

#### skeleton

```python
@property
def skeleton() -> Skeleton
```

(Skeleton):  [Read-Write] Skeleton to use for imported asset. When importing a skeletal mesh, leaving this as "None" will create a new skeleton. When importing an animation, this must be specified.

<a id="unreal.InterchangeGenericCommonSkeletalMeshesAndAnimationsProperties.skeleton"></a>

#### skeleton

```python
@skeleton.setter
def skeleton(value: Skeleton) -> None
```

<a id="unreal.InterchangeGenericCommonSkeletalMeshesAndAnimationsProperties.import_meshes_in_bone_hierarchy"></a>

#### import_meshes_in_bone_hierarchy

```python
@property
def import_meshes_in_bone_hierarchy() -> bool
```

(bool):  [Read-Write] If enabled, meshes nested in bone hierarchies will be imported as meshes instead of being converted to bones. If the meshes are not skinned, they are
added to the skeletal mesh and removed from the list of static meshes.

<a id="unreal.InterchangeGenericCommonSkeletalMeshesAndAnimationsProperties.import_meshes_in_bone_hierarchy"></a>

#### import_meshes_in_bone_hierarchy

```python
@import_meshes_in_bone_hierarchy.setter
def import_meshes_in_bone_hierarchy(value: bool) -> None
```

<a id="unreal.InterchangeGenericCommonSkeletalMeshesAndAnimationsProperties.use_t0_as_ref_pose"></a>

#### use_t0_as_ref_pose

```python
@property
def use_t0_as_ref_pose() -> bool
```

(bool):  [Read-Write] If enabled, frame 0 is used as the reference pose for skeletal meshes.

<a id="unreal.InterchangeGenericCommonSkeletalMeshesAndAnimationsProperties.use_t0_as_ref_pose"></a>

#### use_t0_as_ref_pose

```python
@use_t0_as_ref_pose.setter
def use_t0_as_ref_pose(value: bool) -> None
```

<a id="unreal.InterchangeGenericCommonSkeletalMeshesAndAnimationsProperties.convert_statics_with_morph_targets_to_skeletals"></a>

#### convert_statics_with_morph_targets_to_skeletals

```python
@property
def convert_statics_with_morph_targets_to_skeletals() -> bool
```

(bool):  [Read-Write] If enabled, all static meshes that have morph targets will be imported as skeletal meshes instead.

<a id="unreal.InterchangeGenericCommonSkeletalMeshesAndAnimationsProperties.convert_statics_with_morph_targets_to_skeletals"></a>

#### convert_statics_with_morph_targets_to_skeletals

```python
@convert_statics_with_morph_targets_to_skeletals.setter
def convert_statics_with_morph_targets_to_skeletals(value: bool) -> None
```

<a id="unreal.InterchangeGLTFPipeline"></a>