## DCPNodeHighLightStyleGetParam Objects

```python
class DCPNodeHighLightStyleGetParam(ResultBase)
```

DCPNode High Light Style Get Param

**C++ Source:**

- **Plugin**: WdpAssetAPI
- **Module**: DcpAPI
- **File**: DCPNodeAPIParams.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``can_be_occluded`` (bool):  [Read-Write]
- ``color`` (str):  [Read-Write]
- ``message`` (str):  [Read-Write]
- ``opacity`` (float):  [Read-Write]
- ``opacity_scale`` (float):  [Read-Write]
- ``scene_change_info`` (WdpSceneChangeInfo):  [Read-Write]
- ``success`` (bool):  [Read-Write]

<a id="unreal.DCPNodeHighLightStyleGetParam.__init__"></a>

#### \_\_init\_\_

```python
def __init__(message: str = "",
             scene_change_info: WdpSceneChangeInfo = [[], [], []],
             success: bool = False,
             color: str = "",
             opacity: float = 0.000000,
             opacity_scale: float = 0.000000,
             can_be_occluded: bool = False) -> None
```

<a id="unreal.DCPNodeHighLightStyleGetParam.color"></a>

#### color

```python
@property
def color() -> str
```

(str):  [Read-Write]

<a id="unreal.DCPNodeHighLightStyleGetParam.color"></a>

#### color

```python
@color.setter
def color(value: str) -> None
```

<a id="unreal.DCPNodeHighLightStyleGetParam.opacity"></a>

#### opacity

```python
@property
def opacity() -> float
```

(float):  [Read-Write]

<a id="unreal.DCPNodeHighLightStyleGetParam.opacity"></a>

#### opacity

```python
@opacity.setter
def opacity(value: float) -> None
```

<a id="unreal.DCPNodeHighLightStyleGetParam.opacity_scale"></a>

#### opacity\_scale

```python
@property
def opacity_scale() -> float
```

(float):  [Read-Write]

<a id="unreal.DCPNodeHighLightStyleGetParam.opacity_scale"></a>

#### opacity\_scale

```python
@opacity_scale.setter
def opacity_scale(value: float) -> None
```

<a id="unreal.DCPNodeHighLightStyleGetParam.can_be_occluded"></a>

#### can\_be\_occluded

```python
@property
def can_be_occluded() -> bool
```

(bool):  [Read-Write]

<a id="unreal.DCPNodeHighLightStyleGetParam.can_be_occluded"></a>

#### can\_be\_occluded

```python
@can_be_occluded.setter
def can_be_occluded(value: bool) -> None
```

<a id="unreal.DCPNodeBaseParam"></a>