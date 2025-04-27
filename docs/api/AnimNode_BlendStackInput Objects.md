## AnimNode_BlendStackInput Objects

```python
class AnimNode_BlendStackInput(AnimNode_Base)
```

Input pose that links the blend stack's sample graph with the sample/pose chosen by the blend stack.
Todo:: It might be better to reuse FAnimNode_LinkedInputPose, since we will most likely need variable input pins in the future too.

**C++ Source:**

- **Plugin**: BlendStack
- **Module**: BlendStack
- **File**: AnimNode_BlendStackInput.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``override_play_rate`` (bool):  [Read-Write] If true, the PlayRate input from thos node will override the SequencePlayer or BlendSpacePlayer playrate each frame
- ``play_rate`` (float):  [Read-Write] The play rate multiplier. Can be negative, which will cause the animation to play in reverse.

<a id="unreal.AnimNode_BlendStackInput.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.RigVMBlueprintLoadLogEntry"></a>