## ComponentTrParams Objects

```python
class ComponentTrParams(EidParams)
```

Component Tr Params

**C++ Source:**

- **Plugin**: WdpRuntimeAPI
- **Module**: ApplicationAPI
- **File**: WdpInstanceEntityAPI.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``component_name_to_transform`` (Map[str, ComponentTr]):  [Read-Write]
- ``eid`` (Eid):  [Read-Write]
- ``guid`` (str):  [Read-Write]
- ``hit_keys`` (Set[Name]):  [Read-Write]

<a id="unreal.ComponentTrParams.__init__"></a>

#### \_\_init\_\_

```python
def __init__(component_name_to_transform: Map[str, ComponentTr] = {}) -> None
```

<a id="unreal.ComponentTrParams.component_name_to_transform"></a>

#### component\_name\_to\_transform

```python
@property
def component_name_to_transform() -> Map[str, ComponentTr]
```

(Map[str, ComponentTr]):  [Read-Write]

<a id="unreal.ComponentTrParams.component_name_to_transform"></a>

#### component\_name\_to\_transform

```python
@component_name_to_transform.setter
def component_name_to_transform(value: Map[str, ComponentTr]) -> None
```

<a id="unreal.NodesTrInfo"></a>