## PCGPointProperties Objects

```python
class PCGPointProperties(EnumBase)
```

EPCGPoint Properties

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGPoint.h

<a id="unreal.PCGPointProperties.DENSITY"></a>

#### DENSITY

0: When points are sampled, this density value represents the highest value of the density function within that point's volume. It is also used as a weighted value, for example, when testing points against a threshold in filtering operations.

<a id="unreal.PCGPointProperties.BOUNDS_MIN"></a>

#### BOUNDS_MIN

1: Minimum corner of the point's bounds in local space.

<a id="unreal.PCGPointProperties.BOUNDS_MAX"></a>

#### BOUNDS_MAX

2: Maximum corner of the point's bounds in local space.

<a id="unreal.PCGPointProperties.EXTENTS"></a>

#### EXTENTS

3: Half the local space difference between the maximum and minimum bounds of the point's volume. Can be used with the point's position to represent the volume.

<a id="unreal.PCGPointProperties.COLOR"></a>

#### COLOR

4: An RGBA (four channel) color value.

<a id="unreal.PCGPointProperties.POSITION"></a>

#### POSITION

5: Location component of the point's transform.

<a id="unreal.PCGPointProperties.ROTATION"></a>

#### ROTATION

6: Rotation component of the point's transform.

<a id="unreal.PCGPointProperties.SCALE"></a>

#### SCALE

7: Scale component of the point's transform.

<a id="unreal.PCGPointProperties.TRANSFORM"></a>

#### TRANSFORM

8: The point's transform.

<a id="unreal.PCGPointProperties.STEEPNESS"></a>

#### STEEPNESS

9: A normalized value that establishes how 'hard' or 'soft' that volume will be represented. From 0, it will ramp up linearly increasing its influence over the density from the point's center to up to two times the bounds. At 1, it will represent a binary box function with the size of the point's bounds.

<a id="unreal.PCGPointProperties.LOCAL_CENTER"></a>

#### LOCAL_CENTER

10: The local center location of the point's volume, halfway between the minimum and maximum bounds.

<a id="unreal.PCGPointProperties.SEED"></a>

#### SEED

11: Used to seed random processes during various operations.

<a id="unreal.PCGPointProperties.LOCAL_SIZE"></a>

#### LOCAL_SIZE

12: The difference between the maximum and minimum bounds of the point.

<a id="unreal.PCGPointProperties.SCALED_LOCAL_SIZE"></a>

#### SCALED_LOCAL_SIZE

13: The difference between the maximum and minimum bounds of the point, after only the scale has been applied.

<a id="unreal.PCGExtraProperties"></a>