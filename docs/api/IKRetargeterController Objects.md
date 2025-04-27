## IKRetargeterController Objects

```python
class IKRetargeterController(Object)
```

A stateless singleton (1-per-asset) class used to make modifications to a UIKRetargeter asset.
Use UIKRetargeter.GetController() to get the controller for the asset you want to modify.

**C++ Source:**

- **Plugin**: IKRig
- **Module**: IKRigEditor
- **File**: IKRetargeterController.h

<a id="unreal.IKRetargeterController.snap_bone_to_ground"></a>

#### snap_bone_to_ground

```python
def snap_bone_to_ground(reference_bone: Name,
                        source_or_target: RetargetSourceOrTarget) -> None
```

x.snap_bone_to_ground(reference_bone, source_or_target) -> None
Moves the entire skeleton vertically until the specified bone is the same height off the ground as in the reference pose.

Args:
    reference_bone (Name): 
    source_or_target (RetargetSourceOrTarget):

<a id="unreal.IKRetargeterController.set_source_chain"></a>

#### set_source_chain

```python
def set_source_chain(source_chain_name: Name, target_chain_name: Name) -> bool
```

x.set_source_chain(source_chain_name, target_chain_name) -> bool
Assign a source chain to the given target chain. Animation will be copied from the source to the target.

Args:
    source_chain_name (Name): 
    target_chain_name (Name): 

Returns:
    bool:

<a id="unreal.IKRetargeterController.set_rotation_offset_for_retarget_pose_bone"></a>

#### set_rotation_offset_for_retarget_pose_bone

```python
def set_rotation_offset_for_retarget_pose_bone(
        bone_name: Name, rotation_offset: Quat,
        skeleton_mode: RetargetSourceOrTarget) -> None
```

x.set_rotation_offset_for_retarget_pose_bone(bone_name, rotation_offset, skeleton_mode) -> None
Set a delta rotation for a given bone for the current retarget pose

Args:
    bone_name (Name): 
    rotation_offset (Quat): 
    skeleton_mode (RetargetSourceOrTarget):

<a id="unreal.IKRetargeterController.set_root_settings"></a>

#### set_root_settings

```python
def set_root_settings(root_settings: TargetRootSettings) -> None
```

x.set_root_settings(root_settings) -> None
Set the retarget root settings for this asset.

Args:
    root_settings (TargetRootSettings):

<a id="unreal.IKRetargeterController.set_root_offset_in_retarget_pose"></a>

#### set_root_offset_in_retarget_pose

```python
def set_root_offset_in_retarget_pose(
        translation_offset: Vector,
        source_or_target: RetargetSourceOrTarget) -> None
```

x.set_root_offset_in_retarget_pose(translation_offset, source_or_target) -> None
Set the translation offset on the retarget root bone for the current retarget pose

Args:
    translation_offset (Vector): 
    source_or_target (RetargetSourceOrTarget):

<a id="unreal.IKRetargeterController.set_retarget_op_enabled"></a>

#### set_retarget_op_enabled

```python
def set_retarget_op_enabled(retarget_op_index: int, is_enabled: bool) -> bool
```

x.set_retarget_op_enabled(retarget_op_index, is_enabled) -> bool
Set enabled/disabled status of the given retarget operation.

Args:
    retarget_op_index (int32): 
    is_enabled (bool): 

Returns:
    bool:

<a id="unreal.IKRetargeterController.set_retarget_chain_settings"></a>

#### set_retarget_chain_settings

```python
def set_retarget_chain_settings(target_chain_name: Name,
                                settings: TargetChainSettings) -> bool
```

x.set_retarget_chain_settings(target_chain_name, settings) -> bool
Set the settings for the target chain by name. Returns true if the chain settings were applied, false otherwise.

Args:
    target_chain_name (Name): 
    settings (TargetChainSettings): 

Returns:
    bool:

<a id="unreal.IKRetargeterController.set_preview_mesh"></a>

#### set_preview_mesh

```python
def set_preview_mesh(source_or_target: RetargetSourceOrTarget,
                     preview_mesh: SkeletalMesh) -> None
```

x.set_preview_mesh(source_or_target, preview_mesh) -> None
Set the preview skeletal mesh for either source or target

Args:
    source_or_target (RetargetSourceOrTarget): 
    preview_mesh (SkeletalMesh):

<a id="unreal.IKRetargeterController.set_ik_rig"></a>

#### set_ik_rig

```python
def set_ik_rig(source_or_target: RetargetSourceOrTarget,
               ik_rig: IKRigDefinition) -> None
```

