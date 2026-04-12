## PythonRBFLib Objects

```python
class PythonRBFLib(BlueprintFunctionLibrary)
```

Python RBFLib

**C++ Source:**

- **Plugin**: TAPython
- **Module**: TAPython
- **File**: PythonRBFLib.h

<a id="unreal.PythonRBFLib.set_rbf_params_deminsion"></a>

#### set\_rbf\_params\_deminsion

```python
@classmethod
def set_rbf_params_deminsion(cls, rbf_params: RBFParams,
                             dimensions: int) -> RBFParams
```

X.set_rbf_params_deminsion(rbf_params, dimensions) -> RBFParams
Set RBFParams Deminsion

Args:
    rbf_params (RBFParams): 
    dimensions (int32): 

Returns:
    RBFParams:

<a id="unreal.PythonRBFLib.rbf_fun"></a>

#### rbf\_fun

```python
@classmethod
def rbf_fun(cls, rbf_params: RBFParams,
            targets: Array[PythonRBFTarget]) -> PythonRBFFunction
```

X.rbf_fun(rbf_params, targets) -> PythonRBFFunction
RBFFun

Args:
    rbf_params (RBFParams): 
    targets (Array[PythonRBFTarget]): 

Returns:
    PythonRBFFunction:

<a id="unreal.PythonStructLib"></a>