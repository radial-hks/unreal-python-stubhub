## InterchangeImportTestPlan Objects

```python
class InterchangeImportTestPlan(Object)
```

Define a test plan

**C++ Source:**

- **Plugin**: InterchangeTests
- **Module**: InterchangeTests
- **File**: InterchangeImportTestPlan.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``disabled_test_reason`` (str):  [Read-Write] Why is the test plan disabled.
- ``is_enabled_in_automation_tests`` (bool):  [Read-Write] Whether or not this test plan is currently enabled
- ``steps`` (Array[InterchangeImportTestStepBase]):  [Read-Write] Set of steps to perform to carry out this test plan

<a id="unreal.InterchangeImportTestPlan.run_this_test"></a>

#### run_this_test

```python
def run_this_test() -> None
```

x.run_this_test() -> None
Click here to immediately run this single test through the automation framework

<a id="unreal.InterchangeImportTestStepBase"></a>