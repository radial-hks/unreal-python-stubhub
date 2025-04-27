## AutomationPerformaceHelper Objects

```python
class AutomationPerformaceHelper(Object)
```

Class for use with functional tests which provides various performance measuring features.
Recording of basic, unintrusive performance stats.
Automatic captures using external CPU and GPU profilers.
Triggering and ending of writing full stats to a file.

**C++ Source:**

- **Module**: FunctionalTesting
- **File**: FunctionalTest.h

<a id="unreal.AutomationPerformaceHelper.write_log_file"></a>

#### write_log_file

```python
def write_log_file(capture_dir: str, capture_extension: str) -> None
```

x.write_log_file(capture_dir, capture_extension) -> None
Writes the current set of performance stats records to a csv file in the profiling directory. An additional directory and an extension override can also be used.

Args:
    capture_dir (str): 
    capture_extension (str):

<a id="unreal.AutomationPerformaceHelper.trigger_gpu_trace_if_record_falls_below_budget"></a>

#### trigger_gpu_trace_if_record_falls_below_budget

```python
def trigger_gpu_trace_if_record_falls_below_budget() -> None
```

x.trigger_gpu_trace_if_record_falls_below_budget() -> None
Will trigger a GPU trace next time the current test falls below GPU budget.

<a id="unreal.AutomationPerformaceHelper.tick"></a>

#### tick

```python
def tick(delta_seconds: float) -> None
```

x.tick(delta_seconds) -> None
Begin basic stat recording

Args:
    delta_seconds (float):

<a id="unreal.AutomationPerformaceHelper.stop_cpu_profiling"></a>

#### stop_cpu_profiling

```python
def stop_cpu_profiling() -> None
```

x.stop_cpu_profiling() -> None
Communicates with external profiler to end a CPU capture.

<a id="unreal.AutomationPerformaceHelper.start_cpu_profiling"></a>

#### start_cpu_profiling

```python
def start_cpu_profiling() -> None
```

x.start_cpu_profiling() -> None
Communicates with external profiler to being a CPU capture.

<a id="unreal.AutomationPerformaceHelper.sample"></a>

#### sample

```python
def sample(delta_seconds: float) -> None
```

x.sample(delta_seconds) -> None
Adds a sample to the stats counters for the current performance stats record.

Args:
    delta_seconds (float):

<a id="unreal.AutomationPerformaceHelper.on_begin_tests"></a>

#### on_begin_tests

```python
def on_begin_tests() -> None
```

x.on_begin_tests() -> None
Does any init work across all tests..

<a id="unreal.AutomationPerformaceHelper.on_all_tests_complete"></a>

#### on_all_tests_complete

```python
def on_all_tests_complete() -> None
```

x.on_all_tests_complete() -> None
Does any final work needed as all tests are complete.

<a id="unreal.AutomationPerformaceHelper.is_recording"></a>

#### is_recording

```python
def is_recording() -> bool
```

x.is_recording() -> bool
Returns true if this stats tracker is currently recording performance stats.

Returns:
    bool:

<a id="unreal.AutomationPerformaceHelper.is_current_record_within_render_thread_budget"></a>

#### is_current_record_within_render_thread_budget

```python
def is_current_record_within_render_thread_budget() -> bool
```

x.is_current_record_within_render_thread_budget() -> bool
Is Current Record Within Render Thread Budget

Returns:
    bool:

<a id="unreal.AutomationPerformaceHelper.is_current_record_within_gpu_budget"></a>

#### is_current_record_within_gpu_budget

```python
def is_current_record_within_gpu_budget() -> bool
```

x.is_current_record_within_gpu_budget() -> bool
Is Current Record Within GPUBudget

Returns:
    bool:

<a id="unreal.AutomationPerformaceHelper.is_current_record_within_game_thread_budget"></a>

#### is_current_record_within_game_thread_budget

```python
def is_current_record_within_game_thread_budget() -> bool
```

x.is_current_record_within_game_thread_budget() -> bool
Is Current Record Within Game Thread Budget

Returns:
    bool:

<a id="unreal.AutomationPerformaceHelper.end_stats_file"></a>

#### end_stats_file

```python
def end_stats_file() -> None
```

x.end_stats_file() -> None
Ends recording stats to a file.

<a id="unreal.AutomationPerformaceHelper.end_recording_baseline"></a>

#### end_recording_baseline

```python
def end_recording_baseline() -> None
```

x.end_recording_baseline() -> None
Stops recording the baseline and moves to the main record.

<a id="unreal.AutomationPerformaceHelper.end_recording"></a>

#### end_recording

```python
def end_recording() -> None
```

x.end_recording() -> None
Stops recording performance stats.

<a id="unreal.AutomationPerformaceHelper.begin_stats_file"></a>

#### begin_stats_file

```python
def begin_stats_file(record_name: str) -> None
```

x.begin_stats_file(record_name) -> None
Begins recording stats to a file.

Args:
    record_name (str):

<a id="unreal.AutomationPerformaceHelper.begin_recording_baseline"></a>

#### begin_recording_baseline

```python
def begin_recording_baseline(record_name: str) -> None
```

x.begin_recording_baseline(record_name) -> None
Begins recording a new named performance stats record. We start by recording the baseline

Args:
    record_name (str):

<a id="unreal.AutomationPerformaceHelper.begin_recording"></a>

#### begin_recording

```python
def begin_recording(record_name: str, gpu_budget: float,
                    render_thread_budget: float,
                    game_thread_budget: float) -> None
```

x.begin_recording(record_name, gpu_budget, render_thread_budget, game_thread_budget) -> None
Begins recording a new named performance stats record. We start by recording the baseline.

Args:
    record_name (str): 
    gpu_budget (float): 
    render_thread_budget (float): 
    game_thread_budget (float):

<a id="unreal.FunctionalTestGameMode"></a>