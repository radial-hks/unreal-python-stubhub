## EpicSynth1Patch Objects

```python
class EpicSynth1Patch(StructBase)
```

Epic Synth 1Patch

**C++ Source:**

- **Plugin**: Synthesis
- **Module**: Synthesis
- **File**: EpicSynth1Component.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``patch_cables`` (Array[Synth1PatchCable]):  [Read-Write] Patch cables to patch destinations from the patch source.
- ``patch_source`` (Synth1PatchSource):  [Read-Write] A modular synth patch source (e.g. LFO1/LFO2/Modulation Envelope)

<a id="unreal.EpicSynth1Patch.__init__"></a>

#### __init__

```python
def __init__(patch_source: Synth1PatchSource = Synth1PatchSource.LFO1,
             patch_cables: Array[Synth1PatchCable] = []) -> None
```

<a id="unreal.EpicSynth1Patch.patch_source"></a>

#### patch_source

```python
@property
def patch_source() -> Synth1PatchSource
```

(Synth1PatchSource):  [Read-Write] A modular synth patch source (e.g. LFO1/LFO2/Modulation Envelope)

<a id="unreal.EpicSynth1Patch.patch_source"></a>

#### patch_source

```python
@patch_source.setter
def patch_source(value: Synth1PatchSource) -> None
```

<a id="unreal.EpicSynth1Patch.patch_cables"></a>

#### patch_cables

```python
@property
def patch_cables() -> Array[Synth1PatchCable]
```

(Array[Synth1PatchCable]):  [Read-Write] Patch cables to patch destinations from the patch source.

<a id="unreal.EpicSynth1Patch.patch_cables"></a>

#### patch_cables

```python
@patch_cables.setter
def patch_cables(value: Array[Synth1PatchCable]) -> None
```

<a id="unreal.ModularSynthPreset"></a>