## SynthesisUtilitiesBlueprintFunctionLibrary Objects

```python
class SynthesisUtilitiesBlueprintFunctionLibrary(BlueprintFunctionLibrary)
```

Synthesis Utilities Blueprint Function Library
A library of synthesis related functions for use in Blueprints

**C++ Source:**

- **Plugin**: Synthesis
- **Module**: Synthesis
- **File**: SynthesisBlueprintUtilities.h

<a id="unreal.SynthesisUtilitiesBlueprintFunctionLibrary.get_log_frequency"></a>

#### get_log_frequency

```python
@classmethod
def get_log_frequency(cls, linear_value: float, domain_min: float,
                      domain_max: float, range_min: float,
                      range_max: float) -> float
```

X.get_log_frequency(linear_value, domain_min, domain_max, range_min, range_max) -> float
Returns the log frequency of the input value. Maps linear domain and range values to log output (good for linear slider controlling frequency)

Args:
    linear_value (float): 
    domain_min (float): 
    domain_max (float): 
    range_min (float): 
    range_max (float): 

Returns:
    float:

<a id="unreal.SynthesisUtilitiesBlueprintFunctionLibrary.get_linear_frequency"></a>

#### get_linear_frequency

```python
@classmethod
def get_linear_frequency(cls, log_frequency_value: float, domain_min: float,
                         domain_max: float, range_min: float,
                         range_max: float) -> float
```

X.get_linear_frequency(log_frequency_value, domain_min, domain_max, range_min, range_max) -> float
Returns the log frequency of the input value. Maps linear domain and range values to log output (good for linear slider controlling frequency)

Args:
    log_frequency_value (float): 
    domain_min (float): 
    domain_max (float): 
    range_min (float): 
    range_max (float): 

Returns:
    float:

<a id="unreal.Synth2DSlider"></a>