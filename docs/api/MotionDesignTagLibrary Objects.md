## MotionDesignTagLibrary Objects

```python
class MotionDesignTagLibrary(BlueprintFunctionLibrary)
```

Ava Tag Library

**C++ Source:**

- **Plugin**: Avalanche
- **Module**: AvalancheTag
- **File**: AvaTagLibrary.h

<a id="unreal.MotionDesignTagLibrary.resolve_tag_soft_handle"></a>

#### resolve_tag_soft_handle

```python
@classmethod
def resolve_tag_soft_handle(cls,
                            tag_soft_handle: AvaTagSoftHandle) -> AvaTagHandle
```

X.resolve_tag_soft_handle(tag_soft_handle) -> AvaTagHandle
Resolve Tag Soft Handle

Args:
    tag_soft_handle (AvaTagSoftHandle): 

Returns:
    AvaTagHandle:

<a id="unreal.MotionDesignTagLibrary.resolve_tag_handles"></a>

#### resolve_tag_handles

```python
@classmethod
def resolve_tag_handles(
        cls, tag_handle_container: AvaTagHandleContainer) -> Array[AvaTag]
```

X.resolve_tag_handles(tag_handle_container) -> Array[AvaTag]
Resolve Tag Handles

Args:
    tag_handle_container (AvaTagHandleContainer): 

Returns:
    Array[AvaTag]:

<a id="unreal.MotionDesignTagLibrary.resolve_tag_handle"></a>

#### resolve_tag_handle

```python
@classmethod
def resolve_tag_handle(cls, tag_handle: AvaTagHandle) -> Array[AvaTag]
```

X.resolve_tag_handle(tag_handle) -> Array[AvaTag]
Resolve Tag Handle

Args:
    tag_handle (AvaTagHandle): 

Returns:
    Array[AvaTag]:

<a id="unreal.AvaTransitionBehaviorActor"></a>