## glTFRuntimePhysicsAssetAutoBodyConfig Objects

```python
class glTFRuntimePhysicsAssetAutoBodyConfig(StructBase)
```

Gl TFRuntime Physics Asset Auto Body Config

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: glTFRuntime
- **File**: glTFRuntimeParser.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``collision_scale`` (float):  [Read-Write]
- ``collision_trace_flag`` (CollisionTraceFlag):  [Read-Write]
- ``collision_type`` (EglTFRuntimePhysicsAssetAutoBodyCollisionType):  [Read-Write]
- ``consider_for_bounds`` (bool):  [Read-Write]
- ``disable_all_collisions`` (bool):  [Read-Write]
- ``disable_overlapping_collisions`` (bool):  [Read-Write]
- ``min_bone_size`` (float):  [Read-Write]
- ``physics_type`` (PhysicsType):  [Read-Write]

<a id="unreal.glTFRuntimePhysicsAssetAutoBodyConfig.__init__"></a>

#### \_\_init\_\_

```python
def __init__(
        collision_type:
    EglTFRuntimePhysicsAssetAutoBodyCollisionType = EglTFRuntimePhysicsAssetAutoBodyCollisionType
    .CAPSULE,
        min_bone_size: float = 0.000000,
        disable_overlapping_collisions: bool = False,
        disable_all_collisions: bool = False,
        collision_trace_flag: CollisionTraceFlag = CollisionTraceFlag.
    CTF_USE_DEFAULT,
        physics_type: PhysicsType = PhysicsType.PHYS_TYPE_DEFAULT,
        consider_for_bounds: bool = False,
        collision_scale: float = 0.000000) -> None
```

<a id="unreal.glTFRuntimePhysicsAssetAutoBodyConfig.collision_type"></a>

#### collision\_type

```python
@property
def collision_type() -> EglTFRuntimePhysicsAssetAutoBodyCollisionType
```

(EglTFRuntimePhysicsAssetAutoBodyCollisionType):  [Read-Write]

<a id="unreal.glTFRuntimePhysicsAssetAutoBodyConfig.collision_type"></a>

#### collision\_type

```python
@collision_type.setter
def collision_type(
        value: EglTFRuntimePhysicsAssetAutoBodyCollisionType) -> None
```

<a id="unreal.glTFRuntimePhysicsAssetAutoBodyConfig.min_bone_size"></a>

#### min\_bone\_size

```python
@property
def min_bone_size() -> float
```

(float):  [Read-Write]

<a id="unreal.glTFRuntimePhysicsAssetAutoBodyConfig.min_bone_size"></a>

#### min\_bone\_size

```python
@min_bone_size.setter
def min_bone_size(value: float) -> None
```

<a id="unreal.glTFRuntimePhysicsAssetAutoBodyConfig.disable_overlapping_collisions"></a>

#### disable\_overlapping\_collisions

```python
@property
def disable_overlapping_collisions() -> bool
```

(bool):  [Read-Write]

<a id="unreal.glTFRuntimePhysicsAssetAutoBodyConfig.disable_overlapping_collisions"></a>

#### disable\_overlapping\_collisions

```python
@disable_overlapping_collisions.setter
def disable_overlapping_collisions(value: bool) -> None
```

<a id="unreal.glTFRuntimePhysicsAssetAutoBodyConfig.disable_all_collisions"></a>

#### disable\_all\_collisions

```python
@property
def disable_all_collisions() -> bool
```

(bool):  [Read-Write]

<a id="unreal.glTFRuntimePhysicsAssetAutoBodyConfig.disable_all_collisions"></a>

#### disable\_all\_collisions

```python
@disable_all_collisions.setter
def disable_all_collisions(value: bool) -> None
```

<a id="unreal.glTFRuntimePhysicsAssetAutoBodyConfig.collision_trace_flag"></a>

#### collision\_trace\_flag

```python
@property
def collision_trace_flag() -> CollisionTraceFlag
```

(CollisionTraceFlag):  [Read-Write]

<a id="unreal.glTFRuntimePhysicsAssetAutoBodyConfig.collision_trace_flag"></a>

#### collision\_trace\_flag

```python
@collision_trace_flag.setter
def collision_trace_flag(value: CollisionTraceFlag) -> None
```

<a id="unreal.glTFRuntimePhysicsAssetAutoBodyConfig.physics_type"></a>

#### physics\_type

```python
@property
def physics_type() -> PhysicsType
```

(PhysicsType):  [Read-Write]

<a id="unreal.glTFRuntimePhysicsAssetAutoBodyConfig.physics_type"></a>

#### physics\_type

```python
@physics_type.setter
def physics_type(value: PhysicsType) -> None
```

<a id="unreal.glTFRuntimePhysicsAssetAutoBodyConfig.consider_for_bounds"></a>

#### consider\_for\_bounds

```python
@property
def consider_for_bounds() -> bool
```

(bool):  [Read-Write]

<a id="unreal.glTFRuntimePhysicsAssetAutoBodyConfig.consider_for_bounds"></a>

#### consider\_for\_bounds

```python
@consider_for_bounds.setter
def consider_for_bounds(value: bool) -> None
```

<a id="unreal.glTFRuntimePhysicsAssetAutoBodyConfig.collision_scale"></a>

#### collision\_scale

```python
@property
def collision_scale() -> float
```

(float):  [Read-Write]

<a id="unreal.glTFRuntimePhysicsAssetAutoBodyConfig.collision_scale"></a>

#### collision\_scale

```python
@collision_scale.setter
def collision_scale(value: float) -> None
```

<a id="unreal.glTFRuntimeBoneBoundsFilterHook"></a>