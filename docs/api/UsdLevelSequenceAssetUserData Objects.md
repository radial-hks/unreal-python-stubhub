## UsdLevelSequenceAssetUserData Objects

```python
class UsdLevelSequenceAssetUserData(AssetUserData)
```

We assign these to persistent LevelSequences that bind to one of the actors/components that the stage actor spawns.
We need this as part of a mechanism to automatically repair those bindings when they break if we close/reload the stage.

**C++ Source:**

- **Plugin**: USDCore
- **Module**: USDClasses
- **File**: USDAssetUserData.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``handled_binding_guids`` (Set[Guid]):  [Read-Write] Set of binding GUIDs that we already handled in the past.
  We use this so that we won't try and overwrite the changes in case the user manually clears/modifies a binding we previously setup.
- ``last_checked_signature`` (Guid):  [Read-Write] The LevelSequence has a Guid that is changed every time its state is modified.
  We pay attention to that so that we can avoid reprocessing a LevelSequence that hasn't changed

<a id="unreal.UsdLevelSequenceAssetUserData.last_checked_signature"></a>

#### last_checked_signature

```python
@property
def last_checked_signature() -> Guid
```

(Guid):  [Read-Write] The LevelSequence has a Guid that is changed every time its state is modified.
We pay attention to that so that we can avoid reprocessing a LevelSequence that hasn't changed

<a id="unreal.UsdLevelSequenceAssetUserData.last_checked_signature"></a>

#### last_checked_signature

```python
@last_checked_signature.setter
def last_checked_signature(value: Guid) -> None
```

<a id="unreal.UsdLevelSequenceAssetUserData.handled_binding_guids"></a>

#### handled_binding_guids

```python
@property
def handled_binding_guids() -> Set[Guid]
```

(Set[Guid]):  [Read-Write] Set of binding GUIDs that we already handled in the past.
We use this so that we won't try and overwrite the changes in case the user manually clears/modifies a binding we previously setup.

<a id="unreal.UsdLevelSequenceAssetUserData.handled_binding_guids"></a>

#### handled_binding_guids

```python
@handled_binding_guids.setter
def handled_binding_guids(value: Set[Guid]) -> None
```

<a id="unreal.UsdSparseVolumeTextureAssetUserData"></a>