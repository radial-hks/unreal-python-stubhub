## LowEntryLatentActionBoolean Objects

```python
class LowEntryLatentActionBoolean(Object)
```

Low Entry Latent Action Boolean

**C++ Source:**

- **Plugin**: LowEntryExtStdLib
- **Module**: LowEntryExtendedStandardLibrary
- **File**: LowEntryLatentActionBoolean.h

<a id="unreal.LowEntryLatentActionBoolean.wait_till_done"></a>

#### wait\_till\_done

```python
def wait_till_done(world_context_object: Object,
                   latent_info: LatentActionInfo) -> bool
```

x.wait_till_done(world_context_object, latent_info) -> bool
Waits till the latent action is done.

Args:
    world_context_object (Object): 
    latent_info (LatentActionInfo): 

Returns:
    bool: 

    result (bool):

<a id="unreal.LowEntryLatentActionBoolean.is_done"></a>

#### is\_done

```python
def is_done() -> bool
```

x.is_done() -> bool
Returns true if the latent action is done.

Returns:
    bool:

<a id="unreal.LowEntryLatentActionBoolean.get_result"></a>

#### get\_result

```python
def get_result() -> bool
```

x.get_result() -> bool
Returns the result.

Returns:
    bool: 

    result (bool):

<a id="unreal.LowEntryLatentActionBoolean.done"></a>

#### done

```python
def done(result: bool) -> None
```

x.done(result) -> None
Causes the latent action to be done.

Args:
    result (bool):

<a id="unreal.LowEntryLatentActionFloat"></a>