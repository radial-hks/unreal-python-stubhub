## AnimNode_BlendSpaceGraphBase Objects

```python
class AnimNode_BlendSpaceGraphBase(AnimNode_Base)
```

Allows multiple animations to be blended between based on input parameters

**C++ Source:**

- **Module**: AnimGraphRuntime
- **File**: AnimNode_BlendSpaceGraphBase.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``group_name`` (Name):  [Read-Write] The group name that we synchronize with (NAME_None if it is not part of any group). Note that
  this is the name of the group used to sync the output of this node - it will not force
  syncing of animations contained by it. Animations inside this Blend Space have their own
  options for syncing.
- ``group_role`` (AnimGroupRole):  [Read-Write] The role this Blend Space can assume within the group (ignored if GroupName is not set). Note
  that this is the role of the output of this node, not of animations contained by it.
- ``x`` (float):  [Read-Write] The X coordinate to sample in the blendspace
- ``y`` (float):  [Read-Write] The Y coordinate to sample in the blendspace

<a id="unreal.AnimNode_BlendSpaceGraphBase.__init__"></a>

#### __init__

```python
def __init__(x: float = 0.000000,
             y: float = 0.000000,
             group_name: Name = "None",
             group_role: AnimGroupRole = AnimGroupRole.CAN_BE_LEADER) -> None
```

<a id="unreal.AnimNode_BlendSpaceGraphBase.x"></a>

#### x

```python
@property
def x() -> float
```

(float):  [Read-Write] The X coordinate to sample in the blendspace

<a id="unreal.AnimNode_BlendSpaceGraphBase.x"></a>

#### x

```python
@x.setter
def x(value: float) -> None
```

<a id="unreal.AnimNode_BlendSpaceGraphBase.y"></a>

#### y

```python
@property
def y() -> float
```

(float):  [Read-Write] The Y coordinate to sample in the blendspace

<a id="unreal.AnimNode_BlendSpaceGraphBase.y"></a>

#### y

```python
@y.setter
def y(value: float) -> None
```

<a id="unreal.AnimNode_BlendSpaceGraphBase.group_name"></a>

#### group_name

```python
@property
def group_name() -> Name
```

(Name):  [Read-Write] The group name that we synchronize with (NAME_None if it is not part of any group). Note that
this is the name of the group used to sync the output of this node - it will not force
syncing of animations contained by it. Animations inside this Blend Space have their own
options for syncing.

<a id="unreal.AnimNode_BlendSpaceGraphBase.group_name"></a>

#### group_name

```python
@group_name.setter
def group_name(value: Name) -> None
```

<a id="unreal.AnimNode_BlendSpaceGraphBase.group_role"></a>

#### group_role

```python
@property
def group_role() -> AnimGroupRole
```

(AnimGroupRole):  [Read-Write] The role this Blend Space can assume within the group (ignored if GroupName is not set). Note
that this is the role of the output of this node, not of animations contained by it.

<a id="unreal.AnimNode_BlendSpaceGraphBase.group_role"></a>

#### group_role

```python
@group_role.setter
def group_role(value: AnimGroupRole) -> None
```

<a id="unreal.PoseLinkBase"></a>