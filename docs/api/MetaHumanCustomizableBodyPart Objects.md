## MetaHumanCustomizableBodyPart Objects

```python
class MetaHumanCustomizableBodyPart(StructBase)
```

Meta Human Customizable Body Part

**C++ Source:**

- **Plugin**: MetaHumanSDK
- **Module**: MetaHumanSDKRuntime
- **File**: MetaHumanComponentBase.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``component_name`` (str):  [Read-Write]
- ``control_rig_class`` (type(Class)):  [Read-Write] Control rig to run on the body part. Evaluation happens after the base skeleton.
- ``control_rig_lod_threshold`` (int32):  [Read-Write] * Max LOD level to evaluate the assigned control rig for the body part.
  * For example if you have the threshold set to 2, the control rig will be evaluated for LOD 0, 1, and 2. Setting it to -1 will always evaluate it and disable LODing.
- ``physics_asset`` (PhysicsAsset):  [Read-Write] Physics asset used for rigid body simulation on the body part. Evaluation happens after the base skeleton.
- ``rigid_body_lod_threshold`` (int32):  [Read-Write] * Max LOD level to simulate the rigid bodies of the assigned physics asset.
  * For example if you have the threshold set to 2, simulation will be enabled for LOD 0, 1, and 2. Setting it to -1 will make it simulate always and disable LODing.

<a id="unreal.MetaHumanCustomizableBodyPart.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.PlatformInterfaceDelegateResult"></a>