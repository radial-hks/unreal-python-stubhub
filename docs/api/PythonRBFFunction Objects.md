## PythonRBFFunction Objects

```python
class PythonRBFFunction(Object)
```

Python RBFFunction

**C++ Source:**

- **Plugin**: TAPython
- **Module**: TAPython
- **File**: PythonRBFLib.h

<a id="unreal.PythonRBFFunction.slove"></a>

#### slove

```python
def slove(
        rbf_input: PythonRBFValues,
        log: bool = False) -> Tuple[PythonRBFValues, Array[int], Array[float]]
```

x.slove(rbf_input, log=False) -> (PythonRBFValues, out_weight_indices=Array[int32], out_weights=Array[float])
Slove

Args:
    rbf_input (PythonRBFValues): 
    log (bool): 

Returns:
    tuple: 

    out_weight_indices (Array[int32]): 

    out_weights (Array[float]):

<a id="unreal.PythonRBFValues"></a>