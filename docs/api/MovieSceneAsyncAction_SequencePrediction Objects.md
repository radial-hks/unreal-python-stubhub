## MovieSceneAsyncAction_SequencePrediction Objects

```python
class MovieSceneAsyncAction_SequencePrediction(BlueprintAsyncActionBase)
```

Async BP action that represents a pending prediction that is dispatched on a playing sequence.

**C++ Source:**

- **Module**: MovieSceneTracks
- **File**: MovieScenePredictionSystem.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``failure`` (MovieSceneActorPredictionFailure):  [Read-Write] Called when a message is broadcast on the specified channel. Use GetPayload() to request the message payload.
- ``result`` (MovieSceneActorPredictionResult):  [Read-Write] Called when a message is broadcast on the specified channel. Use GetPayload() to request the message payload.

<a id="unreal.MovieSceneAsyncAction_SequencePrediction.result"></a>

#### result

```python
@property
def result() -> MovieSceneActorPredictionResult
```

(MovieSceneActorPredictionResult):  [Read-Write] Called when a message is broadcast on the specified channel. Use GetPayload() to request the message payload.

<a id="unreal.MovieSceneAsyncAction_SequencePrediction.result"></a>

#### result

```python
@result.setter
def result(value: MovieSceneActorPredictionResult) -> None
```

<a id="unreal.MovieSceneAsyncAction_SequencePrediction.failure"></a>

#### failure

```python
@property
def failure() -> MovieSceneActorPredictionFailure
```

(MovieSceneActorPredictionFailure):  [Read-Write] Called when a message is broadcast on the specified channel. Use GetPayload() to request the message payload.

<a id="unreal.MovieSceneAsyncAction_SequencePrediction.failure"></a>

#### failure

```python
@failure.setter
def failure(value: MovieSceneActorPredictionFailure) -> None
```

<a id="unreal.MovieSceneAsyncAction_SequencePrediction.predict_world_transform_at_time"></a>

#### predict_world_transform_at_time

```python
@classmethod
def predict_world_transform_at_time(
        cls, player: MovieSceneSequencePlayer,
        target_component: SceneComponent,
        time_in_seconds: float) -> MovieSceneAsyncAction_SequencePrediction
```

X.predict_world_transform_at_time(player, target_component, time_in_seconds) -> MovieSceneAsyncAction_SequencePrediction
Initiate an asynchronous prediction for the specified component's world transform at a specific time in a sequence
Changes in attachment between the sequence's current time, and the predicted time are not accounted for
Calling this function on a stopped sequence player is undefined.

Args:
    player (MovieSceneSequencePlayer): An active, currently playing sequence player to use for predicting the transform
    target_component (SceneComponent): The component to predict a world transform for
    time_in_seconds (float): The time within the sequence to predict the transform at

Returns:
    MovieSceneAsyncAction_SequencePrediction: An asynchronous prediction object that contains Result and Failure delegates

<a id="unreal.MovieSceneAsyncAction_SequencePrediction.predict_world_transform_at_frame"></a>

#### predict_world_transform_at_frame

```python
@classmethod
def predict_world_transform_at_frame(
        cls, player: MovieSceneSequencePlayer,
        target_component: SceneComponent,
        frame_time: FrameTime) -> MovieSceneAsyncAction_SequencePrediction
```

X.predict_world_transform_at_frame(player, target_component, frame_time) -> MovieSceneAsyncAction_SequencePrediction
Initiate an asynchronous prediction for the specified component's world transform at a specific time in a sequence
Changes in attachment between the sequence's current time, and the predicted time are not accounted for
Calling this function on a stopped sequence player is undefined.

Args:
    player (MovieSceneSequencePlayer): An active, currently playing sequence player to use for predicting the transform
    target_component (SceneComponent): The component to predict a world transform for
    frame_time (FrameTime): The frame time to predict at in the sequence's display rate

Returns:
    MovieSceneAsyncAction_SequencePrediction: An asynchronous prediction object that contains Result and Failure delegates

<a id="unreal.MovieSceneAsyncAction_SequencePrediction.predict_local_transform_at_time"></a>

#### predict_local_transform_at_time

```python
@classmethod
def predict_local_transform_at_time(
        cls, player: MovieSceneSequencePlayer,
        target_component: SceneComponent,
        time_in_seconds: float) -> MovieSceneAsyncAction_SequencePrediction
```

X.predict_local_transform_at_time(player, target_component, time_in_seconds) -> MovieSceneAsyncAction_SequencePrediction
Initiate an asynchronous prediction for the specified component's local transform at a specific time in a sequence
Changes in attachment between the sequence's current time, and the predicted time are not accounted for
Calling this function on a stopped sequence player is undefined.

Args:
    player (MovieSceneSequencePlayer): An active, currently playing sequence player to use for predicting the transform
    target_component (SceneComponent): The component to predict a world transform for
    time_in_seconds (float): The time within the sequence to predict the transform at

Returns:
    MovieSceneAsyncAction_SequencePrediction: An asynchronous prediction object that contains Result and Failure delegates

<a id="unreal.MovieSceneAsyncAction_SequencePrediction.predict_local_transform_at_frame"></a>

#### predict_local_transform_at_frame

```python
@classmethod
def predict_local_transform_at_frame(
        cls, player: MovieSceneSequencePlayer,
        target_component: SceneComponent,
        frame_time: FrameTime) -> MovieSceneAsyncAction_SequencePrediction
```

X.predict_local_transform_at_frame(player, target_component, frame_time) -> MovieSceneAsyncAction_SequencePrediction
Initiate an asynchronous prediction for the specified component's local transform at a specific time in a sequence
Changes in attachment between the sequence's current time, and the predicted time are not accounted for
Calling this function on a stopped sequence player is undefined.

Args:
    player (MovieSceneSequencePlayer): An active, currently playing sequence player to use for predicting the transform
    target_component (SceneComponent): The component to predict a world transform for
    frame_time (FrameTime): The frame time to predict at in the sequence's display rate

Returns:
    MovieSceneAsyncAction_SequencePrediction: An asynchronous prediction object that contains Result and Failure delegates

<a id="unreal.MovieScene3DConstraintTrack"></a>