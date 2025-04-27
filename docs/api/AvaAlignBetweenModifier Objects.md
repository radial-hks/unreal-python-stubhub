## AvaAlignBetweenModifier Objects

```python
class AvaAlignBetweenModifier(AvaBaseModifier)
```

Moves the modifying actor to the averaged location between an array of specified actors.

**C++ Source:**

- **Plugin**: Avalanche
- **Module**: AvalancheModifiers
- **File**: AvaAlignBetweenModifier.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``modifier_enabled`` (bool):  [Read-Write] Is the modifier enabled or disabled
- ``reference_actors`` (Set[AvaAlignBetweenWeightedActor]):  [Read-Write] Editable set of reference actors and weights used to calculate the average location for this actor

<a id="unreal.AvaAlignBetweenModifier.set_reference_actors"></a>

#### set_reference_actors

```python
def set_reference_actors(
        reference_actors: Set[AvaAlignBetweenWeightedActor]) -> None
```

x.set_reference_actors(reference_actors) -> None
Sets all reference actors and their weights.

Args:
    reference_actors (Set[AvaAlignBetweenWeightedActor]):

<a id="unreal.AvaAlignBetweenModifier.remove_reference_actor"></a>

#### remove_reference_actor

```python
def remove_reference_actor(actor: Actor) -> bool
```

x.remove_reference_actor(actor) -> bool
Removes an actor from the reference list.

Args:
    actor (Actor): 

Returns:
    bool:

<a id="unreal.AvaAlignBetweenModifier.get_reference_actors"></a>

#### get_reference_actors

```python
def get_reference_actors() -> Set[AvaAlignBetweenWeightedActor]
```

x.get_reference_actors() -> Set[AvaAlignBetweenWeightedActor]
Gets all reference actors and their weights.

Returns:
    Set[AvaAlignBetweenWeightedActor]:

<a id="unreal.AvaAlignBetweenModifier.find_reference_actor"></a>

#### find_reference_actor

```python
def find_reference_actor(
        actor: Actor) -> Optional[AvaAlignBetweenWeightedActor]
```

x.find_reference_actor(actor) -> AvaAlignBetweenWeightedActor or None
Finds an actor in the reference list.

Args:
    actor (Actor): 

Returns:
    AvaAlignBetweenWeightedActor or None: 

    out_reference_actor (AvaAlignBetweenWeightedActor):

<a id="unreal.AvaAlignBetweenModifier.add_reference_actor"></a>

#### add_reference_actor

```python
def add_reference_actor(reference_actor: AvaAlignBetweenWeightedActor) -> bool
```

x.add_reference_actor(reference_actor) -> bool
Adds an actor to the reference list.

Args:
    reference_actor (AvaAlignBetweenWeightedActor): 

Returns:
    bool:

<a id="unreal.AvaAttachmentBaseModifier"></a>