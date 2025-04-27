## PredictProjectilePathParams Objects

```python
class PredictProjectilePathParams(StructBase)
```

Input parameters to PredictProjectilePath functions.

**C++ Source:**

- **Module**: Engine
- **File**: GameplayStaticsTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``actors_to_ignore`` (Array[Actor]):  [Read-Write] Actors to ignore when tracing with collision.
- ``draw_debug_time`` (float):  [Read-Write] Duration of debug lines (only relevant for DrawDebugType::Duration)
- ``draw_debug_type`` (DrawDebugTrace):  [Read-Write] Debug drawing duration option.
- ``launch_velocity`` (Vector):  [Read-Write] Initial launch velocity at the start of the trace.
- ``max_sim_time`` (float):  [Read-Write] Maximum simulation time for the virtual projectile.
- ``object_types`` (Array[ObjectTypeQuery]):  [Read-Write] Object type to use, if tracing with collision.
- ``override_gravity_z`` (float):  [Read-Write] Optional override of Gravity (if 0, uses WorldGravityZ).
- ``projectile_radius`` (float):  [Read-Write] Projectile radius, used when tracing for collision. If <= 0, a line trace is used instead.
- ``sim_frequency`` (float):  [Read-Write] Determines size of each sub-step in the simulation (chopping up MaxSimTime). Recommended between 10 to 30 depending on desired quality versus performance.
- ``start_location`` (Vector):  [Read-Write] Location of the start of the trace.
- ``trace_channel`` (CollisionChannel):  [Read-Write] Trace channel to use, if tracing with collision.
- ``trace_complex`` (bool):  [Read-Write] Trace against complex collision (triangles rather than simple primitives) if tracing with collision.
- ``trace_with_channel`` (bool):  [Read-Write] Whether or not to use TraceChannel, if tracing with collision.
- ``trace_with_collision`` (bool):  [Read-Write] Whether to trace along the path looking for blocking collision and stopping at the first hit.

<a id="unreal.PredictProjectilePathParams.__init__"></a>

#### __init__

```python
def __init__(
        start_location: Vector = [0.000000, 0.000000, 0.000000],
        launch_velocity: Vector = [0.000000, 0.000000, 0.000000],
        trace_with_collision: bool = False,
        projectile_radius: float = 0.000000,
        max_sim_time: float = 0.000000,
        trace_with_channel: bool = False,
        trace_channel: CollisionChannel = CollisionChannel.ECC_WORLD_STATIC,
        object_types: Array[ObjectTypeQuery] = [],
        actors_to_ignore: Array[Actor] = [],
        sim_frequency: float = 0.000000,
        override_gravity_z: float = 0.000000,
        draw_debug_type: DrawDebugTrace = DrawDebugTrace.NONE,
        draw_debug_time: float = 0.000000,
        trace_complex: bool = False) -> None
```

<a id="unreal.PredictProjectilePathParams.start_location"></a>

#### start_location

```python
@property
def start_location() -> Vector
```

(Vector):  [Read-Write] Location of the start of the trace.

<a id="unreal.PredictProjectilePathParams.start_location"></a>

#### start_location

```python
@start_location.setter
def start_location(value: Vector) -> None
```

<a id="unreal.PredictProjectilePathParams.launch_velocity"></a>

#### launch_velocity

```python
@property
def launch_velocity() -> Vector
```

(Vector):  [Read-Write] Initial launch velocity at the start of the trace.

<a id="unreal.PredictProjectilePathParams.launch_velocity"></a>

#### launch_velocity

```python
@launch_velocity.setter
def launch_velocity(value: Vector) -> None
```

<a id="unreal.PredictProjectilePathParams.trace_with_collision"></a>

#### trace_with_collision

```python
@property
def trace_with_collision() -> bool
```

(bool):  [Read-Write] Whether to trace along the path looking for blocking collision and stopping at the first hit.

<a id="unreal.PredictProjectilePathParams.trace_with_collision"></a>

#### trace_with_collision

```python
@trace_with_collision.setter
def trace_with_collision(value: bool) -> None
```

<a id="unreal.PredictProjectilePathParams.projectile_radius"></a>

#### projectile_radius

```python
@property
def projectile_radius() -> float
```

(float):  [Read-Write] Projectile radius, used when tracing for collision. If <= 0, a line trace is used instead.

<a id="unreal.PredictProjectilePathParams.projectile_radius"></a>

#### projectile_radius

```python
@projectile_radius.setter
def projectile_radius(value: float) -> None
```

