## GroomInterpolationQuality Objects

```python
class GroomInterpolationQuality(EnumBase)
```

EGroom Interpolation Quality

**C++ Source:**

- **Plugin**: HairStrands
- **Module**: HairStrandsCore
- **File**: GroomSettings.h

<a id="unreal.GroomInterpolationQuality.LOW"></a>

#### LOW

0: Build interpolation data based on nearst neighbor search. Low quality interpolation data, but fast to build (takes a few minutes)

<a id="unreal.GroomInterpolationQuality.MEDIUM"></a>

#### MEDIUM

1: Build interpolation data using curve shape matching search but within a limited spatial range. This is a tradeoff between Low and high quality in term of quality & build time (can takes several dozen of minutes)

<a id="unreal.GroomInterpolationQuality.HIGH"></a>

#### HIGH

2: Build interpolation data using curve shape matching search. This result in high quality interpolation data, but is relatively slow to build (can takes several dozen of minutes)

<a id="unreal.GroomInterpolationWeight"></a>