## DataflowBlueprintLibrary Objects

```python
class DataflowBlueprintLibrary(BlueprintFunctionLibrary)
```

Dataflow Blueprint Library

**C++ Source:**

- **Module**: DataflowEngine
- **File**: DataflowBlueprintLibrary.h

<a id="unreal.DataflowBlueprintLibrary.evaluate_terminal_node_by_name"></a>

#### evaluate_terminal_node_by_name

```python
@classmethod
def evaluate_terminal_node_by_name(cls, dataflow: Dataflow,
                                   terminal_node_name: Name,
                                   result_asset: Object) -> None
```

X.evaluate_terminal_node_by_name(dataflow, terminal_node_name, result_asset) -> None
Find a specific terminal node by name evaluate it using a specific UObject

Args:
    dataflow (Dataflow): 
    terminal_node_name (Name): 
    result_asset (Object):

<a id="unreal.EdGraph"></a>