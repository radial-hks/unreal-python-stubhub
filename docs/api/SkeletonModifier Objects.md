## SkeletonModifier Objects

```python
class SkeletonModifier(Object)
```

FSkeletalMeshSkeletonModifier

**C++ Source:**

- **Plugin**: MeshModelingToolsetExp
- **Module**: SkeletalMeshModifiers
- **File**: SkeletonModifier.h

<a id="unreal.SkeletonModifier.set_skeletal_mesh"></a>

#### set_skeletal_mesh

```python
def set_skeletal_mesh(skeletal_mesh: SkeletalMesh) -> bool
```

x.set_skeletal_mesh(skeletal_mesh) -> bool
Set Skeletal Mesh

Args:
    skeletal_mesh (SkeletalMesh): 

Returns:
    bool:

<a id="unreal.SkeletonModifier.set_bone_transform"></a>

#### set_bone_transform

```python
def set_bone_transform(bone_name: Name, new_transform: Transform,
                       move_children: bool) -> bool
```

x.set_bone_transform(bone_name, new_transform, move_children) -> bool
Sets the bone the desired local transform

Args:
    bone_name (Name): The new bone's name that needs to be moved.
    new_transform (Transform): The new local transform in the bone's parent space.
    move_children (bool): Propagate new transform to children

Returns:
    bool: \c true if the operation succeeded, false otherwise.

<a id="unreal.SkeletonModifier.set_bones_transforms"></a>

#### set_bones_transforms

```python
def set_bones_transforms(bone_names: Array[Name],
                         new_transforms: Array[Transform],
                         move_children: bool) -> bool
```

x.set_bones_transforms(bone_names, new_transforms, move_children) -> bool
Set Bones Transforms

Args:
    bone_names (Array[Name]): 
    new_transforms (Array[Transform]): 
    move_children (bool): 

Returns:
    bool:

<a id="unreal.SkeletonModifier.rename_bones"></a>

#### rename_bones

```python
def rename_bones(old_bone_names: Array[Name],
                 new_bone_names: Array[Name]) -> bool
```

x.rename_bones(old_bone_names, new_bone_names) -> bool
Rename Bones

Args:
    old_bone_names (Array[Name]): 
    new_bone_names (Array[Name]): 

Returns:
    bool:

<a id="unreal.SkeletonModifier.rename_bone"></a>

#### rename_bone

```python
def rename_bone(old_bone_name: Name, new_bone_name: Name) -> bool
```

x.rename_bone(old_bone_name, new_bone_name) -> bool
Rename bones

Args:
    old_bone_name (Name): The current bone's name.
    new_bone_name (Name): The new bone's name.

Returns:
    bool: \c true if the operation succeeded, false otherwise.

<a id="unreal.SkeletonModifier.remove_bones"></a>

#### remove_bones

```python
def remove_bones(bone_names: Array[Name], remove_children: bool) -> bool
```

x.remove_bones(bone_names, remove_children) -> bool
Remove Bones

Args:
    bone_names (Array[Name]): 
    remove_children (bool): 

Returns:
    bool:

<a id="unreal.SkeletonModifier.remove_bone"></a>

#### remove_bone

```python
def remove_bone(bone_name: Name, remove_children: bool) -> bool
```

x.remove_bone(bone_name, remove_children) -> bool
Remove a bone in the skeleton hierarchy

Args:
    bone_name (Name): The new bone's name.
    remove_children (bool): Remove children recursively.

Returns:
    bool: \c true if the operation succeeded, false otherwise.

<a id="unreal.SkeletonModifier.parent_bones"></a>

#### parent_bones

```python
def parent_bones(bone_names: Array[Name], parent_names: Array[Name]) -> bool
```

x.parent_bones(bone_names, parent_names) -> bool
Parent Bones

Args:
    bone_names (Array[Name]): 
    parent_names (Array[Name]): 

Returns:
    bool:

<a id="unreal.SkeletonModifier.parent_bone"></a>

#### parent_bone

```python
def parent_bone(bone_name: Name, parent_name: Name) -> bool
```

x.parent_bone(bone_name, parent_name) -> bool
Parent bones

Args:
    bone_name (Name): The current bone's name.
    parent_name (Name): The new parent's name (Name_NONE to unparent).

Returns:
    bool: \c true if the operation succeeded, false otherwise.

<a id="unreal.SkeletonModifier.orient_bones"></a>

#### orient_bones

```python
def orient_bones(
    bone_names: Array[Name],
    options: OrientOptions = [
        OrientAxis.POSITIVE_X, OrientAxis.POSITIVE_Y, True,
        [0.000000, 1.000000, 0.000000], True
    ]
) -> bool
```

x.orient_bones(bone_names, options=[OrientAxis.POSITIVE_X, OrientAxis.POSITIVE_Y, True, [0.000000, 1.000000, 0.000000], True]) -> bool
Orient Bones

