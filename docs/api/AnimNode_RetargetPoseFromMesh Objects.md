## AnimNode_RetargetPoseFromMesh Objects

```python
class AnimNode_RetargetPoseFromMesh(AnimNode_Base)
```

Anim Node Retarget Pose from Mesh

**C++ Source:**

- **Plugin**: IKRig
- **Module**: IKRig
- **File**: AnimNode_RetargetPoseFromMesh.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``copy_curves`` (bool):  [Read-Write] Copy curves from SouceMeshComponent. This will copy any curves the source/target Skeleton have in common.
- ``custom_retarget_profile`` (RetargetProfile):  [Read-Write] connect a custom retarget profile to modify the retargeter's settings at runtime.
- ``ik_retargeter_asset`` (IKRetargeter):  [Read-Write] Retarget asset to use. Must define a Source and Target IK Rig compatible with the SourceMeshComponent and current anim instance.
- ``lod_threshold`` (int32):  [Read-Write] * Max LOD that this node is allowed to run.
  * For example if you have LODThreshold at 2, it will run until LOD 2 (based on 0 index) when the component LOD becomes 3, it will stop update/evaluate
  * A value of -1 forces the node to execute at all LOD levels.
- ``lod_threshold_for_ik`` (int32):  [Read-Write] * Max LOD that IK is allowed to run.
  * For example if you have LODThresholdForIK at 2, it will skip the IK pass on LODs 3 and greater.
  * This only disables IK and does not affect the Root or FK passes.
  * A value of -1 forces the node to execute at all LOD levels.
- ``source_mesh_component`` (SkeletalMeshComponent):  [Read-Write] The Skeletal Mesh Component to retarget animation from. Assumed to be animated and tick BEFORE this anim instance.
- ``suppress_warnings`` (bool):  [Read-Write] Toggle whether to print warnings about missing or incorrectly configured retarget configurations.
- ``use_attached_parent`` (bool):  [Read-Write] If SourceMeshComponent is not valid, and if this is true, it will look for attached parent as a source

<a id="unreal.AnimNode_RetargetPoseFromMesh.__init__"></a>

#### __init__

```python
def __init__(source_mesh_component: SkeletalMeshComponent = None,
             use_attached_parent: bool = False,
             ik_retargeter_asset: IKRetargeter = None,
             custom_retarget_profile: RetargetProfile = [
                 False, "None", False, "None", False, {}, False,
                 [
                     1.000000, 1.000000, 0.000000,
                     [1.000000, 1.000000, 1.000000], 1.000000, 1.000000,
                     [0.000000, 0.000000, 0.000000],
                     [0.000000, 0.000000, 0.000000], 1.000000, 0.000000
                 ], False,
                 [
                     True, True, True, True, False,
                     WarpingDirectionSource.GOALS, BasicAxis.Y, "None",
                     1.000000, 0.000000, 1.000000
                 ]
             ],
             suppress_warnings: bool = False,
             copy_curves: bool = False,
             lod_threshold: int = 0,
             lod_threshold_for_ik: int = 0) -> None
```

<a id="unreal.AnimNode_RetargetPoseFromMesh.source_mesh_component"></a>

#### source_mesh_component

```python
@property
def source_mesh_component() -> SkeletalMeshComponent
```

(SkeletalMeshComponent):  [Read-Write] The Skeletal Mesh Component to retarget animation from. Assumed to be animated and tick BEFORE this anim instance.

<a id="unreal.AnimNode_RetargetPoseFromMesh.source_mesh_component"></a>

#### source_mesh_component

```python
@source_mesh_component.setter
def source_mesh_component(value: SkeletalMeshComponent) -> None
```

<a id="unreal.AnimNode_RetargetPoseFromMesh.use_attached_parent"></a>

#### use_attached_parent

```python
@property
def use_attached_parent() -> bool
```

