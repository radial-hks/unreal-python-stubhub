## ResultBase Objects

```python
class ResultBase(StructBase)
```

Result Base

**C++ Source:**

- **Plugin**: WdpAPIFrame
- **Module**: WdpAPIFramework
- **File**: ApiResultBase.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``message`` (str):  [Read-Write]
- ``scene_change_info`` (WdpSceneChangeInfo):  [Read-Write]
- ``success`` (bool):  [Read-Write]

<a id="unreal.ResultBase.__init__"></a>

#### \_\_init\_\_

```python
def __init__(message: str = "",
             scene_change_info: WdpSceneChangeInfo = [[], [], []],
             success: bool = False) -> None
```

<a id="unreal.ResultBase.message"></a>

#### message

```python
@property
def message() -> str
```

(str):  [Read-Write]

<a id="unreal.ResultBase.message"></a>

#### message

```python
@message.setter
def message(value: str) -> None
```

<a id="unreal.ResultBase.scene_change_info"></a>

#### scene\_change\_info

```python
@property
def scene_change_info() -> WdpSceneChangeInfo
```

(WdpSceneChangeInfo):  [Read-Write]

<a id="unreal.ResultBase.scene_change_info"></a>

#### scene\_change\_info

```python
@scene_change_info.setter
def scene_change_info(value: WdpSceneChangeInfo) -> None
```

<a id="unreal.ResultBase.success"></a>

#### success

```python
@property
def success() -> bool
```

(bool):  [Read-Write]

<a id="unreal.ResultBase.success"></a>

#### success

```python
@success.setter
def success(value: bool) -> None
```

<a id="unreal.EidResult"></a>