x.set_ik_rig(source_or_target, ik_rig) -> None
Set the IK Rig to use as the source or target (to copy animation FROM/TO)

Args:
    source_or_target (RetargetSourceOrTarget): 
    ik_rig (IKRigDefinition):

<a id="unreal.IKRetargeterController.set_global_settings"></a>

#### set_global_settings

```python
def set_global_settings(global_settings: RetargetGlobalSettings) -> None
```

x.set_global_settings(global_settings) -> None
Get a copy of the global settings for this asset.

Args:
    global_settings (RetargetGlobalSettings):

<a id="unreal.IKRetargeterController.set_current_retarget_pose"></a>

#### set_current_retarget_pose

```python
def set_current_retarget_pose(
        current_pose: Name, source_or_target: RetargetSourceOrTarget) -> bool
```

x.set_current_retarget_pose(current_pose, source_or_target) -> bool
Change which retarget pose is used by the retargeter at runtime

Args:
    current_pose (Name): 
    source_or_target (RetargetSourceOrTarget): 

Returns:
    bool:

<a id="unreal.IKRetargeterController.reset_retarget_pose"></a>

#### reset_retarget_pose

```python
def reset_retarget_pose(pose_to_reset: Name, bones_to_reset: Array[Name],
                        source_or_target: RetargetSourceOrTarget) -> None
```

x.reset_retarget_pose(pose_to_reset, bones_to_reset, source_or_target) -> None
Reset a retarget pose for the specified bones.
If BonesToReset is Empty, will removes all stored deltas, returning pose to reference pose

Args:
    pose_to_reset (Name): 
    bones_to_reset (Array[Name]): 
    source_or_target (RetargetSourceOrTarget):

<a id="unreal.IKRetargeterController.rename_retarget_pose"></a>

#### rename_retarget_pose

```python
def rename_retarget_pose(old_pose_name: Name, new_pose_name: Name,
                         source_or_target: RetargetSourceOrTarget) -> bool
```

x.rename_retarget_pose(old_pose_name, new_pose_name, source_or_target) -> bool
Rename current retarget pose. Returns true if a pose was renamed.

Args:
    old_pose_name (Name): 
    new_pose_name (Name): 
    source_or_target (RetargetSourceOrTarget): 

Returns:
    bool:

<a id="unreal.IKRetargeterController.remove_retarget_pose"></a>

#### remove_retarget_pose

```python
def remove_retarget_pose(pose_to_remove: Name,
                         source_or_target: RetargetSourceOrTarget) -> bool
```

x.remove_retarget_pose(pose_to_remove, source_or_target) -> bool
Remove a retarget pose. Returns true if the pose was found and removed.

Args:
    pose_to_remove (Name): 
    source_or_target (RetargetSourceOrTarget): 

Returns:
    bool:

<a id="unreal.IKRetargeterController.remove_retarget_op"></a>

#### remove_retarget_op

```python
def remove_retarget_op(op_index: int) -> bool
```

x.remove_retarget_op(op_index) -> bool
Remove the retarget op at the given stack index.

Args:
    op_index (int32): 

Returns:
    bool:

<a id="unreal.IKRetargeterController.remove_all_ops"></a>

#### remove_all_ops

```python
def remove_all_ops() -> bool
```

x.remove_all_ops() -> bool
Remove all ops in the stack.

Returns:
    bool:

<a id="unreal.IKRetargeterController.move_retarget_op_in_stack"></a>

#### move_retarget_op_in_stack

```python
def move_retarget_op_in_stack(op_to_move_index: int,
                              target_index: int) -> bool
```

x.move_retarget_op_in_stack(op_to_move_index, target_index) -> bool
Move the retarget op at the given index to the target index.

Args:
    op_to_move_index (int32): 
    target_index (int32): 

Returns:
    bool:

<a id="unreal.IKRetargeterController.get_source_chain"></a>

#### get_source_chain

```python
def get_source_chain(target_chain_name: Name) -> Name
```

x.get_source_chain(target_chain_name) -> Name
Get the name of the source chain mapped to a given target chain (the chain animation is copied FROM).

Args:
    target_chain_name (Name): 

Returns:
    Name:

<a id="unreal.IKRetargeterController.get_rotation_offset_for_retarget_pose_bone"></a>

#### get_rotation_offset_for_retarget_pose_bone

```python
def get_rotation_offset_for_retarget_pose_bone(
        bone_name: Name, source_or_target: RetargetSourceOrTarget) -> Quat
```

