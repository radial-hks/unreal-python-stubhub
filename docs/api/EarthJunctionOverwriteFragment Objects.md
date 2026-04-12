## EarthJunctionOverwriteFragment Objects

```python
class EarthJunctionOverwriteFragment(EarthPropertyFragment)
```

Earth Junction Overwrite Fragment

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: EarthPrefab
- **File**: EarthRoadFragment.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``junction_connection_infos`` (Array[EarthJunctionConnectionInfo]):  [Read-Write] 道路连接关系
- ``valid`` (bool):  [Read-Write] 数据片段是否有效
- ``validated`` (bool):  [Read-Write] 是否已执行数据有效性验证

<a id="unreal.EarthJunctionOverwriteFragment.__init__"></a>

#### \_\_init\_\_

```python
def __init__(
    validated: bool = False,
    valid: bool = False,
    junction_connection_infos: Array[EarthJunctionConnectionInfo] = []
) -> None
```

<a id="unreal.EarthJunctionOverwriteFragment.junction_connection_infos"></a>

#### junction\_connection\_infos

```python
@property
def junction_connection_infos() -> Array[EarthJunctionConnectionInfo]
```

(Array[EarthJunctionConnectionInfo]):  [Read-Write] 道路连接关系

<a id="unreal.EarthJunctionOverwriteFragment.junction_connection_infos"></a>

#### junction\_connection\_infos

```python
@junction_connection_infos.setter
def junction_connection_infos(
        value: Array[EarthJunctionConnectionInfo]) -> None
```

<a id="unreal.EarthRoadJunctionFragment"></a>