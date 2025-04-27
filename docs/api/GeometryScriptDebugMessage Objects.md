## GeometryScriptDebugMessage Objects

```python
class GeometryScriptDebugMessage(StructBase)
```

Geometry Script Debug Message

**C++ Source:**

- **Plugin**: GeometryScripting
- **Module**: GeometryScriptingCore
- **File**: GeometryScriptTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``error_type`` (GeometryScriptErrorType):  [Read-Write]
- ``message`` (Text):  [Read-Write]
- ``message_type`` (GeometryScriptDebugMessageType):  [Read-Write]

<a id="unreal.GeometryScriptDebugMessage.__init__"></a>

#### __init__

```python
def __init__(
        message_type:
    GeometryScriptDebugMessageType = GeometryScriptDebugMessageType.
    ERROR_MESSAGE,
        error_type: GeometryScriptErrorType = GeometryScriptErrorType.NO_ERROR,
        message: Text = "") -> None
```

<a id="unreal.GeometryScriptDebugMessage.message_type"></a>

#### message_type

```python
@property
def message_type() -> GeometryScriptDebugMessageType
```

(GeometryScriptDebugMessageType):  [Read-Write]

<a id="unreal.GeometryScriptDebugMessage.message_type"></a>

#### message_type

```python
@message_type.setter
def message_type(value: GeometryScriptDebugMessageType) -> None
```

<a id="unreal.GeometryScriptDebugMessage.error_type"></a>

#### error_type

```python
@property
def error_type() -> GeometryScriptErrorType
```

(GeometryScriptErrorType):  [Read-Write]

<a id="unreal.GeometryScriptDebugMessage.error_type"></a>

#### error_type

```python
@error_type.setter
def error_type(value: GeometryScriptErrorType) -> None
```

<a id="unreal.GeometryScriptDebugMessage.message"></a>

#### message

```python
@property
def message() -> Text
```

(Text):  [Read-Write]

<a id="unreal.GeometryScriptDebugMessage.message"></a>

#### message

```python
@message.setter
def message(value: Text) -> None
```

<a id="unreal.GeometryScriptCollisionFromMeshOptions"></a>