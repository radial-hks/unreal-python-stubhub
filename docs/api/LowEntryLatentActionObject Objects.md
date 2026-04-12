## LowEntryLatentActionObject Objects

```python
class LowEntryLatentActionObject(Object)
```

Low Entry Latent Action Object

**C++ Source:**

- **Plugin**: LowEntryExtStdLib
- **Module**: LowEntryExtendedStandardLibrary
- **File**: LowEntryLatentActionObject.h

<a id="unreal.LowEntryLatentActionObject.wait_till_done"></a>

#### wait\_till\_done

```python
def wait_till_done(world_context_object: Object,
                   latent_info: LatentActionInfo) -> Object
```

x.wait_till_done(world_context_object, latent_info) -> Object
Waits till the latent action is done.

Args:
    world_context_object (Object): 
    latent_info (LatentActionInfo): 

Returns:
    Object: 

    result (Object):

<a id="unreal.LowEntryLatentActionObject.is_done"></a>

#### is\_done

```python
def is_done() -> bool
```

x.is_done() -> bool
Returns true if the latent action is done.

Returns:
    bool:

<a id="unreal.LowEntryLatentActionObject.get_result"></a>

#### get\_result

```python
def get_result() -> Object
```

x.get_result() -> Object
Returns the result.

Returns:
    Object: 

    result (Object):

<a id="unreal.LowEntryLatentActionObject.done"></a>

#### done

```python
def done(result: Object) -> None
```

x.done(result) -> None
Causes the latent action to be done.

Args:
    result (Object):

<a id="unreal.LowEntryLatentActionString"></a>