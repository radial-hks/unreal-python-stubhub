## AsyncGameplayMessageDelegate Objects

```python
class AsyncGameplayMessageDelegate(MulticastDelegateBase)
```

Proxy object pin will be hidden in K2Node_GameplayMessageAsyncAction. Is used to get a reference to the object triggering the delegate for the follow up call of 'GetPayload'.

Args:
    proxy_object (AsyncAction_ListenForAesMessage): 
    actual_channel (GameplayTag): The actual message channel that we received Payload from (will always start with Channel, but may be more specific if partial matches were enabled)

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: AesMessageSystem
- **File**: AsyncAction_ListenForAesMessage.h

<a id="unreal.AsyncGameplayMessageDelegate.__init__"></a>

#### \_\_init\_\_

```python
def __init__(*args: Any, **kwargs: Any) -> None
```

<a id="unreal.AesBuildingPropertyChangedEvent"></a>