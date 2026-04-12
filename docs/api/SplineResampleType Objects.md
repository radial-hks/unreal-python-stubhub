## SplineResampleType Objects

```python
class SplineResampleType(EnumBase)
```

样条线重采样类型

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: AesAsset
- **File**: AesAssetCommon.h

<a id="unreal.SplineResampleType.INTERPOLATING"></a>

#### INTERPOLATING

0: 将曲线上的点视为途经点再重采样

<a id="unreal.SplineResampleType.SUBDIVISION"></a>

#### SUBDIVISION

1: 将曲线上的点视为控制点再重采样

<a id="unreal.SplineResampleType.ROUND"></a>

#### ROUND

2: 将曲线上拟合圆弧

<a id="unreal.SplineResampleType.NONE"></a>

#### NONE

3: 不进行重采样

<a id="unreal.SplineAlignmentType"></a>