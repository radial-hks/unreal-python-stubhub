## AnimNode_Sync Objects

```python
class AnimNode_Sync(AnimNode_Base)
```

Anim Node Sync

**C++ Source:**

- **Module**: AnimGraphRuntime
- **File**: AnimNode_Sync.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``group_name`` (Name):  [Read-Write] The group name that we synchronize with (NAME_None if it is not part of any group).
- ``group_role`` (AnimGroupRole):  [Read-Write] The role this animation can assume within the group (ignored if GroupName is not set)
- ``source`` (PoseLink):  [Read-Write]

<a id="unreal.AnimNode_Sync.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.AnimNode_TwoWayBlend"></a>