## ApplyMaterialToEntityParams Objects

```python
class ApplyMaterialToEntityParams(ParamsBase)
```

Apply Material to Entity Params

**C++ Source:**

- **Plugin**: WdpRuntimeAPI
- **Module**: ApplicationAPI
- **File**: MaterialToolAPI.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``eid_to_new_material_info`` (Map[int64, NewMaterialsInfoArray]):  [Read-Write]
- ``guid`` (str):  [Read-Write]
- ``hit_keys`` (Set[Name]):  [Read-Write]

<a id="unreal.ApplyMaterialToEntityParams.__init__"></a>

#### \_\_init\_\_

```python
def __init__(
        eid_to_new_material_info: Map[int,
                                      NewMaterialsInfoArray] = {}) -> None
```

<a id="unreal.ApplyMaterialToEntityParams.eid_to_new_material_info"></a>

#### eid\_to\_new\_material\_info

```python
@property
def eid_to_new_material_info() -> Map[int, NewMaterialsInfoArray]
```

(Map[int64, NewMaterialsInfoArray]):  [Read-Write]

<a id="unreal.ApplyMaterialToEntityParams.eid_to_new_material_info"></a>

#### eid\_to\_new\_material\_info

```python
@eid_to_new_material_info.setter
def eid_to_new_material_info(value: Map[int, NewMaterialsInfoArray]) -> None
```

<a id="unreal.EntityMaterialSlot"></a>