## RigVMActionStack Objects

```python
class RigVMActionStack(Object)
```

The Action Stack can be used to track actions happening on a
Graph. Currently the only owner of the ActionStack is the Controller.
Actions can be added to the stack, or they can be understood as
scopes / brackets. For this you can use BeginAction / EndAction / CancelAction
to open / close a bracket. Open brackets automatically record additional
actions occuring during the bracket's lifetime.

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVMDeveloper
- **File**: RigVMControllerActions.h

<a id="unreal.ComputeDataInterface"></a>