<a id="unreal.PredictProjectilePathParams.max_sim_time"></a>

#### max_sim_time

```python
@property
def max_sim_time() -> float
```

(float):  [Read-Write] Maximum simulation time for the virtual projectile.

<a id="unreal.PredictProjectilePathParams.max_sim_time"></a>

#### max_sim_time

```python
@max_sim_time.setter
def max_sim_time(value: float) -> None
```

<a id="unreal.PredictProjectilePathParams.trace_with_channel"></a>

#### trace_with_channel

```python
@property
def trace_with_channel() -> bool
```

(bool):  [Read-Write] Whether or not to use TraceChannel, if tracing with collision.

<a id="unreal.PredictProjectilePathParams.trace_with_channel"></a>

#### trace_with_channel

```python
@trace_with_channel.setter
def trace_with_channel(value: bool) -> None
```

<a id="unreal.PredictProjectilePathParams.trace_channel"></a>

#### trace_channel

```python
@property
def trace_channel() -> CollisionChannel
```

(CollisionChannel):  [Read-Write] Trace channel to use, if tracing with collision.

<a id="unreal.PredictProjectilePathParams.trace_channel"></a>

#### trace_channel

```python
@trace_channel.setter
def trace_channel(value: CollisionChannel) -> None
```

<a id="unreal.PredictProjectilePathParams.object_types"></a>

#### object_types

```python
@property
def object_types() -> Array[ObjectTypeQuery]
```

(Array[ObjectTypeQuery]):  [Read-Write] Object type to use, if tracing with collision.

<a id="unreal.PredictProjectilePathParams.object_types"></a>

#### object_types

```python
@object_types.setter
def object_types(value: Array[ObjectTypeQuery]) -> None
```

<a id="unreal.PredictProjectilePathParams.actors_to_ignore"></a>

#### actors_to_ignore

```python
@property
def actors_to_ignore() -> Array[Actor]
```

(Array[Actor]):  [Read-Write] Actors to ignore when tracing with collision.

<a id="unreal.PredictProjectilePathParams.actors_to_ignore"></a>

#### actors_to_ignore

```python
@actors_to_ignore.setter
def actors_to_ignore(value: Array[Actor]) -> None
```

<a id="unreal.PredictProjectilePathParams.sim_frequency"></a>

#### sim_frequency

```python
@property
def sim_frequency() -> float
```

(float):  [Read-Write] Determines size of each sub-step in the simulation (chopping up MaxSimTime). Recommended between 10 to 30 depending on desired quality versus performance.

<a id="unreal.PredictProjectilePathParams.sim_frequency"></a>

#### sim_frequency

```python
@sim_frequency.setter
def sim_frequency(value: float) -> None
```

<a id="unreal.PredictProjectilePathParams.override_gravity_z"></a>

#### override_gravity_z

```python
@property
def override_gravity_z() -> float
```

(float):  [Read-Write] Optional override of Gravity (if 0, uses WorldGravityZ).

<a id="unreal.PredictProjectilePathParams.override_gravity_z"></a>

#### override_gravity_z

```python
@override_gravity_z.setter
def override_gravity_z(value: float) -> None
```

<a id="unreal.PredictProjectilePathParams.draw_debug_type"></a>

#### draw_debug_type

```python
@property
def draw_debug_type() -> DrawDebugTrace
```

(DrawDebugTrace):  [Read-Write] Debug drawing duration option.

<a id="unreal.PredictProjectilePathParams.draw_debug_type"></a>

#### draw_debug_type

```python
@draw_debug_type.setter
def draw_debug_type(value: DrawDebugTrace) -> None
```

<a id="unreal.PredictProjectilePathParams.draw_debug_time"></a>

#### draw_debug_time

```python
@property
def draw_debug_time() -> float
```

(float):  [Read-Write] Duration of debug lines (only relevant for DrawDebugType::Duration)

<a id="unreal.PredictProjectilePathParams.draw_debug_time"></a>

#### draw_debug_time

```python
@draw_debug_time.setter
def draw_debug_time(value: float) -> None
```

<a id="unreal.PredictProjectilePathParams.trace_complex"></a>

#### trace_complex

```python
@property
def trace_complex() -> bool
```

(bool):  [Read-Write] Trace against complex collision (triangles rather than simple primitives) if tracing with collision.

<a id="unreal.PredictProjectilePathParams.trace_complex"></a>

#### trace_complex

```python
@trace_complex.setter
def trace_complex(value: bool) -> None
```

<a id="unreal.PredictProjectilePathPointData"></a>