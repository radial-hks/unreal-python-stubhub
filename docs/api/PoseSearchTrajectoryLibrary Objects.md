## PoseSearchTrajectoryLibrary Objects

```python
class PoseSearchTrajectoryLibrary(BlueprintFunctionLibrary)
```

Set of functions to help populate a FPoseSearchQueryTrajectory for motion matching.

**C++ Source:**

- **Plugin**: PoseSearch
- **Module**: PoseSearch
- **File**: PoseSearchTrajectoryLibrary.h

<a id="unreal.PoseSearchTrajectoryLibrary.pose_search_generate_trajectory"></a>

#### pose_search_generate_trajectory

```python
@classmethod
def pose_search_generate_trajectory(
    cls,
    anim_instance: Object,
    trajectory_data: PoseSearchTrajectoryData,
    delta_time: float,
    out_trajectory: PoseSearchQueryTrajectory,
    out_desired_controller_yaw_last_update: float,
    history_sampling_interval: float = 0.040000,
    trajectory_history_count: int = 10,
    prediction_sampling_interval: float = 0.200000,
    trajectory_prediction_count: int = 8
) -> Tuple[PoseSearchQueryTrajectory, float, PoseSearchQueryTrajectory]
```

X.pose_search_generate_trajectory(anim_instance, trajectory_data, delta_time, out_trajectory, out_desired_controller_yaw_last_update, history_sampling_interval=0.040000, trajectory_history_count=10, prediction_sampling_interval=0.200000, trajectory_prediction_count=8) -> (out_trajectory=PoseSearchQueryTrajectory, out_desired_controller_yaw_last_update=float, out_trajectory=PoseSearchQueryTrajectory)

todo:: rename InAnimInstance into Context, since it can now be either an AnimInstance or a Character Generates a prediction trajectory based of the current character intent. For use with Character actors.

Args:
    anim_instance (Object): 
    trajectory_data (PoseSearchTrajectoryData): 
    delta_time (float): 
    out_trajectory (PoseSearchQueryTrajectory): 
    out_desired_controller_yaw_last_update (float): 
    history_sampling_interval (float): 
    trajectory_history_count (int32): 
    prediction_sampling_interval (float): 
    trajectory_prediction_count (int32): 

Returns:
    tuple: 

    out_trajectory (PoseSearchQueryTrajectory): 

    out_desired_controller_yaw_last_update (float): 

    out_trajectory (PoseSearchQueryTrajectory):

<a id="unreal.PoseSearchTrajectoryLibrary.pose_search_generate_predictor_trajectory"></a>

#### pose_search_generate_predictor_trajectory

```python
@classmethod
def pose_search_generate_predictor_trajectory(
    cls,
    predictor: Object,
    trajectory_data: PoseSearchTrajectoryData,
    delta_time: float,
    out_trajectory: PoseSearchQueryTrajectory,
    out_desired_controller_yaw_last_update: float,
    history_sampling_interval: float = 0.040000,
    trajectory_history_count: int = 10,
    prediction_sampling_interval: float = 0.200000,
    trajectory_prediction_count: int = 8
) -> Tuple[PoseSearchQueryTrajectory, float, PoseSearchQueryTrajectory]
```

X.pose_search_generate_predictor_trajectory(predictor, trajectory_data, delta_time, out_trajectory, out_desired_controller_yaw_last_update, history_sampling_interval=0.040000, trajectory_history_count=10, prediction_sampling_interval=0.200000, trajectory_prediction_count=8) -> (out_trajectory=PoseSearchQueryTrajectory, out_desired_controller_yaw_last_update=float, out_trajectory=PoseSearchQueryTrajectory)
Generates a prediction trajectory based of the current movement intent. For use with predictors. InPredictor must implement IPoseSearchTrajectoryPredictorInterface

Args:
    predictor (Object): 
    trajectory_data (PoseSearchTrajectoryData): 
    delta_time (float): 
    out_trajectory (PoseSearchQueryTrajectory): 
    out_desired_controller_yaw_last_update (float): 
    history_sampling_interval (float): 
    trajectory_history_count (int32): 
    prediction_sampling_interval (float): 
    trajectory_prediction_count (int32): 

Returns:
    tuple: 

    out_trajectory (PoseSearchQueryTrajectory): 

    out_desired_controller_yaw_last_update (float): 

    out_trajectory (PoseSearchQueryTrajectory):

