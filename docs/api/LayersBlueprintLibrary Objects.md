## LayersBlueprintLibrary Objects

```python
class LayersBlueprintLibrary(BlueprintFunctionLibrary)
```

Function library containing methods for interacting with editor layers

**C++ Source:**

- **Plugin**: ActorLayerUtilities
- **Module**: ActorLayerUtilities
- **File**: ActorLayerUtilities.h

<a id="unreal.LayersBlueprintLibrary.remove_actor_from_layer"></a>

#### remove_actor_from_layer

```python
@classmethod
def remove_actor_from_layer(cls, actor: Actor, layer: ActorLayer) -> None
```

X.remove_actor_from_layer(actor, layer) -> None
Removes the actor from the specified layer

Args:
    actor (Actor): 
    layer (ActorLayer):

<a id="unreal.LayersBlueprintLibrary.get_actors"></a>

#### get_actors

```python
@classmethod
def get_actors(cls, world_context_object: Object,
               actor_layer: ActorLayer) -> Array[Actor]
```

X.get_actors(world_context_object, actor_layer) -> Array[Actor]
Get all the actors in this layer

Args:
    world_context_object (Object): 
    actor_layer (ActorLayer): 

Returns:
    Array[Actor]:

<a id="unreal.LayersBlueprintLibrary.add_actor_to_layer"></a>

#### add_actor_to_layer

```python
@classmethod
def add_actor_to_layer(cls, actor: Actor, layer: ActorLayer) -> None
```

X.add_actor_to_layer(actor, layer) -> None
Adds the actor to the specified layer

Args:
    actor (Actor): 
    layer (ActorLayer):

<a id="unreal.DisplayClusterConfigurationData_Base"></a>