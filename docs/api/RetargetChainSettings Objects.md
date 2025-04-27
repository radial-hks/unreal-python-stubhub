## RetargetChainSettings Objects

```python
class RetargetChainSettings(Object)
```

Retarget Chain Settings

**C++ Source:**

- **Plugin**: IKRig
- **Module**: IKRig
- **File**: IKRetargeter.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``settings`` (TargetChainSettings):  [Read-Write] The settings used to control the motion on this target chain.
- ``source_chain`` (Name):  [Read-Only] The chain on the Source IK Rig asset to copy animation FROM.
- ``target_chain`` (Name):  [Read-Only] The chain on the Target IK Rig asset to copy animation TO.

<a id="unreal.RetargetChainSettings.source_chain"></a>

#### source_chain

```python
@property
def source_chain() -> Name
```

(Name):  [Read-Only] The chain on the Source IK Rig asset to copy animation FROM.

<a id="unreal.RetargetChainSettings.target_chain"></a>

#### target_chain

```python
@property
def target_chain() -> Name
```

(Name):  [Read-Only] The chain on the Target IK Rig asset to copy animation TO.

<a id="unreal.RetargetChainSettings.settings"></a>

#### settings

```python
@property
def settings() -> TargetChainSettings
```

(TargetChainSettings):  [Read-Write] The settings used to control the motion on this target chain.

<a id="unreal.RetargetChainSettings.settings"></a>

#### settings

```python
@settings.setter
def settings(value: TargetChainSettings) -> None
```

<a id="unreal.RetargetRootSettings"></a>