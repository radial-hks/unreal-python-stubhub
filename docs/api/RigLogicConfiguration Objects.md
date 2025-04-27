## RigLogicConfiguration Objects

```python
class RigLogicConfiguration(StructBase)
```

Rig Logic Configuration

**C++ Source:**

- **Plugin**: RigLogic
- **Module**: RigLogicModule
- **File**: RigLogic.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``calculation_type`` (RigLogicCalculationType):  [Read-Write]
- ``load_animated_maps`` (bool):  [Read-Write]
- ``load_blend_shapes`` (bool):  [Read-Write]
- ``load_joints`` (bool):  [Read-Write]
- ``load_machine_learned_behavior`` (bool):  [Read-Write]
- ``load_rbf_behavior`` (bool):  [Read-Write]
- ``load_twist_swing_behavior`` (bool):  [Read-Write]
- ``rotation_order`` (RigLogicRotationOrder):  [Read-Write]
- ``rotation_type`` (RigLogicRotationType):  [Read-Write]
- ``scale_type`` (RigLogicScaleType):  [Read-Write]
- ``translation_type`` (RigLogicTranslationType):  [Read-Write]

<a id="unreal.RigLogicConfiguration.__init__"></a>

#### __init__

```python
def __init__(
        calculation_type: RigLogicCalculationType = RigLogicCalculationType.
    SCALAR,
        load_joints: bool = False,
        load_blend_shapes: bool = False,
        load_animated_maps: bool = False,
        load_machine_learned_behavior: bool = False,
        load_rbf_behavior: bool = False,
        load_twist_swing_behavior: bool = False,
        translation_type: RigLogicTranslationType = RigLogicTranslationType.
    NONE,
        rotation_type: RigLogicRotationType = RigLogicRotationType.NONE,
        rotation_order: RigLogicRotationOrder = RigLogicRotationOrder.XYZ,
        scale_type: RigLogicScaleType = RigLogicScaleType.NONE) -> None
```

<a id="unreal.RigLogicConfiguration.calculation_type"></a>

#### calculation_type

```python
@property
def calculation_type() -> RigLogicCalculationType
```

(RigLogicCalculationType):  [Read-Only]

<a id="unreal.RigLogicConfiguration.load_joints"></a>

#### load_joints

```python
@property
def load_joints() -> bool
```

(bool):  [Read-Only]

<a id="unreal.RigLogicConfiguration.load_blend_shapes"></a>

#### load_blend_shapes

```python
@property
def load_blend_shapes() -> bool
```

(bool):  [Read-Only]

<a id="unreal.RigLogicConfiguration.load_animated_maps"></a>

#### load_animated_maps

```python
@property
def load_animated_maps() -> bool
```

(bool):  [Read-Only]

<a id="unreal.RigLogicConfiguration.load_machine_learned_behavior"></a>

#### load_machine_learned_behavior

```python
@property
def load_machine_learned_behavior() -> bool
```

(bool):  [Read-Only]

<a id="unreal.RigLogicConfiguration.load_rbf_behavior"></a>

#### load_rbf_behavior

```python
@property
def load_rbf_behavior() -> bool
```

(bool):  [Read-Only]

<a id="unreal.RigLogicConfiguration.load_twist_swing_behavior"></a>

#### load_twist_swing_behavior

```python
@property
def load_twist_swing_behavior() -> bool
```

(bool):  [Read-Only]

<a id="unreal.RigLogicConfiguration.translation_type"></a>

#### translation_type

```python
@property
def translation_type() -> RigLogicTranslationType
```

(RigLogicTranslationType):  [Read-Only]

<a id="unreal.RigLogicConfiguration.rotation_type"></a>

#### rotation_type

```python
@property
def rotation_type() -> RigLogicRotationType
```

(RigLogicRotationType):  [Read-Only]

<a id="unreal.RigLogicConfiguration.rotation_order"></a>

#### rotation_order

```python
@property
def rotation_order() -> RigLogicRotationOrder
```

(RigLogicRotationOrder):  [Read-Only]

<a id="unreal.RigLogicConfiguration.scale_type"></a>

#### scale_type

```python
@property
def scale_type() -> RigLogicScaleType
```

(RigLogicScaleType):  [Read-Only]

<a id="unreal.AnimNode_RigLogic"></a>