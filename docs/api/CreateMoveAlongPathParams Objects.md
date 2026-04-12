## CreateMoveAlongPathParams Objects

```python
class CreateMoveAlongPathParams(ParamsBase)
```

Create Move Along Path Params

**C++ Source:**

- **Plugin**: CoveringAPI
- **Module**: CoveringAPIDefine
- **File**: CoveringBoundAPI.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``guid`` (str):  [Read-Write]
- ``hit_keys`` (Set[Name]):  [Read-Write]
- ``loop`` (bool):  [Read-Write]
- ``moving_eid`` (str):  [Read-Write]
- ``path_eid`` (str):  [Read-Write]
- ``reverse`` (bool):  [Read-Write]
- ``speed`` (float):  [Read-Write]

<a id="unreal.CreateMoveAlongPathParams.__init__"></a>

#### \_\_init\_\_

```python
def __init__(moving_eid: str = "",
             path_eid: str = "",
             speed: float = 0.000000,
             loop: bool = False,
             reverse: bool = False) -> None
```

<a id="unreal.CreateMoveAlongPathParams.moving_eid"></a>

#### moving\_eid

```python
@property
def moving_eid() -> str
```

(str):  [Read-Write]

<a id="unreal.CreateMoveAlongPathParams.moving_eid"></a>

#### moving\_eid

```python
@moving_eid.setter
def moving_eid(value: str) -> None
```

<a id="unreal.CreateMoveAlongPathParams.path_eid"></a>

#### path\_eid

```python
@property
def path_eid() -> str
```

(str):  [Read-Write]

<a id="unreal.CreateMoveAlongPathParams.path_eid"></a>

#### path\_eid

```python
@path_eid.setter
def path_eid(value: str) -> None
```

<a id="unreal.CreateMoveAlongPathParams.speed"></a>

#### speed

```python
@property
def speed() -> float
```

(float):  [Read-Write]

<a id="unreal.CreateMoveAlongPathParams.speed"></a>

#### speed

```python
@speed.setter
def speed(value: float) -> None
```

<a id="unreal.CreateMoveAlongPathParams.loop"></a>

#### loop

```python
@property
def loop() -> bool
```

(bool):  [Read-Write]

<a id="unreal.CreateMoveAlongPathParams.loop"></a>

#### loop

```python
@loop.setter
def loop(value: bool) -> None
```

<a id="unreal.CreateMoveAlongPathParams.reverse"></a>

#### reverse

```python
@property
def reverse() -> bool
```

(bool):  [Read-Write]

<a id="unreal.CreateMoveAlongPathParams.reverse"></a>

#### reverse

```python
@reverse.setter
def reverse(value: bool) -> None
```

<a id="unreal.GetMoveAlongPathParams"></a>