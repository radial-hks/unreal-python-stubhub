## OnLevelEditorPostSaveWorld Objects

```python
class OnLevelEditorPostSaveWorld(MulticastDelegateBase)
```

Delegate type for post save world events ( uint32 SaveFlags, UWorld* World, bool bSuccess )

Args:
    save_flags (int32): 
    world (World): 
    success (bool):

**C++ Source:**

- **Module**: LevelEditor
- **File**: LevelEditorSubsystem.h

<a id="unreal.OnLevelEditorPostSaveWorld.__init__"></a>

#### __init__

```python
def __init__(*args: Any, **kwargs: Any) -> None
```

<a id="unreal.OnLevelEditorPreSaveWorld"></a>