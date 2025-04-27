## ControlRigPoseAsset Objects

```python
class ControlRigPoseAsset(Object)
```

An individual Pose made of Control Rig Controls

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: ControlRigPose.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``pose`` (ControlRigControlPose):  [Read-Write]

<a id="unreal.ControlRigPoseAsset.pose"></a>

#### pose

```python
@property
def pose() -> ControlRigControlPose
```

(ControlRigControlPose):  [Read-Write]

<a id="unreal.ControlRigPoseAsset.pose"></a>

#### pose

```python
@pose.setter
def pose(value: ControlRigControlPose) -> None
```

<a id="unreal.ControlRigPoseAsset.select_controls"></a>

#### select_controls

```python
def select_controls(control_rig: ControlRig, do_mirror: bool = False) -> None
```

x.select_controls(control_rig, do_mirror=False) -> None
Select Controls

Args:
    control_rig (ControlRig): 
    do_mirror (bool):

<a id="unreal.ControlRigPoseAsset.save_pose"></a>

#### save_pose

```python
def save_pose(control_rig: ControlRig, use_all: bool) -> None
```

x.save_pose(control_rig, use_all) -> None
Save Pose

Args:
    control_rig (ControlRig): 
    use_all (bool):

<a id="unreal.ControlRigPoseAsset.replace_control_name"></a>

#### replace_control_name

```python
def replace_control_name(current_name: Name, new_name: Name) -> None
```

x.replace_control_name(current_name, new_name) -> None
Replace Control Name

Args:
    current_name (Name): 
    new_name (Name):

<a id="unreal.ControlRigPoseAsset.paste_pose"></a>

#### paste_pose

```python
def paste_pose(control_rig: ControlRig,
               do_key: bool = False,
               do_mirror: bool = False) -> None
```

x.paste_pose(control_rig, do_key=False, do_mirror=False) -> None
Paste Pose

Args:
    control_rig (ControlRig): 
    do_key (bool): 
    do_mirror (bool):

<a id="unreal.ControlRigPoseAsset.get_current_pose"></a>

#### get_current_pose

```python
def get_current_pose(control_rig: ControlRig) -> ControlRigControlPose
```

x.get_current_pose(control_rig) -> ControlRigControlPose
Get Current Pose

Args:
    control_rig (ControlRig): 

Returns:
    ControlRigControlPose: 

    out_pose (ControlRigControlPose):

<a id="unreal.ControlRigPoseAsset.get_control_names"></a>

#### get_control_names

```python
def get_control_names() -> Array[Name]
```

x.get_control_names() -> Array[Name]
Get Control Names

Returns:
    Array[Name]:

<a id="unreal.ControlRigPoseAsset.does_mirror_match"></a>

#### does_mirror_match

```python
def does_mirror_match(control_rig: ControlRig, control_name: Name) -> bool
```

x.does_mirror_match(control_rig, control_name) -> bool
Does Mirror Match

Args:
    control_rig (ControlRig): 
    control_name (Name): 

Returns:
    bool:

<a id="unreal.ControlRigPoseMirrorSettings"></a>