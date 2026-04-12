## DCPRoomHighLightParam Objects

```python
class DCPRoomHighLightParam(ParamsBase)
```

DCPRoom High Light Param

**C++ Source:**

- **Plugin**: WdpAssetAPI
- **Module**: DcpAPI
- **File**: DCPNodeAPIParams.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``can_be_occluded`` (bool):  [Read-Write]
- ``color`` (str):  [Read-Write]
- ``guid`` (str):  [Read-Write]
- ``hit_keys`` (Set[Name]):  [Read-Write]
- ``is_visible`` (bool):  [Read-Write]
- ``opacity`` (float):  [Read-Write]
- ``room_ids`` (Array[int32]):  [Read-Write]

<a id="unreal.DCPRoomHighLightParam.__init__"></a>

#### \_\_init\_\_

```python
def __init__(room_ids: Array[int] = [],
             is_visible: bool = False,
             color: str = "",
             opacity: float = 0.000000,
             can_be_occluded: bool = False) -> None
```

<a id="unreal.DCPRoomHighLightParam.room_ids"></a>

#### room\_ids

```python
@property
def room_ids() -> Array[int]
```

(Array[int32]):  [Read-Write]

<a id="unreal.DCPRoomHighLightParam.room_ids"></a>

#### room\_ids

```python
@room_ids.setter
def room_ids(value: Array[int]) -> None
```

<a id="unreal.DCPRoomHighLightParam.is_visible"></a>

#### is\_visible

```python
@property
def is_visible() -> bool
```

(bool):  [Read-Write]

<a id="unreal.DCPRoomHighLightParam.is_visible"></a>

#### is\_visible

```python
@is_visible.setter
def is_visible(value: bool) -> None
```

<a id="unreal.DCPRoomHighLightParam.color"></a>

#### color

```python
@property
def color() -> str
```

(str):  [Read-Write]

<a id="unreal.DCPRoomHighLightParam.color"></a>

#### color

```python
@color.setter
def color(value: str) -> None
```

<a id="unreal.DCPRoomHighLightParam.opacity"></a>

#### opacity

```python
@property
def opacity() -> float
```

(float):  [Read-Write]

<a id="unreal.DCPRoomHighLightParam.opacity"></a>

#### opacity

```python
@opacity.setter
def opacity(value: float) -> None
```

<a id="unreal.DCPRoomHighLightParam.can_be_occluded"></a>

#### can\_be\_occluded

```python
@property
def can_be_occluded() -> bool
```

(bool):  [Read-Write]

<a id="unreal.DCPRoomHighLightParam.can_be_occluded"></a>

#### can\_be\_occluded

```python
@can_be_occluded.setter
def can_be_occluded(value: bool) -> None
```

<a id="unreal.DCPRoomFocusParam"></a>