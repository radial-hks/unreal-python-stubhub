## MovieSceneTimeWarpExtensions Objects

```python
class MovieSceneTimeWarpExtensions(BlueprintFunctionLibrary)
```

Function library containing methods that relate to time-warp within Sequencer

**C++ Source:**

- **Plugin**: SequencerScripting
- **Module**: SequencerScripting
- **File**: MovieSceneTimeWarpExtensions.h

<a id="unreal.MovieSceneTimeWarpExtensions.to_fixed_play_rate"></a>

#### to_fixed_play_rate

```python
@classmethod
def to_fixed_play_rate(cls, time_warp: MovieSceneTimeWarpVariant) -> float
```

X.to_fixed_play_rate(time_warp) -> double
Retrieve this timewarp's constant play rate. Will throw an error if the timewarp is not a constant play rate.

Args:
    time_warp (MovieSceneTimeWarpVariant): 

Returns:
    double:

<a id="unreal.MovieSceneTimeWarpExtensions.set_fixed_play_rate"></a>

#### set_fixed_play_rate

```python
@classmethod
def set_fixed_play_rate(cls, time_warp: MovieSceneTimeWarpVariant,
                        fixed_play_rate: float) -> MovieSceneTimeWarpVariant
```

X.set_fixed_play_rate(time_warp, fixed_play_rate) -> MovieSceneTimeWarpVariant
Assign a constant playrate to this timewarp, overwriting any existing timewarp implementation.

Args:
    time_warp (MovieSceneTimeWarpVariant): 
    fixed_play_rate (double): 

Returns:
    MovieSceneTimeWarpVariant: 

    time_warp (MovieSceneTimeWarpVariant):

<a id="unreal.MovieSceneTimeWarpExtensions.make_time_warp"></a>

#### make_time_warp

```python
@classmethod
def make_time_warp(cls, fixed_play_rate: float) -> MovieSceneTimeWarpVariant
```

X.make_time_warp(fixed_play_rate) -> MovieSceneTimeWarpVariant
Make Time Warp

Args:
    fixed_play_rate (double): 

Returns:
    MovieSceneTimeWarpVariant:

<a id="unreal.MovieSceneTimeWarpExtensions.conv_time_warp_variant_to_play_rate"></a>

#### conv_time_warp_variant_to_play_rate

```python
@classmethod
def conv_time_warp_variant_to_play_rate(
        cls, time_warp: MovieSceneTimeWarpVariant) -> float
```

X.conv_time_warp_variant_to_play_rate(time_warp) -> double
Converts a timewarp variant struct to a constant play rate

Args:
    time_warp (MovieSceneTimeWarpVariant): 

Returns:
    double:

<a id="unreal.MovieSceneTimeWarpExtensions.conv_play_rate_to_time_warp_variant"></a>

#### conv_play_rate_to_time_warp_variant

```python
@classmethod
def conv_play_rate_to_time_warp_variant(
        cls, constant_play_rate: float) -> MovieSceneTimeWarpVariant
```

X.conv_play_rate_to_time_warp_variant(constant_play_rate) -> MovieSceneTimeWarpVariant
Converts a constant playrate to a timewarp variant

Args:
    constant_play_rate (double): 

Returns:
    MovieSceneTimeWarpVariant:

<a id="unreal.MovieSceneTimeWarpExtensions.break_time_warp"></a>

#### break_time_warp

```python
@classmethod
def break_time_warp(cls, time_warp: MovieSceneTimeWarpVariant) -> float
```

X.break_time_warp(time_warp) -> double
Break Time Warp

Args:
    time_warp (MovieSceneTimeWarpVariant): 

Returns:
    double: 

    fixed_play_rate (double):

<a id="unreal.MovieSceneTrackExtensions"></a>