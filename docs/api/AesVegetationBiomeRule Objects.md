## AesVegetationBiomeRule Objects

```python
class AesVegetationBiomeRule(TableRowBase)
```

植被群落规则表

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: AesAsset
- **File**: AesVegetationAsset.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``biome_rule_map`` (Map[Name, AesVegetationSpeciesArray]):  [Read-Write] 植被群落映射表，键为群落大类，值为该群落对应的资产列表

<a id="unreal.AesVegetationBiomeRule.__init__"></a>

#### \_\_init\_\_

```python
def __init__(
        biome_rule_map: Map[Name, AesVegetationSpeciesArray] = {}) -> None
```

<a id="unreal.AesVegetationBiomeRule.biome_rule_map"></a>

#### biome\_rule\_map

```python
@property
def biome_rule_map() -> Map[Name, AesVegetationSpeciesArray]
```

(Map[Name, AesVegetationSpeciesArray]):  [Read-Write] 植被群落映射表，键为群落大类，值为该群落对应的资产列表

<a id="unreal.AesVegetationBiomeRule.biome_rule_map"></a>

#### biome\_rule\_map

```python
@biome_rule_map.setter
def biome_rule_map(value: Map[Name, AesVegetationSpeciesArray]) -> None
```

<a id="unreal.WdpJsonObjectWrapper"></a>