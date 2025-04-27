## TickFunction Objects

```python
class TickFunction(StructBase)
```

Abstract Base class for all tick functions.

**C++ Source:**

- **Module**: Engine
- **File**: EngineBaseTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``allow_tick_on_dedicated_server`` (bool):  [Read-Write] If we allow this tick to run on a dedicated server
- ``end_tick_group`` (TickingGroup):  [Read-Write] Defines the tick group that this tick function must finish in. These groups determine the relative order of when objects tick during a frame update.
  see: ETickingGroup
- ``start_with_tick_enabled`` (bool):  [Read-Write] If true, this tick function will start enabled, but can be disabled later on.
- ``tick_even_when_paused`` (bool):  [Read-Write] Bool indicating that this function should execute even if the game is paused. Pause ticks are very limited in capabilities. *
- ``tick_group`` (TickingGroup):  [Read-Write] Defines the minimum tick group for this tick function. These groups determine the relative order of when objects tick during a frame update.
  Given prerequisites, the tick may be delayed.
  see: ETickingGroup
  see: FTickFunction::AddPrerequisite()
- ``tick_interval`` (float):  [Read-Write] The frequency in seconds at which this tick function will be executed.  If less than or equal to 0 then it will tick every frame

<a id="unreal.TickFunction.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.ActorTickFunction"></a>