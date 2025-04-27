## AvaAutoFollowModifier Objects

```python
class AvaAutoFollowModifier(AvaAttachmentBaseModifier)
```

Moves the modifying actor along with a specified actor relative to the specified actor's bounds.

**C++ Source:**

- **Plugin**: Avalanche
- **Module**: AvalancheModifiers
- **File**: AvaAutoFollowModifier.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``default_distance`` (Vector):  [Read-Write] The distance from this actor to the followed actor.
- ``followed_alignment`` (AvaAnchorAlignment):  [Read-Write] The alignment for the followed actor's center.
- ``followed_axis`` (int32):  [Read-Write] Which axis should we follow
- ``ignore_hidden_actors`` (bool):  [Read-Write] If true, will search for the next visible actor based on the selected reference container.
  deprecated: Use ReferenceActor instead
- ``local_alignment`` (AvaAnchorAlignment):  [Read-Write] The alignment for this actor's center.
- ``max_distance`` (Vector):  [Read-Write] The maximum distance from this actor to the followed actor.
- ``modifier_enabled`` (bool):  [Read-Write] Is the modifier enabled or disabled
- ``offset_axis`` (Vector):  [Read-Write] Based on followed axis, the direction to offset this actor from the followed actor's bounds.
- ``progress`` (Vector):  [Read-Write] Percent % progress from the maximum distance to the default distance.
- ``reference_actor`` (AvaSceneTreeActor):  [Read-Write]
- ``reference_actor_weak`` (Actor):  [Read-Write] The actor being followed by the modifier. This is user selectable if the Reference Container is set to "Other".
  deprecated: Use ReferenceActor instead
- ``reference_container`` (AvaReferenceContainer):  [Read-Write] The method for finding a reference actor based on it's position in the parent's hierarchy.
  deprecated: Use ReferenceActor instead

<a id="unreal.AvaAutoFollowModifier.reference_container"></a>

#### reference_container

```python
@property
def reference_container() -> AvaReferenceContainer
```

(AvaReferenceContainer):  [Read-Write] The method for finding a reference actor based on it's position in the parent's hierarchy.
deprecated: Use ReferenceActor instead

<a id="unreal.AvaAutoFollowModifier.reference_container"></a>

#### reference_container

```python
@reference_container.setter
def reference_container(value: AvaReferenceContainer) -> None
```

<a id="unreal.AvaAutoFollowModifier.reference_actor_weak"></a>

#### reference_actor_weak

```python
@property
def reference_actor_weak() -> Actor
```

(Actor):  [Read-Write] The actor being followed by the modifier. This is user selectable if the Reference Container is set to "Other".
deprecated: Use ReferenceActor instead

<a id="unreal.AvaAutoFollowModifier.reference_actor_weak"></a>

#### reference_actor_weak

```python
@reference_actor_weak.setter
def reference_actor_weak(value: Actor) -> None
```

<a id="unreal.AvaAutoFollowModifier.ignore_hidden_actors"></a>

#### ignore_hidden_actors

```python
@property
def ignore_hidden_actors() -> bool
```

(bool):  [Read-Write] If true, will search for the next visible actor based on the selected reference container.
deprecated: Use ReferenceActor instead

<a id="unreal.AvaAutoFollowModifier.ignore_hidden_actors"></a>

#### ignore_hidden_actors

```python
@ignore_hidden_actors.setter
def ignore_hidden_actors(value: bool) -> None
```

<a id="unreal.AvaAutoFollowModifier.offset_axis"></a>

#### offset_axis

```python
@property
def offset_axis() -> Vector
```

(Vector):  [Read-Write] Based on followed axis, the direction to offset this actor from the followed actor's bounds.

<a id="unreal.AvaAutoFollowModifier.offset_axis"></a>

#### offset_axis

```python
@offset_axis.setter
def offset_axis(value: Vector) -> None
```

<a id="unreal.AvaAutoFollowModifier.default_distance"></a>

#### default_distance

```python
@property
def default_distance() -> Vector
```

(Vector):  [Read-Write] The distance from this actor to the followed actor.

<a id="unreal.AvaAutoFollowModifier.default_distance"></a>

#### default_distance

```python
@default_distance.setter
def default_distance(value: Vector) -> None
```

<a id="unreal.AvaAutoFollowModifier.max_distance"></a>

#### max_distance

```python
@property
def max_distance() -> Vector
```

(Vector):  [Read-Write] The maximum distance from this actor to the followed actor.

<a id="unreal.AvaAutoFollowModifier.max_distance"></a>

#### max_distance

```python
@max_distance.setter
def max_distance(value: Vector) -> None
```

<a id="unreal.AvaAutoFollowModifier.progress"></a>

#### progress

```python
@property
def progress() -> Vector
```

(Vector):  [Read-Write] Percent % progress from the maximum distance to the default distance.

<a id="unreal.AvaAutoFollowModifier.progress"></a>

#### progress

