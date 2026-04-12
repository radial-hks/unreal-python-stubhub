## TargetingTraceType Objects

```python
class TargetingTraceType(EnumBase)
```

enum: ETargetingTraceType determines the shape of the trace used.

**C++ Source:**

- **Plugin**: TargetingSystem
- **Module**: TargetingSystem
- **File**: TargetingSelectionTask_Trace.h

<a id="unreal.TargetingTraceType.LINE"></a>

#### LINE

0

<a id="unreal.TargetingTraceType.SPHERE"></a>

#### SPHERE

1

<a id="unreal.TargetingTraceType.CAPSULE"></a>

#### CAPSULE

2: With zero rotation, the capsule length runs along the trace's up vector (the cross product of the trace's forward vector and the trace's forward vector flattened onto the XY plane and rotated 90 degrees around the Z vector).

<a id="unreal.TargetingTraceType.BOX"></a>

#### BOX

3

<a id="unreal.SmartObjectTagMergingPolicy"></a>