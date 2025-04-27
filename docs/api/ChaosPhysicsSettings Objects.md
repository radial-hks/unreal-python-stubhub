## ChaosPhysicsSettings Objects

```python
class ChaosPhysicsSettings(StructBase)
```

Settings container for Chaos physics engine settings, accessed in Chaos through a setting provider interface.
See: IChaosSettingsProvider

**C++ Source:**

- **Module**: Engine
- **File**: PhysicsSettings.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``dedicated_thread_buffer_mode`` (ChaosBufferMode):  [Read-Write] The buffering mode to use when running with a dedicated thread
- ``dedicated_thread_tick_mode`` (ChaosSolverTickMode):  [Read-Write] The framerate/timestep ticking mode when running with a dedicated thread
- ``default_threading_model`` (ChaosThreadingMode):  [Read-Write] Default threading model to use on module initialisation. Can be switched at runtime using p.Chaos.ThreadingModel

<a id="unreal.ChaosPhysicsSettings.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.PrimaryAssetRules"></a>