x.get_rotation_offset_for_retarget_pose_bone(bone_name, source_or_target) -> Quat
Get a delta rotation for a given bone for the current retarget pose

Args:
    bone_name (Name): 
    source_or_target (RetargetSourceOrTarget): 

Returns:
    Quat:

<a id="unreal.IKRetargeterController.get_root_settings"></a>

#### get_root_settings

```python
def get_root_settings() -> TargetRootSettings
```

x.get_root_settings() -> TargetRootSettings
Get a copy of the retarget root settings for this asset.

Returns:
    TargetRootSettings:

<a id="unreal.IKRetargeterController.get_root_offset_in_retarget_pose"></a>

#### get_root_offset_in_retarget_pose

```python
def get_root_offset_in_retarget_pose(
        source_or_target: RetargetSourceOrTarget) -> Vector
```

x.get_root_offset_in_retarget_pose(source_or_target) -> Vector
Get the translation offset on the retarget root bone for the current retarget pose

Args:
    source_or_target (RetargetSourceOrTarget): 

Returns:
    Vector:

<a id="unreal.IKRetargeterController.get_retarget_poses"></a>

#### get_retarget_poses

```python
def get_retarget_poses(
        source_or_target: RetargetSourceOrTarget) -> Map[Name, IKRetargetPose]
```

x.get_retarget_poses(source_or_target) -> Map[Name, IKRetargetPose]
Get access to array of retarget poses

Args:
    source_or_target (RetargetSourceOrTarget): 

Returns:
    Map[Name, IKRetargetPose]:

<a id="unreal.IKRetargeterController.get_retarget_op_enabled"></a>

#### get_retarget_op_enabled

```python
def get_retarget_op_enabled(retarget_op_index: int) -> bool
```

x.get_retarget_op_enabled(retarget_op_index) -> bool
Get enabled status of the given Op.

Args:
    retarget_op_index (int32): 

Returns:
    bool:

<a id="unreal.IKRetargeterController.get_retarget_op_at_index"></a>

#### get_retarget_op_at_index

```python
def get_retarget_op_at_index(index: int) -> RetargetOpBase
```

x.get_retarget_op_at_index(index) -> RetargetOpBase
Get access to the given retarget operation.

Args:
    index (int32): 

Returns:
    RetargetOpBase:

<a id="unreal.IKRetargeterController.get_retarget_chain_settings"></a>

#### get_retarget_chain_settings

```python
def get_retarget_chain_settings(
        target_chain_name: Name) -> TargetChainSettings
```

x.get_retarget_chain_settings(target_chain_name) -> TargetChainSettings
Get a copy of the settings for the target chain by name.

Args:
    target_chain_name (Name): 

Returns:
    TargetChainSettings:

<a id="unreal.IKRetargeterController.get_preview_mesh"></a>

#### get_preview_mesh

```python
def get_preview_mesh(source_or_target: RetargetSourceOrTarget) -> SkeletalMesh
```

x.get_preview_mesh(source_or_target) -> SkeletalMesh
Get the preview skeletal mesh

Args:
    source_or_target (RetargetSourceOrTarget): 

Returns:
    SkeletalMesh:

<a id="unreal.IKRetargeterController.get_num_retarget_ops"></a>

#### get_num_retarget_ops

```python
def get_num_retarget_ops() -> int
```

x.get_num_retarget_ops() -> int32
Get the number of Ops in the stack.

Returns:
    int32:

<a id="unreal.IKRetargeterController.get_index_of_retarget_op"></a>

#### get_index_of_retarget_op

```python
def get_index_of_retarget_op(retarget_op: RetargetOpBase) -> int
```

x.get_index_of_retarget_op(retarget_op) -> int32
Get access to the given retarget operation.

Args:
    retarget_op (RetargetOpBase): 

Returns:
    int32:

<a id="unreal.IKRetargeterController.get_ik_rig"></a>

#### get_ik_rig

```python
def get_ik_rig(source_or_target: RetargetSourceOrTarget) -> IKRigDefinition
```

x.get_ik_rig(source_or_target) -> IKRigDefinition
Get either source or target IK Rig

Args:
    source_or_target (RetargetSourceOrTarget): 

Returns:
    IKRigDefinition:

<a id="unreal.IKRetargeterController.get_global_settings"></a>

#### get_global_settings

```python
def get_global_settings() -> RetargetGlobalSettings
```

x.get_global_settings() -> RetargetGlobalSettings
Get a copy of the global settings for this asset.

Returns:
    RetargetGlobalSettings:

<a id="unreal.IKRetargeterController.get_current_retarget_pose_name"></a>

