## SplinePlacementType Objects

```python
class SplinePlacementType(EnumBase)
```

样条线放置类型

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: AesAsset
- **File**: AesAssetCommon.h

<a id="unreal.SplinePlacementType.CONTINUOUS"></a>

#### CONTINUOUS

0: 严格按长度拉伸模型，最后一个模型拉伸到样条的末端，且按样条线扭曲

<a id="unreal.SplinePlacementType.CONTINUOUS_EQUAL_STRETCH"></a>

#### CONTINUOUS\_EQUAL\_STRETCH

1: 均匀拉伸每个模型，且按样条线扭曲

<a id="unreal.SplinePlacementType.DISCRETE"></a>

#### DISCRETE

2: 摆放散点模型，无扭曲

<a id="unreal.LandCover"></a>