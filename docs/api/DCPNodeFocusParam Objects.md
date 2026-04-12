## DCPNodeFocusParam Objects

```python
class DCPNodeFocusParam(DCPNodeBaseParam)
```

DCPNode Focus Param

**C++ Source:**

- **Plugin**: WdpAssetAPI
- **Module**: DcpAPI
- **File**: DCPNodeAPIParams.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``camera_params`` (DCPFocusCameraParams):  [Read-Write]
- ``guid`` (str):  [Read-Write]
- ``hit_keys`` (Set[Name]):  [Read-Write]
- ``node_id`` (int32):  [Read-Write]

<a id="unreal.DCPNodeFocusParam.__init__"></a>

#### \_\_init\_\_

```python
def __init__(
    node_id: int = 0,
    camera_params: DCPFocusCameraParams = [[-30.000000, 0.000000], 1.000000,
                                           1.000000]
) -> None
```

<a id="unreal.DCPNodeFocusParam.camera_params"></a>

#### camera\_params

```python
@property
def camera_params() -> DCPFocusCameraParams
```

(DCPFocusCameraParams):  [Read-Write]

<a id="unreal.DCPNodeFocusParam.camera_params"></a>

#### camera\_params

```python
@camera_params.setter
def camera_params(value: DCPFocusCameraParams) -> None
```

<a id="unreal.DCPNodeHightLightParam"></a>