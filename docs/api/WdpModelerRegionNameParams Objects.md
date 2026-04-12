## WdpModelerRegionNameParams Objects

```python
class WdpModelerRegionNameParams(EidParams)
```

Wdp Modeler Region Name Params

**C++ Source:**

- **Plugin**: AesRuntimeModeler
- **Module**: RuntimeModelerAPI
- **File**: WdpModelerAPI.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``eid`` (Eid):  [Read-Write]
- ``guid`` (str):  [Read-Write]
- ``hit_keys`` (Set[Name]):  [Read-Write]
- ``index_and_name_array`` (Array[ModelerRegionName]):  [Read-Write]

<a id="unreal.WdpModelerRegionNameParams.__init__"></a>

#### \_\_init\_\_

```python
def __init__(index_and_name_array: Array[ModelerRegionName] = []) -> None
```

<a id="unreal.WdpModelerRegionNameParams.index_and_name_array"></a>

#### index\_and\_name\_array

```python
@property
def index_and_name_array() -> Array[ModelerRegionName]
```

(Array[ModelerRegionName]):  [Read-Write]

<a id="unreal.WdpModelerRegionNameParams.index_and_name_array"></a>

#### index\_and\_name\_array

```python
@index_and_name_array.setter
def index_and_name_array(value: Array[ModelerRegionName]) -> None
```

<a id="unreal.WdpModelerRegionSwitchParams"></a>