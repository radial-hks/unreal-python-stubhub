## SoundClass Objects

```python
class SoundClass(Object)
```

Sound Class

**C++ Source:**

- **Module**: Engine
- **File**: SoundClass.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``child_classes`` (Array[SoundClass]):  [Read-Write]
- ``parent_class`` (SoundClass):  [Read-Write]
- ``passive_sound_mix_modifiers`` (Array[PassiveSoundMixModifier]):  [Read-Write] SoundMix Modifiers to activate automatically when a sound of this class is playing.
- ``properties`` (SoundClassProperties):  [Read-Write] Configurable properties like volume and priority.

<a id="unreal.SoundClass.properties"></a>

#### properties

```python
@property
def properties() -> SoundClassProperties
```

(SoundClassProperties):  [Read-Only] Configurable properties like volume and priority.

<a id="unreal.SoundClass.child_classes"></a>

#### child_classes

```python
@property
def child_classes() -> Array[SoundClass]
```

(Array[SoundClass]):  [Read-Only]

<a id="unreal.SoundClass.passive_sound_mix_modifiers"></a>

#### passive_sound_mix_modifiers

```python
@property
def passive_sound_mix_modifiers() -> Array[PassiveSoundMixModifier]
```

(Array[PassiveSoundMixModifier]):  [Read-Only] SoundMix Modifiers to activate automatically when a sound of this class is playing.

<a id="unreal.SoundClass.parent_class"></a>

#### parent_class

```python
@property
def parent_class() -> SoundClass
```

(SoundClass):  [Read-Only]

<a id="unreal.SoundConcurrency"></a>