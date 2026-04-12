## EarthRoadModifierEditorFragment Objects

```python
class EarthRoadModifierEditorFragment(EarthPropertyFragment)
```

Earth Road Modifier Editor Fragment

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: EarthPrefab
- **File**: EarthRoadFragment.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``modifier_range`` (EarthRoadModifierRange):  [Read-Write] 修改道路操作方式
- ``modifier_type`` (EarthRoadModifierType):  [Read-Write] 修改道路操作方式
- ``replacement_lane_asset`` (EarthPrefabAsset):  [Read-Write] 放置的新子资产引用
- ``target_road_lanes`` (Array[EarthModelerEditorRoadLaneType]):  [Read-Write] 目标修改道路种类
- ``valid`` (bool):  [Read-Write] 数据片段是否有效
- ``validated`` (bool):  [Read-Write] 是否已执行数据有效性验证

<a id="unreal.EarthRoadModifierEditorFragment.__init__"></a>

#### \_\_init\_\_

```python
def __init__(
        validated: bool = False,
        valid: bool = False,
        target_road_lanes: Array[EarthModelerEditorRoadLaneType] = [],
        modifier_type: EarthRoadModifierType = EarthRoadModifierType.CUT,
        modifier_range: EarthRoadModifierRange = EarthRoadModifierRange.BOTH,
        replacement_lane_asset: EarthPrefabAsset = None) -> None
```

<a id="unreal.EarthRoadModifierEditorFragment.target_road_lanes"></a>

#### target\_road\_lanes

```python
@property
def target_road_lanes() -> Array[EarthModelerEditorRoadLaneType]
```

(Array[EarthModelerEditorRoadLaneType]):  [Read-Write] 目标修改道路种类

<a id="unreal.EarthRoadModifierEditorFragment.target_road_lanes"></a>

#### target\_road\_lanes

```python
@target_road_lanes.setter
def target_road_lanes(value: Array[EarthModelerEditorRoadLaneType]) -> None
```

<a id="unreal.EarthRoadModifierEditorFragment.modifier_type"></a>

#### modifier\_type

```python
@property
def modifier_type() -> EarthRoadModifierType
```

(EarthRoadModifierType):  [Read-Write] 修改道路操作方式

<a id="unreal.EarthRoadModifierEditorFragment.modifier_type"></a>

#### modifier\_type

```python
@modifier_type.setter
def modifier_type(value: EarthRoadModifierType) -> None
```

<a id="unreal.EarthRoadModifierEditorFragment.modifier_range"></a>

#### modifier\_range

```python
@property
def modifier_range() -> EarthRoadModifierRange
```

(EarthRoadModifierRange):  [Read-Write] 修改道路操作方式

<a id="unreal.EarthRoadModifierEditorFragment.modifier_range"></a>

#### modifier\_range

```python
@modifier_range.setter
def modifier_range(value: EarthRoadModifierRange) -> None
```

<a id="unreal.EarthRoadModifierEditorFragment.replacement_lane_asset"></a>

#### replacement\_lane\_asset

```python
@property
def replacement_lane_asset() -> EarthPrefabAsset
```

(EarthPrefabAsset):  [Read-Write] 放置的新子资产引用

<a id="unreal.EarthRoadModifierEditorFragment.replacement_lane_asset"></a>

#### replacement\_lane\_asset

```python
@replacement_lane_asset.setter
def replacement_lane_asset(value: EarthPrefabAsset) -> None
```

<a id="unreal.EarthRoadModifierFragment"></a>