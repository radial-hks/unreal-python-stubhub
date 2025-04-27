## AvaSceneTreeActor Objects

```python
class AvaSceneTreeActor(StructBase)
```

Ava Scene Tree Actor

**C++ Source:**

- **Plugin**: Avalanche
- **Module**: AvalancheModifiers
- **File**: AvaSceneTreeUpdateModifierExtension.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``reference_actor_weak`` (Actor):  [Read-Write] The actor being followed by the modifier. This is user selectable if the Reference Container is set to "Other"
- ``reference_container`` (AvaReferenceContainer):  [Read-Write] The method for finding a reference actor based on it's position in the parent's hierarchy
- ``skip_hidden_actors`` (bool):  [Read-Write] If true, will search for the next visible actor based on the selected reference container

<a id="unreal.AvaSceneTreeActor.__init__"></a>

#### __init__

```python
def __init__(reference_container: AvaReferenceContainer = AvaReferenceContainer
             .PREVIOUS,
             reference_actor_weak: Actor = None,
             skip_hidden_actors: bool = False) -> None
```

<a id="unreal.AvaSceneTreeActor.reference_container"></a>

#### reference_container

```python
@property
def reference_container() -> AvaReferenceContainer
```

(AvaReferenceContainer):  [Read-Write] The method for finding a reference actor based on it's position in the parent's hierarchy

<a id="unreal.AvaSceneTreeActor.reference_container"></a>

#### reference_container

```python
@reference_container.setter
def reference_container(value: AvaReferenceContainer) -> None
```

<a id="unreal.AvaSceneTreeActor.reference_actor_weak"></a>

#### reference_actor_weak

```python
@property
def reference_actor_weak() -> Actor
```

(Actor):  [Read-Write] The actor being followed by the modifier. This is user selectable if the Reference Container is set to "Other"

<a id="unreal.AvaSceneTreeActor.reference_actor_weak"></a>

#### reference_actor_weak

```python
@reference_actor_weak.setter
def reference_actor_weak(value: Actor) -> None
```

<a id="unreal.AvaSceneTreeActor.skip_hidden_actors"></a>

#### skip_hidden_actors

```python
@property
def skip_hidden_actors() -> bool
```

(bool):  [Read-Write] If true, will search for the next visible actor based on the selected reference container

<a id="unreal.AvaSceneTreeActor.skip_hidden_actors"></a>

#### skip_hidden_actors

```python
@skip_hidden_actors.setter
def skip_hidden_actors(value: bool) -> None
```

<a id="unreal.AvaSequencerDisplayRate"></a>