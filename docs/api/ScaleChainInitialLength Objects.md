## ScaleChainInitialLength Objects

```python
class ScaleChainInitialLength(EnumBase)
```

EScale Chain Initial Length

**C++ Source:**

- **Module**: AnimGraphRuntime
- **File**: AnimNode_ScaleChainLength.h

<a id="unreal.ScaleChainInitialLength.FIXED_DEFAULT_LENGTH_VALUE"></a>

#### FIXED_DEFAULT_LENGTH_VALUE

0: Use the 'DefaultChainLength' input value.

<a id="unreal.ScaleChainInitialLength.DISTANCE"></a>

#### DISTANCE

1: Use distance between 'ChainStartBone' and 'ChainEndBone' (in Component Space)

<a id="unreal.ScaleChainInitialLength.CHAIN_LENGTH"></a>

#### CHAIN_LENGTH

2: Use animated chain length (length in local space of every bone from 'ChainStartBone' to 'ChainEndBone'

<a id="unreal.WarpingEvaluationMode"></a>