<a id="unreal.PoseSearchTrajectoryLibrary.handle_trajectory_world_collisions_with_gravity"></a>

#### handle_trajectory_world_collisions_with_gravity

```python
@classmethod
def handle_trajectory_world_collisions_with_gravity(
    cls,
    world_context_object: Object,
    trajectory: PoseSearchQueryTrajectory,
    starting_velocity: Vector,
    apply_gravity: bool,
    gravity_accel: Vector,
    floor_collisions_offset: float,
    trace_channel: TraceTypeQuery,
    trace_complex: bool,
    actors_to_ignore: Array[Actor],
    draw_debug_type: DrawDebugTrace,
    ignore_self: bool = True,
    max_obstacle_height: float = 10000.000000,
    trace_color: LinearColor = [1.000000, 0.000000, 0.000000, 1.000000],
    trace_hit_color: LinearColor = [0.000000, 1.000000, 0.000000, 1.000000],
    draw_time: float = 5.000000
) -> Tuple[PoseSearchQueryTrajectory,
           PoseSearchTrajectory_WorldCollisionResults]
```

X.handle_trajectory_world_collisions_with_gravity(world_context_object, trajectory, starting_velocity, apply_gravity, gravity_accel, floor_collisions_offset, trace_channel, trace_complex, actors_to_ignore, draw_debug_type, ignore_self=True, max_obstacle_height=10000.000000, trace_color=[1.000000, 0.000000, 0.000000, 1.000000], trace_hit_color=[0.000000, 1.000000, 0.000000, 1.000000], draw_time=5.000000) -> (out_trajectory=PoseSearchQueryTrajectory, collision_result=PoseSearchTrajectory_WorldCollisionResults)
Experimental: Process InTrajectory to apply gravity and handle collisions. Eventually returns the modified OutTrajectory.
If bApplyGravity is true, GravityAccel will be applied.
If FloorCollisionsOffset > 0, vertical collision will be performed to every sample of the trajectory to have the samples float over the geometry (by FloorCollisionsOffset).

Args:
    world_context_object (Object): 
    trajectory (PoseSearchQueryTrajectory): 
    starting_velocity (Vector): 
    apply_gravity (bool): 
    gravity_accel (Vector): 
    floor_collisions_offset (float): 
    trace_channel (TraceTypeQuery): 
    trace_complex (bool): 
    actors_to_ignore (Array[Actor]): 
    draw_debug_type (DrawDebugTrace): 
    ignore_self (bool): 
    max_obstacle_height (float): 
    trace_color (LinearColor): 
    trace_hit_color (LinearColor): 
    draw_time (float): 

Returns:
    tuple: 

    out_trajectory (PoseSearchQueryTrajectory): 

    collision_result (PoseSearchTrajectory_WorldCollisionResults):

<a id="unreal.PoseSearchTrajectoryLibrary.handle_trajectory_world_collisions"></a>

#### handle_trajectory_world_collisions

```python
@classmethod
def handle_trajectory_world_collisions(
    cls,
    world_context_object: Object,
    anim_instance: AnimInstance,
    trajectory: PoseSearchQueryTrajectory,
    apply_gravity: bool,
    floor_collisions_offset: float,
    trace_channel: TraceTypeQuery,
    trace_complex: bool,
    actors_to_ignore: Array[Actor],
    draw_debug_type: DrawDebugTrace,
    ignore_self: bool = True,
    max_obstacle_height: float = 10000.000000,
    trace_color: LinearColor = [1.000000, 0.000000, 0.000000, 1.000000],
    trace_hit_color: LinearColor = [0.000000, 1.000000, 0.000000, 1.000000],
    draw_time: float = 5.000000
) -> Tuple[PoseSearchQueryTrajectory,
           PoseSearchTrajectory_WorldCollisionResults]
```

X.handle_trajectory_world_collisions(world_context_object, anim_instance, trajectory, apply_gravity, floor_collisions_offset, trace_channel, trace_complex, actors_to_ignore, draw_debug_type, ignore_self=True, max_obstacle_height=10000.000000, trace_color=[1.000000, 0.000000, 0.000000, 1.000000], trace_hit_color=[0.000000, 1.000000, 0.000000, 1.000000], draw_time=5.000000) -> (out_trajectory=PoseSearchQueryTrajectory, collision_result=PoseSearchTrajectory_WorldCollisionResults)
Experimental: Process InTrajectory to apply gravity and handle collisions. Eventually returns the modified OutTrajectory.
If bApplyGravity is true, gravity from the UCharacterMovementComponent will be applied.
If FloorCollisionsOffset > 0, vertical collision will be performed to every sample of the trajectory to have the samples float over the geometry (by FloorCollisionsOffset).

