## SoundCueFactoryNew Objects

```python
class SoundCueFactoryNew(Factory)
```

Sound Cue Factory New

**C++ Source:**

- **Module**: AudioEditor
- **File**: SoundCueFactoryNew.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``asset_import_task`` (AssetImportTask):  [Read-Write] Task for importing file via script interfaces
- ``automated_import_data`` (AutomatedAssetImportData):  [Read-Write] Data for how to import files via the automated command line importing interface
- ``context_class`` (type(Class)):  [Read-Write] Class of the context object used to help create the object.
- ``create_new`` (bool):  [Read-Write] The default value to return from CanCreateNew()
- ``edit_after_new`` (bool):  [Read-Write] true if the associated editor should be opened after creating a new object.
- ``editor_import`` (bool):  [Read-Write] true if the factory imports objects from files.
- ``formats`` (Array[str]):  [Read-Write] List of formats supported by the factory. Each entry is of the form "ext;Description" where ext is the file extension.
- ``initial_dialogue_wave`` (DialogueWave):  [Read-Write] An initial dialogue wave to place in the newly created cue
  deprecated: Use Array InitialDialogueWaves instead.
- ``initial_dialogue_waves`` (Array[DialogueWave]):  [Read-Write] Initial dialogue wave(s) to place in the newly created cue(s)
- ``initial_sound_wave`` (SoundWave):  [Read-Write] Initial sound wave to place in the newly created cue
  deprecated: Use Array InitialSoundWaves instead.
- ``initial_sound_waves`` (Array[SoundWave]):  [Read-Write] Initial sound wave(s) to place in the newly created cue(s)
- ``supported_class`` (type(Class)):  [Read-Write] The class manufactured by this factory.
- ``text`` (bool):  [Read-Write] true if the factory imports objects from text.

<a id="unreal.SoundCueFactoryNew.initial_sound_wave"></a>

#### initial_sound_wave

```python
@property
def initial_sound_wave() -> SoundWave
```

(SoundWave):  [Read-Write] Initial sound wave to place in the newly created cue
deprecated: Use Array InitialSoundWaves instead.

<a id="unreal.SoundCueFactoryNew.initial_sound_wave"></a>

#### initial_sound_wave

```python
@initial_sound_wave.setter
def initial_sound_wave(value: SoundWave) -> None
```

<a id="unreal.SoundCueFactoryNew.initial_dialogue_wave"></a>

#### initial_dialogue_wave

```python
@property
def initial_dialogue_wave() -> DialogueWave
```

(DialogueWave):  [Read-Write] An initial dialogue wave to place in the newly created cue
deprecated: Use Array InitialDialogueWaves instead.

<a id="unreal.SoundCueFactoryNew.initial_dialogue_wave"></a>

#### initial_dialogue_wave

```python
@initial_dialogue_wave.setter
def initial_dialogue_wave(value: DialogueWave) -> None
```

<a id="unreal.SoundMixFactory"></a>