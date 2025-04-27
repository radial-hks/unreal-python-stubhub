## LiveLinkPreset Objects

```python
class LiveLinkPreset(Object)
```

Live Link Preset

**C++ Source:**

- **Plugin**: LiveLink
- **Module**: LiveLink
- **File**: LiveLinkPreset.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``sources`` (Array[LiveLinkSourcePreset]):  [Read-Only]
- ``subjects`` (Array[LiveLinkSubjectPreset]):  [Read-Only]

<a id="unreal.LiveLinkPreset.build_from_client"></a>

#### build_from_client

```python
def build_from_client() -> None
```

x.build_from_client() -> None
Reset this preset and build the list of sources and subjects from the client.

<a id="unreal.LiveLinkPreset.apply_to_client_latent"></a>

#### apply_to_client_latent

```python
def apply_to_client_latent(world_context_object: Object,
                           latent_info: LatentActionInfo) -> None
```

x.apply_to_client_latent(world_context_object, latent_info) -> None
Remove all previous sources and subjects and add the sources and subjects from this preset.

Args:
    world_context_object (Object): 
    latent_info (LatentActionInfo):

<a id="unreal.LiveLinkPreset.apply_to_client"></a>

#### apply_to_client

```python
def apply_to_client() -> bool
```

x.apply_to_client() -> bool
Apply to Client

Returns:
    bool:

<a id="unreal.LiveLinkPreset.add_to_client"></a>

#### add_to_client

```python
def add_to_client(recreate_presets: bool = True) -> bool
```

x.add_to_client(recreate_presets=True) -> bool
Add the sources and subjects from this preset, but leave any existing sources and subjects connected.

Args:
    recreate_presets (bool): When true, if subjects and sources from this preset already exist, we will recreate them.

Returns:
    bool: True is all sources and subjects from this preset could be created and added.

<a id="unreal.LiveLinkTimecodeProvider"></a>