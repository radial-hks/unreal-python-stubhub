## DCPRoomFocusParam Objects

```python
class DCPRoomFocusParam(ParamsBase)
```

DCPRoom Focus Param

**C++ Source:**

- **Plugin**: WdpAssetAPI
- **Module**: DcpAPI
- **File**: DCPNodeAPIParams.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``camera_params`` (DCPFocusCameraParams):  [Read-Write]
- ``guid`` (str):  [Read-Write]
- ``hit_keys`` (Set[Name]):  [Read-Write]
- ``room_ids`` (Array[int32]):  [Read-Write]

<a id="unreal.DCPRoomFocusParam.__init__"></a>

#### \_\_init\_\_

```python
def __init__(
    room_ids: Array[int] = [],
    camera_params: DCPFocusCameraParams = [[-30.000000, 0.000000], 1.000000,
                                           1.000000]
) -> None
```

<a id="unreal.DCPRoomFocusParam.room_ids"></a>

#### room\_ids

```python
@property
def room_ids() -> Array[int]
```

(Array[int32]):  [Read-Write]

<a id="unreal.DCPRoomFocusParam.room_ids"></a>

#### room\_ids

```python
@room_ids.setter
def room_ids(value: Array[int]) -> None
```

<a id="unreal.DCPRoomFocusParam.camera_params"></a>

#### camera\_params

```python
@property
def camera_params() -> DCPFocusCameraParams
```

(DCPFocusCameraParams):  [Read-Write]

<a id="unreal.DCPRoomFocusParam.camera_params"></a>

#### camera\_params

```python
@camera_params.setter
def camera_params(value: DCPFocusCameraParams) -> None
```

<a id="unreal.DCPNodeLocationParam"></a>