## AISense_Blueprint Objects

```python
class AISense_Blueprint(AISense)
```

AISense Blueprint

**C++ Source:**

- **Module**: AIModule
- **File**: AISense_Blueprint.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``auto_register_all_pawns_as_sources`` (bool):  [Read-Write] If true all newly spawned pawns will get auto registered as source for this sense.
- ``listener_container`` (Array[AIPerceptionComponent]):  [Read-Write]
- ``listener_data_type`` (type(Class)):  [Read-Write]
- ``notify_type`` (AISenseNotifyType):  [Read-Write]
- ``wants_new_pawn_notification`` (bool):  [Read-Write] whether this sense is interested in getting notified about new Pawns being spawned
      this can be used for example for automated sense sources registration

<a id="unreal.AISense_Blueprint.listener_data_type"></a>

#### listener_data_type

```python
@property
def listener_data_type() -> Class
```

(type(Class)):  [Read-Write]

<a id="unreal.AISense_Blueprint.listener_data_type"></a>

#### listener_data_type

```python
@listener_data_type.setter
def listener_data_type(value: Class) -> None
```

<a id="unreal.AISense_Blueprint.listener_container"></a>

#### listener_container

```python
@property
def listener_container() -> Array[AIPerceptionComponent]
```

(Array[AIPerceptionComponent]):  [Read-Only]

<a id="unreal.AISense_Blueprint.on_update"></a>

#### on_update

```python
def on_update(events_to_process: Array[AISenseEvent]) -> float
```

x.on_update(events_to_process) -> float
returns requested amount of time to pass until next frame.
    Return 0 to get update every frame (WARNING: hits performance)

Args:
    events_to_process (Array[AISenseEvent]): 

Returns:
    float:

<a id="unreal.AISense_Blueprint.on_listener_updated"></a>

#### on_listener_updated

```python
def on_listener_updated(actor_listener: Actor,
                        perception_component: AIPerceptionComponent) -> None
```

x.on_listener_updated(actor_listener, perception_component) -> None


Args:
    actor_listener (Actor): 
    perception_component (AIPerceptionComponent): is ActorListener's AIPerceptionComponent instance

<a id="unreal.AISense_Blueprint.on_listener_unregistered"></a>

#### on_listener_unregistered

```python
def on_listener_unregistered(
        actor_listener: Actor,
        perception_component: AIPerceptionComponent) -> None
```

x.on_listener_unregistered(actor_listener, perception_component) -> None
called when a listener unregistered from this sense. Most often this is called due to actor's death

Args:
    actor_listener (Actor): 
    perception_component (AIPerceptionComponent): is ActorListener's AIPerceptionComponent instance

<a id="unreal.AISense_Blueprint.on_listener_registered"></a>

#### on_listener_registered

```python
def on_listener_registered(
        actor_listener: Actor,
        perception_component: AIPerceptionComponent) -> None
```

x.on_listener_registered(actor_listener, perception_component) -> None


Args:
    actor_listener (Actor): 
    perception_component (AIPerceptionComponent): is ActorListener's AIPerceptionComponent instance

<a id="unreal.AISense_Blueprint.on_new_pawn"></a>

#### on_new_pawn

```python
def on_new_pawn(new_pawn: Pawn) -> None
```

x.on_new_pawn(new_pawn) -> None
called when sense's instance gets notified about new pawn that has just been spawned

Args:
    new_pawn (Pawn):

<a id="unreal.AISense_Blueprint.get_all_listener_components"></a>

#### get_all_listener_components

```python
def get_all_listener_components() -> Array[AIPerceptionComponent]
```

x.get_all_listener_components() -> Array[AIPerceptionComponent]
Get All Listener Components

Returns:
    Array[AIPerceptionComponent]: 

    listener_components (Array[AIPerceptionComponent]):

<a id="unreal.AISense_Blueprint.get_all_listener_actors"></a>

#### get_all_listener_actors

```python
def get_all_listener_actors() -> Array[Actor]
```

x.get_all_listener_actors() -> Array[Actor]
Get All Listener Actors

Returns:
    Array[Actor]: 

    listener_actors (Array[Actor]):

<a id="unreal.AISense_Damage"></a>