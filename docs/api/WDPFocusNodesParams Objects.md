## WDPFocusNodesParams Objects

```python
class WDPFocusNodesParams(ParamsBase)
```

WDPFocus Nodes Params

**C++ Source:**

- **Plugin**: WdpRuntimeAPI
- **Module**: ApplicationAPI
- **File**: WdpCameraControlAPIParamsDefine.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``distance_factor`` (float):  [Read-Write]
- ``eid`` (int64):  [Read-Write]
- ``fly_time`` (float):  [Read-Write]
- ``guid`` (str):  [Read-Write]
- ``hit_keys`` (Set[Name]):  [Read-Write]
- ``node_ids`` (Array[int32]):  [Read-Write]
- ``rotation`` (CameraPresetRotator):  [Read-Write]

<a id="unreal.WDPFocusNodesParams.__init__"></a>

#### \_\_init\_\_

```python
def __init__(eid: int = 0,
             node_ids: Array[int] = [],
             rotation: CameraPresetRotator = [0.000000, 0.000000],
             distance_factor: float = 0.000000,
             fly_time: float = 0.000000) -> None
```

<a id="unreal.WDPFocusNodesParams.eid"></a>

#### eid

```python
@property
def eid() -> int
```

(int64):  [Read-Write]

<a id="unreal.WDPFocusNodesParams.eid"></a>

#### eid

```python
@eid.setter
def eid(value: int) -> None
```

<a id="unreal.WDPFocusNodesParams.node_ids"></a>

#### node\_ids

```python
@property
def node_ids() -> Array[int]
```

(Array[int32]):  [Read-Write]

<a id="unreal.WDPFocusNodesParams.node_ids"></a>

#### node\_ids

```python
@node_ids.setter
def node_ids(value: Array[int]) -> None
```

<a id="unreal.WDPFocusNodesParams.rotation"></a>

#### rotation

```python
@property
def rotation() -> CameraPresetRotator
```

(CameraPresetRotator):  [Read-Write]

<a id="unreal.WDPFocusNodesParams.rotation"></a>

#### rotation

```python
@rotation.setter
def rotation(value: CameraPresetRotator) -> None
```

<a id="unreal.WDPFocusNodesParams.distance_factor"></a>

#### distance\_factor

```python
@property
def distance_factor() -> float
```

(float):  [Read-Write]

<a id="unreal.WDPFocusNodesParams.distance_factor"></a>

#### distance\_factor

```python
@distance_factor.setter
def distance_factor(value: float) -> None
```

<a id="unreal.WDPFocusNodesParams.fly_time"></a>

#### fly\_time

```python
@property
def fly_time() -> float
```

(float):  [Read-Write]

<a id="unreal.WDPFocusNodesParams.fly_time"></a>

#### fly\_time

```python
@fly_time.setter
def fly_time(value: float) -> None
```

<a id="unreal.WDPFollowEntityParams"></a>