## AvaHideEmptyModifier Objects

```python
class AvaHideEmptyModifier(AvaArrangeBaseModifier)
```

Ava Hide Empty Modifier

**C++ Source:**

- **Plugin**: Avalanche
- **Module**: AvalancheModifiers
- **File**: AvaHideEmptyModifier.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``container_actor_weak`` (Actor):  [Read-Write] The container to hide when text is empty, by default self
- ``invert_visibility`` (bool):  [Read-Write] Invert the behaviour and visibility of the container if text is empty
- ``modifier_enabled`` (bool):  [Read-Write] Is the modifier enabled or disabled

<a id="unreal.AvaHideEmptyModifier.set_invert_visibility"></a>

#### set_invert_visibility

```python
def set_invert_visibility(invert: bool) -> None
```

x.set_invert_visibility(invert) -> None
Set Invert Visibility

Args:
    invert (bool):

<a id="unreal.AvaHideEmptyModifier.set_container_actor"></a>

#### set_container_actor

```python
def set_container_actor(actor: Actor) -> None
```

x.set_container_actor(actor) -> None
Set Container Actor

Args:
    actor (Actor):

<a id="unreal.AvaHideEmptyModifier.get_invert_visibility"></a>

#### get_invert_visibility

```python
def get_invert_visibility() -> bool
```

x.get_invert_visibility() -> bool
Get Invert Visibility

Returns:
    bool:

<a id="unreal.AvaHideEmptyModifier.get_container_actor"></a>

#### get_container_actor

```python
def get_container_actor() -> Actor
```

x.get_container_actor() -> Actor
Get Container Actor

Returns:
    Actor:

<a id="unreal.AvaJustifyModifier"></a>