# Profiling code

Note: Only compatible with Python 3.

Install requirements first:

```shell
pip install -r requirements.txt
```

## Memory

Run with:

```
mprof run memory_STEP.py PATH_TO_CONFIG_FILE
```

Where STEP is `preprocess`, `detect`, `cluster`, `templates`, `decovolution`
(profile one step in the pipeline line by line). You need to run
previous steps to generate the results. `pipeline` is also valid, it runs
the complete pipeline.

Run any of the scripts with the `--help` option to see options available.

Plot results:

```
mprof plots
```

## CPU profiler

### Profiling the entire pipeline

Run with:

```shell
kernprof -l cpu_STEP.py
```

Inspect results:

```shell
python -m line_profiler cpu_pipeline.py.lprof
```

## Resources

* [Memory profiling library](https://github.com/pythonprofilers/memory_profiler)
* [CPU profiling library](https://github.com/rkern/line_profiler)

