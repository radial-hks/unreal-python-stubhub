## EarthReplacementLaneInfo Objects

```python
class EarthReplacementLaneInfo(StructBase)
```

定义预制体子资产数据片段的结构体

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: EarthPrefab
- **File**: EarthRoadFragment.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``affect_modifier_range`` (EarthRoadModifierRange):  [Read-Write] 影响资产范围
- ``modifier_type`` (EarthRoadModifierType):  [Read-Write] 修改道路操作方式
- ``ratio_range`` (Vector2f):  [Read-Write] 替换范围（占整条车道长度百分比范围）
- ``replacement_lane_asset`` (EarthPrefabAsset):  [Read-Write] 放置的新子资产引用

<a id="unreal.EarthReplacementLaneInfo.__init__"></a>

#### \_\_init\_\_

```python
def __init__(
    ratio_range: Vector2f = [0.000000, 0.000000],
    modifier_type: EarthRoadModifierType = EarthRoadModifierType.CUT,
    replacement_lane_asset: EarthPrefabAsset = None,
    affect_modifier_range: EarthRoadModifierRange = EarthRoadModifierRange.BOTH
) -> None
```

<a id="unreal.EarthReplacementLaneInfo.ratio_range"></a>

#### ratio\_range

```python
@property
def ratio_range() -> Vector2f
```

(Vector2f):  [Read-Write] 替换范围（占整条车道长度百分比范围）

<a id="unreal.EarthReplacementLaneInfo.ratio_range"></a>

#### ratio\_range

```python
@ratio_range.setter
def ratio_range(value: Vector2f) -> None
```

<a id="unreal.EarthReplacementLaneInfo.modifier_type"></a>

#### modifier\_type

```python
@property
def modifier_type() -> EarthRoadModifierType
```

(EarthRoadModifierType):  [Read-Write] 修改道路操作方式

<a id="unreal.EarthReplacementLaneInfo.modifier_type"></a>

#### modifier\_type

```python
@modifier_type.setter
def modifier_type(value: EarthRoadModifierType) -> None
```

<a id="unreal.EarthReplacementLaneInfo.replacement_lane_asset"></a>

#### replacement\_lane\_asset

```python
@property
def replacement_lane_asset() -> EarthPrefabAsset
```

(EarthPrefabAsset):  [Read-Write] 放置的新子资产引用

<a id="unreal.EarthReplacementLaneInfo.replacement_lane_asset"></a>

#### replacement\_lane\_asset

```python
@replacement_lane_asset.setter
def replacement_lane_asset(value: EarthPrefabAsset) -> None
```

<a id="unreal.EarthReplacementLaneInfo.affect_modifier_range"></a>

#### affect\_modifier\_range

```python
@property
def affect_modifier_range() -> EarthRoadModifierRange
```

(EarthRoadModifierRange):  [Read-Write] 影响资产范围

<a id="unreal.EarthReplacementLaneInfo.affect_modifier_range"></a>

#### affect\_modifier\_range

```python
@affect_modifier_range.setter
def affect_modifier_range(value: EarthRoadModifierRange) -> None
```

<a id="unreal.EarthLaneProfileFragment"></a>