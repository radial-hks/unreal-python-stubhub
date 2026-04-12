## PCGDeterminismSettings Objects

```python
class PCGDeterminismSettings(StructBase)
```

PCGDeterminism Settings

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGDeterminismSettings.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``determinism_test_blueprint`` (type(Class)):  [Read-Write]
- ``native_tests`` (bool):  [Read-Write]
- ``use_blueprint_determinism_test`` (bool):  [Read-Write]

<a id="unreal.PCGDeterminismSettings.__init__"></a>

#### \_\_init\_\_

```python
def __init__(native_tests: bool = False,
             use_blueprint_determinism_test: bool = False,
             determinism_test_blueprint: Class = None) -> None
```

<a id="unreal.PCGDeterminismSettings.native_tests"></a>

#### native\_tests

```python
@property
def native_tests() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PCGDeterminismSettings.native_tests"></a>

#### native\_tests

```python
@native_tests.setter
def native_tests(value: bool) -> None
```

<a id="unreal.PCGDeterminismSettings.use_blueprint_determinism_test"></a>

#### use\_blueprint\_determinism\_test

```python
@property
def use_blueprint_determinism_test() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PCGDeterminismSettings.use_blueprint_determinism_test"></a>

#### use\_blueprint\_determinism\_test

```python
@use_blueprint_determinism_test.setter
def use_blueprint_determinism_test(value: bool) -> None
```

<a id="unreal.PCGDeterminismSettings.determinism_test_blueprint"></a>

#### determinism\_test\_blueprint

```python
@property
def determinism_test_blueprint() -> Class
```

(type(Class)):  [Read-Only]

<a id="unreal.PCGDummyGetPropertyLevel2Struct"></a>