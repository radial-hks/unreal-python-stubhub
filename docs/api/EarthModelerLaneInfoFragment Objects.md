## EarthModelerLaneInfoFragment Objects

```python
class EarthModelerLaneInfoFragment(EarthPropertyFragment)
```

Earth Modeler Lane Info Fragment

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: EarthPrefab
- **File**: EarthRoadModelerFragment.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``modeler_lane_info`` (EarthModelerLaneInfo):  [Read-Write]
- ``valid`` (bool):  [Read-Write] 数据片段是否有效
- ``validated`` (bool):  [Read-Write] 是否已执行数据有效性验证

<a id="unreal.EarthModelerLaneInfoFragment.__init__"></a>

#### \_\_init\_\_

```python
def __init__(
    validated: bool = False,
    valid: bool = False,
    modeler_lane_info: EarthModelerLaneInfo = [
        EarthModelerRoadLaneType.DRIVE, [[""]], 0.000000, 0.000000, 0, True,
        True, EarthPlaceDirection.FORWARD, None, [], None, [[""]]
    ]
) -> None
```

<a id="unreal.EarthModelerLaneInfoFragment.modeler_lane_info"></a>

#### modeler\_lane\_info

```python
@property
def modeler_lane_info() -> EarthModelerLaneInfo
```

(EarthModelerLaneInfo):  [Read-Write]

<a id="unreal.EarthModelerLaneInfoFragment.modeler_lane_info"></a>

#### modeler\_lane\_info

```python
@modeler_lane_info.setter
def modeler_lane_info(value: EarthModelerLaneInfo) -> None
```

<a id="unreal.EarthRoadModelerJunctionPrefab"></a>