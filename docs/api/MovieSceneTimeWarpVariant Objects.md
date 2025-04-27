## MovieSceneTimeWarpVariant Objects

```python
class MovieSceneTimeWarpVariant(StructBase)
```

Numeric variant type that represents a 'time-warp' operation transforming a time into another time.

By default this variant is a literal value that represents a play rate of 1.0 (ie, a 1:1 mapping), but it can be customized
to provide a wide range of different transformations such as looping, clamping and custom curves

**C++ Source:**

- **Module**: MovieScene
- **File**: MovieSceneTimeWarpVariant.h

<a id="unreal.MovieSceneTimeWarpVariant.__init__"></a>

#### __init__

```python
def __init__(fixed_play_rate: float = 0.000000) -> None
```

<a id="unreal.MovieSceneTimeWarpVariant.to_fixed_play_rate"></a>

#### to_fixed_play_rate

```python
def to_fixed_play_rate() -> float
```

x.to_fixed_play_rate() -> double
Retrieve this timewarp's constant play rate. Will throw an error if the timewarp is not a constant play rate.

Returns:
    double:

<a id="unreal.MovieSceneTimeWarpVariant.set_fixed_play_rate"></a>

#### set_fixed_play_rate

```python
def set_fixed_play_rate(fixed_play_rate: float) -> None
```

x.set_fixed_play_rate(fixed_play_rate) -> None
Assign a constant playrate to this timewarp, overwriting any existing timewarp implementation.

Args:
    fixed_play_rate (double):

<a id="unreal.MovieSceneNumericVariant"></a>