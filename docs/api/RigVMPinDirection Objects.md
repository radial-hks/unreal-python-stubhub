## RigVMPinDirection Objects

```python
class RigVMPinDirection(EnumBase)
```

The Pin Direction is used to differentiate different kinds of
pins in the data flow graph - inputs, outputs etc.

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVMFunction.h

<a id="unreal.RigVMPinDirection.INPUT"></a>

#### INPUT

0

<a id="unreal.RigVMPinDirection.OUTPUT"></a>

#### OUTPUT

1: A const input value

<a id="unreal.RigVMPinDirection.IO"></a>

#### IO

2: A mutable output value

<a id="unreal.RigVMPinDirection.VISIBLE"></a>

#### VISIBLE

3: A mutable input and output value

<a id="unreal.RigVMPinDirection.HIDDEN"></a>

#### HIDDEN

4: A const value that cannot be connected to

<a id="unreal.RigVMPinDirection.INVALID"></a>

#### INVALID

5: A mutable hidden value (used for interal state)

<a id="unreal.RigVMFunctionArgumentDirection"></a>