## KBoxElem Objects

```python
class KBoxElem(KShapeElem)
```

Box shape used for collision

**C++ Source:**

- **Module**: Engine
- **File**: BoxElem.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``center`` (Vector):  [Read-Write] Position of the box's origin
- ``collision_enabled`` (CollisionEnabled):  [Read-Write] Course per-primitive collision filtering. This allows for individual primitives to
                be toggled in and out of sim and query collision without changing filtering details.
- ``contribute_to_mass`` (bool):  [Read-Write] True if this shape should contribute to the overall mass of the body it
                belongs to. This lets you create extra collision volumes which do not affect
                the mass properties of an object.
- ``is_generated`` (bool):  [Read-Write] True when the shape was created by the engine and was not imported.
- ``name`` (Name):  [Read-Write] User-defined name for this shape
- ``rest_offset`` (float):  [Read-Write] Offset used when generating contact points. This allows you to smooth out
                the Minkowski sum by radius R. Useful for making objects slide smoothly
                on top of irregularities
- ``rotation`` (Rotator):  [Read-Write] Rotation of the box
- ``x`` (float):  [Read-Write] Extent of the box along the y-axis
- ``y`` (float):  [Read-Write] Extent of the box along the y-axis
- ``z`` (float):  [Read-Write] Extent of the box along the z-axis

<a id="unreal.KBoxElem.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.KSphylElem"></a>