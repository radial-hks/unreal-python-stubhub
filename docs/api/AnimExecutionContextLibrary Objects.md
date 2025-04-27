## AnimExecutionContextLibrary Objects

```python
class AnimExecutionContextLibrary(BlueprintFunctionLibrary)
```

Exposes operations to be performed on anim node contexts

**C++ Source:**

- **Module**: AnimGraphRuntime
- **File**: AnimExecutionContextLibrary.h

<a id="unreal.AnimExecutionContextLibrary.is_active"></a>

#### is_active

```python
@classmethod
def is_active(cls, context: AnimExecutionContext) -> bool
```

X.is_active(context) -> bool
Get whether this branch of the graph is active (i.e. NOT blending out).

Args:
    context (AnimExecutionContext): 

Returns:
    bool:

<a id="unreal.AnimExecutionContextLibrary.get_delta_time"></a>

#### get_delta_time

```python
@classmethod
def get_delta_time(cls, context: AnimUpdateContext) -> float
```

X.get_delta_time(context) -> float
Get the current delta time in seconds

Args:
    context (AnimUpdateContext): 

Returns:
    float:

<a id="unreal.AnimExecutionContextLibrary.get_current_weight"></a>

#### get_current_weight

```python
@classmethod
def get_current_weight(cls, context: AnimUpdateContext) -> float
```

X.get_current_weight(context) -> float
Get the current weight of this branch of the graph

Args:
    context (AnimUpdateContext): 

Returns:
    float:

<a id="unreal.AnimExecutionContextLibrary.get_anim_instance"></a>

#### get_anim_instance

```python
@classmethod
def get_anim_instance(cls, context: AnimExecutionContext) -> AnimInstance
```

X.get_anim_instance(context) -> AnimInstance
Get the anim instance that hosts this context

Args:
    context (AnimExecutionContext): 

Returns:
    AnimInstance:

<a id="unreal.AnimExecutionContextLibrary.convert_to_update_context"></a>

#### convert_to_update_context

```python
@classmethod
def convert_to_update_context(
    cls, context: AnimExecutionContext
) -> Tuple[AnimUpdateContext, AnimExecutionContextConversionResult]
```

X.convert_to_update_context(context) -> (AnimUpdateContext, result=AnimExecutionContextConversionResult)
Convert to an update context

Args:
    context (AnimExecutionContext): 

Returns:
    AnimExecutionContextConversionResult: 

    result (AnimExecutionContextConversionResult):

<a id="unreal.AnimExecutionContextLibrary.convert_to_pose_context"></a>

#### convert_to_pose_context

```python
@classmethod
def convert_to_pose_context(
    cls, context: AnimExecutionContext
) -> Tuple[AnimPoseContext, AnimExecutionContextConversionResult]
```

X.convert_to_pose_context(context) -> (AnimPoseContext, result=AnimExecutionContextConversionResult)
Convert to a pose context

Args:
    context (AnimExecutionContext): 

Returns:
    AnimExecutionContextConversionResult: 

    result (AnimExecutionContextConversionResult):

<a id="unreal.AnimExecutionContextLibrary.convert_to_initialization_context"></a>

#### convert_to_initialization_context

```python
@classmethod
def convert_to_initialization_context(
    cls, context: AnimExecutionContext
) -> Tuple[AnimInitializationContext, AnimExecutionContextConversionResult]
```

X.convert_to_initialization_context(context) -> (AnimInitializationContext, result=AnimExecutionContextConversionResult)
Convert to an initialization context

Args:
    context (AnimExecutionContext): 

Returns:
    AnimExecutionContextConversionResult: 

    result (AnimExecutionContextConversionResult):

<a id="unreal.AnimExecutionContextLibrary.convert_to_component_space_pose_context"></a>

#### convert_to_component_space_pose_context

```python
@classmethod
def convert_to_component_space_pose_context(
    cls, context: AnimExecutionContext
) -> Tuple[AnimComponentSpacePoseContext,
           AnimExecutionContextConversionResult]
```

X.convert_to_component_space_pose_context(context) -> (AnimComponentSpacePoseContext, result=AnimExecutionContextConversionResult)
Convert to a component space pose context

Args:
    context (AnimExecutionContext): 

Returns:
    AnimExecutionContextConversionResult: 

    result (AnimExecutionContextConversionResult):

<a id="unreal.AnimNotify"></a>