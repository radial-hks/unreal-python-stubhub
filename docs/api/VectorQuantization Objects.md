## VectorQuantization Objects

```python
class VectorQuantization(EnumBase)
```

Describes rules for network replicating a vector efficiently

**C++ Source:**

- **Module**: Engine
- **File**: ReplicatedState.h

<a id="unreal.VectorQuantization.ROUND_WHOLE_NUMBER"></a>

#### ROUND_WHOLE_NUMBER

0: Each vector component will be rounded to the nearest whole number.

<a id="unreal.VectorQuantization.ROUND_ONE_DECIMAL"></a>

#### ROUND_ONE_DECIMAL

1: Each vector component will be rounded, preserving one decimal place.

<a id="unreal.VectorQuantization.ROUND_TWO_DECIMALS"></a>

#### ROUND_TWO_DECIMALS

2: Each vector component will be rounded, preserving two decimal places.

<a id="unreal.RotatorQuantization"></a>