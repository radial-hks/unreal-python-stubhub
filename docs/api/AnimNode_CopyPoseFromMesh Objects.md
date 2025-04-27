## AnimNode_CopyPoseFromMesh Objects

```python
class AnimNode_CopyPoseFromMesh(AnimNode_Base)
```

Simple controller to copy a bone's transform to another one.

**C++ Source:**

- **Module**: AnimGraphRuntime
- **File**: AnimNode_CopyPoseFromMesh.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``copy_curves`` (bool):  [Read-Write] Copy curves also from SouceMeshComponent. This will copy the curves if this instance also contains curve attributes
- ``copy_custom_attributes`` (bool):  [Read-Write] Copy custom attributes (animation attributes) from SourceMeshComponent
- ``root_bone_to_copy`` (Name):  [Read-Write] If you want to specify copy root, use this - this will ensure copy only below of this joint (inclusively)
- ``source_mesh_component`` (SkeletalMeshComponent):  [Read-Write] This is used by default if it's valid
- ``use_attached_parent`` (bool):  [Read-Write] If SourceMeshComponent is not valid, and if this is true, it will look for attahced parent as a source
- ``use_mesh_pose`` (bool):  [Read-Write] Use root space transform to copy to the target pose. By default, it copies their relative transform (bone space)

<a id="unreal.AnimNode_CopyPoseFromMesh.__init__"></a>

#### __init__

```python
def __init__(source_mesh_component: SkeletalMeshComponent = None,
             use_attached_parent: bool = False,
             copy_curves: bool = False,
             copy_custom_attributes: bool = False,
             use_mesh_pose: bool = False,
             root_bone_to_copy: Name = "None") -> None
```

<a id="unreal.AnimNode_CopyPoseFromMesh.source_mesh_component"></a>

#### source_mesh_component

```python
@property
def source_mesh_component() -> SkeletalMeshComponent
```

(SkeletalMeshComponent):  [Read-Write] This is used by default if it's valid

<a id="unreal.AnimNode_CopyPoseFromMesh.source_mesh_component"></a>

#### source_mesh_component

```python
@source_mesh_component.setter
def source_mesh_component(value: SkeletalMeshComponent) -> None
```

<a id="unreal.AnimNode_CopyPoseFromMesh.use_attached_parent"></a>

#### use_attached_parent

```python
@property
def use_attached_parent() -> bool
```

(bool):  [Read-Write] If SourceMeshComponent is not valid, and if this is true, it will look for attahced parent as a source

<a id="unreal.AnimNode_CopyPoseFromMesh.use_attached_parent"></a>

#### use_attached_parent

```python
@use_attached_parent.setter
def use_attached_parent(value: bool) -> None
```

<a id="unreal.AnimNode_CopyPoseFromMesh.copy_curves"></a>

#### copy_curves

```python
@property
def copy_curves() -> bool
```

(bool):  [Read-Write] Copy curves also from SouceMeshComponent. This will copy the curves if this instance also contains curve attributes

<a id="unreal.AnimNode_CopyPoseFromMesh.copy_curves"></a>

#### copy_curves

```python
@copy_curves.setter
def copy_curves(value: bool) -> None
```

<a id="unreal.AnimNode_CopyPoseFromMesh.copy_custom_attributes"></a>

#### copy_custom_attributes

```python
@property
def copy_custom_attributes() -> bool
```

(bool):  [Read-Write] Copy custom attributes (animation attributes) from SourceMeshComponent

<a id="unreal.AnimNode_CopyPoseFromMesh.copy_custom_attributes"></a>

#### copy_custom_attributes

```python
@copy_custom_attributes.setter
def copy_custom_attributes(value: bool) -> None
```

<a id="unreal.AnimNode_CopyPoseFromMesh.use_mesh_pose"></a>

#### use_mesh_pose

```python
@property
def use_mesh_pose() -> bool
```

(bool):  [Read-Write] Use root space transform to copy to the target pose. By default, it copies their relative transform (bone space)

<a id="unreal.AnimNode_CopyPoseFromMesh.use_mesh_pose"></a>

#### use_mesh_pose

```python
@use_mesh_pose.setter
def use_mesh_pose(value: bool) -> None
```

<a id="unreal.AnimNode_CopyPoseFromMesh.root_bone_to_copy"></a>

#### root_bone_to_copy

```python
@property
def root_bone_to_copy() -> Name
```

(Name):  [Read-Write] If you want to specify copy root, use this - this will ensure copy only below of this joint (inclusively)

<a id="unreal.AnimNode_CopyPoseFromMesh.root_bone_to_copy"></a>

#### root_bone_to_copy

```python
@root_bone_to_copy.setter
def root_bone_to_copy(value: Name) -> None
```

<a id="unreal.AnimNode_CurveSource"></a>