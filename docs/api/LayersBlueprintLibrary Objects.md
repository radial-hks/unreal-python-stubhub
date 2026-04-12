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

#### remove\_actor\_from\_layer

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

#### get\_actors

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

#### add\_actor\_to\_layer

```python
@classmethod
def add_actor_to_layer(cls, actor: Actor, layer: ActorLayer) -> None
```

X.add_actor_to_layer(actor, layer) -> None
Adds the actor to the specified layer

Args:
    actor (Actor): 
    layer (ActorLayer):

<a id="unreal.AndroidPermissionCallbackProxy"></a>