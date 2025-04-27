## SkeletalControlLibrary Objects

```python
class SkeletalControlLibrary(BlueprintFunctionLibrary)
```

Exposes operations to be performed on a skeletal control anim node
Note: Experimental and subject to change!

**C++ Source:**

- **Module**: AnimGraphRuntime
- **File**: SkeletalControlLibrary.h

<a id="unreal.SkeletalControlLibrary.set_alpha"></a>

#### set_alpha

```python
@classmethod
def set_alpha(cls, skeletal_control: SkeletalControlReference,
              alpha: float) -> SkeletalControlReference
```

X.set_alpha(skeletal_control, alpha) -> SkeletalControlReference
Set the alpha value of this skeletal control

Args:
    skeletal_control (SkeletalControlReference): 
    alpha (float): 

Returns:
    SkeletalControlReference:

<a id="unreal.SkeletalControlLibrary.get_alpha"></a>

#### get_alpha

```python
@classmethod
def get_alpha(cls, skeletal_control: SkeletalControlReference) -> float
```

X.get_alpha(skeletal_control) -> float
Get the alpha value of this skeletal control

Args:
    skeletal_control (SkeletalControlReference): 

Returns:
    float:

<a id="unreal.SkeletalControlLibrary.convert_to_skeletal_control_pure"></a>

#### convert_to_skeletal_control_pure

```python
@classmethod
def convert_to_skeletal_control_pure(
        cls, node: AnimNodeReference) -> Tuple[SkeletalControlReference, bool]
```

X.convert_to_skeletal_control_pure(node) -> (skeletal_control=SkeletalControlReference, result=bool)
Get a skeletal control from an anim node (pure)

Args:
    node (AnimNodeReference): 

Returns:
    tuple: 

    skeletal_control (SkeletalControlReference): 

    result (bool):

<a id="unreal.SkeletalControlLibrary.convert_to_skeletal_control"></a>

#### convert_to_skeletal_control

```python
@classmethod
def convert_to_skeletal_control(
    cls, node: AnimNodeReference
) -> Tuple[SkeletalControlReference, AnimNodeReferenceConversionResult]
```

X.convert_to_skeletal_control(node) -> (SkeletalControlReference, result=AnimNodeReferenceConversionResult)
Get a skeletal control from an anim node

Args:
    node (AnimNodeReference): 

Returns:
    AnimNodeReferenceConversionResult: 

    result (AnimNodeReferenceConversionResult):

<a id="unreal.MovieSceneTransformOrigin"></a>