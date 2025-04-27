## AnimationDataModelNotifiesExtensions Objects

```python
class AnimationDataModelNotifiesExtensions(BlueprintFunctionLibrary)
```

Animation Data Model Notifies Extensions

**C++ Source:**

- **Module**: Engine
- **File**: AnimDataNotifications.h

<a id="unreal.AnimationDataModelNotifiesExtensions.get_payload"></a>

#### get_payload

```python
@classmethod
def get_payload(cls, payload: AnimDataModelNotifPayload) -> EmptyPayload
```

X.get_payload(payload) -> EmptyPayload
Get Payload

Args:
    payload (AnimDataModelNotifPayload): 

Returns:
    EmptyPayload:

<a id="unreal.AnimationDataModelNotifiesExtensions.copy_payload"></a>

#### copy_payload

```python
@classmethod
def copy_payload(cls, payload: AnimDataModelNotifPayload,
                 expected_struct: ScriptStruct,
                 out_payload: EmptyPayload) -> EmptyPayload
```

X.copy_payload(payload, expected_struct, out_payload) -> EmptyPayload
Copy Payload

Args:
    payload (AnimDataModelNotifPayload): 
    expected_struct (ScriptStruct): 
    out_payload (EmptyPayload): 

Returns:
    EmptyPayload: 

    out_payload (EmptyPayload):

<a id="unreal.RawAnimSequenceTrackExtensions"></a>