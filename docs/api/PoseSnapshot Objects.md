## PoseSnapshot Objects

```python
class PoseSnapshot(StructBase)
```

A pose for a skeletal mesh

**C++ Source:**

- **Module**: Engine
- **File**: PoseSnapshot.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``bone_names`` (Array[Name]):  [Read-Write] Array of bone names (corresponding to LocalTransforms)
- ``is_valid`` (bool):  [Read-Write] Whether the pose is valid
- ``local_transforms`` (Array[Transform]):  [Read-Write] Array of transforms per-bone
- ``skeletal_mesh_name`` (Name):  [Read-Write] The name of the skeletal mesh that was used to take this snapshot
- ``snapshot_name`` (Name):  [Read-Write] The name for this snapshot

<a id="unreal.PoseSnapshot.__init__"></a>

#### __init__

```python
def __init__(local_transforms: Array[Transform] = [],
             bone_names: Array[Name] = [],
             skeletal_mesh_name: Name = "None",
             snapshot_name: Name = "None",
             is_valid: bool = False) -> None
```

<a id="unreal.PoseSnapshot.local_transforms"></a>

#### local_transforms

```python
@property
def local_transforms() -> Array[Transform]
```

(Array[Transform]):  [Read-Write] Array of transforms per-bone

<a id="unreal.PoseSnapshot.local_transforms"></a>

#### local_transforms

```python
@local_transforms.setter
def local_transforms(value: Array[Transform]) -> None
```

<a id="unreal.PoseSnapshot.bone_names"></a>

#### bone_names

```python
@property
def bone_names() -> Array[Name]
```

(Array[Name]):  [Read-Write] Array of bone names (corresponding to LocalTransforms)

<a id="unreal.PoseSnapshot.bone_names"></a>

#### bone_names

```python
@bone_names.setter
def bone_names(value: Array[Name]) -> None
```

<a id="unreal.PoseSnapshot.skeletal_mesh_name"></a>

#### skeletal_mesh_name

```python
@property
def skeletal_mesh_name() -> Name
```

(Name):  [Read-Write] The name of the skeletal mesh that was used to take this snapshot

<a id="unreal.PoseSnapshot.skeletal_mesh_name"></a>

#### skeletal_mesh_name

```python
@skeletal_mesh_name.setter
def skeletal_mesh_name(value: Name) -> None
```

<a id="unreal.PoseSnapshot.snapshot_name"></a>

#### snapshot_name

```python
@property
def snapshot_name() -> Name
```

(Name):  [Read-Write] The name for this snapshot

<a id="unreal.PoseSnapshot.snapshot_name"></a>

#### snapshot_name

```python
@snapshot_name.setter
def snapshot_name(value: Name) -> None
```

<a id="unreal.PoseSnapshot.is_valid"></a>

#### is_valid

```python
@property
def is_valid() -> bool
```

(bool):  [Read-Write] Whether the pose is valid

<a id="unreal.PoseSnapshot.is_valid"></a>

#### is_valid

```python
@is_valid.setter
def is_valid(value: bool) -> None
```

<a id="unreal.RandomPlayerSequenceEntry"></a>