## NiagaraDataChannelAsset Objects

```python
class NiagaraDataChannelAsset(Object)
```

Niagara Data Channels are a system for communication between Niagara Systems and with game code/Blueprint.

Data channel assets define the payload as well as some transfer settings.
Niagara Systems can read from and write to data channels via data interfaces.
Blueprint and C++ code can also read from and write to data channels using its API functions.

**C++ Source:**

- **Plugin**: Niagara
- **Module**: Niagara
- **File**: NiagaraDataChannelPublic.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``data_channel`` (NiagaraDataChannel):  [Read-Write]

<a id="unreal.NiagaraDataChannelHandler_Global"></a>