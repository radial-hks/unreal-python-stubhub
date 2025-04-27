## AnimFunctionCallSite Objects

```python
class AnimFunctionCallSite(EnumBase)
```

When to call the function during the execution of the animation graph

**C++ Source:**

- **Module**: AnimGraphRuntime
- **File**: AnimNode_CallFunction.h

<a id="unreal.AnimFunctionCallSite.ON_INITIALIZE"></a>

#### ON_INITIALIZE

0: Called when the node is initialized - i.e. it becomes weighted/relevant in the graph (before child nodes are initialized)

<a id="unreal.AnimFunctionCallSite.ON_UPDATE"></a>

#### ON_UPDATE

1: Called when the node is updated (before child nodes are updated)

<a id="unreal.AnimFunctionCallSite.ON_BECOME_RELEVANT"></a>

#### ON_BECOME_RELEVANT

2: Called when the node is updated for the first time with a valid weight

<a id="unreal.AnimFunctionCallSite.ON_EVALUATE"></a>

#### ON_EVALUATE

3: Called when the node is evaluated (before child nodes are evaluated)

<a id="unreal.AnimFunctionCallSite.ON_INITIALIZE_POST_RECURSION"></a>

#### ON_INITIALIZE_POST_RECURSION

4: Called when the node is initialized - i.e. it becomes weighted/relevant in the graph (after child nodes are initialized)

<a id="unreal.AnimFunctionCallSite.ON_UPDATE_POST_RECURSION"></a>

#### ON_UPDATE_POST_RECURSION

5: Called when the node is updated (after child nodes are updated)

<a id="unreal.AnimFunctionCallSite.ON_BECOME_RELEVANT_POST_RECURSION"></a>

#### ON_BECOME_RELEVANT_POST_RECURSION

6: Called when the node is updated for the first time with a valid weight (after child nodes are updated)

<a id="unreal.AnimFunctionCallSite.ON_EVALUATE_POST_RECURSION"></a>

#### ON_EVALUATE_POST_RECURSION

7: Called when the node is evaluated (after child nodes are evaluated)

<a id="unreal.AnimFunctionCallSite.ON_STARTED_BLENDING_OUT"></a>

#### ON_STARTED_BLENDING_OUT

8: Called when the node is updated, was at full weight and beings to blend out. Called before child nodes are
updated

<a id="unreal.AnimFunctionCallSite.ON_STARTED_BLENDING_IN"></a>

#### ON_STARTED_BLENDING_IN

9: Called when the node is updated, was at zero weight and beings to blend in. Called before child nodes are updated

<a id="unreal.AnimFunctionCallSite.ON_FINISHED_BLENDING_IN"></a>

#### ON_FINISHED_BLENDING_IN

11: Called when the node is updated, was at non-zero weight and becomes full weight. Called before child nodes are
updated

<a id="unreal.LayeredBoneBlendMode"></a>