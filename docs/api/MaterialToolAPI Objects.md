## MaterialToolAPI Objects

```python
class MaterialToolAPI(StandardApiClassBase)
```

Material Tool API

**C++ Source:**

- **Plugin**: WdpRuntimeAPI
- **Module**: ApplicationAPI
- **File**: MaterialToolAPI.h

<a id="unreal.MaterialToolAPI.set_entity_slots_highlight"></a>

#### set\_entity\_slots\_highlight

```python
def set_entity_slots_highlight(
        params: EntitySlotParamsArr) -> Optional[ResultBase]
```

x.set_entity_slots_highlight(params) -> ResultBase or None
Set Entity Slots Highlight

Args:
    params (EntitySlotParamsArr): 

Returns:
    ResultBase or None: 

    out_result (ResultBase):

<a id="unreal.MaterialToolAPI.get_entity_material_slots"></a>

#### get\_entity\_material\_slots

```python
def get_entity_material_slots(
        params: EidArrayParams) -> Optional[GetEntityMaterialSlotsResult]
```

x.get_entity_material_slots(params) -> GetEntityMaterialSlotsResult or None
APIs

Args:
    params (EidArrayParams): 

Returns:
    GetEntityMaterialSlotsResult or None: 

    out_result (GetEntityMaterialSlotsResult):

<a id="unreal.MaterialToolAPI.apply_material_to_entity"></a>

#### apply\_material\_to\_entity

```python
def apply_material_to_entity(
        params: ApplyMaterialToEntityParams) -> Optional[ResultBase]
```

x.apply_material_to_entity(params) -> ResultBase or None
Apply Material to Entity

Args:
    params (ApplyMaterialToEntityParams): 

Returns:
    ResultBase or None: 

    out_result (ResultBase):

<a id="unreal.WdpArrayDuplicateAPI"></a>