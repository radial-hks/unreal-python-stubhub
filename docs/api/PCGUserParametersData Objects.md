## PCGUserParametersData Objects

```python
class PCGUserParametersData(PCGData)
```

PCG Data meant only to be used internally.
It contains a copy of UserParameters for a given graph instance, with overrides in it.
The idea is to have a structure to hold our overrides, provided by the override pins on the Subgraph
and use this as input to PCGUserParametersGetElement. By doing so, we are able to provide the right
parameters to the getter node.

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGUserParametersData.h

<a id="unreal.PCGVisualizeAttributeSettings"></a>