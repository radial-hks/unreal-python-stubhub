## RoundingMode Objects

```python
class RoundingMode(EnumBase)
```

Provides rounding modes for converting numbers into localized text

**C++ Source:**

- **Module**: Engine
- **File**: KismetTextLibrary.h

<a id="unreal.RoundingMode.HALF_TO_EVEN"></a>

#### HALF_TO_EVEN

0: Rounds to the nearest place, equidistant ties go to the value which is closest to an even value: 1.5 becomes 2, 0.5 becomes 0

<a id="unreal.RoundingMode.HALF_FROM_ZERO"></a>

#### HALF_FROM_ZERO

1: Rounds to nearest place, equidistant ties go to the value which is further from zero: -0.5 becomes -1.0, 0.5 becomes 1.0

<a id="unreal.RoundingMode.HALF_TO_ZERO"></a>

#### HALF_TO_ZERO

2: Rounds to nearest place, equidistant ties go to the value which is closer to zero: -0.5 becomes 0, 0.5 becomes 0.

<a id="unreal.RoundingMode.FROM_ZERO"></a>

#### FROM_ZERO

3: Rounds to the value which is further from zero, "larger" in absolute value: 0.1 becomes 1, -0.1 becomes -1

<a id="unreal.RoundingMode.TO_ZERO"></a>

#### TO_ZERO

4: Rounds to the value which is closer to zero, "smaller" in absolute value: 0.1 becomes 0, -0.1 becomes 0

<a id="unreal.RoundingMode.TO_NEGATIVE_INFINITY"></a>

#### TO_NEGATIVE_INFINITY

5: Rounds to the value which is more negative: 0.1 becomes 0, -0.1 becomes -1

<a id="unreal.RoundingMode.TO_POSITIVE_INFINITY"></a>

#### TO_POSITIVE_INFINITY

6: Rounds to the value which is more positive: 0.1 becomes 1, -0.1 becomes 0

<a id="unreal.MemoryUnitStandard"></a>