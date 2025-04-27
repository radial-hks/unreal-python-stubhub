## EngineCustomTimeStep Objects

```python
class EngineCustomTimeStep(Object)
```

A CustomTimeStep control the Engine Framerate/Timestep.
This will update the FApp::CurrentTime/FApp::DeltaTime.
This is useful when you want the engine to be synchronized with an external clock (genlock).

**C++ Source:**

- **Module**: Engine
- **File**: EngineCustomTimeStep.h

<a id="unreal.FixedFrameRateCustomTimeStep"></a>