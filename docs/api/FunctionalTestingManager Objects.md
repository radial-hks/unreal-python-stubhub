## FunctionalTestingManager Objects

```python
class FunctionalTestingManager(BlueprintFunctionLibrary)
```

Functional Testing Manager

**C++ Source:**

- **Module**: FunctionalTesting
- **File**: FunctionalTestingManager.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``on_setup_tests`` (FunctionalTestEventSignature):  [Read-Write]
- ``on_tests_begin`` (FunctionalTestEventSignature):  [Read-Write]
- ``on_tests_complete`` (FunctionalTestEventSignature):  [Read-Write]

<a id="unreal.FunctionalTestingManager.on_setup_tests"></a>

#### on_setup_tests

```python
@property
def on_setup_tests() -> FunctionalTestEventSignature
```

(FunctionalTestEventSignature):  [Read-Write]

<a id="unreal.FunctionalTestingManager.on_setup_tests"></a>

#### on_setup_tests

```python
@on_setup_tests.setter
def on_setup_tests(value: FunctionalTestEventSignature) -> None
```

<a id="unreal.FunctionalTestingManager.on_tests_complete"></a>

#### on_tests_complete

```python
@property
def on_tests_complete() -> FunctionalTestEventSignature
```

(FunctionalTestEventSignature):  [Read-Write]

<a id="unreal.FunctionalTestingManager.on_tests_complete"></a>

#### on_tests_complete

```python
@on_tests_complete.setter
def on_tests_complete(value: FunctionalTestEventSignature) -> None
```

<a id="unreal.FunctionalTestingManager.on_tests_begin"></a>

#### on_tests_begin

```python
@property
def on_tests_begin() -> FunctionalTestEventSignature
```

(FunctionalTestEventSignature):  [Read-Write]

<a id="unreal.FunctionalTestingManager.on_tests_begin"></a>

#### on_tests_begin

```python
@on_tests_begin.setter
def on_tests_begin(value: FunctionalTestEventSignature) -> None
```

<a id="unreal.FunctionalTestingManager.run_all_functional_tests"></a>

#### run_all_functional_tests

```python
@classmethod
def run_all_functional_tests(cls,
                             world_context_object: Object,
                             new_log: bool = True,
                             run_looped: bool = False,
                             failed_tests_repro_string: str = "") -> bool
```

X.run_all_functional_tests(world_context_object, new_log=True, run_looped=False, failed_tests_repro_string="") -> bool
Triggers in sequence all functional tests found on the level.

Args:
    world_context_object (Object): 
    new_log (bool): 
    run_looped (bool): 
    failed_tests_repro_string (str): 

Returns:
    bool: true if any tests have been triggered

<a id="unreal.PhasedAutomationActorBase"></a>