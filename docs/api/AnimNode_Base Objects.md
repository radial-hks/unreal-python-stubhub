## AnimNode_Base Objects

```python
class AnimNode_Base(StructBase)
```

This is the base of all runtime animation nodes

To create a new animation node:
  Create a struct derived from FAnimNode_Base - this is your runtime node
  Create a class derived from UAnimGraphNode_Base, containing an instance of your runtime node as a member - this is your visual/editor-only node

**C++ Source:**

- **Module**: Engine
- **File**: AnimNodeBase.h

<a id="unreal.AnimNode_Base.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.AnimNode_BlendSpaceGraphBase"></a>