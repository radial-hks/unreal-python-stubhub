## KTaperedCapsuleElem Objects

```python
class KTaperedCapsuleElem(KShapeElem)
```

Capsule shape used for collision. Z axis is capsule axis. Has a start and end radius that can differ.

**C++ Source:**

- **Module**: Engine
- **File**: TaperedCapsuleElem.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``center`` (Vector):  [Read-Write] Position of the capsule's origin
- ``collision_enabled`` (CollisionEnabled):  [Read-Write] Course per-primitive collision filtering. This allows for individual primitives to
                be toggled in and out of sim and query collision without changing filtering details.
- ``contribute_to_mass`` (bool):  [Read-Write] True if this shape should contribute to the overall mass of the body it
                belongs to. This lets you create extra collision volumes which do not affect
                the mass properties of an object.
- ``is_generated`` (bool):  [Read-Write] True when the shape was created by the engine and was not imported.
- ``length`` (float):  [Read-Write] Length of line-segment. Add Radius0 and Radius 1 to find total length.
- ``name`` (Name):  [Read-Write] User-defined name for this shape
- ``radius0`` (float):  [Read-Write] Radius of the capsule start point
- ``radius1`` (float):  [Read-Write] Radius of the capsule end point
- ``rest_offset`` (float):  [Read-Write] Offset used when generating contact points. This allows you to smooth out
                the Minkowski sum by radius R. Useful for making objects slide smoothly
                on top of irregularities
- ``rotation`` (Rotator):  [Read-Write] Rotation of the capsule

<a id="unreal.KTaperedCapsuleElem.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.KLevelSetElem"></a>