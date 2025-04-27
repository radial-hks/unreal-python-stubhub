## LevelSequenceBurnInOptions Objects

```python
class LevelSequenceBurnInOptions(Object)
```

Level Sequence Burn in Options

**C++ Source:**

- **Module**: LevelSequence
- **File**: LevelSequenceActor.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``burn_in_class`` (SoftClassPath):  [Read-Write]
- ``settings`` (LevelSequenceBurnInInitSettings):  [Read-Write]
- ``use_burn_in`` (bool):  [Read-Write]

<a id="unreal.LevelSequenceBurnInOptions.use_burn_in"></a>

#### use_burn_in

```python
@property
def use_burn_in() -> bool
```

(bool):  [Read-Write]

<a id="unreal.LevelSequenceBurnInOptions.use_burn_in"></a>

#### use_burn_in

```python
@use_burn_in.setter
def use_burn_in(value: bool) -> None
```

<a id="unreal.LevelSequenceBurnInOptions.burn_in_class"></a>

#### burn_in_class

```python
@property
def burn_in_class() -> SoftClassPath
```

(SoftClassPath):  [Read-Write]

<a id="unreal.LevelSequenceBurnInOptions.burn_in_class"></a>

#### burn_in_class

```python
@burn_in_class.setter
def burn_in_class(value: SoftClassPath) -> None
```

<a id="unreal.LevelSequenceBurnInOptions.settings"></a>

#### settings

```python
@property
def settings() -> LevelSequenceBurnInInitSettings
```

(LevelSequenceBurnInInitSettings):  [Read-Write]

<a id="unreal.LevelSequenceBurnInOptions.settings"></a>

#### settings

```python
@settings.setter
def settings(value: LevelSequenceBurnInInitSettings) -> None
```

<a id="unreal.LevelSequenceBurnInOptions.set_burn_in"></a>

#### set_burn_in

```python
def set_burn_in(burn_in_class: SoftClassPath) -> None
```

x.set_burn_in(burn_in_class) -> None
Loads the specified class path and initializes an instance, then stores it in Settings.

Args:
    burn_in_class (SoftClassPath):

<a id="unreal.LevelSequenceActor"></a>