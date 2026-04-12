## LightOC\_MPC Objects

```python
class LightOC_MPC(StructBase)
```

Light OC MPC

**C++ Source:**

- **Plugin**: SkyCreatorPlugin
- **Module**: SkyCreatorPlugin
- **File**: TOD_Base.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``close_light_interval`` (float):  [Read-Write]
- ``close_light_mpc`` (MatCollectionSetting_Array):  [Read-Write] 根据日出时间提前（负值）或延后（正值）设置材质参数集参数，0代表日出就立刻设置
- ``open_light_interval`` (float):  [Read-Write]
- ``open_light_mpc`` (MatCollectionSetting_Array):  [Read-Write] 根据日落时间提前（负值）或延后（正值）设置材质参数集参数，0代表日落就立刻设置

<a id="unreal.LightOC_MPC.__init__"></a>

#### \_\_init\_\_

```python
def __init__(close_light_interval: float = 0.000000,
             open_light_interval: float = 0.000000,
             close_light_mpc: MatCollectionSetting_Array = [[]],
             open_light_mpc: MatCollectionSetting_Array = [[]]) -> None
```

<a id="unreal.LightOC_MPC.close_light_interval"></a>

#### close\_light\_interval

```python
@property
def close_light_interval() -> float
```

(float):  [Read-Write]

<a id="unreal.LightOC_MPC.close_light_interval"></a>

#### close\_light\_interval

```python
@close_light_interval.setter
def close_light_interval(value: float) -> None
```

<a id="unreal.LightOC_MPC.open_light_interval"></a>

#### open\_light\_interval

```python
@property
def open_light_interval() -> float
```

(float):  [Read-Write]

<a id="unreal.LightOC_MPC.open_light_interval"></a>

#### open\_light\_interval

```python
@open_light_interval.setter
def open_light_interval(value: float) -> None
```

<a id="unreal.LightOC_MPC.close_light_mpc"></a>

#### close\_light\_mpc

```python
@property
def close_light_mpc() -> MatCollectionSetting_Array
```

(MatCollectionSetting_Array):  [Read-Write] 根据日出时间提前（负值）或延后（正值）设置材质参数集参数，0代表日出就立刻设置

<a id="unreal.LightOC_MPC.close_light_mpc"></a>

#### close\_light\_mpc

```python
@close_light_mpc.setter
def close_light_mpc(value: MatCollectionSetting_Array) -> None
```

<a id="unreal.LightOC_MPC.open_light_mpc"></a>

#### open\_light\_mpc

```python
@property
def open_light_mpc() -> MatCollectionSetting_Array
```

(MatCollectionSetting_Array):  [Read-Write] 根据日落时间提前（负值）或延后（正值）设置材质参数集参数，0代表日落就立刻设置

<a id="unreal.LightOC_MPC.open_light_mpc"></a>

#### open\_light\_mpc

```python
@open_light_mpc.setter
def open_light_mpc(value: MatCollectionSetting_Array) -> None
```

<a id="unreal.SkyCreatorNiagaraParameters"></a>