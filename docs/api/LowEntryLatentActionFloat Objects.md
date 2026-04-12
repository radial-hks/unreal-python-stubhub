## LowEntryLatentActionFloat Objects

```python
class LowEntryLatentActionFloat(Object)
```

Low Entry Latent Action Float

**C++ Source:**

- **Plugin**: LowEntryExtStdLib
- **Module**: LowEntryExtendedStandardLibrary
- **File**: LowEntryLatentActionFloat.h

<a id="unreal.LowEntryLatentActionFloat.wait_till_done"></a>

#### wait\_till\_done

```python
def wait_till_done(world_context_object: Object,
                   latent_info: LatentActionInfo) -> float
```

x.wait_till_done(world_context_object, latent_info) -> double
Waits till the latent action is done.

Args:
    world_context_object (Object): 
    latent_info (LatentActionInfo): 

Returns:
    double: 

    result (double):

<a id="unreal.LowEntryLatentActionFloat.is_done"></a>

#### is\_done

```python
def is_done() -> bool
```

x.is_done() -> bool
Returns true if the latent action is done.

Returns:
    bool:

<a id="unreal.LowEntryLatentActionFloat.get_result"></a>

#### get\_result

```python
def get_result() -> float
```

x.get_result() -> double
Returns the result.

Returns:
    double: 

    result (double):

<a id="unreal.LowEntryLatentActionFloat.done"></a>

#### done

```python
def done(result: float) -> None
```

x.done(result) -> None
Causes the latent action to be done.

Args:
    result (double):

<a id="unreal.LowEntryLatentActionInteger"></a>