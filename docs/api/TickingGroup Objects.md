## TickingGroup Objects

```python
class TickingGroup(EnumBase)
```

Determines which ticking group a tick function belongs to.

**C++ Source:**

- **Module**: Engine
- **File**: EngineBaseTypes.h

<a id="unreal.TickingGroup.TG_PRE_PHYSICS"></a>

#### TG_PRE_PHYSICS

0: Any item that needs to be executed before physics simulation starts.

<a id="unreal.TickingGroup.TG_DURING_PHYSICS"></a>

#### TG_DURING_PHYSICS

2: Any item that can be run in parallel with our physics simulation work.

<a id="unreal.TickingGroup.TG_POST_PHYSICS"></a>

#### TG_POST_PHYSICS

4: Any item that needs rigid body and cloth simulation to be complete before being executed.

<a id="unreal.TickingGroup.TG_POST_UPDATE_WORK"></a>

#### TG_POST_UPDATE_WORK

5: Any item that needs the update work to be done before being ticked.

<a id="unreal.TemperatureSeverityType"></a>