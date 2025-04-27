## LightWeightInstanceBlueprintFunctionLibrary Objects

```python
class LightWeightInstanceBlueprintFunctionLibrary(BlueprintFunctionLibrary)
```

Light Weight Instance Blueprint Function Library

**C++ Source:**

- **Module**: Engine
- **File**: LightWeightInstanceBlueprintFunctionLibrary.h

<a id="unreal.LightWeightInstanceBlueprintFunctionLibrary.create_new_light_weight_instance"></a>

#### create_new_light_weight_instance

```python
@classmethod
def create_new_light_weight_instance(cls, actor_class: Class,
                                     transform: Transform,
                                     layer: DataLayerInstance,
                                     world: World) -> ActorInstanceHandle
```

X.create_new_light_weight_instance(actor_class, transform, layer, world) -> ActorInstanceHandle
Returns a handle to a new light weight instance that represents an object of type ActorClass

Args:
    actor_class (type(Class)): 
    transform (Transform): 
    layer (DataLayerInstance): 
    world (World): 

Returns:
    ActorInstanceHandle:

<a id="unreal.LightWeightInstanceBlueprintFunctionLibrary.convert_actor_to_light_weight_instance"></a>

#### convert_actor_to_light_weight_instance

```python
@classmethod
def convert_actor_to_light_weight_instance(
        cls, actor: Actor) -> ActorInstanceHandle
```

X.convert_actor_to_light_weight_instance(actor) -> ActorInstanceHandle
Returns a handle to the light weight representation and destroys Actor if successful; Returns a handle to Actor otherwise

Args:
    actor (Actor): 

Returns:
    ActorInstanceHandle:

<a id="unreal.LightWeightInstanceManager"></a>