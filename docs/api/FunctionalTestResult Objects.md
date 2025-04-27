## FunctionalTestResult Objects

```python
class FunctionalTestResult(EnumBase)
```

EFunctional Test Result

**C++ Source:**

- **Module**: FunctionalTesting
- **File**: FunctionalTest.h

<a id="unreal.FunctionalTestResult.DEFAULT"></a>

#### DEFAULT

0: When finishing a test if you use Default, you're not explicitly stating if the test passed or failed.
Instead you're instead allowing any tested assertions to have decided that for you.  Even if you do
explicitly log success, it can be overturned by errors that occurred during the test.

<a id="unreal.FunctionalTestResult.INVALID"></a>

#### INVALID

1

<a id="unreal.FunctionalTestResult.ERROR"></a>

#### ERROR

2

<a id="unreal.FunctionalTestResult.RUNNING"></a>

#### RUNNING

3

<a id="unreal.FunctionalTestResult.FAILED"></a>

#### FAILED

4

<a id="unreal.FunctionalTestResult.SUCCEEDED"></a>

#### SUCCEEDED

5

<a id="unreal.FunctionalTestLogHandling"></a>