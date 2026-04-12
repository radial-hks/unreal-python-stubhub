## ApiClassBase Objects

```python
class ApiClassBase(Object)
```

Api Class Base

**C++ Source:**

- **Plugin**: WdpAPIFrame
- **Module**: WdpAPIFramework
- **File**: RuntimeAPIClassBase.h

<a id="unreal.ApiClassBase.should_enable_api"></a>

#### should\_enable\_api

```python
def should_enable_api() -> bool
```

x.should_enable_api() -> bool

brief: 是否Enable此API Class中的接口，为true则此Class中API才会生效

Returns:
    bool:

<a id="unreal.ApiClassBase.send_message_to_web"></a>

#### send\_message\_to\_web

```python
def send_message_to_web(message: str) -> None
```

x.send_message_to_web(message) -> None
Send Message to Web

Args:
    message (str):

<a id="unreal.ApiClassBase.on_reset_api_state"></a>

#### on\_reset\_api\_state

```python
def on_reset_api_state() -> bool
```

x.on_reset_api_state() -> bool
On Reset Api State

Returns:
    bool:

<a id="unreal.ApiClassBase.on_record_api_state"></a>

#### on\_record\_api\_state

```python
def on_record_api_state() -> bool
```

x.on_record_api_state() -> bool
On Record Api State

Returns:
    bool:

<a id="unreal.ApiClassBase.get_api_class_name"></a>

#### get\_api\_class\_name

```python
def get_api_class_name() -> Name
```

x.get_api_class_name() -> Name

brief: API Module全局唯一的Name，不可与其他插件的Name重复，建议使用Class Name 即可

Returns:
    Name:

<a id="unreal.ApiClassBase.get_api_category_name"></a>

#### get\_api\_category\_name

```python
def get_api_category_name() -> WdpCategory
```

x.get_api_category_name() -> WdpCategory

brief: API Module全局唯一的Name，不可与其他插件的Name重复，建议使用Class Name 即可

Returns:
    WdpCategory:

<a id="unreal.StandardApiClassBase"></a>