#### get_current_retarget_pose_name

```python
def get_current_retarget_pose_name(
        source_or_target: RetargetSourceOrTarget) -> Name
```

x.get_current_retarget_pose_name(source_or_target) -> Name
Get the current retarget pose

Args:
    source_or_target (RetargetSourceOrTarget): 

Returns:
    Name:

<a id="unreal.IKRetargeterController.get_current_retarget_pose"></a>

#### get_current_retarget_pose

```python
def get_current_retarget_pose(
        source_or_target: RetargetSourceOrTarget) -> IKRetargetPose
```

x.get_current_retarget_pose(source_or_target) -> IKRetargetPose
Get the current retarget pose

Args:
    source_or_target (RetargetSourceOrTarget): 

Returns:
    IKRetargetPose:

<a id="unreal.IKRetargeterController.get_controller"></a>

#### get_controller

```python
@classmethod
def get_controller(cls,
                   retargeter_asset: IKRetargeter) -> IKRetargeterController
```

X.get_controller(retargeter_asset) -> IKRetargeterController
Use this to get the controller for the given retargeter asset

Args:
    retargeter_asset (IKRetargeter): 

Returns:
    IKRetargeterController:

<a id="unreal.IKRetargeterController.get_all_chain_settings"></a>

#### get_all_chain_settings

```python
def get_all_chain_settings() -> Array[RetargetChainSettings]
```

x.get_all_chain_settings() -> Array[RetargetChainSettings]
Get read-only access to the list of settings for each target chain

Returns:
    Array[RetargetChainSettings]:

<a id="unreal.IKRetargeterController.duplicate_retarget_pose"></a>

#### duplicate_retarget_pose

```python
def duplicate_retarget_pose(pose_to_duplicate: Name, new_name: Name,
                            source_or_target: RetargetSourceOrTarget) -> Name
```

x.duplicate_retarget_pose(pose_to_duplicate, new_name, source_or_target) -> Name
Duplicate a retarget pose. Returns the name of the new, duplicate pose (or NAME_None if PoseToDuplicate is not found).

Args:
    pose_to_duplicate (Name): 
    new_name (Name): 
    source_or_target (RetargetSourceOrTarget): 

Returns:
    Name:

<a id="unreal.IKRetargeterController.create_retarget_pose"></a>

#### create_retarget_pose

```python
def create_retarget_pose(new_pose_name: Name,
                         source_or_target: RetargetSourceOrTarget) -> Name
```

x.create_retarget_pose(new_pose_name, source_or_target) -> Name
Add new retarget pose. Returns the name of the new retarget pose.

Args:
    new_pose_name (Name): 
    source_or_target (RetargetSourceOrTarget): 

Returns:
    Name:

<a id="unreal.IKRetargeterController.auto_map_chains"></a>

#### auto_map_chains

```python
def auto_map_chains(auto_map_type: AutoMapChainType,
                    force_remap: bool) -> None
```

x.auto_map_chains(auto_map_type, force_remap) -> None
Use fuzzy string search to find "best" Source chain to map to each Target chain

Args:
    auto_map_type (AutoMapChainType): 
    force_remap (bool):

<a id="unreal.IKRetargeterController.auto_align_bones"></a>

#### auto_align_bones

```python
def auto_align_bones(bones_to_align: Array[Name],
                     method: RetargetAutoAlignMethod,
                     source_or_target: RetargetSourceOrTarget) -> None
```

x.auto_align_bones(bones_to_align, method, source_or_target) -> None
Automatically align an array of bones and store in the current retarget pose. Bones not in a mapped chain will be ignored.

Args:
    bones_to_align (Array[Name]): 
    method (RetargetAutoAlignMethod): 
    source_or_target (RetargetSourceOrTarget):

<a id="unreal.IKRetargeterController.auto_align_all_bones"></a>

#### auto_align_all_bones

```python
def auto_align_all_bones(source_or_target: RetargetSourceOrTarget) -> None
```

x.auto_align_all_bones(source_or_target) -> None
Automatically align all bones in mapped chains and store in the current retarget pose.

Args:
    source_or_target (RetargetSourceOrTarget):

<a id="unreal.IKRetargeterController.add_retarget_op"></a>

#### add_retarget_op

```python
def add_retarget_op(op_class: Class) -> int
```

x.add_retarget_op(op_class) -> int32
Add a new retarget op of the given type to the bottom of the stack. Returns the stack index.

Args:
    op_class (type(Class)): 

Returns:
    int32:

<a id="unreal.IKRetargetFactory"></a>