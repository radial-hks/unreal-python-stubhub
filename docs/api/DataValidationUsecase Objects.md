## DataValidationUsecase Objects

```python
class DataValidationUsecase(EnumBase)
```

EData Validation Usecase

**C++ Source:**

- **Module**: CoreUObject
- **File**: DataValidation.h

<a id="unreal.DataValidationUsecase.NONE"></a>

#### NONE

0: No usecase specified

<a id="unreal.DataValidationUsecase.MANUAL"></a>

#### MANUAL

1: Triggered on user's demand

<a id="unreal.DataValidationUsecase.COMMANDLET"></a>

#### COMMANDLET

2: A commandlet invoked the validation

<a id="unreal.DataValidationUsecase.SAVE"></a>

#### SAVE

3: Saving a package triggered the validation

<a id="unreal.DataValidationUsecase.PRE_SUBMIT"></a>

#### PRE_SUBMIT

4: Submit dialog triggered the validation

<a id="unreal.DataValidationUsecase.SCRIPT"></a>

#### SCRIPT

5: Triggered by blueprint or c++

<a id="unreal.AxisType"></a>