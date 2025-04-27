## ParticleRandomSeedInfo Objects

```python
class ParticleRandomSeedInfo(StructBase)
```

Particle Random Seed Info

**C++ Source:**

- **Module**: Engine
- **File**: ParticleModule.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``get_seed_from_instance`` (bool):  [Read-Write] If true, the module will attempt to get the seed from the owner
  instance. If that fails, it will fall back to getting it from
  the RandomSeeds array.
- ``instance_seed_is_index`` (bool):  [Read-Write] If true, the seed value retrieved from the instance will be an
  index into the array of seeds.
- ``parameter_name`` (Name):  [Read-Write] The name to expose to the placed instances for setting this seed
- ``random_seeds`` (Array[int32]):  [Read-Write] The random seed values to utilize for the module.
  More than 1 means the instance will randomly select one.
- ``randomly_select_seed_array`` (bool):  [Read-Write] If true, then randomly select a seed entry from the RandomSeeds array
- ``reset_seed_on_emitter_looping`` (bool):  [Read-Write] If true, then reset the seed upon the emitter looping.
  For looping environmental effects this should likely be set to false to avoid
  a repeating pattern.

<a id="unreal.ParticleRandomSeedInfo.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.NaniteSettings"></a>