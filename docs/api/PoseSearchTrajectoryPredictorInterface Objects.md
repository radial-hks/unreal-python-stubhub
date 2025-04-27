## PoseSearchTrajectoryPredictorInterface Objects

```python
class PoseSearchTrajectoryPredictorInterface(Interface)
```

Pose Search Trajectory Predictor Interface

**C++ Source:**

- **Plugin**: PoseSearch
- **Module**: PoseSearch
- **File**: PoseSearchTrajectoryPredictor.h

<a id="unreal.PoseSearchTrajectoryPredictorInterface.predict"></a>

#### predict

```python
def predict(num_prediction_samples: int, seconds_per_prediction_sample: float,
            num_history_samples: int) -> PoseSearchQueryTrajectory
```

x.predict(num_prediction_samples, seconds_per_prediction_sample, num_history_samples) -> PoseSearchQueryTrajectory
Predict

Args:
    num_prediction_samples (int32): 
    seconds_per_prediction_sample (float): 
    num_history_samples (int32): 

Returns:
    PoseSearchQueryTrajectory: 

    out_trajectory (PoseSearchQueryTrajectory):

<a id="unreal.PoseSearchTrajectoryPredictorInterface.get_velocity"></a>

#### get_velocity

```python
def get_velocity() -> Vector
```

x.get_velocity() -> Vector
Get Velocity

Returns:
    Vector: 

    out_velocity (Vector):

<a id="unreal.PoseSearchTrajectoryPredictorInterface.get_gravity"></a>

#### get_gravity

```python
def get_gravity() -> Vector
```

x.get_gravity() -> Vector
Get Gravity

Returns:
    Vector: 

    out_gravity_accel (Vector):

<a id="unreal.PoseSearchTrajectoryPredictorInterface.get_current_state"></a>

#### get_current_state

```python
def get_current_state() -> Tuple[Vector, Quat, Vector]
```

x.get_current_state() -> (out_position=Vector, out_facing=Quat, out_velocity=Vector)
Get Current State

Returns:
    tuple: 

    out_position (Vector): 

    out_facing (Quat): 

    out_velocity (Vector):

<a id="unreal.AnimNotifyState_PoseSearchBase"></a>