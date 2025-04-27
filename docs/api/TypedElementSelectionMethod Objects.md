## TypedElementSelectionMethod Objects

```python
class TypedElementSelectionMethod(EnumBase)
```

ETyped Element Selection Method

**C++ Source:**

- **Module**: TypedElementRuntime
- **File**: TypedElementSelectionInterface.h

<a id="unreal.TypedElementSelectionMethod.PRIMARY"></a>

#### PRIMARY

0: Select the "primary" element (eg, a component would favor selecting its owner actor)

<a id="unreal.TypedElementSelectionMethod.SECONDARY"></a>

#### SECONDARY

1: Select the "secondary" element (eg, a component would favor selecting itself)

<a id="unreal.TypedElementSelectionMethod.FROM_SECONDARY"></a>

#### FROM_SECONDARY

2: The "secondary" element is choosing to pass back up the chain (eg. an ISM was selected, but we want to traverse back to the parent element)

<a id="unreal.TwoPlayerSplitScreenType"></a>