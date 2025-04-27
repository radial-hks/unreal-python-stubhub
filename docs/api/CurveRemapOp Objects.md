## CurveRemapOp Objects

```python
class CurveRemapOp(RetargetOpBase)
```

Curve Remap Op

**C++ Source:**

- **Plugin**: IKRig
- **Module**: IKRig
- **File**: CurveRemapOp.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``copy_all_source_curves`` (bool):  [Read-Write] This setting only applies to all curves when exporting retargeted animations.
  True: all source curves are copied to the target animation sequence asset.
  False: only remapped curves are left on the target animation sequence asset.
- ``curves_to_remap`` (Array[CurveRemapPair]):  [Read-Write] Add pairs of Source/Target curve names to remap. While retargeting, the animation from the source curves
  will be redirected to the curves on the target skeletal meshes. Can be used to drive, blendshapes or other downstream systems.
  NOTE: By default the IK Retargeter will automatically copy all equivalently named curves from the source to the
  target. Remapping with this op is only necessary when the target curve name(s) are different.

<a id="unreal.RetargetOpStack"></a>