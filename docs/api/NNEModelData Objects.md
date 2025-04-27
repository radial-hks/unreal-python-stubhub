## NNEModelData Objects

```python
class NNEModelData(Object)
```

This class represents assets that store neural network model data.

Neural network models typically consist of a graph of operations and corresponding parameters as e.g. weights.
UNNEModelData assets store such model data as imported e.g. by the UNNEModelDataFactory class.
An INNERuntime object retrieved by UE::NNE::GetRuntime<T>(const FString& Name) can be used to create an inferable neural network model.

**C++ Source:**

- **Module**: NNE
- **File**: NNEModelData.h

<a id="unreal.NNEModelDataFactory"></a>