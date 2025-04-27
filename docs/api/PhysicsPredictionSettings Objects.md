## PhysicsPredictionSettings Objects

```python
class PhysicsPredictionSettings(StructBase)
```

Physics Prediction Settings

**C++ Source:**

- **Module**: Engine
- **File**: PhysicsSettings.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``enable_physics_history_capture`` (bool):  [Read-Write] Enables FRewindData to cache physics history
  Note: This is not recommended for networked physics unless developing a custom resimulation solution since this starts caching physics on both client and server,
         instead only enable bEnablePhysicsPrediction which will automatically enable FRewindData caching on the client if needed by the chosen replication mode.
- ``enable_physics_prediction`` (bool):  [Read-Write] Enable networked physics prediction (experimental)
  This syncs the physics tick number between client and server and keeps it in sync via time dilation performed on the client, see APlayerController::GetPhysicsTimestamp().
  If an AActor::PhysicsReplicationMode is set to use Resimulation this will also enable RewindData to cache physics history on the client which is required by resimulation replication.
  IMPORTANT: Physics Prediction needs Physics -> Framerate -> Tick Physics Async enabled to function as intended.
- ``max_supported_latency_prediction`` (float):  [Read-Write] Amount of RTT (Round Trip Time) latency for the prediction to support in milliseconds.
- ``resimulation_settings`` (PhysicsReplicationResimulationSettings):  [Read-Write] Default settings for physics replication using EPhysicsReplicationMode::Resimulation.

<a id="unreal.PhysicsPredictionSettings.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.RigidBodyErrorCorrection"></a>