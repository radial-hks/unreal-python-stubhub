## MovieSceneBoundObjectProxy Objects

```python
class MovieSceneBoundObjectProxy(Interface)
```

Movie Scene Bound Object Proxy

**C++ Source:**

- **Module**: MovieScene
- **File**: IMovieSceneBoundObjectProxy.h

<a id="unreal.MovieSceneBoundObjectProxy.bp_get_bound_object_for_sequencer"></a>

#### bp_get_bound_object_for_sequencer

```python
def bp_get_bound_object_for_sequencer(resolved_object: Object) -> Object
```

x.bp_get_bound_object_for_sequencer(resolved_object) -> Object
Retrieve the bound object that this interface wants to animate. Could be 'this' or a transient child object.

Args:
    resolved_object (Object): 

Returns:
    Object: Pointer to the object that should be animated, or nullptr if it's not valid.

<a id="unreal.MovieSceneBindingEventReceiverInterface"></a>