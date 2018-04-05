# Profiling code

Install requirements first:

```shell
pip install -r requirements.txt
```

## Memory

### Profiling the entire pipeline

This first script profiles every step in the pipeline

Docs:

```shell
python pipeline_memory.py --help
```

Execution:

```shell
mprof run pipeline_memory.py PATH_TO_CONFIG_FILE
```

Once it's done you can plot the results:

```shell
mprof plot
```

[See this for details](https://github.com/pythonprofilers/memory_profiler)


### Profiling preprocessor line by line

WIP

## CPU profiler

WIP