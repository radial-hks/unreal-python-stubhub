## MVVMExecutionMode Objects

```python
class MVVMExecutionMode(EnumBase)
```

EMVVMExecution Mode

**C++ Source:**

- **Plugin**: ModelViewViewModel
- **Module**: ModelViewViewModel
- **File**: MVVMExecutionMode.h

<a id="unreal.MVVMExecutionMode.IMMEDIATE"></a>

#### IMMEDIATE

0: Execute the binding as soon as the source value changes.

<a id="unreal.MVVMExecutionMode.DELAYED"></a>

#### DELAYED

1: Execute the binding at the end of the frame before drawing when the source value changes.

<a id="unreal.MVVMExecutionMode.TICK"></a>

#### TICK

2: Always execute the binding at the end of the frame.

<a id="unreal.MVVMExecutionMode.DELAYED_WHEN_SHARED_ELSE_IMMEDIATE"></a>

#### DELAYED_WHEN_SHARED_ELSE_IMMEDIATE

3: When the binding can be triggered from multiple fields, use Delayed. Else, uses Immediate.

<a id="unreal.TypedElementSelectionMethod"></a>