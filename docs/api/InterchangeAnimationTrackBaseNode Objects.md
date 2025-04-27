## InterchangeAnimationTrackBaseNode Objects

```python
class InterchangeAnimationTrackBaseNode(InterchangeBaseNode)
```

Abstract class providing the minimal services required for an animation track node.

**C++ Source:**

- **Plugin**: Interchange
- **Module**: InterchangeNodes
- **File**: InterchangeAnimationTrackSetNode.h

<a id="unreal.InterchangeAnimationTrackBaseNode.set_custom_completion_mode"></a>

#### set_custom_completion_mode

```python
def set_custom_completion_mode(attribute_value: int) -> bool
```

x.set_custom_completion_mode(attribute_value) -> bool
Set how the actor's animated property should behave once its animation completes.

Args:
    attribute_value (int32): 

Returns:
    bool:

<a id="unreal.InterchangeAnimationTrackBaseNode.get_custom_completion_mode"></a>

#### get_custom_completion_mode

```python
def get_custom_completion_mode() -> Optional[int]
```

x.get_custom_completion_mode() -> int32 or None
Get how the actor's animated property behaves once this animation is complete.
The output value will be clamped to the range of values defined in EInterchangeAimationCompletionMode.

Returns:
    int32 or None: 

    attribute_value (int32):

<a id="unreal.InterchangeAnimationTrackSetInstanceNode"></a>