## DCPSDKResult Objects

```python
class DCPSDKResult(StructBase)
```

DCPSDKResult

**C++ Source:**

- **Plugin**: WdpAssetLoader
- **Module**: BimAssetLoader
- **File**: DCPDataBase.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``msg`` (str):  [Read-Write]
- ``success`` (bool):  [Read-Write]

<a id="unreal.DCPSDKResult.__init__"></a>

#### \_\_init\_\_

```python
def __init__(success: bool = False, msg: str = "") -> None
```

<a id="unreal.DCPSDKResult.success"></a>

#### success

```python
@property
def success() -> bool
```

(bool):  [Read-Write]

<a id="unreal.DCPSDKResult.success"></a>

#### success

```python
@success.setter
def success(value: bool) -> None
```

<a id="unreal.DCPSDKResult.msg"></a>

#### msg

```python
@property
def msg() -> str
```

(str):  [Read-Write]

<a id="unreal.DCPSDKResult.msg"></a>

#### msg

```python
@msg.setter
def msg(value: str) -> None
```

<a id="unreal.BimSnapResult"></a>