Args:
    bone_names (Array[Name]): 
    options (OrientOptions): 

Returns:
    bool:

<a id="unreal.SkeletonModifier.orient_bone"></a>

#### orient_bone

```python
def orient_bone(
    bone_name: Name,
    options: OrientOptions = [
        OrientAxis.POSITIVE_X, OrientAxis.POSITIVE_Y, True,
        [0.000000, 1.000000, 0.000000], True
    ]
) -> bool
```

x.orient_bone(bone_name, options=[OrientAxis.POSITIVE_X, OrientAxis.POSITIVE_Y, True, [0.000000, 1.000000, 0.000000], True]) -> bool
Align bones

Args:
    bone_name (Name): The current bone's name.
    options (OrientOptions): The orienting options

Returns:
    bool: \c true if the operation succeeded, false otherwise.

<a id="unreal.SkeletonModifier.mirror_bones"></a>

#### mirror_bones

```python
def mirror_bones(
        bones_name: Array[Name],
        options: MirrorOptions = [AxisType.X, True, "_l", "_r", True]) -> bool
```

x.mirror_bones(bones_name, options=[AxisType.X, True, "_l", "_r", True]) -> bool
Mirror Bones

Args:
    bones_name (Array[Name]): 
    options (MirrorOptions): 

Returns:
    bool:

<a id="unreal.SkeletonModifier.mirror_bone"></a>

#### mirror_bone

```python
def mirror_bone(
        bone_name: Name,
        options: MirrorOptions = [AxisType.X, True, "_l", "_r", True]) -> bool
```

x.mirror_bone(bone_name, options=[AxisType.X, True, "_l", "_r", True]) -> bool
Mirror bones

Args:
    bone_name (Name): The new bone's name.
    options (MirrorOptions): The mirroring options

Returns:
    bool: \c true if the operation succeeded, false otherwise.

<a id="unreal.SkeletonModifier.get_parent_name"></a>

#### get_parent_name

```python
def get_parent_name(bone_name: Name) -> Name
```

x.get_parent_name(bone_name) -> Name
Get Parent Name

Args:
    bone_name (Name): The current bone's name.

Returns:
    Name: \c The current bone's parent name

<a id="unreal.SkeletonModifier.get_children_names"></a>

#### get_children_names

```python
def get_children_names(bone_name: Name,
                       recursive: bool = False) -> Array[Name]
```

x.get_children_names(bone_name, recursive=False) -> Array[Name]
Get Children Names

Args:
    bone_name (Name): The parent's name.
    recursive (bool): If set to true grand-children will also be added recursively

Returns:
    Array[Name]: \c The children names list

<a id="unreal.SkeletonModifier.get_bone_transform"></a>

#### get_bone_transform

```python
def get_bone_transform(bone_name: Name, global_: bool = False) -> Transform
```

x.get_bone_transform(bone_name, global_=False) -> Transform
Get Bone Transform

Args:
    bone_name (Name): The current bone's name.
    global_ (bool): Whether it should return the parent space or global transform

Returns:
    Transform: \c The current bone's transform

<a id="unreal.SkeletonModifier.get_all_bone_names"></a>

#### get_all_bone_names

```python
def get_all_bone_names() -> Array[Name]
```

x.get_all_bone_names() -> Array[Name]
Get All Bone Names

Returns:
    Array[Name]: \c All bone names list

<a id="unreal.SkeletonModifier.commit_skeleton_to_skeletal_mesh"></a>

#### commit_skeleton_to_skeletal_mesh

```python
def commit_skeleton_to_skeletal_mesh() -> bool
```

x.commit_skeleton_to_skeletal_mesh() -> bool
Actually applies the skeleton modifications to the skeletal mesh.

Returns:
    bool: true if commit succeeded.

<a id="unreal.SkeletonModifier.add_bones"></a>

#### add_bones

```python
def add_bones(bones_name: Array[Name], parents_name: Array[Name],
              transforms: Array[Transform]) -> bool
```

x.add_bones(bones_name, parents_name, transforms) -> bool
Add Bones

Args:
    bones_name (Array[Name]): 
    parents_name (Array[Name]): 
    transforms (Array[Transform]): 

Returns:
    bool:

<a id="unreal.SkeletonModifier.add_bone"></a>

#### add_bone

```python
def add_bone(bone_name: Name, parent_name: Name, transform: Transform) -> bool
```

x.add_bone(bone_name, parent_name, transform) -> bool
Creates a new bone in the skeleton hierarchy at desired transform

Args:
    bone_name (Name): The new bone's name.
    parent_name (Name): The new bone parent's name.
    transform (Transform): The default local transform in the parent space.

Returns:
    bool: \c true if the operation succeeded, false otherwise.

<a id="unreal.SkinWeightModifier"></a>