## IKRigEffectorGoal Objects

```python
class IKRigEffectorGoal(Object)
```

IKRig Effector Goal

**C++ Source:**

- **Plugin**: IKRig
- **Module**: IKRig
- **File**: IKRigDefinition.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``bone_name`` (Name):  [Read-Only] The name of the bone that this Goal is located at.
- ``current_transform`` (Transform):  [Read-Write] The current transform of this Goal, in the Global Space of the character.
- ``expose_position`` (bool):  [Read-Write] Should position data be exposed in Blueprint
- ``expose_rotation`` (bool):  [Read-Write] Should rotation data be exposed in Blueprint
- ``goal_name`` (Name):  [Read-Only] The name used to refer to this goal from outside systems.
  This is the name to use when referring to this Goal from Blueprint, Anim Graph, Control Rig or IK Retargeter.
- ``initial_transform`` (Transform):  [Read-Only] The initial transform of this Goal, as defined by the initial transform of the Goal's bone in the retarget pose.
- ``position_alpha`` (float):  [Read-Write] Range 0-1, default is 1. Blend between the input bone position (0.0) and the current goal position (1.0).
- ``preview_mode`` (IKRigGoalPreviewMode):  [Read-Write] Effects how this Goal transform is previewed in the IK Rig editor.
  "Additive" interprets the Goal transform as being relative to the input pose. Useful for previewing animations.
  "Absolute" pins the Goal transform to the Gizmo in the viewport.
- ``rotation_alpha`` (float):  [Read-Write] Range 0-1, default is 1. Blend between the input bone rotation (0.0) and the current goal rotation (1.0).
- ``size_multiplier`` (float):  [Read-Write] The size of the Goal gizmo drawing in the editor viewport.
- ``thickness_multiplier`` (float):  [Read-Write] The thickness of the Goal gizmo drawing in the editor viewport.

<a id="unreal.IKRigEffectorGoal.goal_name"></a>

#### goal_name

```python
@property
def goal_name() -> Name
```

(Name):  [Read-Only] The name used to refer to this goal from outside systems.
This is the name to use when referring to this Goal from Blueprint, Anim Graph, Control Rig or IK Retargeter.

<a id="unreal.IKRigEffectorGoal.bone_name"></a>

#### bone_name

```python
@property
def bone_name() -> Name
```

(Name):  [Read-Only] The name of the bone that this Goal is located at.

<a id="unreal.IKRigEffectorGoal.position_alpha"></a>

#### position_alpha

```python
@property
def position_alpha() -> float
```

(float):  [Read-Write] Range 0-1, default is 1. Blend between the input bone position (0.0) and the current goal position (1.0).

<a id="unreal.IKRigEffectorGoal.position_alpha"></a>

#### position_alpha

```python
@position_alpha.setter
def position_alpha(value: float) -> None
```

<a id="unreal.IKRigEffectorGoal.rotation_alpha"></a>

#### rotation_alpha

```python
@property
def rotation_alpha() -> float
```

(float):  [Read-Write] Range 0-1, default is 1. Blend between the input bone rotation (0.0) and the current goal rotation (1.0).

<a id="unreal.IKRigEffectorGoal.rotation_alpha"></a>

#### rotation_alpha

```python
@rotation_alpha.setter
def rotation_alpha(value: float) -> None
```

<a id="unreal.IKRigEffectorGoal.current_transform"></a>

#### current_transform

```python
@property
def current_transform() -> Transform
```

(Transform):  [Read-Write] The current transform of this Goal, in the Global Space of the character.

<a id="unreal.IKRigEffectorGoal.current_transform"></a>

#### current_transform

```python
@current_transform.setter
def current_transform(value: Transform) -> None
```

<a id="unreal.IKRigEffectorGoal.initial_transform"></a>

#### initial_transform

```python
@property
def initial_transform() -> Transform
```

(Transform):  [Read-Only] The initial transform of this Goal, as defined by the initial transform of the Goal's bone in the retarget pose.

<a id="unreal.IKRigEffectorGoal.preview_mode"></a>

#### preview_mode

```python
@property
def preview_mode() -> IKRigGoalPreviewMode
```

(IKRigGoalPreviewMode):  [Read-Write] Effects how this Goal transform is previewed in the IK Rig editor.
"Additive" interprets the Goal transform as being relative to the input pose. Useful for previewing animations.
"Absolute" pins the Goal transform to the Gizmo in the viewport.

<a id="unreal.IKRigEffectorGoal.preview_mode"></a>

#### preview_mode

```python
@preview_mode.setter
def preview_mode(value: IKRigGoalPreviewMode) -> None
```

<a id="unreal.IKRigEffectorGoal.size_multiplier"></a>

#### size_multiplier

```python
@property
def size_multiplier() -> float
```

(float):  [Read-Write] The size of the Goal gizmo drawing in the editor viewport.

<a id="unreal.IKRigEffectorGoal.size_multiplier"></a>

#### size_multiplier

```python
@size_multiplier.setter
def size_multiplier(value: float) -> None
```

<a id="unreal.IKRigEffectorGoal.thickness_multiplier"></a>

#### thickness_multiplier

```python
@property
def thickness_multiplier() -> float
```

(float):  [Read-Write] The thickness of the Goal gizmo drawing in the editor viewport.

<a id="unreal.IKRigEffectorGoal.thickness_multiplier"></a>

#### thickness_multiplier

```python
@thickness_multiplier.setter
def thickness_multiplier(value: float) -> None
```

<a id="unreal.IKRigEffectorGoal.expose_position"></a>

#### expose_position

```python
@property
def expose_position() -> bool
```

(bool):  [Read-Write] Should position data be exposed in Blueprint

<a id="unreal.IKRigEffectorGoal.expose_position"></a>

#### expose_position

```python
@expose_position.setter
def expose_position(value: bool) -> None
```

<a id="unreal.IKRigEffectorGoal.expose_rotation"></a>

#### expose_rotation

```python
@property
def expose_rotation() -> bool
```

(bool):  [Read-Write] Should rotation data be exposed in Blueprint

<a id="unreal.IKRigEffectorGoal.expose_rotation"></a>

#### expose_rotation

```python
@expose_rotation.setter
def expose_rotation(value: bool) -> None
```

<a id="unreal.IKRigDefinition"></a>