## LocalizableMessageLibrary Objects

```python
class LocalizableMessageLibrary(BlueprintFunctionLibrary)
```

BlueprintFunctionLibrary for LocalizableMessage

**C++ Source:**

- **Plugin**: LocalizableMessage
- **Module**: LocalizableMessageBlueprint
- **File**: LocalizableMessageLibrary.h

<a id="unreal.LocalizableMessageLibrary.reset_localizable_message"></a>

#### reset\_localizable\_message

```python
@classmethod
def reset_localizable_message(
        cls, message: LocalizableMessage) -> LocalizableMessage
```

X.reset_localizable_message(message) -> LocalizableMessage
Resets the Localizable Message

Args:
    message (LocalizableMessage): 

Returns:
    LocalizableMessage: 

    message (LocalizableMessage):

<a id="unreal.LocalizableMessageLibrary.is_empty_localizable_message"></a>

#### is\_empty\_localizable\_message

```python
@classmethod
def is_empty_localizable_message(cls, message: LocalizableMessage) -> bool
```

X.is_empty_localizable_message(message) -> bool
Returns true if the message is empty

Args:
    message (LocalizableMessage): 

Returns:
    bool:

<a id="unreal.LocalizableMessageLibrary.conv_localizable_message_to_text"></a>

#### conv\_localizable\_message\_to\_text

```python
@classmethod
def conv_localizable_message_to_text(cls, world_context_object: Object,
                                     message: LocalizableMessage) -> Text
```

X.conv_localizable_message_to_text(world_context_object, message) -> Text
Conversion function from LocalizableMessage to FText.

Args:
    world_context_object (Object): 
    message (LocalizableMessage): 

Returns:
    Text:

<a id="unreal.Text3DActor"></a>