## AnimNode_SingleNode Objects

```python
class AnimNode_SingleNode(AnimNode_Base)
```

Local anim node for extensible processing.
Cant be used outside of this context as it has no graph node counterpart

**C++ Source:**

- **Module**: Engine
- **File**: AnimSingleNodeInstanceProxy.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``source_pose`` (PoseLink):  [Read-Write]

<a id="unreal.AnimNode_SingleNode.__init__"></a>

#### __init__

```python
def __init__(source_pose: PoseLink = []) -> None
```

<a id="unreal.AnimNode_SingleNode.source_pose"></a>

#### source_pose

```python
@property
def source_pose() -> PoseLink
```

(PoseLink):  [Read-Write]

<a id="unreal.AnimNode_SingleNode.source_pose"></a>

#### source_pose

```python
@source_pose.setter
def source_pose(value: PoseLink) -> None
```

<a id="unreal.CachedAnimStateData"></a>