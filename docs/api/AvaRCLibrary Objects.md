## AvaRCLibrary Objects

```python
class AvaRCLibrary(BlueprintFunctionLibrary)
```

Ava RCLibrary

**C++ Source:**

- **Plugin**: Avalanche
- **Module**: AvalancheRemoteControl
- **File**: AvaRCLibrary.h

<a id="unreal.AvaRCLibrary.get_controlled_actors"></a>

#### get_controlled_actors

```python
@classmethod
def get_controlled_actors(cls, world_context_object: Object,
                          controller: RCVirtualPropertyBase) -> Array[Actor]
```

X.get_controlled_actors(world_context_object, controller) -> Array[Actor]
Get Controlled Actors

Args:
    world_context_object (Object): 
    controller (RCVirtualPropertyBase): 

Returns:
    Array[Actor]:

<a id="unreal.AvaRemoteControlInterface"></a>