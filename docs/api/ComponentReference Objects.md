## ComponentReference Objects

```python
class ComponentReference(BaseComponentReference)
```

Struct that allows for different ways to reference a component using TObjectPtr.
If just an Actor is specified, will return RootComponent of that Actor.

**C++ Source:**

- **Module**: Engine
- **File**: EngineTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``component_property`` (Name):  [Read-Write] Name of component to use. If this is not specified the reference refers to the root component.
- ``other_actor`` (Actor):  [Read-Write] Weak Pointer to a different Actor that owns the Component.
  If this is not provided the reference refers to a component on this / the same actor.
- ``path_to_component`` (str):  [Read-Write] Path to the component from its owner actor

<a id="unreal.ComponentReference.__init__"></a>

#### __init__

```python
def __init__(component_property: Name = "None",
             other_actor: Actor = None) -> None
```

<a id="unreal.ComponentReference.other_actor"></a>

#### other_actor

```python
@property
def other_actor() -> Actor
```

(Actor):  [Read-Write] Weak Pointer to a different Actor that owns the Component.
If this is not provided the reference refers to a component on this / the same actor.

<a id="unreal.ComponentReference.other_actor"></a>

#### other_actor

```python
@other_actor.setter
def other_actor(value: Actor) -> None
```

<a id="unreal.LatentActionInfo"></a>