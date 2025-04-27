## AnimNode_Slot Objects

```python
class AnimNode_Slot(AnimNode_Base)
```

An animation slot node normally acts as a passthru, but a montage or PlaySlotAnimation call from
game code can cause an animation to blend in and be played on the slot temporarily, overriding the
Source input.

**C++ Source:**

- **Module**: AnimGraphRuntime
- **File**: AnimNode_Slot.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``always_update_source_pose`` (bool):  [Read-Write] Whether we should continue to update the source pose regardless of whether it would be used.
- ``slot_name`` (Name):  [Read-Write] The name of this slot, exposed to gameplay code, etc...
- ``source`` (PoseLink):  [Read-Write] The source input, passed thru to the output unless a montage or slot animation is currently playing

<a id="unreal.AnimNode_Slot.__init__"></a>

#### __init__

```python
def __init__(source: PoseLink = [],
             slot_name: Name = "None",
             always_update_source_pose: bool = False) -> None
```

<a id="unreal.AnimNode_Slot.source"></a>

#### source

```python
@property
def source() -> PoseLink
```

(PoseLink):  [Read-Write] The source input, passed thru to the output unless a montage or slot animation is currently playing

<a id="unreal.AnimNode_Slot.source"></a>

#### source

```python
@source.setter
def source(value: PoseLink) -> None
```

<a id="unreal.AnimNode_Slot.slot_name"></a>

#### slot_name

```python
@property
def slot_name() -> Name
```

(Name):  [Read-Write] The name of this slot, exposed to gameplay code, etc...

<a id="unreal.AnimNode_Slot.slot_name"></a>

#### slot_name

```python
@slot_name.setter
def slot_name(value: Name) -> None
```

<a id="unreal.AnimNode_Slot.always_update_source_pose"></a>

#### always_update_source_pose

```python
@property
def always_update_source_pose() -> bool
```

(bool):  [Read-Write] Whether we should continue to update the source pose regardless of whether it would be used.

<a id="unreal.AnimNode_Slot.always_update_source_pose"></a>

#### always_update_source_pose

```python
@always_update_source_pose.setter
def always_update_source_pose(value: bool) -> None
```

<a id="unreal.AnimNode_Sync"></a>