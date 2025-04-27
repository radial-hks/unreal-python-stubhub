## PCGDataType Objects

```python
class PCGDataType(EnumBase)
```

Bitmask containing the various data types supported in PCG. Note that this enum cannot be a blueprint type because
enums have to be uint8 for blueprint, and we already use more than 8 bits in the bitmask.
This is why we have a parallel enum just below that must match on a name basis 1:1 to allow the make/break functions to work properly
in blueprint.
WARNING: Please be mindful that combination of flags that are not explicitly defined there won't be serialized correctly, inducing data loss.

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGCommon.h

<a id="unreal.PCGDataType.POINT"></a>

#### POINT

2

<a id="unreal.PCGDataType.SPLINE"></a>

#### SPLINE

4

<a id="unreal.PCGDataType.LANDSCAPE_SPLINE"></a>

#### LANDSCAPE_SPLINE

8

<a id="unreal.PCGDataType.POLY_LINE"></a>

#### POLY_LINE

12

<a id="unreal.PCGDataType.LANDSCAPE"></a>

#### LANDSCAPE

16

<a id="unreal.PCGDataType.TEXTURE"></a>

#### TEXTURE

32

<a id="unreal.PCGDataType.RENDER_TARGET"></a>

#### RENDER_TARGET

64

<a id="unreal.PCGDataType.SURFACE"></a>

#### SURFACE

112

<a id="unreal.PCGDataType.VOLUME"></a>

#### VOLUME

128

<a id="unreal.PCGDataType.PRIMITIVE"></a>

#### PRIMITIVE

256

<a id="unreal.PCGDataType.DYNAMIC_MESH"></a>

#### DYNAMIC_MESH

1024

<a id="unreal.PCGDataType.CONCRETE"></a>

#### CONCRETE

1534: Simple concrete data.

<a id="unreal.PCGDataType.SPATIAL"></a>

#### SPATIAL

2046: Combinations of concrete data and/or boolean operations.

<a id="unreal.PCGDataType.PARAM"></a>

#### PARAM

134217728

<a id="unreal.PCGDataType.POINT_OR_PARAM"></a>

#### POINT_OR_PARAM

134217730: Combination of Param and Point, necessary for named-based serialization of enums.

<a id="unreal.PCGDataType.OTHER"></a>

#### OTHER

536870912

<a id="unreal.PCGDataType.ANY"></a>

#### ANY

1073741823

<a id="unreal.PCGProjectionColorBlendMode"></a>