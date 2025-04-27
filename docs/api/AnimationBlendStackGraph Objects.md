## AnimationBlendStackGraph Objects

```python
class AnimationBlendStackGraph(AnimationGraph)
```

Animation graph used for blend stacks.
    The result node is the root of the blend graph.
    The input node is dynamically linked to the blend stack's sample pose.

**C++ Source:**

- **Plugin**: BlendStack
- **Module**: BlendStackEditor
- **File**: AnimationBlendStackGraph.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``blend_options`` (AnimGraphBlendOptions):  [Read-Write] Blending options for animation graphs in Linked Animation Blueprints.

<a id="unreal.AnimGraphNode_BlendStack_Base"></a>