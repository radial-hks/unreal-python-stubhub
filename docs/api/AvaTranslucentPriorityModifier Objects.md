## AvaTranslucentPriorityModifier Objects

```python
class AvaTranslucentPriorityModifier(AvaArrangeBaseModifier)
```

Ava Translucent Priority Modifier

**C++ Source:**

- **Plugin**: Avalanche
- **Module**: AvalancheModifiers
- **File**: AvaTranslucentPriorityModifier.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``camera_actor_weak`` (CameraActor):  [Read-Write] The camera actor to compute the distance from
- ``include_children`` (bool):  [Read-Write] If true, will include children too and update their sort priority
- ``mode`` (AvaTranslucentPriorityModifierMode):  [Read-Write] The sort mode we are currently in
- ``modifier_enabled`` (bool):  [Read-Write] Is the modifier enabled or disabled
- ``sort_priority`` (int32):  [Read-Write] The sort priority that will be set on the primitive component for manual mode
- ``sort_priority_offset`` (int32):  [Read-Write] Sort priority offset shared across all modifiers in this same level
- ``sort_priority_step`` (int32):  [Read-Write] Sort priority incremental step shared across all modifiers in this same level

<a id="unreal.AvaTranslucentPriorityModifier.set_sort_priority_step"></a>

#### set_sort_priority_step

```python
def set_sort_priority_step(step: int) -> None
```

x.set_sort_priority_step(step) -> None
Set Sort Priority Step

Args:
    step (int32):

<a id="unreal.AvaTranslucentPriorityModifier.set_sort_priority_offset"></a>

#### set_sort_priority_offset

```python
def set_sort_priority_offset(offset: int) -> None
```

x.set_sort_priority_offset(offset) -> None
Set Sort Priority Offset

Args:
    offset (int32):

<a id="unreal.AvaTranslucentPriorityModifier.set_sort_priority"></a>

#### set_sort_priority

```python
def set_sort_priority(sort_priority: int) -> None
```

x.set_sort_priority(sort_priority) -> None
Set Sort Priority

Args:
    sort_priority (int32):

<a id="unreal.AvaTranslucentPriorityModifier.set_mode"></a>

#### set_mode

```python
def set_mode(mode: AvaTranslucentPriorityModifierMode) -> None
```

x.set_mode(mode) -> None
Set Mode

Args:
    mode (AvaTranslucentPriorityModifierMode):

<a id="unreal.AvaTranslucentPriorityModifier.set_include_children"></a>

#### set_include_children

```python
def set_include_children(include_children: bool) -> None
```

x.set_include_children(include_children) -> None
Set Include Children

Args:
    include_children (bool):

<a id="unreal.AvaTranslucentPriorityModifier.set_camera_actor"></a>

#### set_camera_actor

```python
def set_camera_actor(camera_actor: CameraActor) -> None
```

x.set_camera_actor(camera_actor) -> None
Set Camera Actor

Args:
    camera_actor (CameraActor):

<a id="unreal.AvaTranslucentPriorityModifier.get_sort_priority_step"></a>

#### get_sort_priority_step

```python
def get_sort_priority_step() -> int
```

x.get_sort_priority_step() -> int32
Get Sort Priority Step

Returns:
    int32:

<a id="unreal.AvaTranslucentPriorityModifier.get_sort_priority_offset"></a>

#### get_sort_priority_offset

```python
def get_sort_priority_offset() -> int
```

x.get_sort_priority_offset() -> int32
Get Sort Priority Offset

Returns:
    int32:

<a id="unreal.AvaTranslucentPriorityModifier.get_sort_priority"></a>

#### get_sort_priority

```python
def get_sort_priority() -> int
```

x.get_sort_priority() -> int32
Get Sort Priority

Returns:
    int32:

<a id="unreal.AvaTranslucentPriorityModifier.get_mode"></a>

#### get_mode

```python
def get_mode() -> AvaTranslucentPriorityModifierMode
```

x.get_mode() -> AvaTranslucentPriorityModifierMode
Get Mode

Returns:
    AvaTranslucentPriorityModifierMode:

<a id="unreal.AvaTranslucentPriorityModifier.get_include_children"></a>

#### get_include_children

```python
def get_include_children() -> bool
```

x.get_include_children() -> bool
Get Include Children

Returns:
    bool:

<a id="unreal.AvaTranslucentPriorityModifier.get_camera_actor"></a>

#### get_camera_actor

```python
def get_camera_actor() -> CameraActor
```

x.get_camera_actor() -> CameraActor
Get Camera Actor

Returns:
    CameraActor:

<a id="unreal.AvaVisibilityModifier"></a>