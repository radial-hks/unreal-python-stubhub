## EarthRoadModifierFragment Objects

```python
class EarthRoadModifierFragment(EarthPropertyFragment)
```

Earth Road Modifier Fragment

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: EarthPrefab
- **File**: EarthRoadFragment.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``affect_modifier_range`` (EarthRoadModifierRange):  [Read-Write] 影响资产范围
- ``box_center`` (Vector):  [Read-Write]
- ``box_extend`` (Vector):  [Read-Write]
- ``modifier_type`` (EarthRoadModifierType):  [Read-Write] 修改道路操作方式
- ``replacement_lane_asset`` (EarthPrefabAsset):  [Read-Write] 放置的新子资产引用
- ``road_id`` (int64):  [Read-Write]
- ``target_road_lanes`` (Array[EarthModelerEditorRoadLaneType]):  [Read-Write] 目标修改道路种类
- ``valid`` (bool):  [Read-Write] 数据片段是否有效
- ``validated`` (bool):  [Read-Write] 是否已执行数据有效性验证

<a id="unreal.EarthRoadModifierFragment.__init__"></a>

#### \_\_init\_\_

```python
def __init__(
        validated: bool = False,
        valid: bool = False,
        target_road_lanes: Array[EarthModelerEditorRoadLaneType] = [],
        modifier_type: EarthRoadModifierType = EarthRoadModifierType.CUT,
        road_id: int = 0,
        box_center: Vector = [0.000000, 0.000000, 0.000000],
        box_extend: Vector = [0.000000, 0.000000, 0.000000],
        affect_modifier_range: EarthRoadModifierRange = EarthRoadModifierRange.
    BOTH,
        replacement_lane_asset: EarthPrefabAsset = None) -> None
```

<a id="unreal.EarthRoadModifierFragment.target_road_lanes"></a>

#### target\_road\_lanes

```python
@property
def target_road_lanes() -> Array[EarthModelerEditorRoadLaneType]
```

(Array[EarthModelerEditorRoadLaneType]):  [Read-Write] 目标修改道路种类

<a id="unreal.EarthRoadModifierFragment.target_road_lanes"></a>

#### target\_road\_lanes

```python
@target_road_lanes.setter
def target_road_lanes(value: Array[EarthModelerEditorRoadLaneType]) -> None
```

<a id="unreal.EarthRoadModifierFragment.modifier_type"></a>

#### modifier\_type

```python
@property
def modifier_type() -> EarthRoadModifierType
```

(EarthRoadModifierType):  [Read-Write] 修改道路操作方式

<a id="unreal.EarthRoadModifierFragment.modifier_type"></a>

#### modifier\_type

```python
@modifier_type.setter
def modifier_type(value: EarthRoadModifierType) -> None
```

<a id="unreal.EarthRoadModifierFragment.road_id"></a>

#### road\_id

```python
@property
def road_id() -> int
```

(int64):  [Read-Write]

<a id="unreal.EarthRoadModifierFragment.road_id"></a>

#### road\_id

```python
@road_id.setter
def road_id(value: int) -> None
```

<a id="unreal.EarthRoadModifierFragment.box_center"></a>

#### box\_center

```python
@property
def box_center() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.EarthRoadModifierFragment.box_center"></a>

#### box\_center

```python
@box_center.setter
def box_center(value: Vector) -> None
```

<a id="unreal.EarthRoadModifierFragment.box_extend"></a>

#### box\_extend

```python
@property
def box_extend() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.EarthRoadModifierFragment.box_extend"></a>

#### box\_extend

```python
@box_extend.setter
def box_extend(value: Vector) -> None
```

<a id="unreal.EarthRoadModifierFragment.affect_modifier_range"></a>

#### affect\_modifier\_range

```python
@property
def affect_modifier_range() -> EarthRoadModifierRange
```

(EarthRoadModifierRange):  [Read-Write] 影响资产范围

<a id="unreal.EarthRoadModifierFragment.affect_modifier_range"></a>

#### affect\_modifier\_range

```python
@affect_modifier_range.setter
def affect_modifier_range(value: EarthRoadModifierRange) -> None
```

<a id="unreal.EarthRoadModifierFragment.replacement_lane_asset"></a>

#### replacement\_lane\_asset

```python
@property
def replacement_lane_asset() -> EarthPrefabAsset
```

(EarthPrefabAsset):  [Read-Write] 放置的新子资产引用

<a id="unreal.EarthRoadModifierFragment.replacement_lane_asset"></a>

#### replacement\_lane\_asset

```python
@replacement_lane_asset.setter
def replacement_lane_asset(value: EarthPrefabAsset) -> None
```

<a id="unreal.EarthRoadFragment"></a>