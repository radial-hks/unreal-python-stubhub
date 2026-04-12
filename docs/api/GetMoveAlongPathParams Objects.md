## GetMoveAlongPathParams Objects

```python
class GetMoveAlongPathParams(ResultBase)
```

Get Move Along Path Params

**C++ Source:**

- **Plugin**: CoveringAPI
- **Module**: CoveringAPIDefine
- **File**: CoveringBoundAPI.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``loop`` (bool):  [Read-Write]
- ``message`` (str):  [Read-Write]
- ``moving_eid`` (str):  [Read-Write]
- ``path_eid`` (str):  [Read-Write]
- ``reverse`` (bool):  [Read-Write]
- ``scene_change_info`` (WdpSceneChangeInfo):  [Read-Write]
- ``speed`` (float):  [Read-Write]
- ``success`` (bool):  [Read-Write]

<a id="unreal.GetMoveAlongPathParams.__init__"></a>

#### \_\_init\_\_

```python
def __init__(message: str = "",
             scene_change_info: WdpSceneChangeInfo = [[], [], []],
             success: bool = False,
             moving_eid: str = "",
             path_eid: str = "",
             speed: float = 0.000000,
             loop: bool = False,
             reverse: bool = False) -> None
```

<a id="unreal.GetMoveAlongPathParams.moving_eid"></a>

#### moving\_eid

```python
@property
def moving_eid() -> str
```

(str):  [Read-Write]

<a id="unreal.GetMoveAlongPathParams.moving_eid"></a>

#### moving\_eid

```python
@moving_eid.setter
def moving_eid(value: str) -> None
```

<a id="unreal.GetMoveAlongPathParams.path_eid"></a>

#### path\_eid

```python
@property
def path_eid() -> str
```

(str):  [Read-Write]

<a id="unreal.GetMoveAlongPathParams.path_eid"></a>

#### path\_eid

```python
@path_eid.setter
def path_eid(value: str) -> None
```

<a id="unreal.GetMoveAlongPathParams.speed"></a>

#### speed

```python
@property
def speed() -> float
```

(float):  [Read-Write]

<a id="unreal.GetMoveAlongPathParams.speed"></a>

#### speed

```python
@speed.setter
def speed(value: float) -> None
```

<a id="unreal.GetMoveAlongPathParams.loop"></a>

#### loop

```python
@property
def loop() -> bool
```

(bool):  [Read-Write]

<a id="unreal.GetMoveAlongPathParams.loop"></a>

#### loop

```python
@loop.setter
def loop(value: bool) -> None
```

<a id="unreal.GetMoveAlongPathParams.reverse"></a>

#### reverse

```python
@property
def reverse() -> bool
```

(bool):  [Read-Write]

<a id="unreal.GetMoveAlongPathParams.reverse"></a>

#### reverse

```python
@reverse.setter
def reverse(value: bool) -> None
```

<a id="unreal.CreateMoveAlongPathParams_Batch"></a>