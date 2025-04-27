## RigBone Objects

```python
class RigBone(RigElement)
```

Rig Bone

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigBoneHierarchy.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``global_transform`` (Transform):  [Read-Write]
- ``index`` (int32):  [Read-Only]
- ``initial_transform`` (Transform):  [Read-Write] Initial global transform that is saved in this rig
- ``local_transform`` (Transform):  [Read-Write]
- ``name`` (Name):  [Read-Write]
- ``parent_name`` (Name):  [Read-Only]
- ``type`` (RigBoneType):  [Read-Only] the source of the bone to differentiate procedurally generated, imported etc

<a id="unreal.RigBone.__init__"></a>

#### __init__

```python
def __init__(name: Name = "None",
             index: int = 0,
             parent_name: Name = "None",
             initial_transform: Transform = [[0.000000, 0.000000, 0.000000],
                                             [-0.000000, 0.000000, 0.000000],
                                             [1.000000, 1.000000, 1.000000]],
             global_transform: Transform = [[0.000000, 0.000000, 0.000000],
                                            [-0.000000, 0.000000, 0.000000],
                                            [1.000000, 1.000000, 1.000000]],
             local_transform: Transform = [[0.000000, 0.000000, 0.000000],
                                           [-0.000000, 0.000000, 0.000000],
                                           [1.000000, 1.000000, 1.000000]],
             type: RigBoneType = RigBoneType.IMPORTED) -> None
```

<a id="unreal.RigBone.parent_name"></a>

#### parent_name

```python
@property
def parent_name() -> Name
```

(Name):  [Read-Only]

<a id="unreal.RigBone.initial_transform"></a>

#### initial_transform

```python
@property
def initial_transform() -> Transform
```

(Transform):  [Read-Only] Initial global transform that is saved in this rig

<a id="unreal.RigBone.global_transform"></a>

#### global_transform

```python
@property
def global_transform() -> Transform
```

(Transform):  [Read-Only]

<a id="unreal.RigBone.local_transform"></a>

#### local_transform

```python
@property
def local_transform() -> Transform
```

(Transform):  [Read-Only]

<a id="unreal.RigBone.type"></a>

#### type

```python
@property
def type() -> RigBoneType
```

(RigBoneType):  [Read-Only] the source of the bone to differentiate procedurally generated, imported etc

<a id="unreal.RigJoint"></a>