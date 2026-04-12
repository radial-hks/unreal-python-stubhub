## DCPNodePropertyResult Objects

```python
class DCPNodePropertyResult(ResultBase)
```

DCPNode Property Result

**C++ Source:**

- **Plugin**: WdpAssetAPI
- **Module**: DcpAPI
- **File**: DCPNodeAPIParams.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``lable`` (str):  [Read-Write]
- ``message`` (str):  [Read-Write]
- ``name`` (str):  [Read-Write]
- ``scene_change_info`` (WdpSceneChangeInfo):  [Read-Write]
- ``success`` (bool):  [Read-Write]
- ``value`` (str):  [Read-Write]

<a id="unreal.DCPNodePropertyResult.__init__"></a>

#### \_\_init\_\_

```python
def __init__(message: str = "",
             scene_change_info: WdpSceneChangeInfo = [[], [], []],
             success: bool = False,
             name: str = "",
             lable: str = "",
             value: str = "") -> None
```

<a id="unreal.DCPNodePropertyResult.name"></a>

#### name

```python
@property
def name() -> str
```

(str):  [Read-Write]

<a id="unreal.DCPNodePropertyResult.name"></a>

#### name

```python
@name.setter
def name(value: str) -> None
```

<a id="unreal.DCPNodePropertyResult.lable"></a>

#### lable

```python
@property
def lable() -> str
```

(str):  [Read-Write]

<a id="unreal.DCPNodePropertyResult.lable"></a>

#### lable

```python
@lable.setter
def lable(value: str) -> None
```

<a id="unreal.DCPNodePropertyResult.value"></a>

#### value

```python
@property
def value() -> str
```

(str):  [Read-Write]

<a id="unreal.DCPNodePropertyResult.value"></a>

#### value

```python
@value.setter
def value(value: str) -> None
```

<a id="unreal.DCPNodeTransformResult"></a>