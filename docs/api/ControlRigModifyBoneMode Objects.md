## ControlRigModifyBoneMode Objects

```python
class ControlRigModifyBoneMode(EnumBase)
```

EControl Rig Modify Bone Mode

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_ModifyTransforms.h

<a id="unreal.ControlRigModifyBoneMode.OVERRIDE_LOCAL"></a>

#### OVERRIDE_LOCAL

0: Override existing local transform

<a id="unreal.ControlRigModifyBoneMode.OVERRIDE_GLOBAL"></a>

#### OVERRIDE_GLOBAL

1: Override existing global transform

<a id="unreal.ControlRigModifyBoneMode.ADDITIVE_LOCAL"></a>

#### ADDITIVE_LOCAL

2: Additive to existing local transform.
Input transform is added within the bone's space.

<a id="unreal.ControlRigModifyBoneMode.ADDITIVE_GLOBAL"></a>

#### ADDITIVE_GLOBAL

3: Additive to existing global transform.
Input transform is added as a global offset in the root of the hierarchy.

<a id="unreal.RigVMSimPointIntegrateType"></a>