Args:
    world_context_object (Object): 
    anim_instance (AnimInstance): 
    trajectory (PoseSearchQueryTrajectory): 
    apply_gravity (bool): 
    floor_collisions_offset (float): 
    trace_channel (TraceTypeQuery): 
    trace_complex (bool): 
    actors_to_ignore (Array[Actor]): 
    draw_debug_type (DrawDebugTrace): 
    ignore_self (bool): 
    max_obstacle_height (float): 
    trace_color (LinearColor): 
    trace_hit_color (LinearColor): 
    draw_time (float): 

Returns:
    tuple: 

    out_trajectory (PoseSearchQueryTrajectory): 

    collision_result (PoseSearchTrajectory_WorldCollisionResults):

<a id="unreal.PoseSearchTrajectoryLibrary.get_transform"></a>

#### get_transform

```python
@classmethod
def get_transform(
        cls, trajectory_sample: PoseSearchQueryTrajectorySample) -> Transform
```

X.get_transform(trajectory_sample) -> Transform
Get Transform

Args:
    trajectory_sample (PoseSearchQueryTrajectorySample): 

Returns:
    Transform:

<a id="unreal.PoseSearchTrajectoryLibrary.get_trajectory_velocity"></a>

#### get_trajectory_velocity

```python
@classmethod
def get_trajectory_velocity(cls,
                            trajectory: PoseSearchQueryTrajectory,
                            time1: float,
                            time2: float,
                            extrapolate: bool = False) -> Vector
```

X.get_trajectory_velocity(trajectory, time1, time2, extrapolate=False) -> Vector
Get Trajectory Velocity

Args:
    trajectory (PoseSearchQueryTrajectory): 
    time1 (float): 
    time2 (float): 
    extrapolate (bool): 

Returns:
    Vector: 

    out_velocity (Vector):

<a id="unreal.PoseSearchTrajectoryLibrary.get_trajectory_sample_at_time"></a>

#### get_trajectory_sample_at_time

```python
@classmethod
def get_trajectory_sample_at_time(
        cls,
        trajectory: PoseSearchQueryTrajectory,
        time: float,
        extrapolate: bool = False) -> PoseSearchQueryTrajectorySample
```

X.get_trajectory_sample_at_time(trajectory, time, extrapolate=False) -> PoseSearchQueryTrajectorySample
Get Trajectory Sample at Time

Args:
    trajectory (PoseSearchQueryTrajectory): 
    time (float): 
    extrapolate (bool): 

Returns:
    PoseSearchQueryTrajectorySample: 

    out_trajectory_sample (PoseSearchQueryTrajectorySample):

<a id="unreal.PoseSearchTrajectoryLibrary.get_trajectory_angular_velocity"></a>

#### get_trajectory_angular_velocity

```python
@classmethod
def get_trajectory_angular_velocity(cls,
                                    trajectory: PoseSearchQueryTrajectory,
                                    time1: float,
                                    time2: float,
                                    extrapolate: bool = False) -> Vector
```

X.get_trajectory_angular_velocity(trajectory, time1, time2, extrapolate=False) -> Vector
Get Trajectory Angular Velocity

Args:
    trajectory (PoseSearchQueryTrajectory): 
    time1 (float): 
    time2 (float): 
    extrapolate (bool): 

Returns:
    Vector: 

    out_angular_velocity (Vector):

<a id="unreal.PoseSearchTrajectoryLibrary.draw_trajectory"></a>

#### draw_trajectory

```python
@classmethod
def draw_trajectory(cls, world_context_object: Object,
                    trajectory: PoseSearchQueryTrajectory,
                    debug_thickness: float, height_offset: float) -> None
```

X.draw_trajectory(world_context_object, trajectory, debug_thickness, height_offset) -> None
Draw Trajectory

Args:
    world_context_object (Object): 
    trajectory (PoseSearchQueryTrajectory): 
    debug_thickness (float): 
    height_offset (float):

<a id="unreal.PoseSearchTrajectoryPredictorInterface"></a>