(bool):  [Read-Write] If SourceMeshComponent is not valid, and if this is true, it will look for attached parent as a source

<a id="unreal.AnimNode_RetargetPoseFromMesh.use_attached_parent"></a>

#### use_attached_parent

```python
@use_attached_parent.setter
def use_attached_parent(value: bool) -> None
```

<a id="unreal.AnimNode_RetargetPoseFromMesh.ik_retargeter_asset"></a>

#### ik_retargeter_asset

```python
@property
def ik_retargeter_asset() -> IKRetargeter
```

(IKRetargeter):  [Read-Write] Retarget asset to use. Must define a Source and Target IK Rig compatible with the SourceMeshComponent and current anim instance.

<a id="unreal.AnimNode_RetargetPoseFromMesh.ik_retargeter_asset"></a>

#### ik_retargeter_asset

```python
@ik_retargeter_asset.setter
def ik_retargeter_asset(value: IKRetargeter) -> None
```

<a id="unreal.AnimNode_RetargetPoseFromMesh.custom_retarget_profile"></a>

#### custom_retarget_profile

```python
@property
def custom_retarget_profile() -> RetargetProfile
```

(RetargetProfile):  [Read-Write] connect a custom retarget profile to modify the retargeter's settings at runtime.

<a id="unreal.AnimNode_RetargetPoseFromMesh.custom_retarget_profile"></a>

#### custom_retarget_profile

```python
@custom_retarget_profile.setter
def custom_retarget_profile(value: RetargetProfile) -> None
```

<a id="unreal.AnimNode_RetargetPoseFromMesh.suppress_warnings"></a>

#### suppress_warnings

```python
@property
def suppress_warnings() -> bool
```

(bool):  [Read-Write] Toggle whether to print warnings about missing or incorrectly configured retarget configurations.

<a id="unreal.AnimNode_RetargetPoseFromMesh.suppress_warnings"></a>

#### suppress_warnings

```python
@suppress_warnings.setter
def suppress_warnings(value: bool) -> None
```

<a id="unreal.AnimNode_RetargetPoseFromMesh.copy_curves"></a>

#### copy_curves

```python
@property
def copy_curves() -> bool
```

(bool):  [Read-Write] Copy curves from SouceMeshComponent. This will copy any curves the source/target Skeleton have in common.

<a id="unreal.AnimNode_RetargetPoseFromMesh.copy_curves"></a>

#### copy_curves

```python
@copy_curves.setter
def copy_curves(value: bool) -> None
```

<a id="unreal.AnimNode_RetargetPoseFromMesh.lod_threshold"></a>

#### lod_threshold

```python
@property
def lod_threshold() -> int
```

(int32):  [Read-Write] * Max LOD that this node is allowed to run.
* For example if you have LODThreshold at 2, it will run until LOD 2 (based on 0 index) when the component LOD becomes 3, it will stop update/evaluate
* A value of -1 forces the node to execute at all LOD levels.

<a id="unreal.AnimNode_RetargetPoseFromMesh.lod_threshold"></a>

#### lod_threshold

```python
@lod_threshold.setter
def lod_threshold(value: int) -> None
```

<a id="unreal.AnimNode_RetargetPoseFromMesh.lod_threshold_for_ik"></a>

#### lod_threshold_for_ik

```python
@property
def lod_threshold_for_ik() -> int
```

(int32):  [Read-Write] * Max LOD that IK is allowed to run.
* For example if you have LODThresholdForIK at 2, it will skip the IK pass on LODs 3 and greater.
* This only disables IK and does not affect the Root or FK passes.
* A value of -1 forces the node to execute at all LOD levels.

<a id="unreal.AnimNode_RetargetPoseFromMesh.lod_threshold_for_ik"></a>

#### lod_threshold_for_ik

```python
@lod_threshold_for_ik.setter
def lod_threshold_for_ik(value: int) -> None
```

<a id="unreal.IKRetargetPose"></a>