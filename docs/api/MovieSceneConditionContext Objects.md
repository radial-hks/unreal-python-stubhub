## MovieSceneConditionContext Objects

```python
class MovieSceneConditionContext(StructBase)
```

* Blueprint-friendly struct containing any context needed to evaluate conditions.

**C++ Source:**

- **Module**: MovieScene
- **File**: MovieSceneCondition.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``binding`` (MovieSceneBindingProxy):  [Read-Write] Binding for the bound object currently evaluating this condition if applicable (BindingId will be invalid for conditions on global tracks/sections).
- ``bound_objects`` (Array[Object]):  [Read-Write] Array of objects bound to the binding currently evaluating this condition if applicable (will be empty for conditions on global tracks/sections)
- ``world_context`` (Object):  [Read-Write] The world context

<a id="unreal.MovieSceneConditionContext.__init__"></a>

#### __init__

```python
def __init__(world_context: Object = None,
             binding: MovieSceneBindingProxy = [[], None],
             bound_objects: Array[Object] = []) -> None
```

<a id="unreal.MovieSceneConditionContext.world_context"></a>

#### world_context

```python
@property
def world_context() -> Object
```

(Object):  [Read-Write] The world context

<a id="unreal.MovieSceneConditionContext.world_context"></a>

#### world_context

```python
@world_context.setter
def world_context(value: Object) -> None
```

<a id="unreal.MovieSceneConditionContext.binding"></a>

#### binding

```python
@property
def binding() -> MovieSceneBindingProxy
```

(MovieSceneBindingProxy):  [Read-Write] Binding for the bound object currently evaluating this condition if applicable (BindingId will be invalid for conditions on global tracks/sections).

<a id="unreal.MovieSceneConditionContext.binding"></a>

#### binding

```python
@binding.setter
def binding(value: MovieSceneBindingProxy) -> None
```

<a id="unreal.MovieSceneConditionContext.bound_objects"></a>

#### bound_objects

```python
@property
def bound_objects() -> Array[Object]
```

(Array[Object]):  [Read-Write] Array of objects bound to the binding currently evaluating this condition if applicable (will be empty for conditions on global tracks/sections)

<a id="unreal.MovieSceneConditionContext.bound_objects"></a>

#### bound_objects

```python
@bound_objects.setter
def bound_objects(value: Array[Object]) -> None
```

<a id="unreal.MovieSceneConditionContainer"></a>