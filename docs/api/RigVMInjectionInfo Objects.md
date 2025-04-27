## RigVMInjectionInfo Objects

```python
class RigVMInjectionInfo(Object)
```

The Injected Info is used for injecting a node on a pin.
Injected nodes are not visible to the user, but they are normal
nodes on the graph.

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVMDeveloper
- **File**: RigVMPin.h

<a id="unreal.RigVMInjectionInfo.get_pin"></a>

#### get_pin

```python
def get_pin() -> RigVMPin
```

x.get_pin() -> RigVMPin
Returns the pin of this injected node.

Returns:
    RigVMPin:

<a id="unreal.RigVMInjectionInfo.get_graph"></a>

#### get_graph

```python
def get_graph() -> RigVMGraph
```

x.get_graph() -> RigVMGraph
Returns the graph of this injected node.

Returns:
    RigVMGraph:

<a id="unreal.RigVMPin"></a>