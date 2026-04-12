## WdpEntityReadyEventArgs Objects

```python
class WdpEntityReadyEventArgs(EventArgsBase)
```

Wdp Entity Ready Event Args

**C++ Source:**

- **Plugin**: WdpRuntimeAPI
- **Module**: DataModelAPI
- **File**: WdpSceneAPI.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``eid`` (Eid):  [Read-Write]
- ``progress`` (float):  [Read-Write]

<a id="unreal.WdpEntityReadyEventArgs.__init__"></a>

#### \_\_init\_\_

```python
def __init__(eid: Eid = [0], progress: float = 0.000000) -> None
```

<a id="unreal.WdpEntityReadyEventArgs.eid"></a>

#### eid

```python
@property
def eid() -> Eid
```

(Eid):  [Read-Write]

<a id="unreal.WdpEntityReadyEventArgs.eid"></a>

#### eid

```python
@eid.setter
def eid(value: Eid) -> None
```

<a id="unreal.WdpEntityReadyEventArgs.progress"></a>

#### progress

```python
@property
def progress() -> float
```

(float):  [Read-Write]

<a id="unreal.WdpEntityReadyEventArgs.progress"></a>

#### progress

```python
@progress.setter
def progress(value: float) -> None
```

<a id="unreal.CreateEntityParams"></a>