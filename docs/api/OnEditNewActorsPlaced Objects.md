## OnEditNewActorsPlaced Objects

```python
class OnEditNewActorsPlaced(MulticastDelegateBase)
```

delegate type for triggering when new actors are placed on to the viewport. Triggers before NewActorsDropped if placement is caused by a drop action

Args:
    obj_to_use (Object): 
    placed_actors (Array[Actor]):

**C++ Source:**

- **Module**: UnrealEd
- **File**: EditorActorSubsystem.h

<a id="unreal.OnEditNewActorsPlaced.__init__"></a>

#### __init__

```python
def __init__(*args: Any, **kwargs: Any) -> None
```

<a id="unreal.OnEditPasteActorsBegin"></a>