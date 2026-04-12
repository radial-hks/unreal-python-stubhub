## AsyncAction\_ListenForAesMessage Objects

```python
class AsyncAction_ListenForAesMessage(CancellableAsyncAction)
```

Async Action Listen for Aes Message

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: AesMessageSystem
- **File**: AsyncAction_ListenForAesMessage.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``on_message_received`` (AsyncGameplayMessageDelegate):  [Read-Write] Called when a message is broadcast on the specified channel. Use GetPayload() to request the message payload.

<a id="unreal.AsyncAction_ListenForAesMessage.on_message_received"></a>

#### on\_message\_received

```python
@property
def on_message_received() -> AsyncGameplayMessageDelegate
```

(AsyncGameplayMessageDelegate):  [Read-Write] Called when a message is broadcast on the specified channel. Use GetPayload() to request the message payload.

<a id="unreal.AsyncAction_ListenForAesMessage.on_message_received"></a>

#### on\_message\_received

```python
@on_message_received.setter
def on_message_received(value: AsyncGameplayMessageDelegate) -> None
```

<a id="unreal.AesEditorCommandParams"></a>