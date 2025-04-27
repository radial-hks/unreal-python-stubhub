## ModifyCurveAnimLibrary Objects

```python
class ModifyCurveAnimLibrary(BlueprintFunctionLibrary)
```

Exposes operations that can be run on a Modify Curve Node via Anim Node Functions such as "On Become Relevant" and "On Update".

**C++ Source:**

- **Module**: AnimGraphRuntime
- **File**: ModifyCurveLibrary.h

<a id="unreal.ModifyCurveAnimLibrary.set_curve_map"></a>

#### set_curve_map

```python
@classmethod
def set_curve_map(cls, modify_curve_node: ModifyCurveAnimNodeReference,
                  curve_map: Map[Name, float]) -> ModifyCurveAnimNodeReference
```

X.set_curve_map(modify_curve_node, curve_map) -> ModifyCurveAnimNodeReference
Set Curve Map

Args:
    modify_curve_node (ModifyCurveAnimNodeReference): 
    curve_map (Map[Name, float]): 

Returns:
    ModifyCurveAnimNodeReference:

<a id="unreal.ModifyCurveAnimLibrary.set_apply_mode"></a>

#### set_apply_mode

```python
@classmethod
def set_apply_mode(cls, modify_curve_node: ModifyCurveAnimNodeReference,
                   mode: ModifyCurveApplyMode) -> ModifyCurveAnimNodeReference
```

X.set_apply_mode(modify_curve_node, mode) -> ModifyCurveAnimNodeReference
Set Apply Mode

Args:
    modify_curve_node (ModifyCurveAnimNodeReference): 
    mode (ModifyCurveApplyMode): 

Returns:
    ModifyCurveAnimNodeReference:

<a id="unreal.ModifyCurveAnimLibrary.set_alpha"></a>

#### set_alpha

```python
@classmethod
def set_alpha(cls, modify_curve_node: ModifyCurveAnimNodeReference,
              alpha: float) -> ModifyCurveAnimNodeReference
```

X.set_alpha(modify_curve_node, alpha) -> ModifyCurveAnimNodeReference
Set Alpha

Args:
    modify_curve_node (ModifyCurveAnimNodeReference): 
    alpha (float): 

Returns:
    ModifyCurveAnimNodeReference:

<a id="unreal.ModifyCurveAnimLibrary.get_apply_mode"></a>

#### get_apply_mode

```python
@classmethod
def get_apply_mode(
        cls, modify_curve_node: ModifyCurveAnimNodeReference
) -> ModifyCurveApplyMode
```

X.get_apply_mode(modify_curve_node) -> ModifyCurveApplyMode
Get Apply Mode

Args:
    modify_curve_node (ModifyCurveAnimNodeReference): 

Returns:
    ModifyCurveApplyMode:

<a id="unreal.ModifyCurveAnimLibrary.get_alpha"></a>

#### get_alpha

```python
@classmethod
def get_alpha(cls, modify_curve_node: ModifyCurveAnimNodeReference) -> float
```

X.get_alpha(modify_curve_node) -> float
Get Alpha

Args:
    modify_curve_node (ModifyCurveAnimNodeReference): 

Returns:
    float:

<a id="unreal.ModifyCurveAnimLibrary.convert_to_modify_curve_node_pure"></a>

#### convert_to_modify_curve_node_pure

```python
@classmethod
def convert_to_modify_curve_node_pure(
        cls,
        node: AnimNodeReference) -> Tuple[ModifyCurveAnimNodeReference, bool]
```

X.convert_to_modify_curve_node_pure(node) -> (modify_curve_node=ModifyCurveAnimNodeReference, result=bool)
Get a modify curve context from an anim node context (pure)

Args:
    node (AnimNodeReference): 

Returns:
    tuple: 

    modify_curve_node (ModifyCurveAnimNodeReference): 

    result (bool):

<a id="unreal.ModifyCurveAnimLibrary.convert_to_modify_curve_node"></a>

#### convert_to_modify_curve_node

```python
@classmethod
def convert_to_modify_curve_node(
    cls, node: AnimNodeReference
) -> Tuple[ModifyCurveAnimNodeReference, AnimNodeReferenceConversionResult]
```

X.convert_to_modify_curve_node(node) -> (ModifyCurveAnimNodeReference, result=AnimNodeReferenceConversionResult)
Get a modify curve node context from an anim node context

Args:
    node (AnimNodeReference): 

Returns:
    AnimNodeReferenceConversionResult: 

    result (AnimNodeReferenceConversionResult):

<a id="unreal.PlayMontageCallbackProxy"></a>