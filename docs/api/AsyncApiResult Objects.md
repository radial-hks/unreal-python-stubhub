## AsyncApiResult Objects

```python
class AsyncApiResult(Object)
```

Async Api Result

**C++ Source:**

- **Plugin**: WdpAPIFrame
- **Module**: WdpAPIFramework
- **File**: AsyncApiResult.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``api_name`` (str):  [Read-Only]
- ``guid`` (str):  [Read-Only]
- ``message`` (str):  [Read-Only]
- ``result_field`` (WdpJsonObjectWrapper):  [Read-Write]

<a id="unreal.AsyncApiResult.result_field"></a>

#### result\_field

```python
@property
def result_field() -> WdpJsonObjectWrapper
```

(WdpJsonObjectWrapper):  [Read-Write]

<a id="unreal.AsyncApiResult.result_field"></a>

#### result\_field

```python
@result_field.setter
def result_field(value: WdpJsonObjectWrapper) -> None
```

<a id="unreal.AsyncApiResult.to_string"></a>

#### to\_string

```python
def to_string(success: bool) -> str
```

x.to_string(success) -> str
To String

Args:
    success (bool): 

Returns:
    str:

<a id="unreal.AsyncApiResult.set_message"></a>

#### set\_message

```python
def set_message(message: str) -> None
```

x.set_message(message) -> None
Set Message

Args:
    message (str):

<a id="unreal.AsyncApiResult.mark_async_finish"></a>

#### mark\_async\_finish

```python
def mark_async_finish(success: bool) -> None
```

x.mark_async_finish(success) -> None
Mark Async Finish

Args:
    success (bool):

<a id="unreal.AsyncApiResult.is_valid"></a>

#### is\_valid

```python
def is_valid() -> bool
```

x.is_valid() -> bool
Is Valid

Returns:
    bool:

<a id="unreal.AsyncApiResult.init"></a>

#### init

```python
def init(guid: str, api_name: str, result: ResultBase) -> None
```

x.init(guid, api_name, result) -> None
Init

Args:
    guid (str): 
    api_name (str): 
    result (ResultBase):

<a id="unreal.AsyncApiResult.get_guid"></a>

#### get\_guid

```python
def get_guid() -> str
```

x.get_guid() -> str
Get Guid

Returns:
    str:

<a id="unreal.CustomBpAPIContainer"></a>