```python
@progress.setter
def progress(value: Vector) -> None
```

<a id="unreal.AvaAutoFollowModifier.set_reference_actor"></a>

#### set_reference_actor

```python
def set_reference_actor(reference_actor: AvaSceneTreeActor) -> None
```

x.set_reference_actor(reference_actor) -> None
Set Reference Actor

Args:
    reference_actor (AvaSceneTreeActor):

<a id="unreal.AvaAutoFollowModifier.set_progress"></a>

#### set_progress

```python
def set_progress(progress: Vector) -> None
```

x.set_progress(progress) -> None
Sets the percent % progress from the maximum distance to the default distance.

Args:
    progress (Vector):

<a id="unreal.AvaAutoFollowModifier.set_offset_axis"></a>

#### set_offset_axis

```python
def set_offset_axis(offset_axis: Vector) -> None
```

x.set_offset_axis(offset_axis) -> None
Sets the axis direction to offset this actor from the followed actor's bounds.

Args:
    offset_axis (Vector):

<a id="unreal.AvaAutoFollowModifier.set_max_distance"></a>

#### set_max_distance

```python
def set_max_distance(max_distance: Vector) -> None
```

x.set_max_distance(max_distance) -> None
Sets the maximum distance from this actor to the followed actor.

Args:
    max_distance (Vector):

<a id="unreal.AvaAutoFollowModifier.set_local_alignment"></a>

#### set_local_alignment

```python
def set_local_alignment(local_alignment: AvaAnchorAlignment) -> None
```

x.set_local_alignment(local_alignment) -> None
Sets the alignment for this actor's center.

Args:
    local_alignment (AvaAnchorAlignment):

<a id="unreal.AvaAutoFollowModifier.set_followed_axis"></a>

#### set_followed_axis

```python
def set_followed_axis(followed_axis: int) -> None
```

x.set_followed_axis(followed_axis) -> None
Set Followed Axis

Args:
    followed_axis (int32):

<a id="unreal.AvaAutoFollowModifier.set_followed_alignment"></a>

#### set_followed_alignment

```python
def set_followed_alignment(followed_alignment: AvaAnchorAlignment) -> None
```

x.set_followed_alignment(followed_alignment) -> None
Sets the alignment for the followed actor's center.

Args:
    followed_alignment (AvaAnchorAlignment):

<a id="unreal.AvaAutoFollowModifier.set_default_distance"></a>

#### set_default_distance

```python
def set_default_distance(default_distance: Vector) -> None
```

x.set_default_distance(default_distance) -> None
Sets the distance from this actor to the followed actor.

Args:
    default_distance (Vector):

<a id="unreal.AvaAutoFollowModifier.get_reference_actor"></a>

#### get_reference_actor

```python
def get_reference_actor() -> AvaSceneTreeActor
```

x.get_reference_actor() -> AvaSceneTreeActor
Get Reference Actor

Returns:
    AvaSceneTreeActor:

<a id="unreal.AvaAutoFollowModifier.get_progress"></a>

#### get_progress

```python
def get_progress() -> Vector
```

x.get_progress() -> Vector
Gets the percent % progress from the maximum distance to the default distance.

Returns:
    Vector:

<a id="unreal.AvaAutoFollowModifier.get_offset_axis"></a>

#### get_offset_axis

```python
def get_offset_axis() -> Vector
```

x.get_offset_axis() -> Vector
Gets the axis direction to offset this actor from the followed actor's bounds.

Returns:
    Vector:

<a id="unreal.AvaAutoFollowModifier.get_max_distance"></a>

#### get_max_distance

```python
def get_max_distance() -> Vector
```

x.get_max_distance() -> Vector
Gets the maximum distance from this actor to the followed actor.

Returns:
    Vector:

<a id="unreal.AvaAutoFollowModifier.get_local_alignment"></a>

#### get_local_alignment

```python
def get_local_alignment() -> AvaAnchorAlignment
```

x.get_local_alignment() -> AvaAnchorAlignment
Gets the alignment for this actor's center.

Returns:
    AvaAnchorAlignment:

<a id="unreal.AvaAutoFollowModifier.get_followed_axis"></a>

#### get_followed_axis

```python
def get_followed_axis() -> int
```

x.get_followed_axis() -> int32
Get Followed Axis

Returns:
    int32:

<a id="unreal.AvaAutoFollowModifier.get_followed_alignment"></a>

#### get_followed_alignment

```python
def get_followed_alignment() -> AvaAnchorAlignment
```

x.get_followed_alignment() -> AvaAnchorAlignment
Gets the alignment for the followed actor's center.

Returns:
    AvaAnchorAlignment:

<a id="unreal.AvaAutoFollowModifier.get_default_distance"></a>

#### get_default_distance

```python
def get_default_distance() -> Vector
```

x.get_default_distance() -> Vector
Gets the distance from this actor to the followed actor.

Returns:
    Vector:

<a id="unreal.AvaGeometryBaseModifier"></a>