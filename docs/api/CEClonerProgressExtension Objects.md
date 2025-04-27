## CEClonerProgressExtension Objects

```python
class CEClonerProgressExtension(CEClonerExtensionBase)
```

Extension dealing with clone progress options

**C++ Source:**

- **Plugin**: ClonerEffector
- **Module**: ClonerEffector
- **File**: CEClonerProgressExtension.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``invert_progress`` (bool):  [Read-Write] Invert progress behaviour
- ``progress`` (float):  [Read-Write] Changes visibility of instances based on the total count, 1.f = 100% = all instances visible

<a id="unreal.CEClonerProgressExtension.set_progress"></a>

#### set_progress

```python
def set_progress(progress: float) -> None
```

x.set_progress(progress) -> None
Set Progress

Args:
    progress (float):

<a id="unreal.CEClonerProgressExtension.set_invert_progress"></a>

#### set_invert_progress

```python
def set_invert_progress(invert_progress: bool) -> None
```

x.set_invert_progress(invert_progress) -> None
Set Invert Progress

Args:
    invert_progress (bool):

<a id="unreal.CEClonerProgressExtension.get_progress"></a>

#### get_progress

```python
def get_progress() -> float
```

x.get_progress() -> float
Get Progress

Returns:
    float:

<a id="unreal.CEClonerProgressExtension.get_invert_progress"></a>

#### get_invert_progress

```python
def get_invert_progress() -> bool
```

x.get_invert_progress() -> bool
Get Invert Progress

Returns:
    bool:

<a id="unreal.CEClonerRangeExtension"></a>