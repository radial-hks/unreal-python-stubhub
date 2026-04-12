## EvaluatorMode Objects

```python
class EvaluatorMode(EnumBase)
```

Determines the behavior this node will use when updating and evaluating.

**C++ Source:**

- **Module**: Engine
- **File**: AnimNode_TransitionPoseEvaluator.h

<a id="unreal.EvaluatorMode.EM_STANDARD"></a>

#### EM\_STANDARD

0: DataSource is ticked and evaluated every frame.

<a id="unreal.EvaluatorMode.EM_FREEZE"></a>

#### EM\_FREEZE

1: DataSource is never ticked and only evaluated on the first frame. Every frame after uses the cached pose from the first frame.

<a id="unreal.EvaluatorMode.EM_DELAYED_FREEZE"></a>

#### EM\_DELAYED\_FREEZE

2: DataSource is ticked and evaluated for a given number of frames, then freezes after and uses the cached pose for future frames.

<a id="unreal.MirrorRowType"></a>