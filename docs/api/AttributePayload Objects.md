## AttributePayload Objects

```python
class AttributePayload(EmptyPayload)
```

Attribute Payload

**C++ Source:**

- **Module**: Engine
- **File**: AnimDataNotifications.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``identifier`` (AnimationAttributeIdentifier):  [Read-Write] Identifier of the attribute

<a id="unreal.AttributePayload.__init__"></a>

#### __init__

```python
def __init__(
    identifier: AnimationAttributeIdentifier = [
        "None", "None", -1, None, [""]
    ]
) -> None
```

<a id="unreal.AttributePayload.identifier"></a>

#### identifier

```python
@property
def identifier() -> AnimationAttributeIdentifier
```

(AnimationAttributeIdentifier):  [Read-Only] Identifier of the attribute

<a id="unreal.AnimationAttributeIdentifier"></a>