## AvaLookAtModifier Objects

```python
class AvaLookAtModifier(AvaAttachmentBaseModifier)
```

Rotates the modifying actor to point it's specified axis at another actor.

**C++ Source:**

- **Plugin**: Avalanche
- **Module**: AvalancheModifiers
- **File**: AvaLookAtModifier.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``axis`` (AvaAxis):  [Read-Write] The axis that will point towards the reference actor.
- ``flip_axis`` (bool):  [Read-Write] If true, will flip the look-at direction.
- ``modifier_enabled`` (bool):  [Read-Write] Is the modifier enabled or disabled
- ``reference_actor`` (AvaSceneTreeActor):  [Read-Write]
- ``reference_actor_weak`` (Actor):  [Read-Write] The actor to look at.
  deprecated: Use ReferenceActor instead

<a id="unreal.AvaLookAtModifier.reference_actor_weak"></a>

#### reference_actor_weak

```python
@property
def reference_actor_weak() -> Actor
```

(Actor):  [Read-Write] The actor to look at.
deprecated: Use ReferenceActor instead

<a id="unreal.AvaLookAtModifier.reference_actor_weak"></a>

#### reference_actor_weak

```python
@reference_actor_weak.setter
def reference_actor_weak(value: Actor) -> None
```

<a id="unreal.AvaLookAtModifier.set_reference_actor"></a>

#### set_reference_actor

```python
def set_reference_actor(reference_actor: AvaSceneTreeActor) -> None
```

x.set_reference_actor(reference_actor) -> None
Set Reference Actor

Args:
    reference_actor (AvaSceneTreeActor):

<a id="unreal.AvaLookAtModifier.set_flip_axis"></a>

#### set_flip_axis

```python
def set_flip_axis(flip_axis: bool) -> None
```

x.set_flip_axis(flip_axis) -> None
Sets the look-at direction to be flipped.

Args:
    flip_axis (bool):

<a id="unreal.AvaLookAtModifier.set_axis"></a>

#### set_axis

```python
def set_axis(axis: AvaAxis) -> None
```

x.set_axis(axis) -> None
Sets the axis that will point towards the reference actor.

Args:
    axis (AvaAxis):

<a id="unreal.AvaLookAtModifier.get_reference_actor"></a>

#### get_reference_actor

```python
def get_reference_actor() -> AvaSceneTreeActor
```

x.get_reference_actor() -> AvaSceneTreeActor
Get Reference Actor

Returns:
    AvaSceneTreeActor:

<a id="unreal.AvaLookAtModifier.get_flip_axis"></a>

#### get_flip_axis

```python
def get_flip_axis() -> bool
```

x.get_flip_axis() -> bool
Returns true if flipping the look-at rotation axis.

Returns:
    bool:

<a id="unreal.AvaLookAtModifier.get_axis"></a>

#### get_axis

```python
def get_axis() -> AvaAxis
```

x.get_axis() -> AvaAxis
Returns the axis that will point towards t he reference actor.

Returns:
    AvaAxis:

<a id="unreal.AvaMirrorModifier"></a>