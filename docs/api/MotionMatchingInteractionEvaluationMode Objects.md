## MotionMatchingInteractionEvaluationMode Objects

```python
class MotionMatchingInteractionEvaluationMode(EnumBase)
```

EMotion Matching Interaction Evaluation Mode

**C++ Source:**

- **Plugin**: PoseSearch
- **Module**: PoseSearch
- **File**: AnimNode_MotionMatchingInteraction.h

<a id="unreal.MotionMatchingInteractionEvaluationMode.CONTINUOUS_RESELECTION"></a>

#### CONTINUOUS_RESELECTION

0: Node will continuously provide its availabilities and eventually blend to newly selected animations

<a id="unreal.MotionMatchingInteractionEvaluationMode.SINGLE_SELECTION"></a>

#### SINGLE_SELECTION

1: Node will continuously provide its availabilities to keep the interaction alive, but will play only the first selected animation
the idea is to let the animation play until the end and allow the evenutual state machine playing this node to be able to perform an automatic transition

<a id="unreal.PoseSearchMirrorOption"></a>