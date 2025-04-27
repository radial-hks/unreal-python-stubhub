## AISense_Prediction Objects

```python
class AISense_Prediction(AISense)
```

AISense Prediction

**C++ Source:**

- **Module**: AIModule
- **File**: AISense_Prediction.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``auto_register_all_pawns_as_sources`` (bool):  [Read-Write] If true all newly spawned pawns will get auto registered as source for this sense.
- ``notify_type`` (AISenseNotifyType):  [Read-Write]
- ``wants_new_pawn_notification`` (bool):  [Read-Write] whether this sense is interested in getting notified about new Pawns being spawned
      this can be used for example for automated sense sources registration

<a id="unreal.AISense_Prediction.request_pawn_prediction_event"></a>

#### request_pawn_prediction_event

```python
@classmethod
def request_pawn_prediction_event(cls, requestor: Pawn, predicted_actor: Actor,
                                  prediction_time: float) -> None
```

X.request_pawn_prediction_event(requestor, predicted_actor, prediction_time) -> None
Asks perception system to supply Requestor with PredictedActor's predicted location in PredictionTime seconds
    Location is being predicted based on PredicterActor's current location and velocity

Args:
    requestor (Pawn): 
    predicted_actor (Actor): 
    prediction_time (float):

<a id="unreal.AISense_Prediction.request_controller_prediction_event"></a>

#### request_controller_prediction_event

```python
@classmethod
def request_controller_prediction_event(cls, requestor: AIController,
                                        predicted_actor: Actor,
                                        prediction_time: float) -> None
```

X.request_controller_prediction_event(requestor, predicted_actor, prediction_time) -> None
Asks perception system to supply Requestor with PredictedActor's predicted location in PredictionTime seconds
    Location is being predicted based on PredicterActor's current location and velocity

Args:
    requestor (AIController): 
    predicted_actor (Actor): 
    prediction_time (float):

<a id="unreal.AISense_Sight"></a>