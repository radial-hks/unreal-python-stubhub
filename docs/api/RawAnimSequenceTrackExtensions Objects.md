## RawAnimSequenceTrackExtensions Objects

```python
class RawAnimSequenceTrackExtensions(BlueprintFunctionLibrary)
```

Raw Anim Sequence Track Extensions

**C++ Source:**

- **Module**: Engine
- **File**: AnimTypes.h

<a id="unreal.RawAnimSequenceTrackExtensions.get_scale_keys"></a>

#### get_scale_keys

```python
@classmethod
def get_scale_keys(cls, track: RawAnimSequenceTrack) -> Array[Vector]
```

X.get_scale_keys(track) -> Array[Vector]
Returns the scale keys contained by the FRawAnimSequenceTrack

Args:
    track (RawAnimSequenceTrack): 

Returns:
    Array[Vector]:

<a id="unreal.RawAnimSequenceTrackExtensions.get_rotational_keys"></a>

#### get_rotational_keys

```python
@classmethod
def get_rotational_keys(cls, track: RawAnimSequenceTrack) -> Array[Quat]
```

X.get_rotational_keys(track) -> Array[Quat]
Returns the rotational keys contained by the FRawAnimSequenceTrack

Args:
    track (RawAnimSequenceTrack): 

Returns:
    Array[Quat]:

<a id="unreal.RawAnimSequenceTrackExtensions.get_positional_keys"></a>

#### get_positional_keys

```python
@classmethod
def get_positional_keys(cls, track: RawAnimSequenceTrack) -> Array[Vector]
```

X.get_positional_keys(track) -> Array[Vector]
Returns the positional keys contained by the FRawAnimSequenceTrack

Args:
    track (RawAnimSequenceTrack): 

Returns:
    Array[Vector]:

<a id="unreal.AsyncPhysicsData"></a>