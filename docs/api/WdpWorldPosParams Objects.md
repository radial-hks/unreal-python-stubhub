## WdpWorldPosParams Objects

```python
class WdpWorldPosParams(ParamsBase)
```

Wdp World Pos Params

**C++ Source:**

- **Plugin**: WdpRuntimeAPI
- **Module**: ApplicationAPI
- **File**: ApplicationAPIParamsDefine.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``guid`` (str):  [Read-Write]
- ``hit_keys`` (Set[Name]):  [Read-Write]
- ``world_pos`` (Vector):  [Read-Write]

<a id="unreal.WdpWorldPosParams.__init__"></a>

#### \_\_init\_\_

```python
def __init__(world_pos: Vector = [0.000000, 0.000000, 0.000000]) -> None
```

<a id="unreal.WdpWorldPosParams.world_pos"></a>

#### world\_pos

```python
@property
def world_pos() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.WdpWorldPosParams.world_pos"></a>

#### world\_pos

```python
@world_pos.setter
def world_pos(value: Vector) -> None
```

<a id="unreal.WdpScreenPosResult"></a>