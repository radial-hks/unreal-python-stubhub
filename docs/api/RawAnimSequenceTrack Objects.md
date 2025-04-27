## RawAnimSequenceTrack Objects

```python
class RawAnimSequenceTrack(StructBase)
```

Raw keyframe data for one track.Each array will contain either NumFrames elements or 1 element.
One element is used as a simple compression scheme where if all keys are the same, they'll be
reduced to 1 key that is constant over the entire sequence.

**C++ Source:**

- **Module**: Engine
- **File**: AnimTypes.h

<a id="unreal.RawAnimSequenceTrack.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.RawAnimSequenceTrack.get_scale_keys"></a>

#### get_scale_keys

```python
def get_scale_keys() -> Array[Vector]
```

x.get_scale_keys() -> Array[Vector]
Returns the scale keys contained by the FRawAnimSequenceTrack

Returns:
    Array[Vector]:

<a id="unreal.RawAnimSequenceTrack.get_rotational_keys"></a>

#### get_rotational_keys

```python
def get_rotational_keys() -> Array[Quat]
```

x.get_rotational_keys() -> Array[Quat]
Returns the rotational keys contained by the FRawAnimSequenceTrack

Returns:
    Array[Quat]:

<a id="unreal.RawAnimSequenceTrack.get_positional_keys"></a>

#### get_positional_keys

```python
def get_positional_keys() -> Array[Vector]
```

x.get_positional_keys() -> Array[Vector]
Returns the positional keys contained by the FRawAnimSequenceTrack

Returns:
    Array[Vector]:

<a id="unreal.NonBlendableQuaternionAnimationAttribute"></a>