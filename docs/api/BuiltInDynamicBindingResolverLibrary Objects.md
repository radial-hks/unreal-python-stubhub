## BuiltInDynamicBindingResolverLibrary Objects

```python
class BuiltInDynamicBindingResolverLibrary(BlueprintFunctionLibrary)
```

Default dynamic binding resolver library, with several basic resolver functions.

**C++ Source:**

- **Module**: MovieScene
- **File**: MovieSceneDynamicBinding.h

<a id="unreal.BuiltInDynamicBindingResolverLibrary.resolve_to_player_pawn"></a>

#### resolve_to_player_pawn

```python
@classmethod
def resolve_to_player_pawn(cls,
                           world_context_object: Object,
                           player_controller_index: int = 0
                           ) -> MovieSceneDynamicBindingResolveResult
```

X.resolve_to_player_pawn(world_context_object, player_controller_index=0) -> MovieSceneDynamicBindingResolveResult
Resolve the bound object to the player's pawn

Args:
    world_context_object (Object): 
    player_controller_index (int32): 

Returns:
    MovieSceneDynamicBindingResolveResult:

<a id="unreal.MovieSceneFolder"></a>