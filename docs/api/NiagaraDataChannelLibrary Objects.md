## NiagaraDataChannelLibrary Objects

```python
class NiagaraDataChannelLibrary(BlueprintFunctionLibrary)
```

A C++ and Blueprint accessible library of utility functions for accessing Niagara DataChannel

**C++ Source:**

- **Plugin**: Niagara
- **Module**: Niagara
- **File**: NiagaraDataChannel.h

<a id="unreal.NiagaraDataChannelLibrary.write_to_niagara_data_channel"></a>

#### write_to_niagara_data_channel

```python
@classmethod
def write_to_niagara_data_channel(
        cls, world_context_object: Object, channel: NiagaraDataChannelAsset,
        search_params: NiagaraDataChannelSearchParameters, count: int,
        visible_to_game: bool, visible_to_cpu: bool, visible_to_gpu: bool,
        debug_source: str) -> NiagaraDataChannelWriter
```

X.write_to_niagara_data_channel(world_context_object, channel, search_params, count, visible_to_game, visible_to_cpu, visible_to_gpu, debug_source) -> NiagaraDataChannelWriter
Initializes and returns the Niagara Data Channel writer to write N elements to the given data channel.

Args:
    world_context_object (Object): World to execute in
    channel (NiagaraDataChannelAsset): The channel to write to
    search_params (NiagaraDataChannelSearchParameters): Parameters used when retrieving a specific set of Data Channel Data to read or write like the islands data channel type.
    count (int32): The number of elements to write
    visible_to_game (bool): If true, the data written to this data channel is visible to Blueprint and C++ logic reading from it
    visible_to_cpu (bool): If true, the data written to this data channel is visible to Niagara CPU emitters
    visible_to_gpu (bool): If true, the data written to this data channel is visible to Niagara GPU emitters
    debug_source (str): Instigator for this write, used in the debug hud to track writes to the data channel from different sources

Returns:
    NiagaraDataChannelWriter:

<a id="unreal.NiagaraDataChannelLibrary.read_from_niagara_data_channel"></a>

#### read_from_niagara_data_channel

```python
@classmethod
def read_from_niagara_data_channel(
        cls, world_context_object: Object, channel: NiagaraDataChannelAsset,
        search_params: NiagaraDataChannelSearchParameters,
        read_previous_frame: bool) -> NiagaraDataChannelReader
```

X.read_from_niagara_data_channel(world_context_object, channel, search_params, read_previous_frame) -> NiagaraDataChannelReader
Initializes and returns the Niagara Data Channel reader for the given data channel.

Args:
    world_context_object (Object): World to execute in
    channel (NiagaraDataChannelAsset): The channel to read from
    search_params (NiagaraDataChannelSearchParameters): Parameters used when retrieving a specific set of Data Channel Data to read or write like the islands data channel type.
    read_previous_frame (bool): True if this reader will read the previous frame's data. If false, we read the current frame. Reading the current frame allows for zero latency reads, but any data elements that are generated after this reader is used are missed. Reading the previous frame's data introduces a frame of latency but ensures we never miss any data as we have access to the whole frame.

Returns:
    NiagaraDataChannelReader:

<a id="unreal.NiagaraDataChannelLibrary.get_data_channel_element_count"></a>

#### get_data_channel_element_count

```python
@classmethod
def get_data_channel_element_count(
        cls,
        world_context_object: Object,
        channel: NiagaraDataChannelAsset,
        search_params: NiagaraDataChannelSearchParameters,
        read_previous_frame: bool = True) -> int
```

X.get_data_channel_element_count(world_context_object, channel, search_params, read_previous_frame=True) -> int32
Returns the number of readable elements in the given data channel

Args:
    world_context_object (Object): World to execute in
    channel (NiagaraDataChannelAsset): The channel to read from
    search_params (NiagaraDataChannelSearchParameters): Parameters used when retrieving a specific set of Data Channel Data to read or write like the islands data channel type.
    read_previous_frame (bool): True if this reader will read the previous frame's data. If false, we read the current frame. Reading the current frame allows for zero latency reads, but any data elements that are generated after this reader is used are missed. Reading the previous frame's data introduces a frame of latency but ensures we never miss any data as we have access to the whole frame.

Returns:
    int32:

<a id="unreal.NiagaraDataInterfaceRWBase"></a>