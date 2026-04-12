## glTFRuntimePhysicsBody Objects

```python
class glTFRuntimePhysicsBody(StructBase)
```

Gl TFRuntime Physics Body

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: glTFRuntime
- **File**: glTFRuntimeParser.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``box_auto_collision`` (bool):  [Read-Write]
- ``box_collisions`` (Array[Box]):  [Read-Write]
- ``capsule_auto_collision`` (bool):  [Read-Write]
- ``capsule_collisions`` (Array[glTFRuntimeCapsule]):  [Read-Write]
- ``collision_scale`` (float):  [Read-Write]
- ``collision_trace_flag`` (CollisionTraceFlag):  [Read-Write]
- ``consider_for_bounds`` (bool):  [Read-Write]
- ``disable_collision`` (bool):  [Read-Write]
- ``physics_type`` (PhysicsType):  [Read-Write]
- ``sphere_auto_collision`` (bool):  [Read-Write]
- ``sphere_collisions`` (Array[glTFRuntimeSphere]):  [Read-Write]

<a id="unreal.glTFRuntimePhysicsBody.__init__"></a>

#### \_\_init\_\_

```python
def __init__(collision_trace_flag: CollisionTraceFlag = CollisionTraceFlag.
             CTF_USE_DEFAULT,
             physics_type: PhysicsType = PhysicsType.PHYS_TYPE_DEFAULT,
             consider_for_bounds: bool = False,
             capsule_collisions: Array[glTFRuntimeCapsule] = [],
             sphere_collisions: Array[glTFRuntimeSphere] = [],
             box_collisions: Array[Box] = [],
             sphere_auto_collision: bool = False,
             box_auto_collision: bool = False,
             capsule_auto_collision: bool = False,
             collision_scale: float = 0.000000,
             disable_collision: bool = False) -> None
```

<a id="unreal.glTFRuntimePhysicsBody.collision_trace_flag"></a>

#### collision\_trace\_flag

```python
@property
def collision_trace_flag() -> CollisionTraceFlag
```

(CollisionTraceFlag):  [Read-Write]

<a id="unreal.glTFRuntimePhysicsBody.collision_trace_flag"></a>

#### collision\_trace\_flag

```python
@collision_trace_flag.setter
def collision_trace_flag(value: CollisionTraceFlag) -> None
```

<a id="unreal.glTFRuntimePhysicsBody.physics_type"></a>

#### physics\_type

```python
@property
def physics_type() -> PhysicsType
```

(PhysicsType):  [Read-Write]

<a id="unreal.glTFRuntimePhysicsBody.physics_type"></a>

#### physics\_type

```python
@physics_type.setter
def physics_type(value: PhysicsType) -> None
```

<a id="unreal.glTFRuntimePhysicsBody.consider_for_bounds"></a>

#### consider\_for\_bounds

```python
@property
def consider_for_bounds() -> bool
```

(bool):  [Read-Write]

<a id="unreal.glTFRuntimePhysicsBody.consider_for_bounds"></a>

#### consider\_for\_bounds

```python
@consider_for_bounds.setter
def consider_for_bounds(value: bool) -> None
```

<a id="unreal.glTFRuntimePhysicsBody.capsule_collisions"></a>

#### capsule\_collisions

```python
@property
def capsule_collisions() -> Array[glTFRuntimeCapsule]
```

(Array[glTFRuntimeCapsule]):  [Read-Write]

<a id="unreal.glTFRuntimePhysicsBody.capsule_collisions"></a>

#### capsule\_collisions

```python
@capsule_collisions.setter
def capsule_collisions(value: Array[glTFRuntimeCapsule]) -> None
```

<a id="unreal.glTFRuntimePhysicsBody.sphere_collisions"></a>

#### sphere\_collisions

```python
@property
def sphere_collisions() -> Array[glTFRuntimeSphere]
```

(Array[glTFRuntimeSphere]):  [Read-Write]

<a id="unreal.glTFRuntimePhysicsBody.sphere_collisions"></a>

#### sphere\_collisions

```python
@sphere_collisions.setter
def sphere_collisions(value: Array[glTFRuntimeSphere]) -> None
```

<a id="unreal.glTFRuntimePhysicsBody.box_collisions"></a>

#### box\_collisions

```python
@property
def box_collisions() -> Array[Box]
```

(Array[Box]):  [Read-Write]

<a id="unreal.glTFRuntimePhysicsBody.box_collisions"></a>

#### box\_collisions

```python
@box_collisions.setter
def box_collisions(value: Array[Box]) -> None
```

<a id="unreal.glTFRuntimePhysicsBody.sphere_auto_collision"></a>

#### sphere\_auto\_collision

```python
@property
def sphere_auto_collision() -> bool
```

(bool):  [Read-Write]

<a id="unreal.glTFRuntimePhysicsBody.sphere_auto_collision"></a>

#### sphere\_auto\_collision

```python
@sphere_auto_collision.setter
def sphere_auto_collision(value: bool) -> None
```

<a id="unreal.glTFRuntimePhysicsBody.box_auto_collision"></a>

#### box\_auto\_collision

```python
@property
def box_auto_collision() -> bool
```

(bool):  [Read-Write]

<a id="unreal.glTFRuntimePhysicsBody.box_auto_collision"></a>

#### box\_auto\_collision

```python
@box_auto_collision.setter
def box_auto_collision(value: bool) -> None
```

<a id="unreal.glTFRuntimePhysicsBody.capsule_auto_collision"></a>

#### capsule\_auto\_collision

```python
@property
def capsule_auto_collision() -> bool
```

(bool):  [Read-Write]

<a id="unreal.glTFRuntimePhysicsBody.capsule_auto_collision"></a>

#### capsule\_auto\_collision

```python
@capsule_auto_collision.setter
def capsule_auto_collision(value: bool) -> None
```

<a id="unreal.glTFRuntimePhysicsBody.collision_scale"></a>

#### collision\_scale

```python
@property
def collision_scale() -> float
```

(float):  [Read-Write]

<a id="unreal.glTFRuntimePhysicsBody.collision_scale"></a>

#### collision\_scale

```python
@collision_scale.setter
def collision_scale(value: float) -> None
```

<a id="unreal.glTFRuntimePhysicsBody.disable_collision"></a>

#### disable\_collision

```python
@property
def disable_collision() -> bool
```

(bool):  [Read-Write]

<a id="unreal.glTFRuntimePhysicsBody.disable_collision"></a>

#### disable\_collision

```python
@disable_collision.setter
def disable_collision(value: bool) -> None
```

<a id="unreal.glTFRuntimePhysicsAssetAutoBodyConfig"></a>