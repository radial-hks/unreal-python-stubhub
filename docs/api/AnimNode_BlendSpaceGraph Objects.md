## AnimNode_BlendSpaceGraph Objects

```python
class AnimNode_BlendSpaceGraph(AnimNode_BlendSpaceGraphBase)
```

Allows multiple animations to be blended between based on input parameters

**C++ Source:**

- **Module**: AnimGraphRuntime
- **File**: AnimNode_BlendSpaceGraph.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``group_name`` (Name):  [Read-Write] The group name that we synchronize with (NAME_None if it is not part of any group). Note that
  this is the name of the group used to sync the output of this node - it will not force
  syncing of animations contained by it. Animations inside this Blend Space have their own
  options for syncing.
- ``group_role`` (AnimGroupRole):  [Read-Write] The role this Blend Space can assume within the group (ignored if GroupName is not set). Note
  that this is the role of the output of this node, not of animations contained by it.
- ``x`` (float):  [Read-Write] The X coordinate to sample in the blendspace
- ``y`` (float):  [Read-Write] The Y coordinate to sample in the blendspace

<a id="unreal.AnimNode_BlendSpaceGraph.__init__"></a>

#### __init__

```python
def __init__(x: float = 0.000000,
             y: float = 0.000000,
             group_name: Name = "None",
             group_role: AnimGroupRole = AnimGroupRole.CAN_BE_LEADER) -> None
```

<a id="unreal.AnimNode_Root"></a>