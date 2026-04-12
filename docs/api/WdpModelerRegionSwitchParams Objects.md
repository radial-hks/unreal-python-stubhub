## WdpModelerRegionSwitchParams Objects

```python
class WdpModelerRegionSwitchParams(EidParams)
```

Wdp Modeler Region Switch Params

**C++ Source:**

- **Plugin**: AesRuntimeModeler
- **Module**: RuntimeModelerAPI
- **File**: WdpModelerAPI.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``eid`` (Eid):  [Read-Write]
- ``guid`` (str):  [Read-Write]
- ``hit_keys`` (Set[Name]):  [Read-Write]
- ``index_and_switch_array`` (Array[ModelerRegionSwitch]):  [Read-Write]

<a id="unreal.WdpModelerRegionSwitchParams.__init__"></a>

#### \_\_init\_\_

```python
def __init__(index_and_switch_array: Array[ModelerRegionSwitch] = []) -> None
```

<a id="unreal.WdpModelerRegionSwitchParams.index_and_switch_array"></a>

#### index\_and\_switch\_array

```python
@property
def index_and_switch_array() -> Array[ModelerRegionSwitch]
```

(Array[ModelerRegionSwitch]):  [Read-Write]

<a id="unreal.WdpModelerRegionSwitchParams.index_and_switch_array"></a>

#### index\_and\_switch\_array

```python
@index_and_switch_array.setter
def index_and_switch_array(value: Array[ModelerRegionSwitch]) -> None
```

<a id="unreal.WdpModelerRegionResult"></a>