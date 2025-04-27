## Transform3d Objects

```python
class Transform3d(StructBase)
```

Transform composed of Quat/Translation/Scale.
note: This is implemented in either TransformVectorized.h or TransformNonVectorized.h depending on the platform.

**C++ Source:**

- **Module**: CoreUObject
- **File**: NoExportTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``rotation`` (Quat4d):  [Read-Write] Rotation of this transformation, as a quaternion.
- ``scale3d`` (Vector3d):  [Read-Write] 3D scale (always applied in local space) as a vector.
- ``translation`` (Vector3d):  [Read-Write] Translation of this transformation, as a vector.

<a id="unreal.Transform3d.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.Rotator3d"></a>