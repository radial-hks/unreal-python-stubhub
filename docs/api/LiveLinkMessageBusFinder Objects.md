## LiveLinkMessageBusFinder Objects

```python
class LiveLinkMessageBusFinder(Object)
```

Asset for finding available Message Bus Sources.

**C++ Source:**

- **Plugin**: LiveLink
- **Module**: LiveLink
- **File**: LiveLinkMessageBusFinder.h

<a id="unreal.LiveLinkMessageBusFinder.get_available_providers"></a>

#### get_available_providers

```python
def get_available_providers(
        world_context_object: Object,
        latent_info: LatentActionInfo,
        duration: float = 0.200000) -> Array[ProviderPollResult]
```

x.get_available_providers(world_context_object, latent_info, duration=0.200000) -> Array[ProviderPollResult]
* Broadcasts a message to the network and returns a list of all providers who replied within a set amount of time.
*
*

Args:
    world_context_object (Object): 
    latent_info (LatentActionInfo): 
    duration (float): The amount of time to wait for replies in seconds

Returns:
    Array[ProviderPollResult]: 

    available_providers (Array[ProviderPollResult]): Will contain the collection of found Message Bus Providers. *

<a id="unreal.LiveLinkMessageBusFinder.construct_message_bus_finder"></a>

#### construct_message_bus_finder

```python
@classmethod
def construct_message_bus_finder(cls) -> LiveLinkMessageBusFinder
```

X.construct_message_bus_finder() -> LiveLinkMessageBusFinder
* Constructs a new Message Bus Finder which enables you to detect available Message Bus Providers on the network
*
*

Returns:
    LiveLinkMessageBusFinder: The newly constructed Message Bus Finder

<a id="unreal.LiveLinkMessageBusFinder.connect_to_provider"></a>

#### connect_to_provider

```python
@classmethod
def connect_to_provider(
    cls, provider: ProviderPollResult
) -> Tuple[ProviderPollResult, LiveLinkSourceHandle]
```

X.connect_to_provider(provider) -> (provider=ProviderPollResult, source_handle=LiveLinkSourceHandle)
* Connects to a given Message Bus Provider and returns a handle to the created LiveLink Source
*
*

Args:
    provider (ProviderPollResult): The provider to connect to. *

Returns:
    tuple: 

    provider (ProviderPollResult): The provider to connect to. *

    source_handle (LiveLinkSourceHandle): A handle to the created LiveLink Source, lets you query information about the created source and request a shutdown

<a id="unreal.LiveLinkPreset"></a>