## LowEntryLatentActionInteger Objects

```python
class LowEntryLatentActionInteger(Object)
```

Low Entry Latent Action Integer

**C++ Source:**

- **Plugin**: LowEntryExtStdLib
- **Module**: LowEntryExtendedStandardLibrary
- **File**: LowEntryLatentActionInteger.h

<a id="unreal.LowEntryLatentActionInteger.wait_till_done"></a>

#### wait\_till\_done

```python
def wait_till_done(world_context_object: Object,
                   latent_info: LatentActionInfo) -> int
```

x.wait_till_done(world_context_object, latent_info) -> int32
Waits till the latent action is done.

Args:
    world_context_object (Object): 
    latent_info (LatentActionInfo): 

Returns:
    int32: 

    result (int32):

<a id="unreal.LowEntryLatentActionInteger.is_done"></a>

#### is\_done

```python
def is_done() -> bool
```

x.is_done() -> bool
Returns true if the latent action is done.

Returns:
    bool:

<a id="unreal.LowEntryLatentActionInteger.get_result"></a>

#### get\_result

```python
def get_result() -> int
```

x.get_result() -> int32
Returns the result.

Returns:
    int32: 

    result (int32):

<a id="unreal.LowEntryLatentActionInteger.done"></a>

#### done

```python
def done(result: int) -> None
```

x.done(result) -> None
Causes the latent action to be done.

Args:
    result (int32):

<a id="unreal.LowEntryLatentActionNone"></a>