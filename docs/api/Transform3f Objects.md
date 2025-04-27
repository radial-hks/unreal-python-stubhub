## Transform3f Objects

```python
class Transform3f(StructBase)
```

Transform composed of Quat/Translation/Scale.
note: This is implemented in either TransformVectorized.h or TransformNonVectorized.h depending on the platform.

**C++ Source:**

- **Module**: CoreUObject
- **File**: NoExportTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``rotation`` (Quat4f):  [Read-Write] Rotation of this transformation, as a quaternion.
- ``scale3d`` (Vector3f):  [Read-Write] 3D scale (always applied in local space) as a vector.
- ``translation`` (Vector3f):  [Read-Write] Translation of this transformation, as a vector.

<a id="unreal.Transform3f.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.Vector4"></a>