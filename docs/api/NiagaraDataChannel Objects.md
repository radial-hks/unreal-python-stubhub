## NiagaraDataChannel Objects

```python
class NiagaraDataChannel(Object)
```

Niagara Data Channel

**C++ Source:**

- **Plugin**: Niagara
- **Module**: Niagara
- **File**: NiagaraDataChannel.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``channel_variables`` (Array[NiagaraDataChannelVariable]):  [Read-Write] The variables that define the data contained in this Data Channel.
- ``enforce_tick_group_read_write_order`` (bool):  [Read-Write] If true we ensure that all writes happen in or before the Tick Group specified in EndWriteTickGroup and that all reads happen in tick groups after this.
- ``final_write_tick_group`` (TickingGroup):  [Read-Write] The final tick group that this data channel can be written to.
- ``keep_previous_frame_data`` (bool):  [Read-Write] If true, we keep our previous frame's data. This comes at a memory and performance cost but allows users to avoid tick order dependency by reading last frame's data. Some users will prefer a frame of latency to tick order dependency.
- ``variables`` (Array[NiagaraVariable]):  [Read-Write]
  deprecated: Property 'Variables' is deprecated.

<a id="unreal.NiagaraDataChannel.variables"></a>

#### variables

```python
@property
def variables() -> Array[NiagaraVariable]
```

(Array[NiagaraVariable]):  [Read-Write]
deprecated: Property 'Variables' is deprecated.

<a id="unreal.NiagaraDataChannel.variables"></a>

#### variables

```python
@variables.setter
def variables(value: Array[NiagaraVariable]) -> None
```

<a id="unreal.NiagaraValidationRule"></a>