## CurveEditorFFTFilter Objects

```python
class CurveEditorFFTFilter(CurveEditorFilterBase)
```

Curve Editor FFTFilter

**C++ Source:**

- **Plugin**: CurveEditorTools
- **Module**: CurveEditorTools
- **File**: CurveEditorFFTFilter.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``cutoff_frequency`` (float):  [Read-Write] Normalized between 0-1. In a low pass filter, the lower the value is the smoother the output. In a high pass filter the higher the value the smoother the output.
- ``order`` (int32):  [Read-Write] The number of samples used to filter in the time domain. It maps how steep the roll off is for the filter.
- ``response`` (CurveEditorFFTFilterClass):  [Read-Write] Which FFT filter implementation to use.
- ``type`` (CurveEditorFFTFilterType):  [Read-Write] Which frequencies are allowed through. For example, low-pass will let low frequency through and remove high frequency noise.

<a id="unreal.CurveEditorFFTFilter.cutoff_frequency"></a>

#### cutoff_frequency

```python
@property
def cutoff_frequency() -> float
```

(float):  [Read-Write] Normalized between 0-1. In a low pass filter, the lower the value is the smoother the output. In a high pass filter the higher the value the smoother the output.

<a id="unreal.CurveEditorFFTFilter.cutoff_frequency"></a>

#### cutoff_frequency

```python
@cutoff_frequency.setter
def cutoff_frequency(value: float) -> None
```

<a id="unreal.CurveEditorFFTFilter.type"></a>

#### type

```python
@property
def type() -> CurveEditorFFTFilterType
```

(CurveEditorFFTFilterType):  [Read-Write] Which frequencies are allowed through. For example, low-pass will let low frequency through and remove high frequency noise.

<a id="unreal.CurveEditorFFTFilter.type"></a>

#### type

```python
@type.setter
def type(value: CurveEditorFFTFilterType) -> None
```

<a id="unreal.CurveEditorFFTFilter.response"></a>

#### response

```python
@property
def response() -> CurveEditorFFTFilterClass
```

(CurveEditorFFTFilterClass):  [Read-Write] Which FFT filter implementation to use.

<a id="unreal.CurveEditorFFTFilter.response"></a>

#### response

```python
@response.setter
def response(value: CurveEditorFFTFilterClass) -> None
```

<a id="unreal.CurveEditorFFTFilter.order"></a>

#### order

```python
@property
def order() -> int
```

(int32):  [Read-Write] The number of samples used to filter in the time domain. It maps how steep the roll off is for the filter.

<a id="unreal.CurveEditorFFTFilter.order"></a>

#### order

```python
@order.setter
def order(value: int) -> None
```

<a id="unreal.StaticMeshLODGenerationSettings"></a>