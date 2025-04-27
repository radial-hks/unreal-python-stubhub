## TraceQueryTestResults Objects

```python
class TraceQueryTestResults(Object)
```

Trace Query Test Results

**C++ Source:**

- **Module**: FunctionalTesting
- **File**: TraceQueryTestResults.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``batch_options`` (TraceChannelTestBatchOptions):  [Read-Write]
- ``channel_results`` (TraceQueryTestResultsInner):  [Read-Write] Results for channel trace
- ``object_results`` (TraceQueryTestResultsInner):  [Read-Write] Results for object trace
- ``profile_results`` (TraceQueryTestResultsInner):  [Read-Write] Results for profile trace

<a id="unreal.TraceQueryTestResults.channel_results"></a>

#### channel_results

```python
@property
def channel_results() -> TraceQueryTestResultsInner
```

(TraceQueryTestResultsInner):  [Read-Write] Results for channel trace

<a id="unreal.TraceQueryTestResults.channel_results"></a>

#### channel_results

```python
@channel_results.setter
def channel_results(value: TraceQueryTestResultsInner) -> None
```

<a id="unreal.TraceQueryTestResults.object_results"></a>

#### object_results

```python
@property
def object_results() -> TraceQueryTestResultsInner
```

(TraceQueryTestResultsInner):  [Read-Write] Results for object trace

<a id="unreal.TraceQueryTestResults.object_results"></a>

#### object_results

```python
@object_results.setter
def object_results(value: TraceQueryTestResultsInner) -> None
```

<a id="unreal.TraceQueryTestResults.profile_results"></a>

#### profile_results

```python
@property
def profile_results() -> TraceQueryTestResultsInner
```

(TraceQueryTestResultsInner):  [Read-Write] Results for profile trace

<a id="unreal.TraceQueryTestResults.profile_results"></a>

#### profile_results

```python
@profile_results.setter
def profile_results(value: TraceQueryTestResultsInner) -> None
```

<a id="unreal.TraceQueryTestResults.batch_options"></a>

#### batch_options

```python
@property
def batch_options() -> TraceChannelTestBatchOptions
```

(TraceChannelTestBatchOptions):  [Read-Write]

<a id="unreal.TraceQueryTestResults.batch_options"></a>

#### batch_options

```python
@batch_options.setter
def batch_options(value: TraceChannelTestBatchOptions) -> None
```

<a id="unreal.TraceQueryTestResults.to_string"></a>

#### to_string

```python
def to_string() -> str
```

x.to_string() -> str
Output string value

Returns:
    str:

<a id="unreal.BehaviorTreeFactory"></a>