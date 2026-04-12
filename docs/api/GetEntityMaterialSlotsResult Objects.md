## GetEntityMaterialSlotsResult Objects

```python
class GetEntityMaterialSlotsResult(ResultBase)
```

Get Entity Material Slots Result

**C++ Source:**

- **Plugin**: WdpRuntimeAPI
- **Module**: ApplicationAPI
- **File**: MaterialToolAPI.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``eid_to_material_slots`` (Map[int64, EntityMaterialSlots]):  [Read-Write]
- ``message`` (str):  [Read-Write]
- ``scene_change_info`` (WdpSceneChangeInfo):  [Read-Write]
- ``success`` (bool):  [Read-Write]

<a id="unreal.GetEntityMaterialSlotsResult.__init__"></a>

#### \_\_init\_\_

```python
def __init__(
        message: str = "",
        scene_change_info: WdpSceneChangeInfo = [[], [], []],
        success: bool = False,
        eid_to_material_slots: Map[int, EntityMaterialSlots] = {}) -> None
```

<a id="unreal.GetEntityMaterialSlotsResult.eid_to_material_slots"></a>

#### eid\_to\_material\_slots

```python
@property
def eid_to_material_slots() -> Map[int, EntityMaterialSlots]
```

(Map[int64, EntityMaterialSlots]):  [Read-Write]

<a id="unreal.GetEntityMaterialSlotsResult.eid_to_material_slots"></a>

#### eid\_to\_material\_slots

```python
@eid_to_material_slots.setter
def eid_to_material_slots(value: Map[int, EntityMaterialSlots]) -> None
```

<a id="unreal.OnWdpMaterialHitEventArgs"></a>